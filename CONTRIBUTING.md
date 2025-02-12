# Contributing to the PyCon Africa Website

We love your input! We want to make contributing to this project as easy and transparent as possible, whether it's:
- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Becoming a maintainer

## Setting up locally with venv
### 1. Create virtual environment
#### Using venv
```sh
python -m venv venv
```

#### Using Virtualenv
```sh
python -m virtualenv venv
```

### 2. Activate a virtual environment
While in the root project directory, activate a virtual environment by executing the following command based on your operating system;
- For Unix/macOS run:

```sh
source venv/bin/activate
```
- For windows run:
```sh
.venv/Scripts/activate
```
Install Requirements
```sh
pip install -r dev.requirements.txt
```

### 3. Seeding your database
```sh
python3 manage.py shell < seeder.py  
```

-----------

### 3. Environment Variables
Create a `.env` file at the root folder.

> Please reference, the [.env.example](https://github.com/PyconUg/pycon-uganda/tree/main/.env.example) file for the expected environment variables.

### 4. Managing Database Migrations
With an active virtual environment, run the command below while in the root project directory to apply the current migrations to your database. By default, the migrations will be applied to an SQLite Database that will be autocreated in your root project directory.

```sh
python manage.py migrate
```
Create a superuser account
```sh
python manage.py createsuperuser
```

### 4. Running the 
Run the server by executing the command below
```sh
python manage.py runserver
```
Log into the superuser account [http://localhost/accounts/login]
Access the admin dashboard [http://127.0.0.1:8000/organizers/]
Add an event year [http://127.0.0.1:8000/organizers/home/eventyear/]

## We Develop with Github
We use GitHub to host code, to track issues and feature requests, as well as accept pull requests.

## We Use [Github Flow](https://guides.github.com/introduction/flow/index.html), So All Code Changes Happen Through Pull Requests
Pull requests are the best way to propose changes to the codebase. We actively welcome your pull requests:

1. Fork the repo and create your branch from `master`.
2. If you've added code that should be tested, add tests.
3. If you've changed APIs, update the documentation.
4. Ensure the test suite passes.
5. Make sure your code lints.
6. Issue that pull request!

## Any contributions you make will be under the MIT Software License
In short, when you submit code changes, your submissions are understood to be under the same [MIT License](https://choosealicense.com/licenses/mit/) that covers the project.

## Report bugs using Github's [issues](https://github.com/PyConAfrica/pyconafrica-website/issues)
We use GitHub issues to track public bugs. Report a bug by [opening a new issue](https://github.com/PyConAfrica/pyconafrica-website/issues/new); it's that easy!

## Write bug reports with detail, background, and sample code
**Great Bug Reports** tend to have:
- A quick summary and/or background
- Steps to reproduce
  - Be specific!
  - Give sample code if you can.
- What you expected would happen
- What actually happens
- Notes (possibly including why you think this might be happening, or stuff you tried that didn't work)

People *love* thorough bug reports.

## License
By contributing, you agree that your contributions will be licensed under its MIT License.

## References
This document was adapted from the open-source contribution guidelines for [Facebook's Draft](https://github.com/facebook/draft-js/blob/master/CONTRIBUTING.md)


