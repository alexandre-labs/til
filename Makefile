.ONESHELL:
venv:
	test -d venv || python3 -m venv venv
poetry-setup:venv
	. venv/bin/activate
	pip install poetry
install:poetry-setup
	. venv/bin/activate
	poetry install
dev:install
	. venv/bin/activate
	pre-commit install --install-hooks
test:
	. venv/bin/activate
	poetry run py.test --cov=til --cov-fail-under=90 && mypy --ignore-missing-imports til
ptw:
	. venv/bin/activate
	poetry run ptw --runner "pytest --cov=til  --cov-report=html" tests/
