"""
    # TODO jstejska: Package description
"""

from autologging import logged, traced

import messaging_abstraction.client
from .client import Client


@logged
@traced
class Receiver(Client, messaging_abstraction.client.Receiver):
    """Core python receiver client."""

    def __init__(self):
        messaging_abstraction.client.Receiver.__init__(self)
        Client.__init__(self)
