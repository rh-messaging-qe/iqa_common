"""
    # TODO jstejska: Package description
"""

from autologging import logged, traced

import amom.client
from .client import Client


@logged
@traced
class Receiver(Client, amom.client.Receiver):
    """Core python receiver client."""

    def __init__(self):
        amom.client.Receiver.__init__(self)
        Client.__init__(self)
