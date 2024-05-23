# Camera streaming using opencv and flask
# Author: Kevin Stark

'''
用opencv在摄像头端捕获视频帧。
通过Python的Flask服务器以MJPEG格式发送到客户端client.py
可以通过"IP地址:端口号"访问这个程序的主页。例如 https://127.0.0.1:5000
可以通过"IP地址:端口号/video"打开视频流。例如 https://127.0.0.1:5000/video
通过os.getenv读取系统变量保护隐私。
templates/index.html用于测试Flask服务器是否正常运行，不影响视频流的传输。

使用方法：
1. 连接摄像头硬件
2. 安装必要的库。
3. 根据自己实际情况修改IP地址和端口号。
* 如果纯本地，则无需修改。
* 如果是本地摄像头硬件+云端服务器进行后继图像处理，则在本程序 local_camera.py中把local_ip设置为本地计算机的公网IP，在client.py中把id设置为同样的公网IP以实现通信。
* 涉及服务器的话需要一定的网络知识，例如设置防火墙、端口转发等。
3. 在相机端运行local_camera.py
4. 在客户端运行client.py
'''

from flask import Flask, render_template, Response
import cv2
import os

app = Flask(__name__)

camera = cv2.VideoCapture(0)
print("Camera is opened: ", camera.isOpened())

# get frame from camera
def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            print("Failed to read frame")
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)  # encoder images format into streaming data.
            if not ret:
                print("Failed to encode frame")
                continue
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# home page of flask application (not necessary for video streaming, just for testing the html page.) 
@app.route('/')
def index():
    print("Rendering homepage")
    return render_template('index.html')

# video streaming route
@app.route('/video')
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    # local_ip = os.getenv('FLASK_IP', '127.0.0.1') # 如果要严格的单ip地址访问，请采用这个。
    local_ip = '0.0.0.0' # 如果要宽松的ip访问，请采用这个。
    local_port = os.getenv('FLASK_PORT', '5000')
    app.run(host=local_ip, port=local_port)