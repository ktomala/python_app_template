# {{cookiecutter.project_title}} Development Guidelines

## Requirements

* Python>=3.6
* `make` command

## Initializing development environment

Initialize and install all necessary support requirements for project
development.

`make init-develop`

## Initializing project for development

Initialize and install all necessary requirements for project itself.

`make init`

## Bumping version

Bump major version: `make release-major`

Bump minor version: `make release-minor`

Bump patch version: `make release-patch`

## Building Documentation

To build and compile documentation.

`make docs`

## Performing tests

To perform package tests.

`make test`

## Cleaning repository

`make clean`

## i18n support (locales)

Initialize message catalog: `python setup.py init_catalog`

Extract messages from project: `python setup.py extract_messages`

Update catalog from project: `python setup.py update_catalog`

Compile message catalog: `python setup.py compile_catalog`
