# update and install essential tools
apt update
apt install build-essential -y
apt install python3-pip git -y
apt install python3-venv -y

# install openalpr
apt install openalpr

# download weights
wget https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.weights -O ./yolov4/yolov4.weights
