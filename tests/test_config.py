# -*- coding: utf-8 -*-

from main.app import create_app
from main.config import ProdConfig, DevConfig, TestConfig


def test_production_config():
    app = create_app(ProdConfig)
    assert app.config['ENV'] == 'prod'


def test_development_config():
    app = create_app(DevConfig)
    assert app.config['ENV'] == 'dev'


def test_testing_config():
    app = create_app(TestConfig)
    assert app.config['ENV'] == 'test'
