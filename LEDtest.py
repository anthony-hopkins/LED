#!/usr/bin/python

import RPi.GPIO as GPIO
import sys
import time

class TestLED:

    def ledOn(self, pin):
        try:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.HIGH)
        except KeyboardInterrupt:
            GPIO.cleanup()
        except Exception as e:
            print(e)
            GPIO.cleanup()


    def ledOff(self, pin):
        try:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)
        except KeyboardInterrupt:
            GPIO.cleanup()
        except Exception as e:
            print(e)
            GPIO.cleanup()
