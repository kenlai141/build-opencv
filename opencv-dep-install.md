### Install opencv dependancies
```bash
sudo apt install -y libgtk-3-dev
sudo apt install -y ffmpeg
sudo apt install -y libavcodec-dev libavformat-dev libavutil-dev libswscale-dev libavresample-dev
sudo apt install -y libyaml-cpp-dev libgoogle-glog-dev libgflags-dev
```
```bash
sudo apt-get install -y libjpeg8-dev libtiff5-dev libjasper-dev libpng12-dev
sudo apt-get install -y libgtk2.0-dev
sudo apt-get install -y libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install -y libatlas-base-dev gfortran
sudo apt-get install -y libhdf5-serial-dev
sudo apt-get install -y python2.7-dev
```

*********************************************************************
```bash
cd ~/Downloads
```
Download below files
<a href="https://hkpc-my.sharepoint.com/:u:/g/personal/kenlai_hkpc_org/EV-VN6E5SlBLsMnr7dqtx5IB9fMYXz2j3PiwMHGWsHjgKQ?e=myihCm" target="_blank">opencv-4.1.0</a>
[opencv-4.1.0](https://hkpc-my.sharepoint.com/:u:/g/personal/kenlai_hkpc_org/EV-VN6E5SlBLsMnr7dqtx5IB9fMYXz2j3PiwMHGWsHjgKQ?e=myihCm)

[opencv_contrib-4.1.0](https://hkpc-my.sharepoint.com/:u:/g/personal/kenlai_hkpc_org/EcGCNUHhWBBNnEkRsnnF7gwB5pBtT5TP0wVqrBOBE0TrGg?e=EAL0v1)

unzip ```opencv-4.1.0.zip``` and ```opencv_contrib-4.1.0.zip```
********************************************************************

********************************************************************
```bash
cd ~/Downloads/opencv-4.1.0
mkdir build
cd build
```
********************************************************************
Make sure the current directory is ```~/Downloads/opencv-4.1.0/build/```

```bash
cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D WITH_CUDA=ON \
    -D ENABLE_FAST_MATH=1 \
    -D CUDA_FAST_MATH=1 \
    -D WITH_CUBLAS=1 \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib-4.1.0/modules \
    -D BUILD_opencv_cudacodec=OFF \
    -D BUILD_EXAMPLES=ON ..
```

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

NO need
(optional) 
```bash
-D PYTHON3_EXECUTABLE=$(which python3) \
-D PYTHON3_LIBRARY=/home/ai/venv_t14/lib/python3.6/config-3.6m-x86_64-linux-gnu/libpython3.6m.so \
-D PYTHON3_INCLUDE_DIR=~/venv_t14/include/python3.6m \
-D PYTHON3_NUMPY_INCLUDE_DIR=~/venv_t14/lib/python3.6/site-packages/numpy/core/include \
-D BUILD_opencv_python3=ON \
-D PYTHON3_PACKAGES_PATH=lib/xxxxxxx/site-packages \
```
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

```bash
nproc
make -j $(($(nproc) - 1))
```
```bash
sudo make install
sudo ldconfig
```
