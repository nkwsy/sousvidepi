#!/usr/bin/python

# Import required Python libraries
import RPi.GPIO as GPIO
import time

# Use BCM GPIO references instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# init list with pin numbers

pinList = [37]

#set relay pin number
relay = 37
# loop through pins and set mode and state to 'low'

for i in pinList:
    GPIO.setwarnings(False)
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.LOW)

def off(i) :
        for i in pinList:
          GPIO.output(i, GPIO.LOW)
#         GPIO.cleanup()
          print i
          #time.sleep(1)
          break

def on(i) :
        for i in pinList:
          GPIO.output(i, GPIO.HIGH)
#         GPIO.cleanup()
          print "heater on"
          #time.sleep(10)
          break



try:
    on(relay)
    off(relay)

except KeyboardInterrupt:
  print "  Quit"
  # Reset GPIO settings
  GPIO.cleanup()


from w1thermsensor import W1ThermSensor
import time


def getTemp():
    sensor = W1ThermSensor()
    temperature_in_celsius = sensor.get_temperature()
    temperature_in_fahrenheit = sensor.get_temperature(W1ThermSensor.DEGREES_F)
    temperature_in_all_units = sensor.get_temperatures([
        W1ThermSensor.DEGREES_C,
        W1ThermSensor.DEGREES_F,
        W1ThermSensor.KELVIN])
    print temperature_in_fahrenheit
    return temperature_in_fahrenheit

print temperature_in_all_units
x = 0

userTemp = raw_input("What temp in F")
cookTime = raw_input("Max cooking time")
startTime = raw_input("Do you want a start time? if so use format 6:30 am . else put n")
def cooking(userTemp,cookTime):
    t0 = time.time()
    curTime = 0
    while curTime < cookTime:
        t1= time.time()
        curTime = t0-t1
        curTemp = getTemp()
        diffTemp = userTemp - curTemp
        if diffTemp >= 10:
            on(i)
            time.sleep(30)
            off(i)
        if diffTemp < 10 and diffTemp > 2:
            on(i)
            time.sleep(10)
            off(i)
            time.sleep(10)
        if diffTemp <= 2:
            on(i)
            time.sleep(1)
            off(i)
            time.sleep(2)
        if diffTemp <= 0:
            time.sleep(4)





while x == 0:
    print temperature_in_fahrenheit
time.sleep(2)
