import amom.client
from .client import Client


class Connector(Client, amom.client.Connector):
    def __init__(self):
        Client.__init__(self)
        amom.client.Connector.__init__(self)
