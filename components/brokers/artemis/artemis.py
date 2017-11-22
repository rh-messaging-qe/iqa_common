from amom.broker import Broker
from ...nodes import Node

import components.network.aplication.messaging as protocols


class Artemis(Broker):
    """
    Apache ActiveMQ Artemis has a proven non blocking architecture. It delivers outstanding performance.
    """
    supported_protocols = [protocols.Amqp10(), protocols.Mqtt(), protocols.Stomp(), protocols.Openwire()]
    name = 'Artemis'

    def __init__(self, node: Node):
        Broker.__init__(self, node=node)


