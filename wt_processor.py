import threading


class Processor:

    _LOCK = threading.Lock()

    def __init__(self, name):
        self.name = name

    def process(self, line):
        self._LOCK.acquire()
        try:
            print(
                "["
                + self.name
                + "]: "
                + line)
        finally:
            self._LOCK.release()

