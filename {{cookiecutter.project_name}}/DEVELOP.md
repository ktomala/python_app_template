# {{cookiecutter.project_title}} Development Guidelines

## Requirements

* Python>=3.6
* `make` command

### Make on Windows

You can install make on Windows with multiple ways:

* nmake from Visual Studio
* Install MinGW which has make inside MSYS (http://www.mingw.org/wiki/MSYS)
* Add make to Git Bash

#### Make using Git Bash on Windows

 1. Go to https://sourceforge.net/projects/ezwinports/files/.
 2. Download make-4.1-2-without-guile-w32-bin.zip (get the version without guile).
 3. Extract zip.
 4. Copy the contents to your Git\mingw64\ merging the folders, but do NOT overwrite/replace any existing files.

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
