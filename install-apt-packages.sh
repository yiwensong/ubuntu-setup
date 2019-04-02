#!/bin/sh
apt-add-repository -y ppa:neovim-ppa/stable
apt-add-repository -y ppa:git-core/ppa
apt-add-repository -y ppa:fish-shell/release-3
apt-add-repository -y ppa:deadsnakes/ppa
apt-add-repository -y ppa:pi-rho/dev
apt-get update -y
apt-get install -y\
    python3.7\
    curl\
    git\
    vim-gtk\
    libevent-dev\
    python-software-properties\
    software-properties-common\
    fish\
    neovim\
    python3-virtualenv\
    libncurses-dev
apt-get upgrade -y
apt autoremove -y