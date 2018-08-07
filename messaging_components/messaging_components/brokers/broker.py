import messaging_abstraction.broker
from ..node import Node


class Broker(messaging_abstraction.broker.Broker):
    """
    Broker component
    """
    def __init__(self, node: Node):
        self.node = node
