import amom.client as client
from .client import Client


class Sender(Client, client.Sender):
    def __init__(self):
        client.Sender.__init__(self)
        Client.__init__(self)
