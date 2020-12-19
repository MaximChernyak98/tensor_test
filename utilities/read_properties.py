import configparser
import os

config = configparser.RawConfigParser()
path_to_configuration = os.path.join('.', 'configurations', 'config.ini')
config.read(path_to_configuration)


class ReadConfig:
    @staticmethod
    def get_yandex_search_url():
        url = config.get('common info', 'yandex_search_URL')
        return url

    @staticmethod
    def get_yandex_pictures_url():
        url = config.get('common info', 'yandex_pictures_URL')
        return url
