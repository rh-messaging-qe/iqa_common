from components.brokers import Broker
from components.node import Node
import components.protocols as protocols


class Qpid(Broker):
    """
    Qpid broker
    A message-oriented middleware message broker written in C++ that stores, routes, and forwards messages using AMQP.
    """
    supported_protocols = [protocols.Amqp10()]
    name = 'Qpid C++ Broker'

    def __init__(self, node: Node):
        Broker.__init__(self, node=node)
