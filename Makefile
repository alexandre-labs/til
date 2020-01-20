

SHELL := /bin/bash

venv:
	python3 -m venv venv
	source venv/bin/activate; pip install poetry
install: venv
	. venv/bin/activate && poetry install
dev:install
	pre-commit install --install-hooks
test:
	poetry run pytest tests && mypy --ignore-missing-imports til
ptw:
	poetry run ptw --runner "pytest --cov=til  --cov-report=html" tests/
