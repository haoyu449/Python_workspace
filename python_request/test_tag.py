import pytest
import requests
import yaml

from python_request.tag import Tag


class Test_tag:
    def setup_class(self):
        conf = yaml.safe_load(open('conf.yaml'))
        secret = conf['corpsecret']
        self.tag = Tag(secret=secret)

    # 创建标签，断言
    @pytest.mark.parametrize('name,id', [('TU', '8'),
                                         ('TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT', '2')
                                         ])
    def test_create_tag(self, name, id):
        r = self.tag.create_tag(name=name, id=id)
        if len(name) > 32:
            assert r['errcode'] == 40058
        else:
            assert r['errcode'] == 0

    # 更新标签，获取标签列表，断言
    @pytest.mark.parametrize('name,id', [('TI', '11')])
    def test_update_tag(self, name, id):
        self.tag.update_tag(name=name, id=id)
        r2 = self.tag.get_tag_list()
        tag_list = self.tag.jsonpath_res(r2, '$..tagname')
        tag_name = self.tag.jsonpath_res(r2, '$..taglist[?(@.tagid==11)].tagname')[0]
        # print(tag_list)
        # print(tag_name)
        assert name in tag_list
        assert name == tag_name

    # 删除标签，断言
    @pytest.mark.parametrize('id', ['8'])
    def test_delete_tag(self, id):
        r = self.tag.delete_tag(id=id)
        assert r['errcode'] == 0

    # 获取标签成员，断言
    @pytest.mark.parametrize('id', ['10'])
    def test_get_tag_member(self, id):
        r = self.tag.get_tag_member(id=id)
        assert r['errmsg'] == 'ok'

    # 新增标签成员，获取标签成员，断言
    @pytest.mark.parametrize('id,user,list', [('12', ['test_6', "test_8"], '3')])
    def test_add_tag_member(self, id, user, list):
        self.tag.add_tag_member(id=id, user=user, list=list)
        member_list = self.tag.get_tag_member(id=id)
        r = self.tag.jsonpath_res(member_list, '$..name')
        assert 'test_6', 'test_8' in r

    # 删除标签成员，断言
    @pytest.mark.parametrize('id,user,list', [('12', 'test_6', '3')])
    def test_delete_tag_member(self, id, user, list):
        r = self.tag.delete_tag_member(id=id, user=user, list=list)
        assert r['errmsg'] == 'deleted'
