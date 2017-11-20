from amom.node import Node


class Broker:
    """
    Abstract broker class
    """
    supported_protocols = []
    name = ''

    def __init__(self, node: Node):
        self.node = node
        self.logs = None  # @TODO
