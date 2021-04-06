from flask import request
from flask_restful import Resource, reqparse
from sdk.weibo import Api
from sdk.process.Task import Task
import math

parser = reqparse.RequestParser()
parser.add_argument(
    "id", type=str, nullable=False, required=True)
parser.add_argument(
    "limit", type=int, nullable=True, required=False)


class CommentTask(Resource):
    def __init__(self):
        self.api = Api()

    def post(self):
        args = parser.parse_args()
        count = self.api.getCommentCount(
            args.get('id'), request.user['access_token'])
        limit = args.get('limit')
        process_count = 0
        t = Task()
        try:
            for index in range(1, math.ceil(count / 200)):
                comments = self.api.getComment(
                    args.get('id'), request.user['access_token'], index)
                for comment in comments:
                    t.append(comment['text'])
                    process_count += 1
                    if not (limit is None) and process_count >= limit:
                        break

        except Exception as e:
            print(e)
        return {
            "data": t.process(),
            "count": count,
            "process_count": process_count
        }
