from flask import Flask, jsonify, request
from flask_restful import Api
from flask_cors import CORS
from sdk.config import Config
from api.Token import Token, TokenDecoder
from api.User import User
from api.Timeline import Timeline
from api.CommentTask import CommentTask

app = Flask(__name__)
restapp = Api(app)
cors = CORS(app)

config = Config("config.yaml")
decoder = TokenDecoder(config)


@app.before_request
def checkToken():
    if request.method == "OPTIONS":
        return None
    if request.path == '/token' or request.path == "/meta":
        return None
    token = request.headers.get("Authorization")
    if token is None:
        raise Exception("Unauthorized")
    if not token.startswith("Bearer "):
        raise Exception("Token is not bearer")
    jwt = token[7:]
    playload = decoder.decode(jwt)
    request.user = playload
    return None


restapp.add_resource(Token, "/token", resource_class_args=[config])
restapp.add_resource(User, "/user")
restapp.add_resource(Timeline, "/timeline")
restapp.add_resource(CommentTask, "/task/comment")
