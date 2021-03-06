from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from flask_security import UserMixin, RoleMixin
import datetime

#   https://pythonhosted.org/Flask-Security/quickstart.html
#   python manage.py db upgrade && python manage.py db revision --autogenerate


db = SQLAlchemy()


class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.TIMESTAMP, default=func.current_timestamp())
    date_modified = db.Column(db.TIMESTAMP, default=func.current_timestamp(),
                              onupdate=func.current_timestamp())


roles_users = db.Table('roles_users',
                       db.Column('final_user_id', db.Integer(),
                                 db.ForeignKey('final_user.id')),
                       db.Column('role_id', db.Integer(),
                                 db.ForeignKey('role.id')))


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class FinalUser(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    social_id = db.Column(db.String(64), nullable=True, unique=True)
    email = db.Column(db.String(255), unique=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(255))
    create_date = db.Column(db.DateTime, default=datetime.datetime.now)
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(45))
    current_login_ip = db.Column(db.String(45))
    login_count = db.Column(db.Integer)
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))


# Code for desmostration the flask upload


class FinalUserImage(BaseModel):
    __tablename__ = 'final_user_image'
    user_id = db.Column(db.Integer, db.ForeignKey('final_user.id'))
    image_filename = db.Column(db.Text(), default=None, nullable=True)
    image_url = db.Column(db.Text(), default=None, nullable=True)


class Vehicle(db.Model):
    __tablename__ = 'vehicle'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    year = db.Column(db.String(4), default=None, nullable=False)
    type = db.Column(db.Text(), default=None, nullable=True)
    brand = db.Column(db.Text(), default=None, nullable=False)
    model = db.Column(db.Text(), default=None, nullable=False)
    fuel_type = db.Column(db.Text(), default=None, nullable=True)
    transmision = db.Column(db.Text(), default=None, nullable=False)
    kilometrage = db.Column(db.Integer(), default=None, nullable=False)
    motor = db.Column(db.Float(), default=None, nullable=False)
    color = db.Column(db.Text(), default=None, nullable=True)
    power = db.Column(db.Integer(), default=None, nullable=True)
    doors = db.Column(db.Integer(), default=None, nullable=True)
    state = db.Column(db.Text(), default=None, nullable=True)
    price = db.Column(db.Float(), default=None, nullable=True)
    isPublication = db.Column(db.Boolean(), default=None, nullable=False)
