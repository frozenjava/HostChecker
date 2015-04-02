import sys
import os
import time
import signal

LOG_PATH = "/tmp/HostChecker.log"

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
    """

    f = open(LOG_PATH, "w")
    f.write(str(int(time.time())))
    f.close()

def read_timestamp():
    """
    Writes the current timestamp to a file.
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

    while True:

        current_time = int(time.time())
        current_hour = int(time.localtime(current_time)[3])

        if (current_hour >= 22) or (current_hour <= 7):
        
            if not os.path.isfile(LOG_PATH):
                write_timestamp()

            logged_time = read_timestamp()
            seconds_past = current_time - logged_time

            if ping_host(host) == 0:
                print "ping"
                if seconds_past >= 20*60:
                    """ lights_on() """
                    time.sleep(5 * 60)
                    """ lights_off() """
                write_timestamp()

        else:
            print "Not between 22:00 and 03:00"
            time.sleep(4)

        time.sleep(1)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        host = sys.argv[1]
        main(host)
