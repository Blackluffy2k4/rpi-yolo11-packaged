#!/usr/bin/env bash
set -e
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip setuptools wheel
sudo apt update
sudo apt install -y python3-picamera2 libatlas-base-dev libcap-dev
python -m pip install -r requirements.txt
echo ' Setup complete. Activate: source .venv/bin/activate'
