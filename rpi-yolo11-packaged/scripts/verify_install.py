import sys, cv2
print('Python:', sys.version.split()[0])
print('OpenCV:', cv2.__version__)
try:
    import ultralytics; print('Ultralytics:', ultralytics.__version__)
except Exception as e:
    print('Ultralytics error:', e)
try:
    import importlib.metadata as im; print('cvzone:', im.version('cvzone'))
except Exception as e:
    print('cvzone error:', e)
