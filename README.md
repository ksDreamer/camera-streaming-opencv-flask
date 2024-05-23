# Camera streaming using opencv and flask
Author: Kevin Stark

## English Introduction
Capture video frames on the camera end (local_camera.py) using OpenCV.  
Send to client (client.py) in MJPEG format through Python's Flask server.  
You can access the homepage of this program through "IP address: port number". For example https://127.0.0.1:5000  
You can start the video stream through "[IP address]:[port number]/video". For example https://127.0.0.1:5000/video  
Protect privacy by reading system variables through os.getenv.  
Templates/index.html is used to test whether the Flask server is running properly and does not affect the video streaming.

Usage:
1. Connect the camera hardware
2. Install necessary libraries.
3. Modify the IP address and port number according to your actual situation.  
*If it is purely local, no modification is required.  
*If the local camera hardware and cloud server are used for subsequent image processing, set the local_ip to the local computer's public IP in the program local_camera.py, and set the ID to the same public IP in client.py to achieve communication.  
*If it involves servers, certain network knowledge is required, such as setting up firewalls, port forwarding, etc.  
3. Run local_camera.py on the camera end
4. Run client.py on the client side

## 中文介绍
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
