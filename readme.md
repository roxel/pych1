Chapter-Python #1
===

Apps in this project:
* `todos` - basic example: TemplateView, DRF ModelViewSet
* `places` - Django REST Framework and Graphene GraphQL schema

===

Steps to start: 

1. `pip install pipenv` - install pipenv; without pipenv you can install all dependencies manually, preferably in virtualenv, using `pip install` command for all libraries listed in `./Pipfile` packages
1. `pipenv install` - install dependencies
1. `docker-compose up` - start database
1. `python manage.py migrate` - run migrations
1. `python manage.py createsuperuser` - create admin user, accessed on: http://localhost:8000/admin/
1. `python manage.py runserver` - start development server
