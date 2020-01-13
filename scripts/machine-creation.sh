#!/bin/bash

sudo apt-get update

sudo apt-get install -y build-essential

# install cuda
wget https://developer.nvidia.com/compute/cuda/10.0/Prod/local_installers/cuda-repo-ubuntu1604-10-0-local-10.0.130-410.48_1.0-1_amd64
sudo apt-key add /var/cuda-repo-10-0-local-10.0.130-410.48/7fa2af80.pub
sudo dpkg -i cuda-repo-ubuntu1604-10-0-local-10.0.130-410.48_1.0-1_amd64
sudo apt-get update
sudo apt-get install -y --allow-unauthenticated cuda
export PATH=/usr/local/cuda-10.0/bin${PATH:+:${PATH}}

# install cudnn
wget http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1604/x86_64/libcudnn7_7.5.1.10-1+cuda10.0_amd64.deb
sudo dpkg -i libcudnn7_7.5.1.10-1+cuda10.0_amd64.deb

wget http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1604/x86_64/libcudnn7-dev_7.5.1.10-1+cuda10.0_amd64.deb
sudo dpkg -i libcudnn7-dev_7.5.1.10-1+cuda10.0_amd64.deb

# install needed packages
sudo apt-get install -y cmake \
	git \
	libatlas-base-dev \
	libprotobuf-dev \
	libleveldb-dev \
	libsnappy-dev \
	libhdf5-serial-dev \
	protobuf-compiler \
	libboost-all-dev \
	libgflags-dev \
	libgoogle-glog-dev \
	liblmdb-dev \
	pciutils \
	python3-setuptools \
	python3-dev \
	python3-pip \
	opencl-headers \
	ocl-icd-opencl-dev \
	libviennacl-dev \
	libcanberra-gtk-module \
	libopencv-dev \
	htop \
	tmux \
	ffmpeg \
	xinit

# install common python packages
pip3 install tensorflow-gpu torch torchvision ipython jupyter keras opencv-python screen
pip install --upgrade google-cloud-bigquery
pip install --upgrade google-cloud-storage