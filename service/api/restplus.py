import logging

from flask import Blueprint, current_app
from flask_restplus import Api

from service.api.namespaces.v1.users_ns import api as users

log = logging.getLogger(__name__)

bp = Blueprint('api', __name__, url_prefix='/v1')
api = Api(bp, version='1', title='Skylove Events API',
          description='Skylove API service')

api.add_namespace(users)

@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)

    if not current_app.debug:
        return {'message': message}, 500
