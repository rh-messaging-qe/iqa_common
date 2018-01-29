from autologging import logged, traced
from amom.node import Node
from odict import odict


import components.network.aplication.messaging as protocols
from amom.client.client import ExternalClient


class Timeout:
    def __init__(self, handler):
        self.registrated_handler = handler

    def on_timer_task(self, event):
        self.registrated_handler.timeout(event)


@logged
@traced
class Client(ExternalClient):
    """
    Python Proton client
    """
    supported_protocols = [protocols.Amqp10()]
    name = 'Python Proton client'
    version = '1.0.1'

    def __init__(self, node: Node):
        ExternalClient.__init__(self, node)
