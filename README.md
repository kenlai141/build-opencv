# Build OpenCV-4.1.0 with CUDA-10.0 in Ubuntu-18.04

```
sudo apt-get update
sudo apt-get install -y python3-dev python3-pip [//]:# make sure using python 3.6
sudo apt-get install ubuntu-desktop
reboot
```

Change to display card output
1. open Software updater 
2. settings
3. Additional drivers 
4. Using Nvidia 430 
5. Apply changes 
6. wait to complete 
7. reboot

```
pip3 install --upgrade dm-sonnet==1.35
pip3 install --upgrade Cython
pip3 install --upgrade Flask
pip3 install --upgrade imageio
pip3 install --upgrade scikit-learn==0.20.3
pip3 install --upgrade tensorflow-gpu==1.14
pip3 install --upgrade keras==2.3.1
pip3 install --upgrade tensorflow-probability==0.7.0
pip3 install --upgrade pandas
pip3 install --upgrade joblib
sudo apt update -y
sudo apt upgrade -y --no-install-recommends
sudo apt install -y build-essential pkg-config cmake git wget curl unzip
```

Then follow the files order:
1. install-cuda-10.0-ubuntu-18.04.md
2. install-dlib.md
3. install-opencv-4.1.0.md
4. verify installed.md
