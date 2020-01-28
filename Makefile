.ONESHELL:
venv:
	test -d /tmp/venv || python3 -m venv /tmp/venv
	. /tmp/venv/bin/activate
	pip install poetry
install:venv
	. /tmp/venv/bin/activate
	poetry install
dev:install
	. /tmp/venv/bin/activate
	pre-commit install --install-hooks
test:
	. /tmp/venv/bin/activate
	poetry run py.test --cov=til --cov-fail-under=90 && mypy --ignore-missing-imports til
ptw:
	. /tmp/venv/bin/activate
	poetry run ptw --runner "pytest --cov=til  --cov-report=html" tests/
