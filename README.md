# learn-flask

This project was created for learning purposes. You can copy or reuse it. 
If you use this project and sell the end project then you need to include 
MIT license in your final license. 
See [MIT license](https://opensource.org/licenses/MIT) for more details. 

## Install

### Python

Ensure pyenv is installed. 
In this case pipenv will be able to install required python version automatically.

```bash
PIPENV_YES=true pipenv install
```

### MySQL

1. Install docker
1. Run `docker-compose up -d`
1. Now you can connect to DB as:
   ```
   host=127.0.0.1
   username=root
   password=root_pass # from MYSQL_ROOT_PASSWORD in .env
   port=3310          # from MYSQL_PORT_1 in .env
   ```


## Run

```bash
docker-compose up -d
make run
# Open http://127.0.0.1:5000/
# Press CTRL+C to stop
docker-compose down
```

## Add/Update dependencies

```bash
pipenv install [package names]
# if "Locking Failed!":
pipenv lock --pre --clear
```

## Check/Fix code style

(Credit to https://sourcery.ai/blog/python-best-practices/)

Run python black, isort and flake8 in order to improve code style:
```bash
make code_style
```

## Test 

### All

1. Start DB `docker-compose up -d`
1. Run tests:
   ```bash
   #Simply test
   make test
   # Test and get coverage. See generated coverage_html_report/index.html for coverage details
   make coverage_test 
   # Fail when coverage is bellow 100%
   make strict_test 
   ```
1. Stop DB `docker-compose down`

### Specific test

1. Start DB `docker-compose up -d`
1. Run test:
   export PYTHONPATH=`pwd`
   ```bash
   # trigger test via path to test file and method name 
   # pytest <test_file_path>::<method_name>
   # For example:
   pytest ./tests/test_flow/do_something_private_integration_test.py::test_post_do_something_private_needs_user
   ```
1. Stop DB `docker-compose down`
