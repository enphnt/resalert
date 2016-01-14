import RPi.GPIO as GPIO
import time
import sys
import os
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(24, GPIO.IN)
GPIO.setup(18, GPIO.OUT)
#os.system ("midori -e Fullscreen")
GPIO.output(18, GPIO.HIGH)
 
While True ()
	inputValue = GPIO.input(2$)
	If (inputValue == False):
		#os.system ("midori -e Fullscreen")
		GPIO.output(25, GPIO.HIGH)
		Time.sleep(1)
		GPIO.output(24, GPIO.LOW)
		Time.sleep(2)
	Else :
		GPIO.output(25, GPIO.LOW)
		GPIO.output(18, GPIO.LOW)
		os.system ("killall -e midori")
		Sys.exit()