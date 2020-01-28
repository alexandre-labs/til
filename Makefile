

SHELL := /bin/bash

venv:
	python3 -m venv venv
	source venv/bin/activate; pip install poetry
install:
	pip install poetry && poetry install
install-venv:venv
	source venv/bin/activate; poetry install
dev:install
	pre-commit install --install-hooks
test:
	poetry run py.test --cov=jus_brasil --cov-fail-under=90 && mypy --ignore-missing-imports til
ptw:
	poetry run ptw --runner "pytest --cov=til  --cov-report=html" tests/
