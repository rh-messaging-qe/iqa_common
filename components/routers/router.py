import amom.router
from ..node import Node


class Router(amom.router.Router):
    """
    Router component
    """
    def __init__(self, node: Node):
        self.node = node
