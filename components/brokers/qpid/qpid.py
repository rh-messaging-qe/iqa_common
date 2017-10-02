from amom.broker import Broker
import amom.protocol as protocols


class Qpid(Broker):
    """

    """
    supported_protocols = [protocols.Amqp10()]

    def __init__(self, node):
        Broker.__init__(self)
