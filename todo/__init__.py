import os
from flask import Flask

def create_app():
  app = Flask(__name__)

  app.config.from_mapping(
    SECRET_KEY = 'mikey',
    DATABASE_HOST = os.environ.get("FLASK_DATABASES_HOST"),
    DATABASE_PASSWORD = os.environ.get("FLASK_DATABASES_PASSWORD"),
    DATABASE_USER = os.environ.get("FLASK_DATABASES_USER"),
    DATABASE_DB = os.environ.get("FLASK_DATABASES_DB"),
  )

  from . import db

  db.init_app(app)

  from . import auth
  app.register_blueprint(auth.bp)

  @app.route("/hola")
  def hola():
    return "chanchito feliz"

  return app