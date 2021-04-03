from settings import *
import json

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'  
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(20), unique=True)  
    name = db.Column(db.String(40), nullable=False)
    mobile = db.Column(db.String, nullable=False, unique=True)
    age = db.Column(db.Integer, nullable=False)

    def json(self):
        return {'id': self.id , 'uid': self.uid , 'name': self.name , 'mobile': self.mobile , 'age': self.age}

    def add_user(_uid, _name, _mobile, _age):
        new_user = User(uid= _uid, name=_name, mobile=_mobile, age=_age)
        db.session.add(new_user)  
        db.session.commit()

    def get_all_users():
        return [User.json(user) for user in User.query.all()]

    def get_user_uid(_uid):
        return [User.json(User.query.filter_by(uid=_uid).first())]

    def get_user_age(_age):
        return [User.json(User.query.filter(User.age(age=_age)).all())]

    def get_user_mobile(_mobile):
        return [User.json(User.query.filter_by(mobile=_mobile).first())]

    def get_user_name(_name):
        return [User.json(User.query.filter_by(name=_name).all())]