from autologging import logged, traced

import components.network.aplication.messaging as protocols
from amom.client.client import ExternalClient


@logged
@traced
class Client(ExternalClient):
    """
    NodeJS RHEA client
    """
    supported_protocols = [protocols.Amqp10()]
    name = 'NodeJS RHEA client'
    version = '1.0'

    def __init__(self):
        ExternalClient.__init__(self)
