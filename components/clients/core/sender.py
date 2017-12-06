from autologging import logged, traced

import amom.client
from .client import Client


@logged
@traced
class Sender(Client, amom.client.Sender):
    """
    Core python sender client
    """
    def __init__(self):
        amom.client.Sender.__init__(self)
        Client.__init__(self)
