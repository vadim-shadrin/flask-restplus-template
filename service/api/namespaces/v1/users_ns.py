from flask_restplus import Resource, Namespace, reqparse
from flask import request
from sevice.api.repo.user import User

import requests

api = Namespace('users', description='Users')

@api.route('/online')
class Online(Resource):
    @api.doc('online')
    def get(self):
        user_id = request.args.get('user_id')
        user = User().user_online(user_id)
        return {"user": user}, 200

@api.route('/is_online')
class isOnline(Resource):
    @api.doc('is_online')
    def get(self):
        user_id = request.args.get('user_id')
        user = User().is_user_online(user_id)
        return {"user": user}, 200
