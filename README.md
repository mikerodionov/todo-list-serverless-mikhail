# Serverless REST API Todo List App

This is a sample REST API Todo List App configured for deployment using [Serverless Framework](https://www.serverless.com/) to AWS. App consist of number of Python functions which are deployed to AWS Lambda (AWS SAM). Intended for Assignment 1-A which involves use pf the following components:

GitHub - code control/repo
Serverless Framework - CI/CD orquestration
Serverless Framework - build
AWS Lambda - business logic
DynamoDB - persistent data storage
AWS API Gateway - API
AWS CloudWatch/Serverless Framework - monitoring

Optional requirement - tests (not implemented):

Unit test (PyTest)
Coverage test (coverage)
Quality test (flake8)
Security test (bandit)
Complexity test (radon - PyPi)

Repository structure:

```
├── package.json
├── README.md
├── serverless.yml
├── test
│   ├── example
│   │   ├── README.md
│   │   ├── TestToDo.py
│   │   ├── ToDoCreateTable.py
│   │   ├── ToDoDeleteItem.py
│   │   ├── ToDoGetItem.py
│   │   ├── ToDoListItems.py
│   │   ├── ToDoPutItem.py
│   │   └── ToDoUpdateItem.py
│   ├── integration
│   └── unit
└── todos
    ├── create.py
    ├── decimalencoder.py
    ├── delete.py
    ├── get.py
    ├── __init__.py
    ├── list.py
    ├── todoTableClass.py
    └── update.py
```

# Prerequisites/additional notes

Note on branches:

**Feature** - branch for adding new feature(s) (Translate function) which is getting merged with Develop after review/local tests.

**Develop** - maing development branch, merge triggers Serverless pipeline to deploy/update Staging environment in AWS. Optionally tests can be added for validation at this stage.

**Master** - main/production branch mergin into it deploys/updates Production environment in AWS.
