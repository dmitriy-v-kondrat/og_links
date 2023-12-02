Python 3.8.10

Django 4.2.7


Add the .env file to the project root and edit it.

    SECRET_KEY='your key'
    DEBUG=True
    DJANGO_ALLOWED_HOSTS='localhost 127.0.0.1 [::1]'

    SQL_ENGINE=django.db.backends.postgresql
    SQL_DATABASE=links
    SQL_USER= your user
    SQL_PASSWORD= your password
    SQL_HOST=db
    SQL_PORT=5432
    
    PGDATA=/var/tmp/postgresql/data/pgdata
    POSTGRES_DB=links
    POSTGRES_USER= your user
    POSTGRES_PASSWORD= your password


Now lifetime access and refresh token days=1

Change lifetime token:

    settings.SIMPLE_JWT


Build project in a docker:

    docker-compose build


Run project:

    docker-compose up


Register users:

    /api/register/


Login (returns an access and refresh web
token pair to prove the authentication.):

    /token/


Specification:

    /schema/redoc/