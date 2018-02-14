"""
    # TODO jstejska: Package description
"""

from autologging import logged, traced
from amom.node import Node

import components.network.aplication.messaging as protocols
from components.clients.external.externalclient import ExternalClient


@logged
@traced
class Client(ExternalClient):
    """Python Proton client."""

    supported_protocols = [protocols.Amqp10()]
    name = 'Python Proton client'
    version = '1.0.1'

    def __init__(self, node: Node):
        ExternalClient.__init__(self, node)

