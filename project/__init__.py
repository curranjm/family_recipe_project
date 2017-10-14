################################################################################
# imports
################################################################################
from flask import Flask

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


################################################################################
# blueprints
################################################################################
from project.users.views import users_blueprint
from project.recipes.views import recipes_blueprint

# register the blueprints
app.register_blueprint(users_blueprint)
app.register_blueprint(recipes_blueprint)
