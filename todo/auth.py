import functools

from flask import (
  Blueprint, flash, g, render_template, request, url_for, session
)

from werkzeug.security import check_password_hash, generate_password_hash

from todo.db import get_db

bp = Blueprint('auth',url_prefix='/auth')

@bp.route('/register', methods=['GET','POST'])
def register():
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
    db, c = get_db()
    err = None

    c.execute(
      'select id from user where username = %s'
    )
    if not username:
      error = 'Username es requerido'
    if not password:
      error = 'Password es requerido'
    elif c.fetchone() is not None:
      error = 'Usuario {} se encuentra registrado.'.format(username)

    if error is None: 
      c.execute(
        'insert into user (username,password) values(%s,%s)',
        (username,generate_password_hash(password))
      )
      db.commit()
      return redirect(url_for('auth.login'))

    flash(error)

  return render_template('auth/register.html')




