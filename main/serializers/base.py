# -*- coding: utf-8 -*-


import logging

import bleach
from marshmallow import Schema, post_dump

from main.exceptions import InvalidSchema


class BaseSchema(Schema):
    def handle_error(self, error, data):
        """Log and raise our custom exception when (de)serialization fails."""

        logging.error(error.messages)
        raise InvalidSchema.invalid_schema(error.messages)

    class Meta:
        strict = True

    @post_dump
    def prevent_xss(self, data):
        for k, v in data.items():
            try:
                data[k] = bleach.clean(v)
            except TypeError:
                logging.warning('Cannot clean content {}'.format(v))
        return data
