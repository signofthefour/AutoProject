#!bin/bash

pip install -r requirements.txt
sudo cat .my_commands.sh >> ~/.bashrc
sudo apt-get update
. ~/.bashrc