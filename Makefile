build:
	python3 -m build --sdist --wheel ./

test:
	pytest

deploy:
	twine upload dist/*