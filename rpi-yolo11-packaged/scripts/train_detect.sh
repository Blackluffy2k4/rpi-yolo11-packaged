#!/usr/bin/env bash
set -e
source .venv/bin/activate
yolo train model=yolo11n.pt data=dataset/data.yaml imgsz=640 epochs=50 device=cpu
