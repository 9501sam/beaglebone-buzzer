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
note = {
        1: 261.63, 
        2: 293.66, 
        3: 329.63, 
        4: 349.23, 
        5: 392.00, 
        6: 440.00, 
        7: 493.88, 
        11: 523.25, 
        22: 587.33
        }
# piece = ["G4", "G4", "A4", "B4", "D5", "B4", "A4", "G4", "A4", "B4", "G4"]
piece = [5, 5, 6, 7, 7, 6, 5, 4, 3, 3, ]

for i in piece:
    PWM.start(BUZZER, duty_cycle = volume, frequency = note[i])
    time.sleep(0.5)
    PWM.set_duty_cycle(BUZZER, float(0.1))
    time.sleep(0.05)


PWM.stop(BUZZER)
PWM.cleanup()

# while True:
#     try:
#         print((sonar.distance,))
#         distance = sonar.distance
#         
#         if distance < 10:
#             PWM.set_frequency(BUZZER, float(C5))
#         elif distance < 20:
#             PWM.set_frequency(BUZZER, float(B4))
#         elif distance < 30:
#             PWM.set_frequency(BUZZER, float(A4))
#         elif distance < 40:
#             PWM.set_frequency(BUZZER, float(G4))
#         elif distance < 50:
#             PWM.set_frequency(BUZZER, float(F4))
#         elif distance < 60:
#             PWM.set_frequency(BUZZER, float(E4))
#         elif distance < 70:
#             PWM.set_frequency(BUZZER, float(D4))
#         elif distance < 80:
#             PWM.set_frequency(BUZZER, float(C4))
#     
#     except RuntimeError:
#         print("Retrying!")
#         PWM.set_frequency(BUZZER, float(C4))
#         # PWM.start(BUZZER, 0)
#         # PWM.set_duty_cycle(BUZZER, float(0))
#     except KeyboardInterrupt:
#         PWM.stop(BUZZER)
#         PWM.cleanup()
#     time.sleep(1)

PWM.stop(BUZZER)
PWM.cleanup()
