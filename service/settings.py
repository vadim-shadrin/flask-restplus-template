import os


class RestplusConfig(object):
    SWAGGER_UI_DOC_EXPANSION = 'list'
    RESTPLUS_VALIDATE = True
    RESTPLUS_MASK_SWAGGER = False
    ERROR_404_HELP = False
    API_VERSION = 'v1'


class Config(RestplusConfig):
    FLASK_SERVER_NAME = '0.0.0.0:8888'  # NOT SERVER_NAME !!!
    PORT = int(os.environ.get('APP_PORT', 5000))
    DEBUG = True  # Do not use debug mode in production
    FLASK_DEBUG_DISABLE_STRICT = True
    SECRET_KEY = 'devkey'
    AEROSPIKE_CONFIG = { 
        'hosts': [
            (os.getenv('AEROSPIKE_HOST'), int(os.getenv('AEROSPIKE_PORT')))
        ],
        'policies': { 'timeout': 1000 },
    }

    # ES_SERVER = {'url': os.environ.get('ELASTIC_URL', 'http://elastic.beta.seomator.com'),
    #              'port': os.environ.get('ELASTIC_PORT', 80),
    #              'timeout': os.environ.get('ELASTIC_TIMEOUT', 120),
    #              'http_auth': {
    #                  'login': os.environ.get('ELASTIC_LOGIN', 'beta'),
    #                  'password': os.environ.get('ELASTIC_PASSWORD', '443322')}
    #              }
