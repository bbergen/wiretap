import sys

import channel
from trailer import Tailer


def callback(line):
    sys.stdout.write(line)

channels = channel.list_channels()
print("[DEBUG]: Channels Loaded")
channel = channels['delve.imperium']
t = Tailer(channel, callback)
t.start_tail()
