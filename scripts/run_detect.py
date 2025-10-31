import argparse, time, cv2, numpy as np
from ultralytics import YOLO
from picamera2 import Picamera2
from libcamera import Transform

def load_names(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return [x.strip() for x in f if x.strip()]
    except Exception:
        return None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="yolo11n.pt")
    ap.add_argument("--imgsz", type=int, default=640)
    ap.add_argument("--conf", type=float, default=0.25)
    ap.add_argument("--width", type=int, default=640)
    ap.add_argument("--height", type=int, default=480)
    ap.add_argument("--hflip", action="store_true")
    ap.add_argument("--vflip", action="store_true")
    ap.add_argument("--track", action="store_true")
    ap.add_argument("--tracker", choices=["botsort", "bytetrack"], default="botsort")
    ap.add_argument("--labels", default="dataset/classes.txt")
    args = ap.parse_args()

    names = load_names(args.labels)
    model = YOLO(args.model); model.fuse()

    picam2 = Picamera2()
    config = picam2.create_video_configuration(
        main={"size": (args.width, args.height), "format": "RGB888"},
        transform=Transform(hflip=args.hflip, vflip=args.vflip)
    )
    picam2.configure(config); picam2.start()

    t0 = time.time(); frames = 0
    try:
        while True:
            frame = picam2.capture_array()
            bgr = frame[:, :, ::-1].copy()
            if args.track:
                results = model.track(bgr, conf=args.conf, imgsz=args.imgsz, persist=True, tracker=f"{args.tracker}.yaml", verbose=False)
            else:
                results = model.predict(bgr, conf=args.conf, imgsz=args.imgsz, verbose=False)
            r = results[0]
            if hasattr(r, "boxes") and r.boxes is not None:
                boxes = r.boxes.xyxy.cpu().numpy().astype(int)
                clss = r.boxes.cls.cpu().numpy().astype(int) if r.boxes.cls is not None else []
                confs = r.boxes.conf.cpu().numpy() if r.boxes.conf is not None else []
                ids = (r.boxes.id.cpu().numpy().astype(int) if getattr(r.boxes, "id", None) is not None else [-1]*len(boxes))
                for i, (x1,y1,x2,y2) in enumerate(boxes):
                    cls = clss[i] if i < len(clss) else -1
                    conf = confs[i] if i < len(confs) else 0.0
                    tid = ids[i] if i < len(ids) else -1
                    label = names[cls] if names and 0 <= cls < len(names) else str(cls)
                    tag = f"{label} {conf:.2f}" + (f" id:{tid}" if tid!=-1 else "")
                    cv2.rectangle(bgr, (x1,y1), (x2,y2), (0,255,0), 2)
                    cv2.putText(bgr, tag, (x1, max(15,y1-5)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1, cv2.LINE_AA)
            frames += 1
            if frames % 20 == 0:
                fps = frames / (time.time()-t0 + 1e-9)
                cv2.putText(bgr, f"FPS: {fps:.1f}", (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 2)
            cv2.imshow("YOLO11 Detect/Track", bgr)
            if cv2.waitKey(1) & 0xFF == 27:
                break
    finally:
        cv2.destroyAllWindows(); picam2.stop()

if __name__ == "__main__":
    main()
