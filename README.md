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
```

### Install from `Pipfile.lock`

```bash
pipenv install --ignore-pipfile
```

## Code style

(Credit to https://sourcery.ai/blog/python-best-practices/)

```bash
pipenv run black
pipenv run isort .
pipenv run flake8
```

## Testing

```bash
PYTHONPATH=. pipenv run pytest --cov
# Fail when coverage is low
PYTHONPATH=. pipenv run pytest --cov --cov-fail-under=100
```

## Running

```bash
pipenv shell
FLASK_APP=learn_app/simple_app.py FLASK_ENV=development flask run
# CTRL+C
exit
```