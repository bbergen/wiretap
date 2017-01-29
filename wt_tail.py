from wt_exception import WiretapFileException
import os
import time


class Tailer:
    def __init__(self, channel):
        self.channel = channel
        self.running = False

    def start_tail(self):
        self.running = True
        #TODO(bryan) implement

    def stop_tail(self):
        self.running = False


def tail_file(path, callback):
    """
    Opens file at the path, and tails it
    New lines are passed to the callback
    :param path: string
    :param callback: function(string)
    """
    exists = os.path.exists(path)
    if not exists:
        raise WiretapFileException("Invalid File Path")
    else:
        file = open(path)
        lines = fetch_lines(file)
        for line in lines:
            callback(line)


def fetch_lines(file):
    file.seek(0, 2)
    while True:
        line = file.readline()
        if not line:
            time.sleep(1)
            continue
        yield line


