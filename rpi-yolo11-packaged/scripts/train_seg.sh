#!/usr/bin/env bash
set -e
source .venv/bin/activate
yolo train task=segment model=yolo11n-seg.pt data=dataset/data.yaml imgsz=640 epochs=50 device=cpu
