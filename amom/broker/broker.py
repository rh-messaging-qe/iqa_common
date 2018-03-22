from .queue import Queues


class Broker:
    """
    Abstract broker class
    """
    supported_protocols = []
    name = ''

    def __init__(self):
        self.queues = Queues()
