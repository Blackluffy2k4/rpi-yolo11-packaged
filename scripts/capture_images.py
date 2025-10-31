import argparse, time, os, cv2
from picamera2 import Picamera2
from libcamera import Transform

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out-dir", default="dataset/images/train")
    ap.add_argument("--width", type=int, default=640)
    ap.add_argument("--height", type=int, default=480)
    ap.add_argument("--hflip", action="store_true")
    ap.add_argument("--vflip", action="store_true")
    ap.add_argument("--interval", type=float, default=0.5)
    ap.add_argument("--preview", action="store_true")
    args = ap.parse_args()

    os.makedirs(args.out_dir, exist_ok=True)
    picam2 = Picamera2()
    config = picam2.create_video_configuration(
        main={"size": (args.width, args.height), "format": "RGB888"},
        transform=Transform(hflip=args.hflip, vflip=args.vflip)
    )
    picam2.configure(config)
    picam2.start()
    print(f"Saving frames to {args.out_dir}. Ctrl+C to stop.")
    try:
        while True:
            frame = picam2.capture_array()  # RGB
            ts = time.strftime("%Y%m%d_%H%M%S")
            path = os.path.join(args.out_dir, f"img_{ts}_{int(time.time()*1000)%1000:03d}.jpg")
            cv2.imwrite(path, frame[:, :, ::-1])  # save as BGR
            if args.preview:
                cv2.imshow("Capture", frame[:, :, ::-1])
                if cv2.waitKey(1) & 0xFF == 27:
                    break
            time.sleep(args.interval)
    except KeyboardInterrupt:
        pass
    finally:
        if args.preview:
            cv2.destroyAllWindows()
        picam2.stop()
        print("Done.")

if __name__ == "__main__":
    main()
