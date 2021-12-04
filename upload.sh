#!/bin/bash
# requires pip3 install wheel
# would recommend to upgrade pip too
# for future simplicity evaluate flit
# https://packaging.python.org/tutorials/packaging-projects/
sudo python3 -m pip install wheel twine
python -m pip install --upgrade build
rm -r dist/*
rm -r .tox
rm -r .cache
rm -r __pycache__
rm .coverage
rm -r _build
rm -r _static
rm -r _templates
python3 setup.py sdist | grep defaults
python3 setup.py bdist_wheel | grep defaults
# Check if long-description render works fine:
py -m twine check dist/*

# Upload to pypi
twine upload dist/*
