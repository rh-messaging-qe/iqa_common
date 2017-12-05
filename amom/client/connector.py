from .client import Client


class Connector(Client):
    """
    Abstract class of client's connectors.
    """
    def __init__(self):
        Client.__init__(self)
