import traceback
from time import strftime

from flask import Flask, request, Response, json

from service.settings import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    with app.app_context():
        from service.api.restplus import bp as api_bp
        app.register_blueprint(api_bp)

        @app.errorhandler(Exception)
        def exceptions(e):
            tb = traceback.format_exc()
            timestamp = strftime('[%Y-%b-%d %H:%M]')
            app.logger.error(
                '%s %s "%s %s" [%s] 5xx INTERNAL SERVER ERROR\n%s',
                timestamp,
                request.remote_addr,
                request.method,
                request.full_path,
                request.scheme,
                tb
            )
            return e

        @app.route("/health_check")
        def health_check():
            """
            Health check
            ---
            tags:
                - util
            responses:
                200:
                    description: Returns "OK"
            """
            return Response("OK", content_type="text/plain")

        @app.route("/access-denied")
        def access_denied():
            return Response(json.dumps({"error": "access-denied"}), content_type='application/json', status=403)

        @app.route("/token-required")
        def token_required():
            return Response(json.dumps({"error": "token-required"}), content_type='application/json', status=403)

    return app
