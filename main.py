import sys
import Adafruit_DHT
import datetime
# import random
from voice_var import ISAC_Ready, isac_t_v_low, isac_t_medium_low, isac_t_low
import pygame

pygame.init()
isac_on_ready = pygame.mixer.Sound(ISAC_Ready)
now = datetime.datetime.now()

isac_on_ready.play()
while pygame.mixer.music.get_busy():
    continue

# !!!!!!!!!
# For the time being out of the city and the normal Internet, I will learn to use this module correctly,
# as well as some others. At the moment, there is an example for working with a sensor.
# !!!!!!!!!

# Parse command line parameters.

sensor_args = {'11': Adafruit_DHT.DHT11,
               '22': Adafruit_DHT.DHT22,
               '2302': Adafruit_DHT.AM2302}
if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
    sensor = sensor_args[sys.argv[1]]
    pin = sys.argv[2]
else:
    print
    'usage: sudo ./Adafruit_DHT.py [11|22|2302] GPIOpin#'
    print
    'example: sudo ./Adafruit_DHT.py 2302 4 - Read from an AM2302 connected to GPIO #4'
    sys.exit(1)

# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

# Un-comment the line below to convert the temperature to Fahrenheit.

temperature = temperature * 9/5.0 + 32

# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).  
# If this happens try again!

if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
else:
    print('Failed to get reading. Try again!')
    sys.exit(1)

if 32 < temperature:
    isac_t_low.play()
elif 14 < temperature:
    isac_t_medium_low.play()
elif -4 < temperature:
    isac_t_v_low.play()
else:
    pass


pygame.quit()
