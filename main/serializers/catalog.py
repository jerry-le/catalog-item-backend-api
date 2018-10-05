# -*- coding: utf-8 -*-

from marshmallow import fields

from .base import BaseSchema


class CatalogSchema(BaseSchema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
