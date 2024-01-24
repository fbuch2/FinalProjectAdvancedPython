install:
	python -m pip install --upgrade pip && pip install -r requirements.txt

test:
	pytest

unittest:
	python -m unittest

flake8:
	flake8 *

lint:
	pylint *