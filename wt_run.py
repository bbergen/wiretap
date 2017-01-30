import logging
import sys

import wt_channel
from wt_tailer import Tailer


def callback(line):
    """ Simple callback for testing purposes """
    sys.stdout.write(line)

# Testing Script start
logging.warning("Starting Wiretap")
channels = wt_channel.list_channels()
logging.warning("Channels Loaded")
channel_name = "delve.imperium"
logging.warning("Tailing: " + channel_name)
channel = channels[channel_name]
t = Tailer(channel, callback)
t.start_tail()
