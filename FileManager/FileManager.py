from FileManager.XlsxFile import XlsFile
from FileManager.YamlFile import FileYaml

import os.path
import yaml
import datetime
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def read_xls_file(path):
    try:
        xls_file = XlsFile(path)
        x, y, angle, timestamp = xls_file.read_position()
    except:
        log('Error opening data {}'.format(path))
        x = None
        y = None
        angle = None
        timestamp = None
    return x, y, angle, timestamp


def save_data_file(path, x, y, angle, timestamp, linear_velocity, angular_velocity, x_error, y_error, angle_error):
    result = None
    try:
        xls_file = XlsFile(path)
        xls_file.save_position(x, y, angle, timestamp, linear_velocity, angular_velocity, x_error, y_error, angle_error)
        result = True
    except:
        log('Error saving data in {}'.format(path))
        result = False
    return result


def exist_file(file):
    is_file = os.path.isfile(file)
    if is_file:
        logger.info('File {} exists'.format(file))
    else:
        logger.info('File {} does not exist'.format(file))
    return is_file
    
    
def create_file(file, lines):
    logger.info('Creating {} file'.format(file))
    with open(file, 'w') as f:
        for line in lines:
            f.write('{}\r\n'.format(line))
            
            
def read_file(file):
    logger.info('Reading file {}'.format(file))
    result = []
    with open(file, 'r') as f:
        for line in f.readlines():
            result.append(line)
    return result


def create_configuration(file='Setup/config.yaml', data={'baud': 9600, 'port': 'COM3'}):
    logger.info('Creating the configuration file')
    with open(file, 'w') as f:
        yaml.dump(data, f)
        

def read_configuration():
    baud = None
    port = None
    try:
        logger.info('Reading configuration file')
        configuration = FileYaml()
        baud = configuration.baud
        port = configuration.port
    except:
        log('Error reading the configuration file')
    return port, baud


def log(error, file='log.txt'):
    logger.info('Saving an error in the log file')
    now = datetime.datetime.now().strftime('%Y_%m_%d %H:%M')
    with open(file, mode='a') as f:
        f.write('******************************************************************************************************'
                '*****************\r\n')
        f.write('{}\r\n'.format(now))
        f.write('{}\r\n'.format(error))
        f.write('******************************************************************************************************'
                '*****************\r\n')
