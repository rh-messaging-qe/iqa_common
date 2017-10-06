from .client import Client


class Connector(Client):
    def __init__(self):
        Client.__init__(self)
