Bootstrap: debootstrap
OSVersion: xenial
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

%runscript
    exec echo "The runscript is the containers default runtime command!"

%setup

    # Thread about Snap install on Singularity: https://groups.google.com/a/lbl.gov/forum/#!topic/singularity/wGfm_nf-b2I
    # presumes snap is already installed on my host system
    snap install cloudcompare
    snap refresh --edge cloudcompare

    # copy a snap installed directory to the container root file system
    SNAP_BASE=/snap
    mkdir -p ${SINGULARITY_ROOTFS}$SNAP_BASE

    # Copy cloudcompare
    cp -R $SNAP_BASE ${SINGULARITY_ROOTFS}

    echo "Looking in directory '$SINGULARITY_ROOTFS' for /bin/sh"
        if [ ! -x "$SINGULARITY_ROOTFS/bin/sh" ]; then
            echo "Hrmm, this container does not have /bin/sh installed..."
            exit 1
        fi
    exit 0

%environment

%post
    echo 'export PATH=$PATH:/snap/bin'>>$SINGULARITY_ENVIRONMENT
    echo "deb http://us.archive.ubuntu.com/ubuntu/ xenial main restricted universe multiverse" >> /etc/apt/sources.list

    apt-get update
    apt-get -y upgrade
    apt-get -y install emacs vim nano \
    lshw lsb-release bash-completion \
    kmod iputils-ping net-tools \
    squashfuse fuse snapd make wget curl
 
    systemctl enable snapd

    wget https://sourceforge.net/projects/virtualgl/files/2.5.2/virtualgl_2.5.2_amd64.deb/download -O /tmp/virtualgl_2.5.2_amd64.deb
    apt-get -y install mesa-utils mesa-utils-extra x11-apps
    dpkg -i /tmp/virtualgl_2.5.2_amd64.deb

    apt-get install -y blender meshlab
