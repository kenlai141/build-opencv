# Build OpenCV-4.1.0 with CUDA-10.0 in Ubuntu-18.04

## If install from ubuntu-server

```bash
sudo apt-get update
sudo apt-get install -y python3-dev python3-pip # make sure using python 3.6
sudo pip3 install --upgrade pip # make sure using pip3 > 19.0.0
sudo apt-get install ubuntu-desktop
reboot
```

## Install from ubuntu-desktop

Change to display card output
1. open Software updater 
2. settings
3. Additional drivers 
4. Using Nvidia 430 
5. Apply changes 
6. wait to complete 
7. reboot

Download or create the requirements.txt
```bash
pip3 install -r requirements.txt
```

```bash
sudo apt update -y
sudo apt upgrade -y --no-install-recommends
sudo apt install -y build-essential pkg-config cmake git wget curl unzip
```

Then follow the files order:
1. install-cuda-10.0-ubuntu-18.04.md
2. install-dlib.md
3. install-opencv-4.1.0.md
4. verify installed.md
