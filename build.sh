#!/usr/bin/env bash
python3 -m venv ./venv
./venv/bin/python -m pip install pip --upgrade
./venv/bin/python -m pip install -e src