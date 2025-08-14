# LED Control - Raspberry Pi GPIO LED Library

A Python library for controlling LEDs connected to Raspberry Pi GPIO pins. This project provides simple, reliable LED control functionality including basic on/off operations, timed blinking, and automatic GPIO cleanup for safe operation.

## 🚀 Features

- **Simple LED Control** - Easy on/off and timed operations
- **GPIO Safety** - Automatic pin cleanup and error handling
- **Raspberry Pi Integration** - Native GPIO control using RPi.GPIO library
- **BCM Pin Numbering** - Uses Broadcom pin references for compatibility
- **Error Handling** - Graceful handling of interruptions and exceptions
- **Resource Management** - Automatic GPIO cleanup on errors
- **Cross-Platform** - Works on all Raspberry Pi models with GPIO
- **Lightweight** - Minimal dependencies and memory footprint

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- [Raspberry Pi](https://www.raspberrypi.org/) (any model with GPIO pins)
- [Raspberry Pi OS](https://www.raspberrypi.org/software/) (or compatible Linux distribution)
- [Python 3](https://www.python.org/downloads/) (3.6+ recommended)
- [RPi.GPIO](https://pypi.org/project/RPi.GPIO/) library
- LED components (LED, resistor, connecting wires)

## 🛠️ Quick Start

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd LED
```

### 2. Install Dependencies

```bash
# Install RPi.GPIO library
sudo pip3 install RPi.GPIO

# Or install via apt
sudo apt-get install python3-rpi.gpio
```

### 3. Connect Hardware

Connect your LED to the Raspberry Pi:
- **LED Anode (+)**: GPIO pin (e.g., GPIO 18)
- **LED Cathode (-)**: Through 220Ω resistor to GND
- **Resistor**: 220Ω current-limiting resistor
- **Power**: 3.3V logic level (GPIO pins)

### 4. Basic Usage

```python
from LEDs import LED

# Initialize LED controller
led = LED()

# Basic operations
led.ledOn(18)      # Turn on LED on GPIO 18
led.ledOff(18)     # Turn off LED on GPIO 18
led.ledTimed(18, 2)  # Blink LED for 2 seconds
```

## 🏗️ Project Structure

```
LED/
├── LEDs.py                        # Main LED control library
└── README.md                      # This documentation
```

## 🔧 Configuration

### GPIO Pin Configuration

The LED controller uses:
- **Pin Mode**: BCM (Broadcom) numbering system
- **Pin Direction**: All pins configured as OUTPUT
- **Voltage Level**: 3.3V logic (Raspberry Pi standard)
- **Current Limit**: 16mA per pin (use resistors for LEDs)

### LED Specifications

- **Voltage**: 3.3V logic level compatible
- **Current**: Use current-limiting resistors (220Ω recommended)
- **Polarity**: Ensure correct anode/cathode connection
- **Type**: Any standard LED (5mm, 3mm, etc.)

## 📦 Dependencies

### Core Components

- **RPi.GPIO** - Raspberry Pi GPIO control library
- **Python 3** - Runtime environment
- **time** - Timing functions for delays

### Hardware Requirements

- **Raspberry Pi** - Single-board computer
- **LED Components** - LED, current-limiting resistor
- **Connecting Wires** - Jumper wires for connections
- **Breadboard** - Optional, for prototyping

## 🐳 Usage Examples

### Basic LED Control

```python
from LEDs import LED
import time

# Initialize LED controller
led = LED()

# Simple on/off operations
led.ledOn(18)      # Turn on LED
time.sleep(1)      # Wait 1 second
led.ledOff(18)     # Turn off LED
```

### LED Blinking Patterns

```python
# Blink LED for specific duration
led.ledTimed(18, 0.5)    # Blink for 0.5 seconds

# Create blinking pattern
for i in range(5):
    led.ledOn(18)
    time.sleep(0.2)
    led.ledOff(18)
    time.sleep(0.2)
```

### Multiple LED Control

```python
# Control multiple LEDs
led_pins = [18, 23, 24, 25]

# Turn on all LEDs
for pin in led_pins:
    led.ledOn(pin)

# Turn off all LEDs
for pin in led_pins:
    led.ledOff(pin)

# Blink all LEDs in sequence
for pin in led_pins:
    led.ledTimed(pin, 0.3)
```

### Integration with Other Projects

```python
class LEDIndicator:
    def __init__(self, pin):
        self.led = LED()
        self.pin = pin
    
    def show_status(self, status):
        """Show status with LED patterns."""
        if status == "success":
            self.led.ledTimed(self.pin, 1.0)  # Long blink
        elif status == "error":
            # Rapid blinking for error
            for _ in range(3):
                self.led.ledTimed(self.pin, 0.2)
        elif status == "warning":
            self.led.ledTimed(self.pin, 0.5)  # Medium blink
```

## 🚀 Development Workflow

### Running LED Control

```bash
# Basic operation
python3 -c "
from LEDs import LED
led = LED()
led.ledOn(18)
"

# Test timed operation
python3 -c "
from LEDs import LED
led = LED()
led.ledTimed(18, 2)
"
```

### GPIO Management

```bash
# Check GPIO status
gpio readall

# Monitor GPIO activity
sudo python3 -u -c "
from LEDs import LED
led = LED()
led.ledOn(18)
"

# Clean up GPIO
python3 -c "
import RPi.GPIO as GPIO
GPIO.cleanup()
"
```

### Debugging

```bash
# Run with verbose output
python3 -v -c "
from LEDs import LED
led = LED()
"

# Check LED connections
gpio -g mode 18 out
gpio -g write 18 1
```

## 🔍 Application Features

### LED Operations

- **On/Off Control**: Simple HIGH/LOW pin control
- **Timed Blinking**: Automatic on/off with specified duration
- **Pin Configuration**: Automatic GPIO setup for each operation
- **State Management**: Clear pin state control

### Safety Features

- **Automatic Cleanup**: GPIO pins cleaned up after each operation
- **Error Handling**: Graceful handling of interruptions and errors
- **Resource Management**: Proper GPIO cleanup on exceptions
- **Pin Protection**: Safe pin configuration and operation

### GPIO Management

- **BCM Numbering**: Uses Broadcom pin references
- **Output Configuration**: All pins configured as OUTPUT
- **Warning Suppression**: Clean operation without GPIO warnings
- **Pin Isolation**: Each operation handles its own pin setup

## 🚨 Important Notes

### Safety Considerations

- **Current Limiting**: Always use resistors with LEDs
- **Voltage Levels**: GPIO pins output 3.3V (not 5V)
- **Pin Protection**: Don't exceed 16mA per pin
- **Physical Safety**: Keep hands clear during testing

### Limitations

- **Raspberry Pi Only**: Designed specifically for Raspberry Pi GPIO
- **Single Pin Operations**: Each method operates on one pin at a time
- **Basic Functionality**: Simple on/off and timed operations
- **No PWM**: Basic digital control only

### Best Practices

- **Use Resistors**: Always include current-limiting resistors
- **Check Connections**: Verify LED polarity and connections
- **Test Gradually**: Start with simple operations before complex patterns
- **Clean Up**: Always clean up GPIO when done

## 🚀 Production Deployment

For production use, consider:

1. **Multiple LED Support** - Extend for controlling multiple LEDs simultaneously
2. **PWM Control** - Add brightness control with PWM
3. **Pattern Sequences** - Implement complex LED patterns and animations
4. **Status Indicators** - Use LEDs for system status and notifications
5. **Monitoring** - Add LED health monitoring and diagnostics
6. **Configuration Files** - Use configuration files for LED setups

## 🔧 Customization

### Adding New LED Operations

```python
class AdvancedLED(LED):
    def ledPulse(self, pin, duration, frequency):
        """Create pulsing LED effect."""
        start_time = time.time()
        while time.time() - start_time < duration:
            self.ledOn(pin)
            time.sleep(1/frequency)
            self.ledOff(pin)
            time.sleep(1/frequency)
    
    def ledFade(self, pin, duration):
        """Simulate fade effect with rapid blinking."""
        steps = 100
        for i in range(steps):
            on_time = (i / steps) * (duration / steps)
            off_time = ((steps - i) / steps) * (duration / steps)
            self.ledOn(pin)
            time.sleep(on_time)
            self.ledOff(pin)
            time.sleep(off_time)
```

### LED Pattern Sequences

```python
class LEDPatterns(LED):
    def knight_rider(self, pins, cycles=3):
        """Knight Rider style LED pattern."""
        for _ in range(cycles):
            # Forward sweep
            for pin in pins:
                self.ledOn(pin)
                time.sleep(0.1)
                self.ledOff(pin)
            
            # Reverse sweep
            for pin in reversed(pins):
                self.ledOn(pin)
                time.sleep(0.1)
                self.ledOff(pin)
    
    def wave_pattern(self, pins, duration=2):
        """Wave-like LED pattern."""
        for _ in range(int(duration * 10)):
            for i, pin in enumerate(pins):
                if i % 2 == 0:
                    self.ledOn(pin)
                else:
                    self.ledOff(pin)
            time.sleep(0.1)
            for i, pin in enumerate(pins):
                if i % 2 == 1:
                    self.ledOn(pin)
                else:
                    self.ledOff(pin)
            time.sleep(0.1)
```

### Integration with Sensors

```python
class SensorLED(LED):
    def __init__(self, led_pin, sensor_pin):
        super().__init__()
        self.led_pin = led_pin
        self.sensor_pin = sensor_pin
    
    def sensor_indicator(self):
        """Light LED based on sensor input."""
        GPIO.setup(self.sensor_pin, GPIO.IN)
        if GPIO.input(self.sensor_pin):
            self.ledOn(self.led_pin)
        else:
            self.ledOff(self.led_pin)
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly on actual hardware
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Happy LED Control! 💡**
