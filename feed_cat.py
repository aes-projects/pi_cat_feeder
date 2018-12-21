#!/usr/bin/env python

from gpiozero import Servo
from time import sleep
import sys

gpio_num = 17
initial_value = 1
time_open = 1

servo = Servo(gpio_num, initial_value=initial_value)

sleep(time_open)
servo.min()
sleep(time_open)
servo.max()
sleep(time_open)
