"""
Politecnico di Torino, Information Systems, Semester of 2021-2022
Group 14, Buddy+

The models file of the service.

"""

from app import db
from sqlalchemy.orm import backref


# Association table for the many-to-many relationship of the User and Interests
interest_table = db.Table('interest_table',
    db.Column('user_id', db.Integer, db.ForeignKey('user.user_id'), 
        primary_key=True),
    db.Column('interest_id', db.Integer, 
        db.ForeignKey('interests.interest_id'), primary_key=True)
)


# Class modeling a single Interests object
class Interests(db.Model):
    __tablename__ = 'interests'
    interest_id = db.Column(db.Integer, primary_key=True)
    interest_descr = db.Column(db.Text, nullable=False)
    interest_name = db.Column(db.String(30), nullable=False)
    chosen_by_users = db.relationship('User', secondary=interest_table, 
        lazy='dynamic', backref='interested_in')

    def __repr__(self):
        return self


# Class modeling a single User object
class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(12), unique=True, nullable=False)
    email = db.Column(db.String(35), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(25), nullable=False)
    surname = db.Column(db.String(35), nullable=False)
    current_location = db.Column(db.String(35), nullable=False)
    nationality = db.Column(db.String(25), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    is_buddy = db.Column(db.Boolean, nullable=False)
    is_student = db.Column(db.Boolean, nullable=False)
    current_uni = db.Column(db.String(35), nullable=False)
    mother_tongue = db.Column(db.String(50), nullable=False)
    """
    Under construction for future implementations.

    given_reviews = db.relationship('Review', backref='user', lazy=True)
    event_participant = db.relationship('Event', backref='user', lazy=True)
    """
    def __repr__(self):
        return self


"""
Plenty of future implementations planned out, waiting for resources.



class Review(db.Model):
    __tablename__ = 'review'

    review_id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    stars = db.Column(db.Integer, nullable=False)
    post_date = db.Column(db.DateTime, nullable=False)
    # reviewee_id = db.Column(db.Integer, nullable=False)
    rewiever_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    reviewer = db.relationship('User')
    
    def __repr__(self):
        return self

review_table = db.Table(
    'review_table',
    db.Column('user_id')
)


event_table = db.Table(
    'event_table',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('event_id', db.Integer, db.ForeignKey('event.id'), primary_key=True),
)


class Event(db.Model):
    __tablename__ = 'event'

    event_id = db.Column(db.Integer, primary_key=True)
    event_location = db.Column(db.String(50), nullable=False)
    event_time = db.Column(db.DateTime, nullable=False)
    event_buddy_id = db.Column(db.String(50), db.ForeignKey('user.id'))
    event_buddy = db.relationship("User", backref=backref("request", uselist=False))
    event_participant = db.Column(db.String(50), nullable=True)
    
    
    def __repr__(self):
        return self
"""