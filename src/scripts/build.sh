#!/bin/bash

# Uninstall existing huefy package
pip uninstall -y huefy

# Remove __pycache__ directories
find . -type d -name '__pycache__' -exec rm -rf {} +

# Remove build artifacts
rm -rf build/ dist/ *.egg-info/

# Rebuild the package
python setup.py sdist bdist_wheel

# Install in editable mode
pip install -e .
