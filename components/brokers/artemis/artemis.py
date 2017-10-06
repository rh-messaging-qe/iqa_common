from amom.broker import Broker
import components.network.aplication.messaging as protocols
from components.nodes import Node


class Artemis(Broker):
    """

    """
    supported_protocols = [protocols.Amqp10(), protocols.Mqtt(), protocols.Stomp(), protocols.Openwire()]

    def __init__(self, node: Node):
        Broker.__init__(self, node=node)


