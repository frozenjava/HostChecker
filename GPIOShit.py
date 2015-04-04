import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
# arrays for pin numbers
pinListAll = [17, 27, 22, 23]
pinListOn = [17, 27]
pinListOff = [22, 23]
# loop through pins and set mode and state to 'low'
 
for i in pinListAll:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)


# main loop
def lights_on():
    """
    Turn on the lights
    :return: None
    """
    try:
        for i in pinListOn:
            GPIO.output(i, GPIO.LOW)
            time.sleep(1.5)
	    GPIO.output(i, GPIO.HIGH)
	    time.sleep(1)
    except Exception:
        pass


def lights_off():
    """
    Turn off the lights
    :return: None
    """
    try:
        for i in pinListOff:
            GPIO.output(i, GPIO.LOW)
            time.sleep(1.5)
	    GPIO.output(i, GPIO.HIGH)
	    time.sleep(1)
    except Exception:
        pass


def cleanup():
    """
    Cleanup memory shit or whatever this does
    :return: None
    """
    GPIO.cleanup()
