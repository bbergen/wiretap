import logging
import threading

import wt_channel


# Testing Script start
logging.warning("Starting Wiretap")
channels = wt_channel.list_channels()
logging.warning("Channels Loaded")
test_channel_1 = "wiretap_test"
test_channel_2 = 'delve.imperium'
channel_1 = channels[test_channel_1]
channel_2 = channels[test_channel_2]

channel_threads = []
runner_1 = wt_channel.ChannelRunner(channel_1)
runner_2 = wt_channel.ChannelRunner(channel_2)

channel_threads.append(runner_1)
channel_threads.append(runner_2)

for r in channel_threads:
    t = threading.Thread(target=r.run)
    logging.warning("Starting: " + r.channel.channel_name)
    t.start()

logging.warning("All Channels Started")

