import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

counter = 0
try:
	while counter < 30:
		print "LED 1  on"
		GPIO.output(18,GPIO.HIGH)
		time.sleep(1)
		print "LED 2  on"
		GPIO.output(17,GPIO.HIGH)
		time.sleep(1)
		print "LED 3 on"
		GPIO.output(27,GPIO.HIGH)
		time.sleep(3)
		print "LED off"
		GPIO.output(18,GPIO.LOW)
		GPIO.output(17,GPIO.LOW)
		GPIO.output(27,GPIO.LOW)
		counter = counter + 1
except KeyboardInterrupt:
	print "\n", counter
finally:
	GPIO.cleanup()