from autologging import logged, traced

import amom.client
from .client import Client


@logged
@traced
class Connector(Client, amom.client.Connector):
    """
    External NodeJS connector client
    """
    def __init__(self):
        amom.client.Connector.__init__(self)
        Client.__init__(self)
