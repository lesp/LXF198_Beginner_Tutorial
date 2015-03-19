import RPi.GPIO as GPIO
from time import sleep
from threading import Thread

#Setup the GPIO to show no errors, even if there are.
GPIO.setwarnings(False)
#We will be using the Broadcom pin numbering system
GPIO.setmode(GPIO.BCM)

#Variables that we will use to address our LED, Button and Buzzer

red = 14
amber = 15
green = 18
button = 23
buzzer = 25

GPIO.setup(red, GPIO.OUT)
GPIO.setup(amber, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
try:
    while True:
        GPIO.output(green,1)
        print("Green Lights Cars In Motion")
        sleep(0.2)
        if GPIO.input(button) == False:
            GPIO.output(green,0)
            GPIO.output(amber,1)
            sleep(2)
            GPIO.output(amber,0)
            GPIO.output(red,1)
            for i in range(10):
                print(" W A L K ")
                GPIO.output(green,1)
                GPIO.output(buzzer,1)
                sleep(0.2)
                GPIO.output(green,0)
                GPIO.output(buzzer,0)
                sleep(0.2)
            GPIO.output(red,0)
            sleep(2)
except KeyboardInterrupt:
    GPIO.cleanup()
