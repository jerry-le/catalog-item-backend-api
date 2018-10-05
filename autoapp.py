# -*- coding: utf-8 -*-
"""Create application instance"""

from main.app import create_app
from main.config import config

CONFIG = config['default']

app = create_app(CONFIG)
