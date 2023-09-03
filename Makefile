# Makefile for Python application

# Set up Python environment
setup:
	python3 -m pip install --upgrade pip
	pip install flake8 pytest pylint black isort
	if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

# Check Black formatting
black-it:
	find . -name "*.py" -exec black {} +

# Lint with Pylint
pylint:
	find . -name "*.py" -exec pylint {} +

# Run Pytest
pytest:
	pytest

# Sort imports with isort
isort:
	find . -name "*.py" -exec isort {} +

# All-in-one command to run all checks
all: setup isort black-it pylint pytest
