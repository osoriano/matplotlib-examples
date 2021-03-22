#!/bin/bash
set -o errexit
set -o pipefail
set -o nounset

cd /repo

pip install --upgrade pip
pip install --upgrade pipenv

pipenv install --dev
pipenv run black --target-version py38 --skip-string-normalization src
pipenv run pylint src
pipenv run python -m unittest discover --start-directory src
FLASK_APP=src/routes.py pipenv run flask run --host=0.0.0.0
bash
