# flask-restplus

## Resources

- [Tutorial #1](https://www.freecodecamp.org/news/how-to-use-python-and-flask-to-build-a-web-app-an-in-depth-tutorial-437dbfe9f1c6/ "Python and Flask Web App")

- [Tutorial #2](https://www.freecodecamp.org/news/structuring-a-flask-restplus-web-service-for-production-builds-c2ec676de563/#what-is-flask-restplus "Flask-RESTPlus Service")

- [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/index.html "VirtualEnvWrapper Docs")

## App Structure

The model package contains all database models
The service package contains all business logic
The controller package contains all application endpoints

## Update Packages

Run the following command

```os
pip freeze > requirements.txt
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
