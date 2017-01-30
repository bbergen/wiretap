import os
import time

from wt_exception import WiretapFileException


class Tailer:
    """
    Used for Tailing Eve Online Chat Channels
    See wt_channel.Channel
    """
    def __init__(self, channel, writer):
        """
        Configures a Tailer instance
        :param channel: wt_channel.Channel fully configured
        :param writer: object responsible for writing our the read lines
        """
        self.channel = channel
        self.writer = writer
        self.frequency = 1
        self.running = False

    def start_tail(self):
        """
        TODO(bryan) self._tail_file() should run in a seperate thread so this thread is non-blocking
        TODO(bryan) error checking on channel loading
        Starts the tailing of the configured channel
        :return: void
        """
        self.running = True
        self._check_file()
        self._tail_file()

    def stop_tail(self):
        """
        TODO(bryan) pointless until start_tail is properly threaded.
        Stops the tailing of the configured channel
        :return: void
        """
        self.running = False

    def _check_file(self):
        """
        TODO(bryan) this abstraction might be better residing in Channel itself
        Checks the configured channel to see if it exists
        :return: void
        :raises: WiretapFileException if the channel is not present
        """
        path = self.channel.get_file()
        exists = os.path.exists(path)
        if not exists:
            raise WiretapFileException("Invalid Channel File")

    def _tail_file(self):
        """
        TODO(bryan) proper error handling on IO
        internal implementation of the tailing of the configured channel
        :return: void
        """
        path = self.channel.get_file()
        file = open(path, encoding='utf-16', errors='ignore')  # Eve chat logs are in UTF-16
        lines = self._fetch(file)
        for line in lines:
            # line = line.rstrip()
            self.writer.write(line)

    def _fetch(self, file):
        """
        Generator for lines by line reading of the passed file
        :param file: the file associated with the configured channel
        :return: new additions to file, line by line
        """
        file.seek(0, 2)
        while self.running:
            line = file.readline()
            if not line:
                time.sleep(self.frequency)
                continue
            yield line



