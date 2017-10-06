import amom.client as client
from .client import Client


class Receiver(Client, client.Receiver):
    def __init__(self):
        client.Receiver.__init__(self)
        Client.__init__(self)
