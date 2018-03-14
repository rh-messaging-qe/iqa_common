from unittest import TestCase

from amom.node import Node
from amom.router import Router


class TestRouter(TestCase):
    node = Node(hostname='x')

    def test_router_node(self):
        router = Router(node=self.node)
        assert router.node.hostname == 'x'
