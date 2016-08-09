#!/bin/sh

sudo apt-get --assume-yes install git

wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py

pip install apscheduler
pip install flask

APP_NAME='lumens'
APP_HOME=/opt/${APP_NAME}
APP_BIN=${APP_HOME}/bin
APP_LOGS_DIR=/var/log/${APP_NAME}

if [ -d ${APP_HOME} ]; then
    cd ${APP_HOME}
    git pull
else
    cd /opt
    git clone https://github.com/gurumitts/${APP_NAME}.git
    cd ${APP_HOME}
    git pull
fi

if [ ! -d ${APP_LOGS_DIR} ]; then
    mkdir ${APP_LOGS_DIR}
fi

cp -f ${APP_BIN}/${APP_NAME} /etc/init.d/

update-rc.d ${APP_NAME} defaults



