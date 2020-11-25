import mysql.connector
# ejecutar comandos en la terminal, para poder crear tablas y relaciones entre ellas via comando sin tener que ingresar a workbench
import click

from flask import current_app, g  # g es una variable que se encuentra en toda la app.. se setea y obtienen variables
# para acceder a las variables de configuracion como el host
from flask.cli import with_appcontext 
from .schema import instructions

def get_db():
  if 'db' not in g:
    g.db = mysql.connector.connect(
      host = current_app.config["DATABASE_HOST"],
      user = current_app.config["DATABASE_USER"],
      password = current_app.config["DATABASE_PASSWORD"],
      database = current_app.config["DATABASE_DB"]
    )
    g.c = g.db.cursor(dictionary=True)
  return g.db,g.c

def close_db(e=None):
  db = g.pop('db',None)
  if db is not None:
    db.close()

def init_db():
  db,c = get_db()
  for i in instructions:
    c.execute(i)
  db.commit()

@click.command("init-db")
@with_appcontext
def init_db_command():
  init_db()
  click.echo("Base de datos inicializada")

def init_app(app):
  app.teardown_appcontext(close_db)
  app.cli.add_command(init_db_command)
