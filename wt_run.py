import sys
import channel


def callback(line):
    sys.stdout.write(line)

for value in channel.list_channels().values():
    print(value.__str__() + " " + value.get_file())
