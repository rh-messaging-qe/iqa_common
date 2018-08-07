from .queue import Queue


class Queues(list):
    """
    Abstract Queue class
    """
    def __init__(self):
        pass

    def queue_add(self, queue: Queue):
        """
        API: Add queue

        :param queue:
        :return:
        """
        self.append(queue)
        self._queue_add()

    def _queue_add(self):
        """
        IMPLEMENTATION POST HOOK:
            Add queue to broker
        """
        raise NotImplementedError

    def queue_remove(self, queue: Queue):
        """
        API: Remove queue

        :param queue:
        :return:
        """
        self.remove(queue)
        self._queue_remove()

    def _queue_remove(self):
        """
        IMPLEMENTATION POST HOOK:
            Remove queue from broker post hook
        """
        raise NotImplementedError
