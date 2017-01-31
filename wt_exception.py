
class WiretapFileException(Exception):
    """
    Used to abstract low level IO errors
    when configuring Wiretap Channels and Tailers
    """
    pass


class ChannelNotFoundException(Exception):
    """ Used when a channel does not exist """
    pass


class ChannelProcessException(Exception):
    """ Used when there is an error processing the channel feed """
    pass
