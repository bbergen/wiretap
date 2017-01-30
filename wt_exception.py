
class WiretapFileException(Exception):
    """ Used to abstract low level IO errors when configuring Wiretap Channels and Tailers """
    pass


class ChannelNotFoundException(Exception):
    """ Used when a channel does not exist """
    pass
