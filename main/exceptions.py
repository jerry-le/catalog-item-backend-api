# -*- coding: utf-8 -*-

from flask import jsonify


def template(message, status_code=500, info=None):
    """Error payload template. This is based on the idea of Twilio.

    For more detail: https://blog.restcase.com/rest-api-error-codes-101/
    """

    return {
        'status_code': status_code,
        'message': message,
        # 'code': custom_code, # custom code is not necessary for now
        'more_info': info,
    }


#: Common errors
UNKNOWN_ERROR = template('Unknown errors', status_code=500)

#: Catalog errors
CATALOG_NOT_FOUND = template('Catalog not found', status_code=404)
CATALOG_ALREADY_EXISTED = template('Catalog has already existed',
                                   status_code=404)

#: Article errors
SLUG_ALREADY_EXISTED = template('The slug is already existed. Please choose the '
                                'other one, or let the system create it '
                                'automatically for you', status_code=404)

#: User errors
USER_NOT_FOUND = template('User not found', status_code=404)
USER_ALREADY_EXISTED = template('User has already existed', status_code=404)

#: Authentication errors
LOGIN_BY_EMAIL_FAIL = template('Email or password is not correct!',
                               status_code=404)


class BaseError(Exception):
    def __init__(self, **kwargs):
        Exception.__init__(self)
        self.payload = kwargs
        self.status_code = kwargs['status_code']

    def to_json(self):
        rv = self.payload
        return jsonify(rv)


class InvalidUsage(BaseError):
    def __init__(self, **kwargs):
        BaseError.__init__(self, **kwargs)

    @classmethod
    def unknown_error(cls):
        return cls(**UNKNOWN_ERROR)

    @classmethod
    def catalog_not_found(cls):
        return cls(**CATALOG_NOT_FOUND)

    @classmethod
    def catalog_already_existed(cls):
        return cls(**CATALOG_NOT_FOUND)

    @classmethod
    def user_not_found(cls):
        return cls(**USER_NOT_FOUND)

    @classmethod
    def user_already_existed(cls):
        return cls(**USER_ALREADY_EXISTED)

    @classmethod
    def article_slug_already_existed(cls):
        return cls(**SLUG_ALREADY_EXISTED)


class InvalidSchema(BaseError):
    def __init__(self, **kwargs):
        BaseError.__init__(self, **kwargs)

    @classmethod
    def invalid_schema(cls, data):
        return cls(**template('Invalid schema', status_code=400, info=data))


class AuthenticationError(BaseError):
    def __init__(self, **kwargs):
        BaseError.__init__(self, **kwargs)

    @classmethod
    def login_by_email_fail(cls):
        return cls(**LOGIN_BY_EMAIL_FAIL)
