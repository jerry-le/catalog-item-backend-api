from flask import Blueprint
from flask_apispec import use_kwargs, marshal_with

from main.exceptions import InvalidUsage
from main.models.catalog import CatalogModel
from main.serializers.catalog import CatalogSchema

blueprint = Blueprint('catalog', __name__)


@blueprint.route('/catalogs/<int:catalog_id>', methods=('GET',))
@marshal_with(CatalogSchema())
def get_catalog(catalog_id):
    catalog = CatalogModel.query.get(catalog_id)
    if not catalog:
        return InvalidUsage.catalog_not_found()
    return catalog


@blueprint.route('/catalogs/<int:catalog_id>', methods=('PUT',))
@use_kwargs(CatalogSchema())
@marshal_with(CatalogSchema())
def update_catalog(catalog_id, **kwargs):
    catalog = CatalogModel.query.get(catalog_id)

    if not catalog:
        raise InvalidUsage.catalog_not_found()

    catalog.update(**kwargs)
    return catalog


@blueprint.route('/catalogs/<int:catalog_id>', methods=('DELETE',))
def delete_catalog(catalog_id):
    catalog = CatalogModel.query.get(catalog_id)
    if not catalog:
        raise InvalidUsage.catalog_not_found()

    catalog.delete()
    return '', 204


@blueprint.route('/catalogs', methods=('POST',))
@use_kwargs(CatalogSchema())
@marshal_with(CatalogSchema())
def create_catalog(**kwargs):
    catalog = CatalogModel.query.filter_by(**kwargs).one_or_none()

    if catalog:
        raise InvalidUsage.catalog_already_existed()

    catalog = CatalogModel(**kwargs).save()
    return catalog, 201


@blueprint.route('/catalogs', methods=('GET',))
@marshal_with(CatalogSchema(many=True))
def get_catalogs():
    catalogs = CatalogModel.query.all()
    # TODO: paging, sorting, filtering, field selection
    # https://blog.mwaysolutions.com/2014/06/05/10-best-practices-for-better-restful-api/
    return catalogs
