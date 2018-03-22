import messaging_abstraction.router
from ..node import Node


class Router(messaging_abstraction.router.Router):
    """
    Router component
    """
    def __init__(self, node: Node):
        self.node = node
