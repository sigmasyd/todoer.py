variables de entorno a ejecutar

```
python3 -m venv venv
. venv/bin/activate
export FLASK_APP=todo
export FLASK_ENV=development
export FLASK_DATABASES_HOST='localhost'
export FLASK_DATABASES_PASSWORD='usr'
export FLASK_DATABASES_USER='usr'
export FLASK_DATABASES_DB='todoer'

flask init-db

flask run
```