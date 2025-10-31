# Raspberry Pi YOLO11 Starter (Detection, Segmentation, Tracking)
A small, battle-tested starter for running **Ultralytics YOLO11** on **Raspberry Pi (Pi 4/5, Raspberry Pi OS Bookworm 64‑bit)** with **Picamera2 + OpenCV + cvzone** — including dataset capture, labeling with LabelImg, training, and real‑time detection/segmentation with optional tracking (BoT‑SORT/ByteTrack).

## Quick start
```bash
cd rpi-yolo11-packaged
bash scripts/setup_venv.sh
source .venv/bin/activate
bash scripts/fix_path.sh
python scripts/verify_install.py

python scripts/capture_images.py --out-dir dataset/images/train --width 640 --height 480 --hflip --vflip --interval 0.5

bash scripts/labelimg_install.sh
labelImg dataset/images/train dataset/classes.txt

nano dataset/data.yaml

bash scripts/train_detect.sh
bash scripts/train_seg.sh

python scripts/run_detect.py --model runs/detect/train/weights/best.pt --track
python scripts/run_seg.py --model runs/segment/train/weights/best.pt --track
```
