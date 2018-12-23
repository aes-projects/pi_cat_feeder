#!/usr/bin/env python

from gpiozero import Servo, AngularServo
from time import sleep, asctime, time
from datetime import datetime
from requests import post
import sys
import numpy as np
import os
from glob import glob

url = os.environ.get"FEEDER_URL")

min_angle = -54
max_angle = 47
num_angles = 20

mygpio = 17

time = .3

def main(time, mygpio, url, min_angle, max_angle, num_angles):
    try:
        status = dispense(time, servo, num_angles)
    except Exception as exception:
        status = "failure"
    finally:
        poster(url, status)
        
#         append positive feed file with status
#         poster(, status)

        

def dispense(time, mygpio, min_angle, max_angle, num_angles):
    servo = AngularServo(mygpio, min_angle = min_angle, max_angle = max_angle, initial_angle = min_angle)
    num_angles = num_angles
    angles = np.linspace(servo.min_angle, servo.max_angle, num_angles)
    time_step = time/num_angles
    for angle in np.concatenate((angles, angles[::-1])):
        servo.angle = int(angle)
        sleep(time_step)
    servo.detach()
    return("success")

def poster(url, status)
    log_files = glob("log_*.json")
    synced = True
    if log_files:
        for file in log_files:
            if os.path.isfile(file):
                with open(file) as log_file:
                    log = json.load(log_file)
                try:
                    post(url, data={"log":log})
                except:
                    synced = False
    
    try:
        post(url, data={"status":status})
    except Exception as exception:
        new_log = dict(exception=exception, status=status, time=asctime())
        with open("log_" + str(time()) + ".json", 'w') as log_file:
            json.dumps(new_log, log_file)
    else:
        if synced:
            try:
                os.remove(log_files)

                

main(time, mygpio, url, min_angle, max_angle, num_angles)
sys.exit(0)