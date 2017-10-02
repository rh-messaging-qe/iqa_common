from amom.client import Client
from amom.protocol import Amqp10


class Client(Client):
    """
    Internal core
    """
    supported_protocols = [Amqp10]
    name = 'Internal core client'
    version = '0.1'

    def __init__(self):
        Client.__init__(self)

