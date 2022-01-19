import time
import board
import adafruit_hcsr04
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
from adafruit_hcsr04 import HCSR04

GPIO.setup("P8_38", GPIO.IN)
