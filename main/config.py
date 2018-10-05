import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # Secrete key for encoding and decoding access token
    # TODO: Move hard code config into ENV config
    SECRET_KEY = 'REPLACE THIS WITH SUPER SECRET KEY'

    # Living time of access token is 1 year
    JWT_EXPIRATION_DELTA = timedelta(seconds=60 * 60 * 24 * 365)
    JWT_SECRET_KEY = 'KAJDJKHUWHIUWHDUWHDO118hNKJANDJKNASKJDN'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Allow cross-origin resource sharing on these urls
    CORS_ORIGIN_WHITELIST = [
        'http://0.0.0.0:5000'
    ]


class DevConfig(Config):
    ENV = 'dev'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}' \
        .format(os.path.join(basedir, 'data-dev.db'))


class TestConfig(Config):
    ENV = 'test'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


class ProdConfig(Config):
    ENV = 'prod'
    # Allow flask restful return JSON exception
    PROPAGATE_EXCEPTIONS = True

    # SQLALCHEMY_DATABASE_URI = 'sqlite:///{}' \
    #     .format(os.path.join(basedir, 'data.db'))

    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1/catalog_item'


config = {
    'develop': DevConfig,
    'testing': TestConfig,
    'product': ProdConfig,

    'default': ProdConfig
}
