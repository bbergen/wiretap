from wt_exception import WiretapFileException
import os
import time


class Tailer:
    def __init__(self, channel, callback):
        self.channel = channel
        self.callback = callback
        self.frequency = 1
        self.running = False

    def start_tail(self):
        self.running = True
        self._check_file()
        self._tail_file()

    def stop_tail(self):
        self.running = False

    def _check_file(self):
        path = self.channel.get_file()
        exists = os.path.exists(path)
        if not exists:
            raise WiretapFileException("Invalid Channel File")

    def _tail_file(self):
        path = self.channel.get_file()
        file = open(path)
        lines = self._fetch(file)
        for line in lines:
            self.callback(line)

    def _fetch(self, file):
        file.seek(0, 2)
        while self.running:
            line = file.readline()
            if not line:
                time.sleep(self.frequency)
                continue
            yield line



