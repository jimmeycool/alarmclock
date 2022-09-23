#!/bin/bash

cd ~/repos/alarmclock

source ./.venv/bin/activate

git pull

pip install -r ./requirements.txt

python3 ./run.py