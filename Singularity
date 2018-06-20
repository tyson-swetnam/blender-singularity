Bootstrap: debootstrap
OSVersion: xenial
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

%runscript
    exec echo "Starting Blender"
    exec blender
%setup
    echo "Looking in directory '$SINGULARITY_ROOTFS' for /bin/sh"
        if [ ! -x "$SINGULARITY_ROOTFS/bin/sh" ]; then
            echo "Hrmm, this container does not have /bin/sh installed..."
            exit 1
        fi
    exit 0

%post
    echo "deb http://us.archive.ubuntu.com/ubuntu/ xenial main restricted universe multiverse" >> /etc/apt/sources.list

    apt-get update
    apt-get -y upgrade
    apt-get install -y emacs vim nano \
    lshw lsb-release bash-completion \
    kmod iputils-ping net-tools \ 
    make wget curl

    wget https://sourceforge.net/projects/virtualgl/files/2.5.2/virtualgl_2.5.2_amd64.deb/download -O /tmp/virtualgl_2.5.2_amd64.deb
    apt-get -y install mesa-utils mesa-utils-extra x11-apps
    dpkg -i /tmp/virtualgl_2.5.2_amd64.deb
    
    # Install Blender & Meshlab
    apt-get install -y blender meshlab
