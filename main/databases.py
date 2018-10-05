# -*- coding: utf-8 -*-
from datetime import datetime

from flask_sqlalchemy import Model
from sqlalchemy.orm import relationship

from main.extensions import db


class CRUDMixin(Model):
    """Mixin that adds convenience methods for CRUD (create, read, update,
    delete) operations.
    """

    @classmethod
    def create(cls, **kwargs):
        """Create a new record and save it the database."""
        instance = cls(**kwargs)
        return instance.save()

    def update(self, commit=True, **kwargs):
        """Update specific fields of a record."""
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        return commit and self.save() or self

    def save(self, commit=True):
        """Save the record."""
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def delete(self, commit=True):
        """Remove the record from the database."""
        db.session.delete(self)
        return commit and db.session.commit()


class TimestampMixin(object):
    """Inherit this class to automatically create 2 fields: `created_at` and
    `updated_at` in the database.  The `updated_at` is updated whenever any
    fields changed.
    """

    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow,
                           onupdate=datetime.utcnow, nullable=False)


class PKMixin(object):
    """
    From Mike Bayer's "Building the app" talk
    https://speakerdeck.com/zzzeek/building-the-app

    A mixin that adds a surrogate integer 'primary key' column named ``id`` to
    any declarative-mapped class.
    """

    id = db.Column(db.Integer, primary_key=True)


db.Model = db.make_declarative_base(CRUDMixin, None)
Model = db.Model
relationship = relationship
