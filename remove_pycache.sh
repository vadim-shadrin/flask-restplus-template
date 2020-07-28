#!/usr/bin/env bash
set -e

echo "Removing venv subdirectory"
rm -rf venv

echo "Removing .pytest_cache subdirectory"
rm -rf **/*/.pytest_cache

echo "removing __pycache__ subdirectories"
for file in $(find ./ -name __pycache__); do
    rm -r $file;
done
