import configparser
import os

config = configparser.RawConfigParser()
path_to_configuration = os.path.join('.', 'configurations', 'config.ini')
config.read(path_to_configuration)


class ReadConfig:
    @staticmethod
    def get_application_url():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def get_username():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def get_password():
        password = config.get('common info', 'password')
        return password
