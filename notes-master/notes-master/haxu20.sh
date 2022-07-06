#!/bin/bash
# Hax 修复 Ubuntu 20.04 更新问题
# Author：Misaka-blog

sed -i 's/us.archive.ubuntu.com/eu.archive.ubuntu.com/' /etc/apt/sources.list
apt-get update
rm -f haxu20.sh
