import sys
import wt_tail


def callback(line):
    sys.stdout.write(line)


path = 'C:\\Users\\bryan\\Documents\\EVE\\logs\\Chatlogs\\delve.imperium_20170129_041551.txt'
wt_tail.tail_file(path, callback)
