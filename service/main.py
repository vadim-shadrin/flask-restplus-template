import traceback

from flask import request, Response, json

from service.app import create_app

from time import strftime

app = create_app()

@app.errorhandler(Exception)
def exceptions(e):
    app.aerospike.close()
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

app.logger.info('>>>>> Starting development server at http://{}/<<<<<'.format(app.config['FLASK_SERVER_NAME']))

if __name__ == "__main__":
    app.run(debug=app.config['DEBUG'], host='0.0.0.0', port=app.config['PORT'])
