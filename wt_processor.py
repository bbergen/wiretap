import re
import string
import threading

from wt_exception import ChannelProcessException


_BLUE_PHRASES = ['clr', 'clear', 'blue', 'friendly', 'empty', 'status']


class Processor:

    _LOCK = threading.Lock()

    def __init__(self, name):
        self.name = name
        self.system = ""

    def set_system(self, system):
        self.system = system

    def process(self, line):
        line = Processor._process(line)
        self._LOCK.acquire()
        try:
            print(
                "["
                + self.name
                + "]: "
                + line)
        finally:
            self._LOCK.release()

    @staticmethod
    def _process(raw):
        try:
            end = raw.index("]") + 2
            stripped = raw[end:]
            end_character = stripped.index(" >")
            speaker_name = stripped[:end_character].strip()
            line_content = stripped[end_character + 2:].strip()
            no_punctuation = Processor._strip_punctuation(line_content)

            word_tokens = no_punctuation.split(' ')
            blues = set(word_tokens).intersection(_BLUE_PHRASES)
            if blues:
                print("NO HOSTILES HERE BOYS")
                return raw

            for word in word_tokens:
                match = re.search(".*-.*", word)
                if match:
                    system = match.group(0)

        except:
            raise ChannelProcessException("Error Processing Feed")
        return raw

    # noinspection PyTypeChecker
    @staticmethod
    def _strip_punctuation(line):
        table = str.maketrans({key: None for key in string.punctuation})
        return line.translate(table)



