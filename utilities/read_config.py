from configparser import RawConfigParser

config = RawConfigParser()
config.read("C:/PythonProject2/configurations/config.ini")

class Configurations:
    @staticmethod
    def get_url():
        url = config.get('admin','Home_page_url')
        return url
