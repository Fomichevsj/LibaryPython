import signal

from psutil._pswindows import TimeoutExpired


def alarm_handler(signum, frame):
    raise TimeoutExpired

def input_with_timeout(prompt, timeout):
    # set signal handler
    signal.signal(signal.SIGBREAK, alarm_handler)
    signal.signal(timeout) # produce SIGALRM in `timeout` seconds

    try:
        return input(prompt)
    finally:
        signal.signal(0) # cancel alarm
s = input_with_timeout("вводи", 10)