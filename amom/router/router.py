from inspect import stack

from ..node import Node



class Router:
    def __init__(self, node: Node):
        self.node = node
        pass

    @staticmethod
    def _not_supported():
        print("Function %s is not supported for this router." % stack()[1][3])
