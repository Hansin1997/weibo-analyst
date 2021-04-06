from flask import request
from flask_restful import Resource, reqparse
from sdk.weibo import Api

getUserParser = reqparse.RequestParser()
getUserParser.add_argument(
    "uid", type=str, nullable=True, required=False)


class User(Resource):
    def __init__(self):
        self.api = Api()

    def get(self):
        args = getUserParser.parse_args()
        return self.api.getUser(request.user['sub'], request.user['access_token'])
