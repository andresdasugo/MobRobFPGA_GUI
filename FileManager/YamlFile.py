import yaml


class FileYaml:
    def __init__(self, file='Setup/config.yaml'):
        with open(file, mode='r') as f:
            self._config = yaml.load(f, Loader=yaml.FullLoader)
        self._port = self._config['port']
        self._baud = self._config['baud']

    @property
    def baud(self):
        return self._baud

    @property
    def port(self):
        return self._port
