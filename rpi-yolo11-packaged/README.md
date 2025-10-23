# rpi-yolo11-packaged (Raspberry Pi · YOLO11 · Picamera2 · OpenCV)

Bộ khởi tạo đã kiểm chứng để chạy **Ultralytics YOLO11** trên **Raspberry Pi 4/5 (Raspberry Pi OS Bookworm 64-bit)**: thu ảnh → gán nhãn (LabelImg) → huấn luyện (detect/seg) → suy luận thời gian thực + theo dõi ID (BoT-SORT/ByteTrack).

## 1) Yêu cầu
- Raspberry Pi 4/5, Raspberry Pi OS **Bookworm 64-bit**.
- Camera hỗ trợ **libcamera** (PiCamera V2/V3/HQ).
- Python 3.9+.
- Kết nối mạng để cài gói.

## 2) Cài đặt nhanh

```bash
# clone hoặc copy repo vào Pi
cd rpi-yolo11-packaged

# tạo môi trường ảo + cài phụ thuộc hệ thống tối thiểu + Python deps (pinned)
bash scripts/setup_venv.sh
source .venv/bin/activate

# (khuyên dùng) thêm ~/.local/bin vào PATH để gọi lệnh `yolo`
bash scripts/fix_path.sh

# kiểm tra phiên bản đã cài
python scripts/verify_install.py
