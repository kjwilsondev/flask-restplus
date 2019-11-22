# flask-restplus

## Resources

- [Tutorial #1](https://www.freecodecamp.org/news/how-to-use-python-and-flask-to-build-a-web-app-an-in-depth-tutorial-437dbfe9f1c6/ "Python and Flask Web App")

- [Tutorial #2](https://www.freecodecamp.org/news/structuring-a-flask-restplus-web-service-for-production-builds-c2ec676de563/#what-is-flask-restplus "Flask-RESTPlus Service")

- [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/index.html "VirtualEnvWrapper Docs")

- [CRUDing for PostgreSQL](https://www.compose.com/articles/using-postgresql-through-sqlalchemy/ "PostgreSQL through SQLAlchemy")

## App Structure

The model package contains all database models
The service package contains all business logic
The controller package contains all application endpoints

## Update Packages

Run the following command

```os
pip freeze > requirements.txt
```

## Initiate Database Folder

Initiate a migration folder using init command for alembic to perform the migrations.

```os
python manage.py db init
python manage.py db migrate --message 'initial database migration'
python manage.py db upgrade
```

Should have new sqlLite database
flask_boilerplate_main.db
generated inside main folder

Each time the database model changes,
repeat the migrate and upgrade commands

## Virtual Env Commands

Create Env

```os
mkproject [name]
```

List all Envs

```os
ls $WORKON_HOME
```

Reactivate Env

```os
workon [name]
```

Delete Env

```os
rmvirtualenv [name]
```

### Neccessary Packages

- **Flask-bcrypt**
  - for hashing passwords and tokens
- **flask-restplus**
- **Flask-Migrate**
  - SQLAlchemy database migrations
- **pyjwt**
  - python library for encoding JWT tokens
- **Flask-Script**
- **flask_testing**
