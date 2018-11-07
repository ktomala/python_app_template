Basic Python Application Cookiecutter template
==============================================

About
-----

This is a basic application template for your Python projects. It allows
you to quickly setup sensible defaults and some boilerplate files for your
project. It uses Cookiecutter as a scaffolding engine.

Features
--------

* Requirements and requirements-development files
* Makefile for simpler management
* Pytest and coverage integrated
* Pylint checks
* Sensible gitignore files
* Babel internationalization support
* Bumpversion for easy application version management
* Sphinx documentation support

Usage
-----

First you have to install Cookiecutter:

.. code::bash

  pip install --user cookiecutter


After installing Cookiecutter you can simply create a directory where you want
your project to be and run cookiecutter:

.. code::bash

  mkdir -p ~/src/your_project
  cd ~/src/your_project
  cookiecutter https://github.com/ktomala/python_app_template.git


This will setup project template with the specified name from `project_name`
variable inside the directory you are currently in.
