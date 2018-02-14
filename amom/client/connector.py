"""
    # TODO jstejska: Package description
"""

from .client import Client


class Connector(Client):
    """Abstract class of client's connectors."""

    def __init__(self):
        super(Connector, self).__init__()
