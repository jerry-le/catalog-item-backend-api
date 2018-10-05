# -*- coding: utf-8 -*-
import json

from main.models.user import UserModel


def _create_article(testclient, user):
    data = {
        'title': 'This is a blog ...',
        'content': 'This is the blog content ...',
        'user_id': user.id
    }
    resp = testclient.post('/articles', data=data)
    return resp


class TestArticleView(object):
    def test_create_article(self, testclient, user):
        # Let the user post a new article
        resp = _create_article(testclient, user)
        first_article = json.loads(resp.data)
        print(first_article)
        print(first_article.keys())
        assert all(
            key in first_article
            for key in ['id', 'created_at', 'updated_at', 'slug', 'title',
                        'user_id']
        )
        assert resp.status_code == 201

        # Now, he/she create another article with the same title. The system
        # should generate different slug for him/her
        # TODO: Why user is only used 1 time
        resp = _create_article(testclient, user)
        assert resp.status_code == 201
        second_article = json.loads(resp.data)
        assert second_article['slug'] != first_article['slug']
