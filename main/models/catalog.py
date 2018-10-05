from main.databases import Model, TimestampMixin, PKMixin
from main.extensions import db


class CatalogModel(Model, PKMixin, TimestampMixin):
    __tablename__ = 'catalog'

    name = db.Column(db.String(80))

    # items = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self, *args, **kwargs):
        db.Model.__init__(self, *args, **kwargs)
