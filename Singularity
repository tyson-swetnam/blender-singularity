Bootstrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/
Include: yum

%help
Abandon all hope, ye who enter here.

%files
    ~/blender-singularity/config.py
    ~/blender-singularity/render.sh
    
%setup
    yum install wget
%environment

%post
    
    # Update everything
    yum update -y
    yum install -y gcc kernel-devel-`uname -r`

    # Install latest NVIDIA Drivers
    wget http://us.download.nvidia.com/XFree86/Linux-x86_64/390.67/NVIDIA-Linux-x86_64-390.67.run
    sudo /bin/bash ./NVIDIA-Linux-x86_64-390.67.run
    
    # Set GPU to be persistent, disable autoboost
    nvidia-smi -pm 1
    nvidia-smi --auto-boost-def
    
    # Install video driver dependencies
    yum -y install freetype freetype-devel libpng-devel
    yum -y install mesa-libGLU-devel
    yum -y install libX11-devel mesa-libGL-devel perl-Time-HiRes

    # Install Blender
    wget https://builder.blender.org/download//blender-2.79-3ee606621cf-linux-glibc219-x86_64.tar.bz2
    tar -jxvf blender-2.79-3ee606621cf-linux-glibc219-x86_64.tar.bz2

 %labels
    Maintainer Tyson Lee Swetnam
    Version v0.1
    Date 2018-6-15
