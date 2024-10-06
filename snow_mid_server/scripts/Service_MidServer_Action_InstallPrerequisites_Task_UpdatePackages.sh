#!/bin/bash

set -ex

sudo dnf update -y
sudo dnf install wget unzip -y
# Pre-requisites for ServiceNow Xanadu
# https://docs.servicenow.com/bundle/xanadu-servicenow-platform/page/product/mid-server/task/t_InstallAMIDServerOnLinux.html
sudo dnf -y install glibc.i686