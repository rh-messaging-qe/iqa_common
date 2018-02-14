"""
    # TODO jstejska: Package description
"""

from autologging import logged, traced
from components.nodes.node import Node

import components.network.aplication.messaging as protocols
from components.clients.external.externalclient import ExternalClient


@logged
@traced
class Client(ExternalClient):
    """NodeJS RHEA client"""

    supported_protocols = [protocols.Amqp10()]
    name = 'NodeJS RHEA client'
    version = '1.0'

    def __init__(self, node: Node):
        ExternalClient.__init__(self, node)
