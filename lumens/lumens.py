import RPi.GPIO as GPIO
import time
import logging
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()

led_pins = {'r': 26, 'b': 26, 'g': 26, 'w': 26}

#set up gpio
print GPIO.VERSION
GPIO.setmode(GPIO.BCM)


class Lumens:

    def __init__(self):
        logging.getLogger('lumens').info('Butler is starting...')
        for led in led_pins:
            pin = led_pins[led]
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, 1)

    def toggle(self, led):
        pin = led_pins[led]
        logging.getLogger('lumens').info('toggle %s %s' % (led, pin))
        current_status = GPIO.input(pin)
        if current_status == 1:
            GPIO.output(pin, 0)
        else:
            GPIO.output(pin, 1)
