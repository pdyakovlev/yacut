from datetime import datetime

from flask import url_for

from yacut import db


class URLMap(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    original: str = db.Column(db.String(256), nullable=False)
    short: str = db.Column(db.String(16))
    timestamp: datetime = db.Column(db.DateTime, default=datetime.utcnow())

    def to_dict(self):
        value = dict(
            url=self.original,
            short_link=url_for(
                'short_url', short=self.short, _external=True
            )
        )
        return value

    def from_dict(self, data):
        for key, value in zip(('original', 'short'), ('url', 'custom_id')):
            setattr(self, key, data[value])
