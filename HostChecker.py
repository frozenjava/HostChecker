import sys
import os
import time
import GPIOShit
import signal

LOG_PATH = "/tmp/HostChecker.log"


def sig_handler(signal, frame):
    """
    Handle signals
    :param signal: the signal
    :param frame: the frame
    :return: None
    """
    GPIOShit.cleanup()


def ping_host(host):
    """
    Ping the host to see if its up
    :param host: The host to ping
    :return status: Is the host around, true or false
    """

    status = os.system("ping " + host + " -c 1 -W 1 > /dev/null")

    return status


def write_timestamp():
    """
    Writes the current timestamp to a file.
    :return: None
    """

    f = open(LOG_PATH, "w")
    f.write(str(int(time.time())))
    f.close()


def read_timestamp():
    """
    Writes the current timestamp to a file.
    :return timestamp: The timestamp to return
    """

    f = open(LOG_PATH, "r")
    timestamp = int(f.read())
    f.close()

    return timestamp


def main(host):
    """
    The main program
    :param args: The arguments for the program
    :return: None
    """

    sebkinne_is_a_wizard = True

    while sebkinne_is_a_wizard:

        current_time = int(time.time())
        current_hour = int(time.localtime(current_time)[3])

        if (current_hour >= 22) or (current_hour <= 3):
        
            if not os.path.isfile(LOG_PATH):
                write_timestamp()

            logged_time = read_timestamp()
            seconds_past = current_time - logged_time

            if ping_host(host) == 0:
                if seconds_past >= 20*60:
                    GPIOShit.lights_on()
                    time.sleep(5 * 60)
                    GPIOShit.lights_off()
                write_timestamp()

        else:
            print "Not between 22:00 and 03:00"
            time.sleep(4)

        time.sleep(1)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        host = sys.argv[1]
        signal.signal(signal.SIGINT, sig_handler)
        main(host)
