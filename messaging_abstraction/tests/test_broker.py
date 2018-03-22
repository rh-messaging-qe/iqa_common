import pytest

from messaging_abstraction.broker import Broker, Address, Queue
from messaging_abstraction.broker.queue import Queue


class TestBroker:
    def test_broker_queue_add(self):
        broker = Broker()
        address = Address(value='x')
        queue = Queue(name='x', address=address)

        with pytest.raises(NotImplementedError):
            broker.queues.queue_add(queue)

        assert broker.queues[0].name == 'x'

    def test_broker_queue_remove(self):
        broker = Broker()
        address = Address(value='x')
        queue = Queue(name='x', address=address)

        with pytest.raises(NotImplementedError):
            broker.queues.queue_add(queue)
        assert broker.queues[0].name == 'x'

        with pytest.raises(NotImplementedError):
            broker.queues.queue_remove(queue)
        assert len(broker.queues) == 0
