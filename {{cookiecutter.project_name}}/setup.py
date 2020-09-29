# -*- coding: utf-8 -*-

"""Setup for {{cookiecutter.project_title}}."""

from setuptools import setup, find_packages
from babel.messages import frontend as babel


with open('README.md') as f:
    readme = f.read()

{%- if cookiecutter.use_license == "yes" -%}
with open('LICENSE.md') as f:
    license = f.read()
{% endif %}

setup(
    name='{{cookiecutter.project_name}}',
    version='0.0.0',
    description='{{cookiecutter.short_description}}',
    long_description=readme,
    author='{{cookiecutter.author}}',
    author_email='{{cookiecutter.author_email}}',
{%- if cookiecutter.project_url != "https://your_project.com" -%}
    url='{{cookiecutter.project_url}}',
{% endif %}
{%- if cookiecutter.use_license == "yes" -%}
    license=license,
{% endif %}
    packages=find_packages(exclude=('tests', 'docs')),
{%- if cookiecutter.use_command_line_script == "yes" -%}
    entry_points={
        'console_scripts': [
            '{{cookiecutter.script_name}}={{cookiecutter.project_name}}.{{cookiecutter.project_main}}:{{cookiecutter.project_main_entrypoint}}'
        ]
    },
{% endif %}
    cmdclass={
        'compile_catalog': babel.compile_catalog,
        'extract_messages': babel.extract_messages,
        'init_catalog': babel.init_catalog,
        'update_catalog': babel.update_catalog
    }
)
