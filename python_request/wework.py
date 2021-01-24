import requests

from python_request.base_api import BaseApi


class WeWork(BaseApi):
    def __init__(self, secret):
        self.token = self.get_token(secret=secret)

    def get_token(self, secret):
        req = {
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            'params': {
                'corpid': 'ww5a4380a0a967f488',
                'corpsecret': secret
            },
            'method': 'GET'

        }

        r = self.send(req)
        return r.json()['access_token']
