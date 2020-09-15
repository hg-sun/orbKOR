import os, sys
import configparser

class ConfigMgr:
    def __init__(self, current_path):
        self.config = configparser.ConfigParser()
        self.config.read(os.path.join(current_path, 'rsc', 'config', 'config.ini'))

    def getValue(self, session, key):
        return self.config[session][key]

    def getSession(self, session):
        return self.config[session]
