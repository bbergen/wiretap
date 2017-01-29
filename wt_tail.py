import os
import time


class WiretapFileException(Exception):
    pass


def tail_file(path, callback):
    exists = os.path.exists(path)
    if not exists:
        raise WiretapFileException("Invalid File Path")
    else:
        file = open(path)
        lines = fetch_lines(file)
        for line in lines:
            callback(line)


def fetch_lines(file):
    file.seek(0, 2)
    while True:
        line = file.readline()
        if not line:
            time.sleep(1)
            continue
        yield line


