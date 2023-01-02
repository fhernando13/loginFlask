import os
from dotenv import load_dotenv
from flask import Flask
from models.ModelUsuarios import Users
from routes.routesOperations import operations
from routes.routesLogin import login
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager 


load_dotenv()
user_db = os.getenv('USER_DB')
pass_db = os.getenv('PASS_DB')
url_db = os.getenv('URL_DB')
name_db = os.getenv('NAME_DB')
full_url_db = f'postgresql://{user_db}:{pass_db}@{url_db}/{name_db}'


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = full_url_db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'my_secret_key'
csrf = CSRFProtect(app)
login_manager = LoginManager()
login_manager.init_app(app)


SQLAlchemy(app)


app.register_blueprint(operations)
app.register_blueprint(login)


@login_manager.user_loader
def load_user(id_user):
    return Users.query.get(id_user)



