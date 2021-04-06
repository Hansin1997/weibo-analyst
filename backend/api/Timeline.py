from flask import request
from flask_restful import Resource, reqparse
from sdk.weibo import Api

getUserParser = reqparse.RequestParser()
getUserParser.add_argument(
    "page", type=str, nullable=True, required=False, default=1)


class Timeline(Resource):
    def __init__(self):
        self.api = Api()

    def get(self):
        args = getUserParser.parse_args()
        return self.api.getTimeline(request.user['access_token'], args.get("page"))
