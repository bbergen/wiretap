import datetime
import getpass
import os


class Channel:
    def __init__(self):
        self.dir = ""
        self.file_name = ""
        self.channel_name = ""
        self.date = ""
        self.time = ""

    def get_file(self):
        return self.dir + self.file_name

    def __str__(self):
        return "[" \
            + self.date \
            + ":" \
            + str(self.time) \
            + " - " \
            + self.channel_name \
            + "]"


def list_channels():
    user = getpass.getuser()
    base_path = "C:\\Users\\" + user + "\\Documents\\Eve\\logs\\Chatlogs\\"
    today = datetime.datetime.utcnow().strftime("%Y%m%d")
    most_recent = {}
    for filename in os.listdir(base_path):
        filename = filename[:-4]
        time = int(filename[-6:])
        filename = filename[:-7]
        date = filename[-8:]
        channel_name = filename[:-9]
        if date == today:
            channel = Channel()
            channel.file_name = filename + ".txt"
            channel.dir = base_path
            channel.channel_name = channel_name
            channel.date = date
            channel.time = time
            if most_recent.get(channel_name):
                newest_channel = most_recent.get(channel_name)
                if time > newest_channel.time:
                    most_recent[channel_name] = channel
            else:
                most_recent[channel_name] = channel

    return most_recent





