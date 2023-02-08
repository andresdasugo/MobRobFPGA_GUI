from Graphics.mainWindow_ import *
from Graphics.ConfWindow import *
from PyQt5.QtGui import QPixmap, QIcon

from ZigBee.ZigBee import ZigBeeModule
import FileManager.FileManager as File

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

from datetime import datetime

import logging
import json


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self._position_x = None
        self._position_y = None
        self._angle = None
        self._timestamp = None
        self._linear_velocity = None
        self._angular_velocity = None
        self._x_error = None
        self._y_error = None
        self._angle_error = None
        self._file_path = None
        self._draw = False
        self._line_type = 'k'
        self._image_play_pause = 'play'
        self.setupUi(self)
        self._zigbee = None
        self._zigbee_connect = False

        self._size_x = [-1 * float(self.size_x.text())/2, float(self.size_x.text())/2]
        self._size_y = [-1 * float(self.size_y.text())/2, float(self.size_y.text())/2]

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setParent(self.graphicsView)
        self.canvas.setGeometry(0, 0, self.graphicsView.width(), self.graphicsView.height())
        self.canvas.mpl_connect('button_press_event', self._onclick)
        self._plot(self._position_x, self._position_y, grid=False, x_lim=self._size_x, y_lim=self._size_y)

        self.console.setReadOnly(True)
        self._load_images()
        self._load_robot_id()
        self._load_control_type()
        self._actions_connect()

        self.show()

    def _onclick(self, event):
        if event.xdata and event.ydata:
            self.positionX.setText(str(event.xdata)[0:4])
            self.positionY.setText(str(event.ydata)[0:4])

    def _arena_size(self):
        self._size_x = [-1 * float(self.size_x.text())/2, float(self.size_x.text())/2]
        self._size_y = [-1 * float(self.size_y.text())/2, float(self.size_y.text())/2]
        self._plot(self._position_x, self._position_y, draw=self._draw, line_type=self._line_type,
                   x_lim=self._size_x, y_lim=self._size_y)

    def _show_tracking(self):
        self._line_type = 'k*--' if self.show_tracking.isChecked() else 'k*'
        self._plot(self._position_x, self._position_y, line_type=self._line_type, draw=self._draw, x_lim=self._size_x,
                   y_lim=self._size_y)
                   
    def _play_pause(self):
        logger.info('Playing or pausing drawing data')
        if self._image_play_pause == 'play':
            self._image_play_pause = 'pause'
            self.play_pause_button.setIcon(QIcon('Graphics/icons8-pausa-52.png'))
        else:
            self._image_play_pause = 'play'
            self.play_pause_button.setIcon(QIcon('Graphics/icons8-play-96.png'))
            
    def _erase_arena(self):
        logger.info('Erasing arena data')
        self._position_x = []
        self._position_y = []
        self._angle = []
        self._linear_velocity = []
        self._angular_velocity = []
        self._x_error = []
        self._y_error = []
        self._angle_error = []
        self._plot(self._position_x, self._position_y, line_type=self._line_type, draw=self._draw, grid=True,
                       x_lim=self._size_x, y_lim=self._size_y)
                       
    def _discover_robots(self):
        if self._zigbee_connect:
            logger.info('Discovering robots IDs')
            self._style_connect_button('Discovering')
            devices = self._zigbee.discover_ids()
            File.create_file('Setup/RobotIDs.txt', devices)
            self._style_connect_button('Connected')
            self._load_robot_id()

    def _plot(self, x, y, line_type='*', grid=True, draw=False, x_lim=[0, 2], y_lim=[0, 2]):
        logger.info('Drawing data')
        self.figure.clear()
        axes = self.figure.add_subplot(1, 1, 1)
        axes.set_title('ROBOT POSE')
        axes.set_xlabel('Position (m)')
        axes.set_ylabel('Position (m)')
        axes.set_xlim(x_lim[0], x_lim[1])
        axes.set_ylim(y_lim[0], y_lim[1])
        axes.grid(grid)
        if draw:
            if x and y:
                circle = plt.Circle((x[-1], y[-1]), radius=0.1, fill=False)
                axes.add_artist(circle)
            axes.plot(x, y, line_type, label='Robot 1')
            axes.legend(loc='upper left')
            self.canvas.draw()

    def _actions_connect(self):
        self.confButtom.clicked.connect(self._configWindow)
        self.exitButtom.clicked.connect(self.close)
        self.connectButtom.clicked.connect(self._connected)
        self.loadFileButtom.clicked.connect(self._open_data_file)
        self.save.clicked.connect(self._save_data_file)
        self.set_size.clicked.connect(self._arena_size)
        self.sendConfigurationButtom.clicked.connect(self._send_data)
        self.play_pause_button.clicked.connect(self._play_pause)
        self.clear_button.clicked.connect(self._erase_arena)
        self.discoveryButtom.clicked.connect(self._discover_robots)

        self.checkConsole.stateChanged.connect(self._enable_textarea)
        self.show_tracking.stateChanged.connect(self._show_tracking)
        
    def _send_data(self):
        #if self._zigbee_connect:
        message = self._create_json({"from":1,"to":0,"cnt":3,"type":0,"body":{"x":0,"y":0,"t":-0.005952,"lv":2,"av":-1.209766,"xe":1,"ye":1,"te":3.147545}})
        id_remote = self.robot_id.currentText()
        print(message)
            #self._zigbee.send(id_remote, message)
            
    def _create_json(self, data):
        return json.dumps(data)

    def _open_data_file(self):
        self._file_path, _filter = QtWidgets.QFileDialog.getOpenFileName(self, 'Select data file',
                                                                         filter="Excel files *.xls;;Excel files *.xlsx")
        if self._file_path:
            self._draw = True
            self._position_x, self._position_y, self._angle, self._timestamp = File.read_xls_file(self._file_path)
            if not self._position_x:
                QMessageBox.information(self, 'Information', "File don't have information", QMessageBox.Close)
                grid = False
            self._line_type = 'k*--' if self.show_tracking.isChecked() else 'k*'
            if self._zigbee and self._zigbee.running:
                self._stop_comunication()
            self._plot(self._position_x, self._position_y, line_type=self._line_type, draw=self._draw, grid=True,
                       x_lim=self._size_x, y_lim=self._size_y)

    def _save_data_file(self):
        if self._position_x:
            self._file_path, _filter = QtWidgets.QFileDialog.getSaveFileName(self, 'Save data file',
                                                                             filter="Excel files *.xls;;"
                                                                                    "Excel files *.xlsx")
            has_extension = self._file_path.find('.xls')
            if self._file_path:
                if has_extension < 0:
                    extension = _filter.split('*')[1]
                    self._file_path = self._file_path + extension
                if File.save_data_file(
                        self._file_path, self._position_x, self._position_y, self._angle, self._timestamp,
                        self._linear_velocity, self._angular_velocity, self._x_error, self._y_error,
                        self._angle_error
                ):
                    message = 'Save data correctly'
                else:
                    message = 'Error saving data'
                QMessageBox.information(self, 'Information', message, QMessageBox.Close)
        else:
            QMessageBox.information(self, 'Information', 'There are not information to save', QMessageBox.Close)

    def _enable_textarea(self):
        self.console.setReadOnly(not self.checkConsole.isChecked())
        if self.checkConsole.isChecked():
            self.console.setStyleSheet('background-color: white')
        else:
            self.console.setStyleSheet('background-color: rgb(239, 235, 231)')

    def _connected(self):
        if not self._zigbee_connect:
            logger.info('Connecting the zigbee device')
            if not File.exist_file('Setup/config.yaml'):
                QMessageBox.question(self, 'Information', 'Configuration file does not exist\r\nPlease create it',
                                           QMessageBox.Cancel)
            else:
                try:
                    self._zigbee_connect = True
                    self._position_x = []
                    self._position_y = []
                    self._angle = []
                    self._timestamp = []
                    parameters = File.read_configuration()
                    self._draw = True
                    self._line_type = 'k*--' if self.show_tracking.isChecked() else 'k*'
                    self._zigbee = ZigBeeModule(parameters)
                    self._zigbee.read_update.connect(self._handler_zigbee_communication)
                    self._zigbee.start()
                    logger.info('Zigbee device connected')
                    self._style_connect_button('Connected')
                except:
                    self._zigbee_connect = False
                    self.status.setText('Failed Connection')
        else:
            self._style_connect_button('Disconnected')
            self._stop_communication()
            self._zigbee_connect = False

    def _style_connect_button(self, status):
        if status == 'Connected':
            button = 'Disconnect'
            color = 'green'
        elif status == 'Disconnected':
            button = 'Connect'
            color = 'red'
        else:
            button = 'Discovering robots IDs...'
            color = 'yellow'
        self.connectButtom.setText(button)
        self.status.setText(status)
        self.status.setStyleSheet('background-color: {}'.format(color))

    def _handler_zigbee_communication(self, value):
        try:
            if self.checkConsole.isChecked():
                self.console.appendPlainText(value)
            _position_x, _position_y, _angle, _linear_velocity, _angular_velocity, _x_error, _y_error, _angle_error = \
                self._zigbee.decode_message(value)
            now = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
            self._position_x.append(_position_x)
            self._position_y.append(_position_y)
            self._angle.append(_angle)
            self._timestamp.append(now)
            self._linear_velocity.append(_linear_velocity)
            self._angular_velocity.append(_angular_velocity)
            self._x_error.append(_x_error)
            self._y_error.append(_y_error)
            self._angle_error.append(_angle_error)
            self._plot(self._position_x, self._position_y, line_type=self._line_type, draw=self._draw, grid=True,
                       x_lim=self._size_x, y_lim=self._size_y)
        except:
            File.log('Error with the message\r\n{}'.format(value))

    def _load_robot_id(self):
        try:
            logger.info('Reading RobotIDs file')
            if File.exist_file('Setup/RobotIDs.txt'):
                lines = File.read_file('Setup/RobotIDs.txt')
                if len(lines) > 0:
                    for line in lines:
                        self.robot_id.addItem(line.rstrip())
                else:
                    File.log('There are no parameters in the RobotIDs file')
        except FileNotFoundError as e:
            File.log(e)

    def _load_control_type(self):
        try:
            logger.info('Reading TypeControls file')
            lines = File.read_file('Setup/TypeControls.txt')
            if len(lines) > 0:
                for line in lines:
                    text = line.split(',')
                    self.control_type.addItem(text[1].rstrip())
            else:
                File.log('There are no parameters in the TypeControls file')
        except FileNotFoundError as e:
            File.log(e)

    def _configWindow(self):
        ConfigWindow(self)

    def _load_images(self):
        self.logo_gira.setPixmap(QPixmap('Graphics/Logo GIRA.png'))
        self.logo_u.setPixmap(QPixmap('Graphics/logo uptc negro.png'))
        self.vigilado.setPixmap(QPixmap('Graphics/vigilado_pos_jpg.png'))
        self.play_pause_button.setIcon(QIcon('Graphics/icons8-play-96.png'))
        self.clear_button.setIcon(QIcon('Graphics/icons8-erase-96.png'))
        self.discoveryButtom.setIcon(QIcon('Graphics/icons8-google-web-search-96.png'))

    def _stop_communication(self):
        self._zigbee.running = False
        self._zigbee.wait()
        if self._zigbee is not None and self._zigbee.is_open():
            self._zigbee.close()

        self._zigbee_connect = False

    def closeEvent(self, event):
        if self._zigbee and self._zigbee.is_open():
            self._stop_communication()
        super(MainWindow, self).closeEvent(event)
