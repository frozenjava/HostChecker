import sys
import os
import time

import RPi.GPIO as GPIO


def lightson(pin_list):
    try:
       while True:
          for i in pin_list:
             GPIO.output(i, GPIO.LOW)
             time.sleep(.5)
    except Exception:
        pass


def lightsoff(pin_list):
    try:
       while True:
          for i in pin_list:
             GPIO.output(i, GPIO.HIGH)
             time.sleep(.5)
    except Exception:
        pass


def ping_host(host):
    """
    Ping the host to see if its up
    :param host: The host to ping
    :return status: Is the host around, true or false
    """

    status = os.system("ping host -c 1")

    return status


def lights_off():
    """
    Do nothing for now
    :return:
    """


def main(args):
    """
    The main program
    :param args: The arguments for the program
    :return: None
    """

    # The host to ping
    host = args[1]

    pinList = [17, 27, 22, 23]

    log_file = "/tmp/HostChecker.log"

    sebkinne = "is_a_wizard"

    while sebkinne == "is_a_wizard":

        current_time = int(time.time())

        if time.localtime(time.time())[3] > 22 < 3:

            if os.exists(log_file):
                f = open(log_file, "w")
                f.write(str(current_time))
                f.close()

            f = open(log_file, "r")
            previous_time = int(f.read())
            f.close()

            seconds_past = current_time - previous_time

            if ping_host(host) == 0:

                #if minutes_past > 20*60:

                f = open(log_file, "w")
                f.write(str(current_time))
                f.close()

            else:

                if seconds_past > 20*60:
                    lights_off()



        time.sleep(5)

if __name__ == "__main__":
    main(sys.argv)
