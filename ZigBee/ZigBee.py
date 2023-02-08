from PyQt5.QtCore import QThread, pyqtSignal

import json
import re
import time

from digi.xbee.devices import XBeeDevice

from enum import Enum

is_data_message = re.compile(r'^X: ?.+Y: ?.+Angle: ?.+$')
values_searching = re.compile(r'(?:[\w]+): ?(?P<x>[\d]*.?[\d]*) ?(?:[\w]+): ?(?P<y>[\d]*.?[\d]*) ?(?:[\w]+): ?'
                              r'(?P<angle>[\d]*.?[\d]*)')


class Message_type(Enum):
    Motor_Telem = 0
    Sensor_Telem = 1
    Lidar = 2
    Control_output = 3
    Home_cmd = 4
    Goal_cmd = 5
    Control_cmd = 6
    Status = 7
    Status_request = 8
    Stop_cmd = 9
    Star_cmd = 10
    Starting_pose = 11


class ZigBeeModule(QThread):
    read_update = pyqtSignal(str)

    def __init__(self, parameters):
        QThread.__init__(self)
        self._port = parameters[0]
        self._baud = parameters[1]
        self._zigbee = XBeeDevice(self._port, self._baud)
        self._zigbee.open()
        self._zigbee.flush_queues()
        self._x = 0.0
        self._y = 0.0
        self._angle = 0.0
        self._linear_velocity = 0.0
        self._angular_velocity = 0.0
        self._x_error = 0.0
        self._y_error = 0.0
        self._angle_error = 0.0
        self.running = True

    def run(self):
        self.running = True
        while self.running:
            QThread.msleep(1)
            xbee_message = self._zigbee.read_data()
            if xbee_message is not None:
                value = xbee_message.data.decode()[:-2]
                self.read_update.emit(value)

    def is_open(self):
        return self._zigbee.is_open()

    def open(self):
        self._zigbee.open()

    def close(self):
        self._zigbee.close()

    def read(self):
        return self._zigbee.readline().decode('ascii')
        
    def send(self, id_remote, message):
        xbee_network = self._zigbee.get_network()
        remote_device = xbee_network.discover_device(id_remote)
        self._zigbee.send_data_async(remote_device, message)
        
    def discover_ids(self):
        result = []
        xbee_network = self._zigbee.get_network()
        xbee_network.set_discovery_timeout(15)  # 15 seconds.
        xbee_network.clear()

        # Callback for discovered devices.
        def callback_device_discovered(remote):
            result.append(['Robot ' + str(len(result)), remote])
            print(result)

        # Callback for discovery finished.
        def callback_discovery_finished(status):
            if status == NetworkDiscoveryStatus.SUCCESS:
                print("Discovery process finished successfully.")
            else:
                print("There was an error discovering devices: %s" % status.description)
        xbee_network.add_device_discovered_callback(callback_device_discovered)
        xbee_network.add_discovery_process_finished_callback(callback_discovery_finished)
        xbee_network.start_discovery_process()
        print("Discovering remote XBee devices...")
        while xbee_network.is_discovery_running():
            time.sleep(0.1)
        return result

    def decode_message(self, message):
        json_structure = json.loads(message)
        print(json_structure['type'])
        if json_structure['type'] == Message_type.Motor_Telem.value:
            self._x = float(json_structure['body']['x']) / 1000
            self._y = float(json_structure['body']['y']) / 1000
            self._angle = float(json_structure['body']['t'])
            self._linear_velocity = float(json_structure['body']['lv'])
            self._angular_velocity = float(json_structure['body']['av'])
            self._x_error = float(json_structure['body']['xe'])
            self._y_error = float(json_structure['body']['ye'])
            self._angle_error = float(json_structure['body']['te'])
        return self._x, self._y, self._angle, self._linear_velocity, self._angular_velocity, self._x_error,\
               self._y_error, self._angle_error