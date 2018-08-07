"""
    # TODO jstejska: Package description
"""

from autologging import logged, traced

import messaging_abstraction.client
from .client import Client


@logged
@traced
class Connector(Client, messaging_abstraction.client.Connector):
    """Core python connector client."""

    def __init__(self):
        messaging_abstraction.client.Connector.__init__(self)
        Client.__init__(self)
