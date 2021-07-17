#.DEFAULT_GOAL := help

help:
	@echo "make help \t\t- print supported commands"
	@echo "make \t\t\t- same as 'make hello'"
	@echo "make run \t\t- run application"
	@echo "make test \t\t- run py-tests"
	@echo "make coverage_test \t- run py-tests and get test coverage"
	@echo "make strict_test \t- run py-tests and fail when coverage is bellow 100%"
	@echo "make black \t\t- run python black to improve code style."
	@echo "make isort \t\t- run python isort to improve code style."
	@echo "make flake8 \t\t- run python flake8 to show code warnings that cannot be fixed automatically."
	@echo "make code_style \t- run 'black', 'isort' and 'flake8' make commands all at once"

run:
	pipenv run flask run

test:
	PYTHONPATH=`pwd` pipenv run pytest

coverage_test:
	PYTHONPATH=`pwd` pipenv run pytest --cov --cov-report html

strict_test:
	PYTHONPATH=`pwd` pipenv run pytest --cov --cov-report html --cov-fail-under=100

code_style: black isort flake8

black:
	PIPENV_IGNORE_VIRTUALENVS=1 pipenv run black .

isort:
	PIPENV_IGNORE_VIRTUALENVS=1 pipenv run isort .

flake8:
	PIPENV_IGNORE_VIRTUALENVS=1 pipenv run flake8 .
