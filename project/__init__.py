################################################################################
# imports
################################################################################
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

################################################################################
# config
################################################################################
"""
The ‘instance_relative_config’ flag being set to true causes the loading of
configuration files to be relative to the instance folder instead of the default
setting of the root (top-level) directory.
"""
app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('flask.cfg')

db = SQLAlchemy(app)

# password encryption initialization
bcrypt = Bcrypt(app)

# flask_login initialization
login_manager = LoginManager()           # get the login manager object
login_manager.init_app(app)              # tell it about the application
login_manager.login_view = "users.login" # connect it to the login function
                                         # in the users blueprint
from project.models import User
# This decorator generates the function used by Flask-Login to reload the user
# object from the user ID that is stored for each session.
@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()



################################################################################
# blueprints
################################################################################
from project.users.views import users_blueprint
from project.recipes.views import recipes_blueprint

# register the blueprints
app.register_blueprint(users_blueprint)
app.register_blueprint(recipes_blueprint)
