import requests
import json


class Api:
    def getTokens(self, code, redirect_uri, client_id, client_secret):
        rep = requests.post("https://api.weibo.com/oauth2/access_token",
                            data={
                                "client_id": client_id,
                                "client_secret": client_secret,
                                "grant_type": "authorization_code",
                                "redirect_uri": redirect_uri,
                                "code": code
                            })
        if rep.status_code >= 200 and rep.status_code <= 299:
            return rep.text
        else:
            raise Exception(rep.text)

    def getToken(self, code, redirect_uri, client_id, client_secret):
        return json.loads(self.getTokens(code, redirect_uri, client_id, client_secret))

    def getUser(self, uid, access_token):
        rep = requests.get("https://api.weibo.com/2/users/show.json", params={
            "access_token": access_token,
            "uid": uid
        })
        if rep.status_code >= 200 and rep.status_code <= 299:
            return json.loads(rep.text)
        else:
            raise Exception(rep.text)

    def getTimeline(self, access_token, page):
        rep = requests.get("https://api.weibo.com/2/statuses/home_timeline.json", params={
            "access_token": access_token,
            "count": 100,
            "page": page
        })

        if rep.status_code >= 200 and rep.status_code <= 299:
            return json.loads(rep.text)
        else:
            raise Exception(rep.text)

    def getCommentCount(self, idd, access_token):
        rep = requests.get("https://api.weibo.com/2/statuses/count.json", params={
            "access_token": access_token,
            "ids": idd
        })

        if rep.status_code >= 200 and rep.status_code <= 299:
            tmp = json.loads(rep.text)
            if len(tmp) == 0:
                raise Exception("Comment dosen't exists")
            return tmp[0]['comments']
        else:
            raise Exception(rep.text)

    def getComment(self, idd, access_token, page):
        rep = requests.get("https://api.weibo.com/2/comments/show.json", params={
            "access_token": access_token,
            "id": idd,
            "count": 200,
            "page": page,
            "trim_user": 1
        })

        if rep.status_code >= 200 and rep.status_code <= 299:
            return json.loads(rep.text)['comments']
        else:
            raise Exception(rep.text)
