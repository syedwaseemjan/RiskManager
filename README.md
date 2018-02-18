# RiskManager
An example web-based app to demonstrate the database schema for Insurance business.

## Concept

Sqlite DB is used for storing data. Sqlalchemy is used to help with the queries. I have used a service layer which is an internal API of this system. On top of this internal API, two  applications have been implemented.

1. Restful API
2. Frontend

Restful API is used for CRUD operations. Frontend application is used for serving static files(CSS, JS, HTML).
Frontend is developed in Vue Framework. Dashboard.js is reponsible for doing all ajax requests to API.

Functional tests are added for testing all the endpoints. I am using 

1. Nose
2. Mock
3. Factory boy

## Development Environment

At the bare minimum you'll need the following for your development environment:

1. [Python](http://www.python.org/)
2. [Sqlite](https://sqlite.org)

### Local Setup

The following assumes you have all of the recommended tools listed above installed.

#### 1. Clone the project:

    $ git clone git@github.com:syedwaseemjan/RiskManager.git
    $ cd RiskManager

#### 2. Create and initialize virtualenv for the project:

    $ mkdir manager_virtualenv
    $ virtualenv manager_virtualenv
    $ source manager_virtualenv/bin/activate
    $ pip install -r requirements.txt

#### 3. Setup the Sqlite DB (Add default admin user):

    $ python manage.py create_db
    $ python manage.py init_db

#### 4. Run tests:
    
    $ nosetests -vv --collect-only (To see where exactly nose is looking for testcases. It won't run the tests if the file is executable)
    $ chmod -x $(find tests/ -name '*.py')  - (To make your testcase files not executable. This command is tested on MAC only)
    $ nosetests -v

#### 5. Run the server:

    $ python runserver.py

#### 6. Load the system in browser:

    Visit http://127.0.0.1:5000


## API Documentation:

REST API documentation (OpenAPI specification based) is provided in docs folder. It can be verified by using [swagger online editor](https://swagger.io/swagger-editor/).