"""
    # TODO jstejska: Package description
"""

from autologging import logged, traced

import messaging_abstraction.client
from .client import Client


@logged
@traced
class Sender(Client, messaging_abstraction.client.Sender):
    """Core python sender client."""

    def __init__(self):
        messaging_abstraction.client.Sender.__init__(self)
        Client.__init__(self)
