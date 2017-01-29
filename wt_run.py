import sys
import wt_find_file
import wt_tail


def callback(line):
    sys.stdout.write(line)


path = wt_find_file.find("delve.imperium")
wt_tail.tail_file(path, callback)
