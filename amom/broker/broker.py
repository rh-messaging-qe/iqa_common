from amom.node import Node


class Broker:
    """

    """
    supported_protocols = None

    def __init__(self, node: Node):
        self.node = node
        self.logs = None  # @TODO
