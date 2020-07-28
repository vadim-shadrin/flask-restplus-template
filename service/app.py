import os

import aerospike

from service.settings import Config

from flask import Flask

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    with app.app_context():
        app.aerospike = aerospike.client(app.config['AEROSPIKE_CONFIG']).connect()
        from service.api.restplus import bp as api_bp
        app.register_blueprint(api_bp)
        return app
