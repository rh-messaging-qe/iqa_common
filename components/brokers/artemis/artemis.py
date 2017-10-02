from amom.broker import Broker
import amom.protocol as protocols


class Artemis(Broker):
    """

    """
    supported_protocols = [protocols.Amqp10(), protocols.Mqtt(), protocols.Stomp(), protocols.Openwire()]

    def __init__(self, node):
        Broker.__init__(self)

