from autologging import logged, traced

import amom.client
from .client import Client


@logged
@traced
class Sender(Client, amom.client.Sender):
    """
    External NodeJS sender client
    """
    def __init__(self):
        amom.client.Sender.__init__(self)
        Client.__init__(self)
