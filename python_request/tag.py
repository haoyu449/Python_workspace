from python_request.wework import WeWork


class Tag(WeWork):
    def create_tag(self, name, id):
        req = {
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/tag/create',
            'method': 'POST',
            'params': {'access_token': self.token},
            'json': {"tagname": name, "tagid": id}
        }
        r = self.send(req)
        return r.json()

    def update_tag(self, name, id):
        req = {
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/tag/update',
            'method': 'POST',
            'params': {'access_token': self.token},
            'json': {"tagid": id, "tagname": name}
        }
        r = self.send(req)
        return r.json()

    def delete_tag(self, id):
        req = {
            'url': f'https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token={self.token}&tagid={id}',
            'method': 'GET'
        }
        r = self.send(req)
        print(r.json())
        return r.json()

    def get_tag_member(self, id):
        req = {
            'url': f'https://qyapi.weixin.qq.com/cgi-bin/tag/get?access_token={self.token}&tagid={id}',
            'method': 'get'
        }
        r = self.send(req)
        return r.json()

    def get_tag_list(self):
        req = {
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/tag/list',
            'method': 'GET',
            'params': {'access_token': self.token}
        }

        r = self.send(req)
        return r.json()

    def add_tag_member(self, id, user, list):
        req = {
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/tag/addtagusers',
            'method': 'POST',
            'params': {'access_token': self.token},
            'json': {"tagid": id, "userlist": [user], "partylist": [list]}
        }
        r = self.send(req)
        return r.json()

    def delete_tag_member(self, id, user, list):
        req = {
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/tag/deltagusers',
            'method': 'POST',
            'params': {'access_token': self.token},
            'json': {"tagid": id, "userlist": [user], "partylist": [list]}
        }
        r = self.send(req)
        return r.json()
