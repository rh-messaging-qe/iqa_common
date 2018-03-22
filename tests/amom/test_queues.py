import pytest

from broker.queue import Queue, Queues
from broker.address import Address

address = Address(value='address_1')
queue = Queue(name='Test_Queue_1', address=address)
queues = Queues()


class TestQueue:

    def test_queue_name(self):
        assert queue.name == 'Test_Queue_1'

    def test_queue_address(self):
        assert queue.address == address


class TestQueues:
    def test_add_queue(self):
        test_queues = queues

        with pytest.raises(NotImplementedError):
            test_queues.queue_add(queue)

        assert test_queues[0].name == 'Test_Queue_1'

    def test_remove_queue(self):
        test_addres = Address(value='x')
        test_queues = Queues()
        test_queue = Queue(name='Test_Queue_1', address=test_addres)

        with pytest.raises(NotImplementedError):
            test_queues.queue_add(test_queue)

        assert len(test_queues) == 1

        with pytest.raises(NotImplementedError):
            test_queues.queue_remove(test_queue)

        assert len(test_queues) == 0

    def test_remove_from_queues(self):
        test_queues = Queues()

        test_queue1 = Queue(name='Test_Queue_1', address=Address(value='1'))
        test_queue2 = Queue(name='Test_Queue_2', address=Address(value='2'))
        test_queue3 = Queue(name='Test_Queue_3', address=Address(value='3'))

        with pytest.raises(NotImplementedError):
            test_queues.queue_add(test_queue1)

        with pytest.raises(NotImplementedError):
            test_queues.queue_add(test_queue2)

        with pytest.raises(NotImplementedError):
            test_queues.queue_add(test_queue3)

        assert len(test_queues) == 3

        with pytest.raises(NotImplementedError):
            test_queues.queue_remove(test_queue2)

        expected = [test_queue1, test_queue3]

        assert test_queues == expected


