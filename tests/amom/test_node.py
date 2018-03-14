from unittest import TestCase
import pytest

from amom.node import Node


class TestNode(TestCase):

    node = Node(hostname='abc123', ip='127.0.0.1')

    def test_hostname(self):
        assert self.node.hostname == 'abc123'

    def test_ip(self):
        assert self.node.ip == '127.0.0.1'

    def test_execute(self):
        with pytest.raises(NotImplementedError):
            self.node.execute('cmd')

    def test_ping(self):
        with pytest.raises(NotImplementedError):
            self.node.ping()
