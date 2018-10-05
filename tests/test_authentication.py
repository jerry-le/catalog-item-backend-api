# -*- coding: utf-8 -*-
import itertools
import json

from main.exceptions import LOGIN_BY_EMAIL_FAIL


def _register_user(testclient):
    data = {
        'username': 'jerry le',
        'email': 'test@gmail.com',
        'password': '12345678@ABC',
    }
    return testclient.post('/users', data=data)


class TestAuthentication(object):
    def test_register_user_by_email(self, testclient):
        resp = _register_user(testclient)
        data = json.loads(resp.data)
        print(data)
        assert resp.status_code == 201
        assert all(
            key in data
            for key in ['id', 'email', 'username', 'google_id', 'image_url',
                        'token']
        )

        # Register with existing email
        resp = _register_user(testclient)
        assert resp.status_code == 404

    def test_register_user_by_email_with_invalid_data(self, testclient):
        # Only the last combination data is valid
        combine_data = {
            'username': [None, '', 1234, 'jerry le'],
            'email': [None, '', 'not a email', 'test@gmail.com'],
            'password': [None, '', '1234567', '12345678']
        }
        combinations = itertools.product(*combine_data.values())

        num_valid_combine = 0
        for combination in combinations:
            data = dict((k, v) for k, v in zip(combine_data.keys(), combination))
            print(data)
            resp = testclient.post(
                '/users',
                data=data
            )
            num_valid_combine += 1 if resp.status_code != 400 else 0
            assert num_valid_combine <= 1

    def test_sign_in_by_email(self, testclient):
        # Register new user
        resp = _register_user(testclient)
        data = json.loads(resp.data)

        # Sign in registered user
        resp = testclient.post('/users/auth/email', data={
            'email': data.get('email'),
            'password': '12345678@ABC'
        })
        assert resp.status_code == 200

        # Sign in wrong password
        resp = testclient.post('/users/auth/email', data={
            'email': data.get('email'),
            'password': 'wrong password'
        })
        assert resp.status_code == 404
        assert (json.loads(resp.data)['message'] ==
                LOGIN_BY_EMAIL_FAIL['message'])

        # Sign in with not-existed email
        resp = testclient.post('/users/auth/email', data={
            'email': 'not.existed@email.com',
            'password': 'wrong password'
        })
        assert resp.status_code == 404
        assert (json.loads(resp.data)['message'] ==
                LOGIN_BY_EMAIL_FAIL['message'])
