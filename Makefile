.ONESHELL:
venv:
	test -d venv || python3.8 -m venv venv
poetry-setup:venv
	test -d venv && . venv/bin/activate
	test poetry || pip install poetry
install:poetry-setup
	. venv/bin/activate
	poetry install
dev:install
	. venv/bin/activate
	pre-commit install --install-hooks
test:install
	. venv/bin/activate
	poetry run py.test tests/unit &&\
	   	poetry run py.test tests/integration &&\
	   	poetry run mypy --ignore-missing-imports til
cov:install
	. venv/bin/activate
	poetry run py.test --cov=til --cov-fail-under=90 tests
ptw:install
	. venv/bin/activate
	poetry run ptw --runner "pytest " tests/
