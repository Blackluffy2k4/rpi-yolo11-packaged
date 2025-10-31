#!/usr/bin/env bash
set -e
sudo apt update
sudo apt install -y python3-pyqt5
python -m pip install --user -U labelImg lxml
echo 'Run: labelImg dataset/images/train dataset/classes.txt'
