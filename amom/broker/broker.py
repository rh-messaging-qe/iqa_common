from ..node import Node
from ..queue import Queues


class Broker:
    """
    Abstract broker class
    """
    supported_protocols = []
    name = ''

    def __init__(self, node: Node):
        self.node = node
        self.queues = Queues()
