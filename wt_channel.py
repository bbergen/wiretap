import datetime
import getpass
import os

from wt_tailer import Tailer
from wt_processor import Processor


class ChannelRunner:
    """ Simple Runner that starts the tailing of a configured Channel """

    def __init__(self, channel):
        self.channel = channel
        self.writer = Processor(channel.channel_name)

    def run(self):
        """ Starts tailing the Channel """
        t = Tailer(self.channel, self.writer)
        t.start_tail()


class Channel:
    """
    Abstraction of an Eve Online Chat Channel
    """
    def __init__(self):
        self.dir = ""
        self.file_name = ""
        self.channel_name = ""
        self.date = ""
        self.time = ""
        self.extension = ".txt"

    def get_file(self):
        """
        Creates an absolute path to the channel's file
        :return: String used to open the channel's file
        """
        return self.dir + self.file_name + self.extension

    def __str__(self):
        return "[" \
            + self.date \
            + ":" \
            + str(self.time) \
            + " - " \
            + self.channel_name \
            + "]"


def list_channels():
    """
    TODO(bryan) search previous day if none found for current day,
        as eve may be open across 00:00:00 UTC

    Checks the log directory for today's chat logs and returns
    a map of Channel objects mapped to their channel name
    :return: {'channel_name': channel}
    """
    user = getpass.getuser()
    base_path = "C:\\Users\\" + user + "\\Documents\\Eve\\logs\\Chatlogs\\"
    today = datetime.datetime.utcnow().strftime("%Y%m%d")
    most_recent = {}
    for filename in os.listdir(base_path):
        filename = filename[:-4]
        full_filename = filename
        time = filename[-6:]
        filename = filename[:-7]
        date = filename[-8:]
        channel_name = filename[:-9]
        if date == today:
            channel = Channel()
            channel.file_name = full_filename
            channel.dir = base_path
            channel.channel_name = channel_name
            channel.date = date
            channel.time = time
            if most_recent.get(channel_name):
                newest_channel = most_recent.get(channel_name)
                if int(time) > int(newest_channel.time):
                    most_recent[channel_name] = channel
            else:
                most_recent[channel_name] = channel

    return most_recent





