import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
# init list with pin numbers
pinList = [17, 27, 22, 23]
# loop through pins and set mode and state to 'low'
 
for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)


# main loop
def lights_on():
    """
    Turn on the lights
    :return: None
    """
    try:
        for i in pinList:
            GPIO.output(i, GPIO.LOW)
            time.sleep(.5)
            #GPIO.cleanup()
    except Exception:
        pass


def lights_off():
    """
    TUrn off the lights
    :return: None
    """
    try:
        for i in pinList:
            GPIO.output(i, GPIO.HIGH)
            time.sleep(.5)
            #GPIO.cleanup()
    except Exception:
        pass