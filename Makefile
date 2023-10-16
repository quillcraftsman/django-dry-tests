server:
	python manage.py runserver

makemigrations:
	python manage.py makemigrations

test:
	python manage.py test

dry-test:
	python manage.py test --tag="dry"

django-test:
	python manage.py test --tag="django"

coverage:
	coverage run --source='.' manage.py test
	coverage html --omit=settings/asgi.py,settings/wsgi.py,manage.py,setup.py,package.py
	coverage report --omit=settings/asgi.py,settings/wsgi.py,manage.py,setup.py,package.py --fail-under=100

django-coverage:
	coverage run --source='.' manage.py test --tag="django"
	coverage html --omit=settings/asgi.py,settings/wsgi.py,manage.py,setup.py,package.py,demo/tests/*,dry_tests/*,quickstart/*
	coverage report --omit=settings/asgi.py,settings/wsgi.py,manage.py,setup.py,package.py,demo/tests/*,dry_tests/*,quickstart/* --fail-under=100

dry-coverage:
	coverage run --source='.' manage.py test --tag="dry"
	coverage html --omit=settings/asgi.py,settings/wsgi.py,manage.py,setup.py,package.py,demo/tests/*
	coverage report --omit=settings/asgi.py,settings/wsgi.py,manage.py,setup.py,package.py,demo/tests/* --fail-under=100

yamllint:
	yamllint -d relaxed .

black:
	black .

build:
	python -m build

install:
	make build
	pip install dist/*.whl

uninstall:
	pip uninstall django-dry-tests -y
	rm -rf dist
	rm -rf django_dry_tests.egg-info

reinstall:
	make uninstall
	make install

pylint:
	pylint $(shell git ls-files '*.py')

lint:
	make yamllint
	make pylint

sphinx-help:
	make help -f Sphinxfile

package_docs:
	sphinx-apidoc -o docs/package dry_tests/