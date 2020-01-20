

SHELL := /bin/bash

venv:
	python3 -m venv venv
	source venv/bin/activate; pip install poetry

install:
	. venv/bin/activate
	poetry install
test:
	poetry run pytest
