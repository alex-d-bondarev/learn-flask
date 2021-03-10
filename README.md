# learn-flask

## Installing

```bash
pyenv global 3.9.1
pipenv --python 3.9.1 install
```

### Add/Update dependencies

```bash
pipenv install [package names]
```

### Install from `Pipfile.lock`

```bash
pipenv install --ignore-pipfile
```

## Running

### General

```bash
pipenv shell
# Have fun
exit
```

### Hello World

```bash
pipenv shell
FLASK_APP=hello.py FLASK_ENV=development flask run
# CTRL+C
exit
```