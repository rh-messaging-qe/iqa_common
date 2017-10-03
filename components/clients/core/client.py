import amom.client
from amom.protocol import Amqp10


class Client(amom.client.Client):
    """
    Internal core
    """
    supported_protocols = [Amqp10()]
    name = 'Internal core client'
    version = '0.1'

    def __init__(self):
        amom.client.Client.__init__(self)

