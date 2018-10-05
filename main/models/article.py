from slugify import slugify

from main.databases import Model, PKMixin, TimestampMixin, relationship
from main.extensions import db


class ArticleModel(Model, PKMixin, TimestampMixin):
    __tablename__ = 'item'

    title = db.Column(db.String(256), nullable=False)
    slug = db.Column(db.Text, unique=True, nullable=False)
    content = db.Column(db.Text)
    user_id = db.Column(db.ForeignKey('user.id'), nullable=False)
    user = relationship('UserModel', backref=db.backref('articles'))

    def __init__(self, *args, **kwargs):
        if not kwargs.get('slug'):
            # If users doesn't specify the slug, we will generate it for them
            kwargs['slug'] = slugify(kwargs['title'])

        db.Model.__init__(self, *args, **kwargs)
