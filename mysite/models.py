from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

# create a new SQLAlchemy object
db = SQLAlchemy()

# Base model that for other models to inherit from
class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
            onupdate=db.func.current_timestamp())

# Model for poll topics
class Icon(Base):
    name = db.Column(db.String(500))
    tooltip_id = db.Column(db.Integer, db.ForeignKey('tooltip.id'))
    sprite_id = db.Column(db.Integer, db.ForeignKey('sprite.id'))
    tooltip = db.relationship('Tooltip', foreign_keys=[tooltip_id],
            backref=db.backref('icon', lazy='dynamic'))
    sprite = db.relationship('Sprite',foreign_keys=[sprite_id])


    # user friendly way to display the object
    def __repr__(self):
        return self.name

# Model for poll options
class Tooltip(Base):
    name = db.Column(db.String(200))

# Polls model to connect topics and options together
class Sprite(Base):

    # Columns declaration
    name = db.Column(db.String(200))
    title = db.Column(db.String(200))


    def __repr__(self):
        # a user friendly way to view our objects in the terminal
        return self.name
