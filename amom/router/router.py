from inspect import stack

from ..node import Node


class Router:
    """
    Abstract messaging Router
    """
    name = ''

    def __init__(self, node: Node):
        self.node = node
