import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

class Display(object):
    def __init__(self, LED_PIN=18):
        self.LED = LED_PIN
        GPIO.setup(self.LED, GPIO.OUT)
        self._backlight = GPIO.input(self.LED)

    @property
    def backlight(self):
        return self._backlight

    @backlight.setter
    def backlight(self, value):
        GPIO.output(self.LED, value)
        self._backlight = value
