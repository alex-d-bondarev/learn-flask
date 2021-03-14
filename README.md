# learn-flask

This project was created for learning purposes. You can copy or reuse it. 
If you use this project and sell the end project then you need to include 
MIT license in your final license. 
See [MIT license](https://opensource.org/licenses/MIT) for more details. 

## Install

```bash
pyenv global 3.9.1
pipenv --python 3.9.1 install
pipenv install --ignore-pipfile
```

## Run

```bash
pipenv shell
flask run
# Open http://127.0.0.1:5000/
# Press CTRL+C to stop
exit
```

## Add/Update dependencies

```bash
pipenv install [package names]
# if "Locking Failed!":
pipenv lock --pre --clear
# In the end ensure everything went fine
pipenv check
```

## Check/Fix code style

(Credit to https://sourcery.ai/blog/python-best-practices/)

```bash
PIPENV_IGNORE_VIRTUALENVS=1 pipenv run black .
PIPENV_IGNORE_VIRTUALENVS=1 pipenv run isort .
PIPENV_IGNORE_VIRTUALENVS=1 pipenv run flake8 .
```

## Test

```bash
#Simply test
PYTHONPATH=`pwd` pipenv run pytest
# Test and get coverage. See generated coverage_html_report/index.html for coverage details
PYTHONPATH=`pwd` pipenv run pytest --cov --cov-report html
# Fail when coverage is low
PYTHONPATH=`pwd` pipenv run pytest --cov --cov-report html --cov-fail-under=100
```
