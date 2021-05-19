from setuptools import setup, find_packages

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Needed for dependencies
INSTALL_REQUIRES = [
      'wheel',
]   

{%- set license_classifiers = {
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'ISC license': 'License :: OSI Approved :: ISC License (ISCL)',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
} %}

setup(
    name = '{{cookiecutter.package_name}}',
    packages = find_packages(),
    version = '0.1.0',
    description = '{{cookiecutter.short_description}}',
    long_description_content_type = 'text/markdown',
    long_description = long_description,
    author='{{cookiecutter.github_username}}',
    classifiers=[
        {%- if cookiecutter.open_source_license in license_classifiers %}
        '{{ license_classifiers[cookiecutter.open_source_license] }}',
        {%- endif %}
        ],
    install_requires = INSTALL_REQUIRES,
    python_requires = '>=3.7',
    test_suite='tests',
    zip_safe = False
)
