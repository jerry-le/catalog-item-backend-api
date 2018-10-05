# -*- coding: utf-8 -*-
import json

from main.exceptions import CATALOG_NOT_FOUND
from main.models.catalog import CatalogModel


class TestCatalogViews(object):

    def test_create_catalog(self, testclient):
        data = {
            'name': 'Music'
        }
        resp = testclient.post('/catalogs', data=data)
        assert resp.status_code == 201
        assert 'id' in json.loads(resp.data)
        assert json.loads(resp.data).get('name') == 'Music'

    def test_get_catalogs(self, testclient):
        CatalogModel(name='Catalog 1').save()
        CatalogModel(name='Catalog 2').save()

        resp = testclient.get('/catalogs')
        assert resp.status_code == 200
        assert len(json.loads(resp.data)) == 2

    def test_delete_catalog(self, testclient):
        # Test delete non-existing catalog
        resp = testclient.delete(
            '/catalogs/{}'.format(1),
        )
        assert resp.status_code == 404
        assert json.loads(resp.data)['message'] == CATALOG_NOT_FOUND['message']

        # Test delete success
        catalog = CatalogModel(name='Catalog 1')
        catalog.save()
        resp = testclient.delete(
            '/catalogs/{}'.format(catalog.id),
        )
        assert resp.status_code == 204

    def test_get_catalog(self, testclient):
        catalog = CatalogModel(name='Catalog 1')
        catalog.save()

        res = testclient.get(
            '/catalogs/{}'.format(catalog.id)
        )
        assert res.status_code == 200

    def test_update_catalog(self, testclient):
        # Test update success
        catalog = CatalogModel(name='Catalog 1')
        catalog.save()

        res = testclient.put(
            '/catalogs/{}'.format(catalog.id),
            data={'name': 'Catalog 2'},
        )
        assert res.status_code == 200
        assert json.loads(res.data).get('name') == 'Catalog 2'

        # Test update with invalid data
        resp = testclient.put(
            '/catalogs/{}'.format(catalog.id),
            data={'wrong_schema': 'Catalog 2'},
        )
        assert resp.status_code == 400
        assert (json.loads(resp.data)['more_info']['name'] ==
                ['Missing data for required field.'])
