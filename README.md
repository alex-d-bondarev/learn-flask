# learn-flask

## Installing

```bash
pyenv global 3.9.1
pipenv --python 3.9.1 install
```

### Add/Update dependencies

```bash
pipenv install [package names]
# if "Locking Failed!":
pipenv lock --pre --clear
# In the end ensure everything went fine
pipenv check
```

### Install from `Pipfile.lock`

```bash
pipenv install --ignore-pipfile
```

## Code style

(Credit to https://sourcery.ai/blog/python-best-practices/)

```bash
pipenv run black
PIPENV_IGNORE_VIRTUALENVS=1 pipenv run isort .
PIPENV_IGNORE_VIRTUALENVS=1 pipenv run flake8
```

## Testing

```bash
# Generate coverage in htmlcov folder
PYTHONPATH=`pwd` pipenv run pytest --cov --cov-report html
# Fail when coverage is low
PYTHONPATH=`pwd` pipenv run pytest --cov --cov-report html --cov-fail-under=100
exit
```

## Running

```bash
pipenv shell
FLASK_APP=learn_app/simple_app.py FLASK_ENV=development flask run
# CTRL+C
exit
```