#!/usr/bin/python
"""
Raspberry Pi LED Control Library

This module provides simple LED control functionality for Raspberry Pi GPIO pins.
It includes basic operations like turning LEDs on/off and timed blinking,
with proper error handling and GPIO cleanup.
"""

import RPi.GPIO as GPIO
import sys
import time


class LED:
    """LED control class for Raspberry Pi GPIO pins.
    
    This class provides methods to control individual LEDs connected to GPIO pins,
    including basic on/off control and timed operations with automatic cleanup.
    """

    def __init__(self):
        """Initialize LED controller with GPIO configuration."""
        GPIO.setmode(GPIO.BCM)        # Use BCM (Broadcom) pin numbering
        GPIO.setwarnings(False)       # Disable GPIO warnings for cleaner operation

    def ledOn(self, pin):
        """Turn on LED connected to specified GPIO pin.
        
        Args:
            pin (int): GPIO pin number (BCM numbering)
        """
        try:
            GPIO.setup(pin, GPIO.OUT)      # Configure pin as output
            GPIO.output(pin, GPIO.HIGH)    # Set pin to HIGH (3.3V) to turn on LED
        except KeyboardInterrupt:
            print("LED operation interrupted by user")
            GPIO.cleanup()
        except Exception as e:
            print(f"Error turning on LED: {e}")
            GPIO.cleanup()

    def ledOff(self, pin):
        """Turn off LED connected to specified GPIO pin.
        
        Args:
            pin (int): GPIO pin number (BCM numbering)
        """
        try:
            GPIO.setup(pin, GPIO.OUT)      # Configure pin as output
            GPIO.output(pin, GPIO.LOW)     # Set pin to LOW (0V) to turn off LED
        except KeyboardInterrupt:
            print("LED operation interrupted by user")
            GPIO.cleanup()
        except Exception as e:
            print(f"Error turning off LED: {e}")
            GPIO.cleanup()

    def ledTimed(self, pin, delay):
        """Blink LED for specified duration.
        
        Args:
            pin (int): GPIO pin number (BCM numbering)
            delay (float): Duration in seconds to keep LED on
        """
        try:
            GPIO.setup(pin, GPIO.OUT)      # Configure pin as output
            GPIO.output(pin, GPIO.HIGH)    # Turn on LED
            time.sleep(delay)              # Wait for specified duration
            GPIO.output(pin, GPIO.LOW)     # Turn off LED
        except KeyboardInterrupt:
            print("LED timing operation interrupted by user")
            GPIO.cleanup()
        except Exception as e:
            GPIO.cleanup()
            print(f"Error during LED timing operation: {e}")
