import amom.broker
from ..node import Node


class Broker(amom.broker.Broker):
    """
    Broker component
    """
    def __init__(self, node: Node):
        self.node = node
