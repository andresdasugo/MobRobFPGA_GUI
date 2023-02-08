import serial
import sys


def scan(ports=20):
    SerialDevices = []
    platform = sys.platform
    serial_name = 'COM{}' if platform == 'win32' else '/dev/ttyACM{}'
    for i in range(ports):
        try:
            port = serial_name.format(str(i))
            s = serial.Serial(port)
            SerialDevices.append(s.portstr)
            s.close()
        except:
            pass
    return SerialDevices
