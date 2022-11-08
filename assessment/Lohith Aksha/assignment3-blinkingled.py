import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)

while True:
  GPIO.output(40, GPIO.HIGH)
  time.sleep(1)
  GPIO.output(40, GPIO.LOW)
  time.sleep(1)
