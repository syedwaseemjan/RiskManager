[![Build Status](https://travis-ci.org/syedwaseemjan/RiskManager.svg?branch=master)](https://travis-ci.org/syedwaseemjan/RiskManager)
# RiskManager
An example web-based app to demonstrate the database schema for Insurance business, well documented (through swagger) and tested (through nosetests) Rest API, a clean single page vuejs frontend application, continuous integration with Tavis CI and a serverless deployment on AWS Lambda through zappa.

## Concept

Sqlite DB is used for storing data. Sqlalchemy is used to help with the queries. I have used a service layer which is an internal API of this system. On top of this internal API, two  applications have been implemented.

1. Restful API
2. Frontend

Restful API is used for CRUD operations. Frontend application is used for serving static files(CSS, JS, HTML).
and is developed in Vue Framework. I have built the frontend through webpack. dashboard.py loads index.html from where Vue.js based frontend gets generated.
Functional tests are added for testing all the endpoints. I am using 

1. Nose
2. Mock
3. Factory boy

## Development Environment

At the bare minimum you'll need the following for your development environment:

1. [Python](http://www.python.org/)
2. [Sqlite](https://sqlite.org)
3. [Node](https://nodejs.org/en/).

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

#### 3. Setup the Sqlite DB:

    $ python manage.py create_db
    $ python manage.py init_db

#### 4. Run tests:
    
    $ nosetests -vv --collect-only (To see where exactly nose is looking for testcases. It won't run the tests if the file is executable)
    $ chmod -x $(find tests/ -name '*.py')  - (To make your testcase files not executable. This command is tested on MAC only)
    $ nosetests -v

### Build the frontend (Optional):
Do it only if you have made any changes in the frontend code otherwise I have already pushed build.js in dist folder.

    $ cd app/frontend/app
    $ npm run build

#### 5. Run the server:

    $ python runserver.py

#### 6. Load the system in browser:

    Visit http://127.0.0.1:5000

### Development:
For local development, I run both the Flask Development Server in parallel to webpack-dev-server. This allows me to serve the Flask api endpoint while still taking advantage of the hot-reload and eslinter.
    
    $ cd app/frontend/app
    $ npm run dev (Before running this command you need to remove "assets" tags from index.html. These tags are used when we load index.html through flask.)

## API Documentation:

REST API documentation (OpenAPI specification based) is provided in docs folder. It can be verified by using [swagger online editor](https://swagger.io/swagger-editor/). Also, Database ER diagram is in docs folder.

## Deployment:

I have deployed this project on AWS Lambda with the help of [zappa](https://github.com/Miserlou/Zappa). Currently it can be viewed here.

https://y16svgzfa2.execute-api.us-east-1.amazonaws.com/dev

### Steps required to deploy it on AWS Lambda with zappa

#### 1. Create IAM User:
    Save Access Key ID and Secret Access Key. We will need it to create Named Profile.

#### 2. Give your IAM User following permissions:

    a. AWSLambdaFullAccess
    b. IAMFullAccess
    c. AmazonS3FullAccess
    d. AmazonAPIGatewayInvokeFullAccess
    e. AmazonAPIGatewayAdministrator
    f. CloudFormationFullAccess (This one is my custom permission. Use the following policies to create this. You can name it anything you like.)
        

        {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Action": [
                        "cloudformation:CreateStack",
                        "cloudformation:DescribeStacks",
                        "cloudformation:DescribeStackEvents",
                        "cloudformation:DescribeStackResource",
                        "cloudformation:DescribeStackResources",
                        "cloudformation:GetTemplate",
                        "cloudformation:ValidateTemplate",
                        "cloudformation:DeleteStack",
                        "cloudformation:UpdateStack"
                    ],
                    "Resource": "*"
                }
            ]
        }

#### 3. Create Named Profile on your local machine. It will be used by boto:

    $ aws configure
    $ AWS Access Key ID [None]: *********
    $ AWS Secret Access Key [None]: **************
    $ Default region name [None]: us-east-1
    $ Default output format [None]: json

#### 3. Use Zappa commands to deploy it:

    $ zappa deploy dev
    $ zappa update dev