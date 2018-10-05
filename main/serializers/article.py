# -*- coding: utf-8 -*-
from marshmallow import fields

from main.serializers.base import BaseSchema


class ArticleSchema(BaseSchema):
    title = fields.String(required=True)
    slug = fields.String()
    content = fields.String(required=True)
    user_id = fields.Integer(required=True)

    id = fields.Integer(dump_only=True)
    created_at = fields.DateTime(dump_only=True, required=True)
    updated_at = fields.DateTime(dump_only=True, required=True)
