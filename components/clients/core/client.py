from autologging import logged, traced
import amom.client
from components.network.aplication.messaging import Amqp10

import threading

from proton.handlers import MessagingHandler
from proton.reactor import Container


class Timeout:
    def __init__(self, handler):
        self.registrated_handler = handler

    def on_timer_task(self, event):
        self.registrated_handler.timeout(event)


@logged
@traced
class Client(amom.client.Client):
    """
    Internal core
    """
    supported_protocols = [Amqp10()]
    name = 'Internal core client'
    version = '0.1'

    def __init__(self):
        amom.client.Client.__init__(self)
