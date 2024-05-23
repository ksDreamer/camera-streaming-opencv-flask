import requests
import cv2
import numpy as np
import os

# Replace with the correct URL of your Flask app
id = os.getenv('FLASK_IP', '127.0.0.1')
port = os.getenv('FLASK_PORT', '5000')
url = f"http://{id}:{port}/video"

stream = requests.get(url, stream=True)

bytes = b''
for chunk in stream.iter_content(chunk_size=1024):
    print(f"Received a chunk of {len(chunk)} bytes")
    bytes += chunk
    a = bytes.find(b'\xff\xd8')
    b = bytes.find(b'\xff\xd9')
    if a != -1 and b != -1:
        print(f"Found a JEPG iamge of {len(bytes[a:b+2])} bytes")
        jpg = bytes[a:b+2]
        bytes = bytes[b+2:]
        img = cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
        if img is None:
            print("Error decoding image")
        else:
            print("Received a new frame")
            cv2.imshow('Video stream', img)
        if cv2.waitKey(1) == 27:  # Exit if ESC key is pressed
            break

cv2.destroyAllWindows()