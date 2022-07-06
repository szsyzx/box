#!/bin/bash

sed -i "s/^#\?precedence ::ffff:0:0/96  100/precedence ::ffff:0:0/96  100/g" /etc/gai.conf;
