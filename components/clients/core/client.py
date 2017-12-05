from autologging import logged, traced

import components.network.aplication.messaging as protocols
from amom.client.client import NativeClient


class Timeout:
    def __init__(self, handler):
        self.registrated_handler = handler

    def on_timer_task(self, event):
        self.registrated_handler.timeout(event)


@logged
@traced
class Client(NativeClient):
    """
    Internal core Proton mapping client
    """
    supported_protocols = [protocols.Amqp10()]
    name = 'Internal core client'
    version = '0.1'

    # Core client atributes


    def __init__(self):
        NativeClient.__init__(self)
