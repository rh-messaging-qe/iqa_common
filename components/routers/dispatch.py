from amom.router import Router
from amom.node import Node


class Dispatch(Router):
    def __init__(self, node=Node()):
        Router.__init__(self, node=node)
