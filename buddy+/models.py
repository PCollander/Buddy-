from app import db
from sqlalchemy.orm import relationship

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(12), unique=True, nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    current_location = db.Column(db.String(50), nullable=False)
    nationality = db.Column(db.String(50), nullable=False)
    date_of_birth = db.Column(db.DateTime, nullable=False) #the class diagram needs changing
    is_buddy = db.Column(db.Boolean, nullable=False)
    is_student = db.Column(db.Boolean, nullable=False)
    current_uni= db.Column(db.String(50), nullable=False)
    mother_tongue = db.Column(db.String(50), nullable=False)
    #given_reviews = db.relationship('Review', backref='user', lazy=True)
    chosen_interests = relationship('Interest', backref='user', lazy=True)
    event_participant = relationship('Event', backref='user', lazy=True)

class Review():
    
    review_id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    stars = db.Column(db.Integer, nullable=False) #has to be given as a dropown to ensure correct value range
    post_date = db.Column(db.DateTime, nullable=False)
    #reviewee_id = db.Column(db.Integer, nullable=False)
    #rewiever_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

interest_table = db.Table('interest_table',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), nullable=False),
    db.Column('interest_id', db.Integer, db.ForeignKey('interest.id'), nullable=False)
)

class Interest():

    interest_id = db.Column(db.Integer, primary_key=True)
    interest_descr = db.Column(db.Text, nullable=False)
    interest_name = db.Column(db.String(30), nullable=False)
    chosen_by_users = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

event_table = db.Table('event_table',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('event_id', db.Integer, db.ForeignKey('event.id'), primary_key=True),

)

class Event():

    event_id = db.Column(db.Integer, primary_key=True)
    event_location = db.Column(db.String(50), nullable=False)
    event_time = db.Column(db.DateTime, nullable=False)
    event_buddy = #something clever
    event_participant = #something clever
