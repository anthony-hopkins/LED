#!/usr/bin/python

import RPi.GPIO as GPIO
import sys
import time

class LED:

    def __init__(self):
       GPIO.setmode(GPIO.BCM)
       GPIO.setwarnings(False)

    def ledOn(self, pin):
        try:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.HIGH)
        except KeyboardInterrupt:
            GPIO.cleanup()
        except Exception as e:
            print(e)
            GPIO.cleanup()

    def ledOff(self, pin):
        try:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)
        except KeyboardInterrupt:
            GPIO.cleanup()
        except Exception as e:
            print(e)
            GPIO.cleanup()

    def ledTimed(self, pin, delay):
        try:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(delay)
            GPIO.output(pin, GPIO.LOW)
        except KeyboardInterrupt:
            GPIO.cleanup()
        except Exception as e:
            GPIO.cleanup()
            print(e)
