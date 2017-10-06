import amom.client as client
from .client import Client


class Connector(Client, client.Connector):
    def __init__(self):
        client.Connector.__init__(self)
        Client.__init__(self)
