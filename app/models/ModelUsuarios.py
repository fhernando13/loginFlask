from utils.conexion import db
from werkzeug.security import generate_password_hash, check_password_hash 
from flask_login import UserMixin

class Users(db.Model, UserMixin):
    id_user = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(255)) 
    lastname = db.Column(db.String(255))
    nickname = db.Column(db.String(12))
    password = db.Column(db.String(128))

    def __init__(self, name, lastname, nickname, password):
        self.name = name
        self.lastname = lastname
        self.nickname = nickname
        self.password = self.create_pw(password)
 
    def create_pw(self, password):
        self.password = generate_password_hash(password)

    def check_pw(self, password):
        return check_password_hash(self.password, password)
    
    def get_id(self):
        return str(self.id_user)



    


    
    
