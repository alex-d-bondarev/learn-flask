#.DEFAULT_GOAL := hello

hello:
	@echo "make hello - print supported commands"
	@echo "make - same as 'make hello'"
	@echo "make strict_test - run py-tests and fail when coverage is bellow 100%"

strict_test:
	PYTHONPATH=`pwd` pipenv run pytest --cov --cov-report html --cov-fail-under=100
