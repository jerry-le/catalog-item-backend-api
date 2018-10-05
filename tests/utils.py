# -*- coding: utf-8 -*-
import json


def get_api_headers(access_token=None):
    return {
        # 'Authorization': 'JWT ' + access_token,
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }


class TestClient(object):

    def __init__(self, flask_test_client):
        self.testclient = flask_test_client

    def post(self, url, data, headers=None, content_type='application/json'):
        return self.testclient.post(
            url,
            data=json.dumps(data),
            headers=headers or get_api_headers(),
            content_type=content_type
        )

    def get(self, url, headers=None, content_type='application/json'):
        return self.testclient.get(
            url,
            headers=headers or get_api_headers(),
            content_type=content_type
        )

    def delete(self, url, headers=None, content_type='application/json'):
        return self.testclient.delete(
            url,
            headers=headers or get_api_headers(),
            content_type=content_type
        )

    def put(self, url, data, headers=None, content_type='application/json'):
        return self.testclient.put(
            url,
            headers=headers or get_api_headers(),
            data=json.dumps(data),
            content_type=content_type
        )


def create_user():
    pass
