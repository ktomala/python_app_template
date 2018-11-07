# Settings

PROJECT := {{cookiecutter.project_name}}
TESTS := tests
DOCS := docs
PACKAGES := $(PROJECT) $(TESTS)

.PHONY: all
all: init init-develop check test docs

# Requirements

.PHONY: init
init:
	pip install -r requirements.txt

.PHONY: init-develop
init-develop: init
	pip install -r requirements-development.txt
	python setup.py develop

# Bumpversion management

.PHONY: release-patch
release-patch: init-develop
	bumpversion patch
	python setup.py develop

.PHONY: release-minor
release-minor: init-develop
	bumpversion minor
	python setup.py develop

.PHONY: release-major
release-major: init-develop
	bumpversion major
	python setup.py develop

# Checks and linters

.PHONY: check
check: pylint pylama

.PHONY: pylint
pylint: init-develop
	pylint $(PACKAGES) --rcfile=.pylintrc

.PHONY: pylama
pylama: init-develop
	pylama $(PACKAGES)

# Tests

.PHONY: test
test: init-develop
	pytest $(TESTS)

# Documentation

.PHONY: docs
docs: init-develop
	$(MAKE) -C $(DOCS) html

# Cleanup

.PHONY: clean
clean: .clean-build .clean-docs .clean-test .clean-install

.PHONY: .clean-install
.clean-install:
	find $(PACKAGES) -name '*.pyc' -delete
	find $(PACKAGES) -name '__pycache__' -delete
	rm -rf *.egg-info

.PHONY: .clean-test
.clean-test:
	rm -rf .cache .pytest .coverage htmlcov xmlreport

.PHONY: .clean-docs
.clean-docs:
	rm -rf docs/_build

.PHONY: .clean-build
.clean-build:
	rm -rf *.spec dist build
