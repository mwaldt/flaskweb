FLASK = .venv/bin/flask
PYTHON = .venv/bin/python3
PIP = .venv/bin/pip
PYTEST = .venv/bin/pytest

help:
	@echo 'The following commands can be used.'
	@echo ''
	$(call find.functions)

setup: requirements.txt
	python3 -m venv .venv
	$(PIP) install -e . -r requirements.txt

run: setup
	$(FLASK) flaskexample/app.py

shell: setup
	$(PYTHON)

test_setup: setup
	$(PIP) install -r requirements-test.txt

test: test_setup
	$(PYTEST) tests/

clean:
	rm -rf __pycache__
	rm -rf .venv

.PHONY: run clean setup test test_setup
