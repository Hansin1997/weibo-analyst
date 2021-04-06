from flask import request
from flask_restful import Resource, reqparse
from sdk.weibo import Api
import jwt
import time

getTokenParser = reqparse.RequestParser()
getTokenParser.add_argument(
    "code", type=str, nullable=False, required=True)
getTokenParser.add_argument(
    "redirect_uri", type=str, nullable=False, required=True)
getTokenParser.add_argument(
    "client_id", type=str, nullable=False, required=True)
getTokenParser.add_argument(
    "client_secret", type=str, nullable=False, required=True)


class TokenDecoder:
    def __init__(self, config):
        self.config = config.data

    def decode(self, token):
        playload = jwt.decode(
            token, self.config['jwt']['secret'], verify=True,  algorithms=['HS256'])
        return playload


class Token(Resource):
    def __init__(self, config):
        self.config = config.data
        self.api = Api()

    def get(self):
        args = getTokenParser.parse_args()
        accessToken = self.api.getToken(
            args.get("code"), args.get("redirect_uri"), args.get("client_id"), args.get("client_secret"))
        iat = int(time.time()*1000)
        exp = iat + int(accessToken['expires_in'])
        playload = {
            "access_token": accessToken['access_token'],
            "sub": accessToken['uid'],
            "isRealName": accessToken['isRealName'],
            "exp": int(exp/1000),
            "iat": int(iat/1000)
        }
        return {
            "jwt": jwt.encode(playload, self.config['jwt']['secret']),
            "access_token": accessToken['access_token'],
            "expired_at": exp,
            "uid": accessToken['uid']
        }
