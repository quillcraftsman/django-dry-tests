test:
	python manage.py test

server:
	python manage.py runserver

coverage:
	coverage run --source='.' manage.py test
	coverage report --omit=settings/asgi.py,settings/wsgi.py,manage.py,setup.py --fail-under=100
	coverage html --omit=settings/asgi.py,settings/wsgi.py,manage.py,setup.py

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
	pip uninstall django-dry-tests
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