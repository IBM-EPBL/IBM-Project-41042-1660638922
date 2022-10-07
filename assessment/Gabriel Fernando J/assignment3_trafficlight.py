from gpiozero import Button, TrafficLights, Buzzer
import time

buzz = Buzzer(15)
b = Button(21)
light = TrafficLights(25,8,7)

while True:
  b.wait_for_press()
  buzz.on()
  light.green.on()
  time.sleep(1)
  light.amber.on()
  time.sleep(1)
  light.red.on()
  time.sleep(1)
  light.off()
  buzz.off()
  
