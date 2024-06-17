build:
	rm -r build dist &  python3 -m build --sdist --wheel ./

test:
	pytest

deploy:
	twine upload dist/*

install:
	pip install jjutils