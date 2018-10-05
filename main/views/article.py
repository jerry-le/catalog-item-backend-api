# -*- coding: utf-8 -*-
from flask import Blueprint
from flask_apispec import use_kwargs, marshal_with
from sqlalchemy.exc import IntegrityError

from main.exceptions import InvalidUsage
from main.extensions import db
from main.models.article import ArticleModel
from main.serializers.article import ArticleSchema

blueprint = Blueprint('article', __name__)


@blueprint.route('/articles', methods=['POST'])
@use_kwargs(ArticleSchema())
@marshal_with(ArticleSchema())
def create_article(**kwargs):
    try:
        article = ArticleModel(**kwargs).save()
    except IntegrityError:
        db.session.rollback()
        raise InvalidUsage.article_slug_already_existed()

    return article, 201
