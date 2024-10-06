# !/bin/bash

set -ex

# remove service
sudo /servicenow/@@{snow_instance_name}@@/agent/bin/mid.sh remove
