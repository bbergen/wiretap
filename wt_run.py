import logging
import sys

import wt_channel
from wt_tailer import Tailer


class ChannelWriter:
    def __init__(self, name):
        self.name = name

    def write(self, line):
        sys.stdout.write(
            "["
            + self.name
            + "]: "
            + line)


def callback(line):
    """ Simple callback for testing purposes """
    sys.stdout.write(line)

# Testing Script start
logging.warning("Starting Wiretap")
channels = wt_channel.list_channels()
logging.warning("Channels Loaded")
channel_name = "wiretap_test"
logging.warning("Tailing: " + channel_name)
channel = channels[channel_name]
writer = ChannelWriter(channel_name)
t = Tailer(channel, writer)
t.start_tail()
