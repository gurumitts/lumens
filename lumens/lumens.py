import RPi.GPIO as GPIO
from random import randint
import logging
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()

led_pins = {'r': 26, 'b': 20, 'g': 21, 'w': 19}

#set up gpio
print GPIO.VERSION
GPIO.setmode(GPIO.BCM)


class Lumens:

    def __init__(self):
        logging.getLogger('lumens').info('lumens is starting...')
        self.random_mode = False
        for led in led_pins:
            pin = led_pins[led]
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, 1)
        scheduler.start()
        scheduler.add_job(self._randomize, 'interval', minutes=2)

    def toggle(self, led):
        pin = led_pins[led]
        logging.getLogger('lumens').info('toggle %s %s' % (led, pin))
        current_status = GPIO.input(pin)
        if current_status == 1:
            GPIO.output(pin, 0)
        else:
            GPIO.output(pin, 1)

    def random(self):
        if self.random_mode:
            self.random_mode = False
        else:
            self.random_mode = True
        logging.getLogger('lumens').info('random mode is %s' % self.random_mode)

    def _randomize(self):
        if self.random_mode:
            self._all_off()
            pin = led_pins[led_pins.keys()[randint(0, 3)]]
            GPIO.output(pin, 1)

    def _all_off(self):
        for led in led_pins:
            pin = led_pins[led]
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, 0)



