import random

def temp_hum_gen():
  temperature = random.randint(20, 60)
  humidity = random.randint(30, 60)
  return humidity, temperature

humidity = temperature = 0
while True:
    if temperature < 45:
        humidity, temperature = temp_hum_gen()
        print('Humidity:', humidity, 'Temperature:', temperature)
    else:
        print('High Temperature Detected')
