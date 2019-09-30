#!/bin/sh
VERSION=11.0.2
curl --fail --location --output /tmp/ripgrep_${VERSION}_amd64.deb https://github.com/BurntSushi/ripgrep/releases/download/$VERSION/ripgrep_${VERSION}_amd64.deb
sudo dpkg -i /tmp/ripgrep_${VERSION}_amd64.deb
