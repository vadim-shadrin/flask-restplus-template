#!/bin/sh

# without this commands docker-compose don't rebuild container if tests were used
sudo rm -rf tests/__pycache__
sudo rm -rf tests/functional/__pycache__
sudo rm -rf tests/integration/api/__pycache__
sudo rm -rf tests/unit/__pycache__

# this commands just delete pycache
sudo rm -rf mb_api/__pycache__
sudo rm -rf mb_api/api/__pycache__
sudo rm -rf mb_api/api/namespaces/__pycache__
sudo rm -rf mb_api/oauth/__pycache__
