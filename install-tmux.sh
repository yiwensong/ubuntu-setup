#!/bin/sh
VERSION=2.8
pushd /tmp
wget https://github.com/tmux/tmux/releases/download/${VERSION}/tmux-${VERSION}.tar.gz -O tmux.tar.gz
tar -xvzf tmux.tar.gz
cd tmux-${VERSION}
./configure && make
make install
