import time
import board
import adafruit_hcsr04
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
from adafruit_hcsr04 import HCSR04
TX = board.P9_11 # trag
RX = board.P9_13 # echo
sonar = adafruit_hcsr04.HCSR04(trigger_pin=TX, echo_pin=RX)

volume = 1
BUZZER = "P8_13"
GPIO.setup(BUZZER, GPIO.OUT)
distance = 100.0
PWM.start(BUZZER, duty_cycle = volume, frequency = 100)
while True:
    try:
        print((sonar.distance,))
        distance = sonar.distance
        PWM.set_frequency(BUZZER, float(distance * 20))
    except RuntimeError:
        print("Retrying!")
        # PWM.start(BUZZER, 0)
        # PWM.set_duty_cycle(BUZZER, float(0))
    except KeyboardInterrupt:
        PWM.stop(BUZZER)
        PWM.cleanup()
    time.sleep(0.25)

while True:
    try:
        print((sonar.distance,))
        distance = sonar.distance
        if distance < 5.0:
            PWM.set_duty_cycle(BUZZER, float(0))
            time.sleep(0.1)
            PWM.set_duty_cycle(BUZZER, float(volume))

        elif distance < 10.0:
            PWM.set_duty_cycle(BUZZER, float(0))
            time.sleep(0.5)
            PWM.set_duty_cycle(BUZZER, float(volume))

        elif distance < 15.0:
            PWM.set_duty_cycle(BUZZER, float(0))
            time.sleep(1)
            PWM.set_duty_cycle(BUZZER, float(volume))

        elif distance < 25.0:
            PWM.set_duty_cycle(BUZZER, float(0))
            time.sleep(1.5)
            PWM.set_duty_cycle(BUZZER, float(volume))

        elif distance < 50.0:
            PWM.set_duty_cycle(BUZZER, float(0))
            time.sleep(2)
            PWM.set_duty_cycle(BUZZER, float(volume))

        else:
            PWM.start(BUZZER, volume)

    except RuntimeError:
        print("Retrying!")
        PWM.start(BUZZER, 0)
        PWM.set_duty_cycle(BUZZER, float(0))
      
    except KeyboardInterrupt:
        PWM.stop(BUZZER)
        PWM.cleanup()
    time.sleep(0.1)

PWM.start(BUZZER, 0)
PWM.set_duty_cycle(BUZZER, float(0))
time.sleep(0.5)
