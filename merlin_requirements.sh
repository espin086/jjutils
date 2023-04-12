#!/bin/bash
echo '################ Preparing Merlin Video Embedding Environment#####################'

echo '----------------------------------------------------------------------------------'
echo 'DOWNLOADING ANACONDA TO LOCAL MACHINE'
echo '----------------------------------------------------------------------------------'
#wget -nc https://repo.anaconda.com/archive/Anaconda2-5.2.0-Linux-x86_64.sh

#bash Anaconda2-5.2.0-Linux-x86_64.sh

echo '----------------------------------------------------------------------------------'
echo "INSTALLING YOUTUBE DOWNLOADER FROM GITHUB: https://github.com/rg3/youtube-dl#installation"
echo '----------------------------------------------------------------------------------'
#sudo curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl
#sudo chmod a+rx /usr/local/bin/youtube-dl

echo '----------------------------------------------------------------------------------'
echo 'INSTALLING YOUTUBE INCEPTION MODEL FROM GITHUB: https://github.com/google/youtube-8m.git'
echo '----------------------------------------------------------------------------------'
#sudo apt install git-all
#git clone https://github.com/google/youtube-8m.git

echo '---------------------------------------------------------------------------------'
echo 'LOADING REQUIRED PYTHON PACKAGES (e.g. OpenCV2)'
echo '---------------------------------------------------------------------------------'
#sudo apt install python-pip
#sudo apt-get update
#sudo apt-get install libgtk2.0-dev
#pip2 install -r requirements.txt
#pip2 install opencv-python

echo '---------------------------------------------------------------------------------'
echo 'CREATING LOCAL DIRECTORIES TO SAVE LOCAL DATA'
echo '---------------------------------------------------------------------------------'
#mkdir -p lookup_tables logs  embeddings frames tfrecords videos/clean_videos videos/raw_videos


echo '---------------------------------------------------------------------------------'
echo 'COMMANDS TO CONFIGURE OPEN COMPUTER VISION 2 (OPENCV2)'
echo '---------------------------------------------------------------------------------'

#prior to running the conda command the terminal needs to be reset
#reset

#downloading opencv
conda install -c menpo opencv
#downloaing dependencies of opencv
conda install -c defaults libprotobuf protobuf
conda install -c conda-forge ffmpeg

echo '---------------------------------------------------------------------------------'
echo 'INSTALLING GOOGLE CLOUD STORAGE'
echo '---------------------------------------------------------------------------------'
conda install -c conda-forge google-cloud-storage
#IF YOU RESTART YOUR MACHINE, RERUN THIS need to remove boto from the settings for program to work
sudo rm -f /etc/boto.cfg

echo '---------------------------------------------------------------------------------'
echo 'REMOVING ARCHIVE.TXT WHICH WILL ERASE RECORDS OF ALL VIDEOS THAT HAVE BEEN DOWNLOADED'
echo '---------------------------------------------------------------------------------'
#rm ../logs/archive.txt


echo '---------------------------------------------------------------------------------'
echo 'MANUAL INSTALLATION OF PACKAGES - SEEMS TO BE NO AUTOMATED WAY TO DO THIS'
echo '---------------------------------------------------------------------------------'
