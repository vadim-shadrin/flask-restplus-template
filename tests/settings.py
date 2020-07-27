from mb_api.settings import Config


class TestConfig(Config):
    TESTING = True
    DEBUG = True
    # ES_SERVER = {
    #     'url': 'http://localhost', 'port': 9200, 'timeout': 120, 'http_auth': {'login': 'beta', 'password': '443322'}
    #     }
