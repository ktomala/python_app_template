develop: init init-develop test
.PHONY: develop

init:
	pip install -r requirements.txt

init-develop:
	pip install -r requirements-development.txt
	python setup.py develop

release-patch:
	bumpversion patch
	python setup.py develop

release-minor:
	bumpversion minor
	python setup.py develop

release-major:
	bumpversion major
	python setup.py develop

test:
	pytest tests
