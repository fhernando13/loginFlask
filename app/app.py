from flask import Flask
from models.ModelUsuarios import Users
from routes.routesOperations import operations
from routes.routesLogin import login
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:admin@localhost/logintarea"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
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



