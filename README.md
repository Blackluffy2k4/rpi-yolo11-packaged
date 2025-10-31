# Raspberry Pi YOLO11 Starter (Detection, Segmentation, Tracking)
A small, battle-tested starter for running **Ultralytics YOLO11** on **Raspberry Pi (Pi 4/5, Raspberry Pi OS Bookworm 64‑bit)** with **Picamera2 + OpenCV + cvzone** — including dataset capture, labeling with LabelImg, training, and real‑time detection/segmentation with optional tracking (BoT‑SORT/ByteTrack).

```bash
# 1) Chuẩn bị venv
sudo apt update
sudo apt install -y python3-venv python3-pip
python3 -m venv ~/venvs/vision
source ~/venvs/vision/bin/activate

# 2) Nâng pip & công cụ build
python -m pip install -U pip setuptools wheel

# 3) (Khuyên dùng) Cài PyTorch CPU trước
python -m pip install -U --index-url https://download.pytorch.org/whl/cpu torch torchvision

# 4) Cài đúng phiên bản yêu cầu
python -m pip install -U "opencv-python==4.10.0.84" "ultralytics==8.3.3" "cvzone==1.6.1"

# 5) Kiểm tra phiên bản
python - <<'PY'
import cv2, ultralytics, pkg_resources as pr
print("OpenCV:", cv2.__version__)
print("Ultralytics:", ultralytics.__version__)
print("cvzone:", pr.get_distribution("cvzone").version)
PY

```
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
