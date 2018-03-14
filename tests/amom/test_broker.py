from unittest import TestCase
import pytest

from amom.node import Node
from amom.broker import Broker
from amom.queue import Queue


class TestBroker(TestCase):
    node = Node(hostname='TestNode', ip='127.0.0.1')
    broker = Broker(node=node)

    def test_broker_node(self):
        assert self.broker.node.hostname == 'TestNode'
        assert self.broker.node.ip =='127.0.0.1'

    def test_broker_queue_add(self):
        broker = Broker(node=self.node)
        queue = Queue(name='x', address='x')

        with pytest.raises(NotImplementedError):
            broker.queues.queue_add(queue)

        assert broker.queues[0].name == 'x'

    def test_broker_queue_remove(self):
        broker = Broker(node=self.node)
        queue = Queue(name='x', address='x')

        with pytest.raises(NotImplementedError):
            broker.queues.queue_add(queue)
        assert broker.queues[0].name == 'x'

        with pytest.raises(NotImplementedError):
            broker.queues.queue_remove(queue)
        assert len(broker.queues) == 0
