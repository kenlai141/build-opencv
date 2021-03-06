### CUDA-10.0 + cuDNN 7.6.4 + TensorRT
reference: https://medium.com/@maniac.tw/ubuntu-18-04-%E5%AE%89%E8%A3%9D-nvidia-driver-418-cuda-10-tensorflow-1-13-a4f1c71dd8e5

0. Add NVIDIA repository into apt

```bash
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-repo-ubuntu1804_10.0.130-1_amd64.deb
sudo dpkg -i cuda-repo-ubuntu1804_10.0.130-1_amd64.deb
sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pub
sudo apt update
wget http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/nvidia-machine-learning-repo-ubuntu1804_1.0.0-1_amd64.deb
sudo apt install ./nvidia-machine-learning-repo-ubuntu1804_1.0.0-1_amd64.deb
sudo apt update
```

1. Installed NVIDIA Driver

```bash
ubuntu-drivers devices
```

2. Install CUDA 10.0 & cuDNN 7.6.4

```bash
sudo apt-get install --no-install-recommends \
    cuda-10-0 \
    libcudnn7=7.6.4.38-1+cuda10.0  \
    libcudnn7-dev=7.6.4.38-1+cuda10.0
```

3. Install TensorRT 5.1.5.0

```bash
sudo apt update && sudo apt-get install nvinfer-runtime-trt-repo-ubuntu1804-5.1.5-ga-cuda10.0 \
    && sudo apt update && sudo apt install -y --no-install-recommends \ 
    libnvinfer-dev=5.1.5-1+cuda10.0
```
Other approach: https://dmitry.ai/t/topic/41

4. Set environment variable

***************************************************************
Make sure you are in directory ```~/```
```bash
cd ~
sudo echo "export PATH=$PATH:/usr/local/cuda/bin" >> .bashrc
sudo echo "export LD_LIBRARY_PATH=/usr/local/cuda/lib64" >> .bashrc
source .bashrc
```
***************************************************************

5. Verify installed

```bash
nvidia-smi
nvcc -V
```

```bash
reboot 
```
