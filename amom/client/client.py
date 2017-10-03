from __future__ import print_function

from components.protocols import Amqp10, Mqtt, Stomp
from amom.node import Node


class Client:
    """

    """

    # Required variables
    supported_protocols = []
    name = ''
    version = ''
    ###

    def __init__(self):
        self.logs = None  # @TODO

    @property
    def get_supported_protocols(self):
        yield self.supported_protocols

    @property
    def get_name(self):
        yield self.supported_protocols

    @property
    def get_version(self):
        yield self.version


class NativeClient(Client):
    def __init__(self):
        Client.__init__(self)
        pass


class ExternalClient(Client):
    def __init__(self, node=Node()):
        super(ExternalClient, self).__init__()
        self.node = node


class Proton(NativeClient):
    """

    """
    supported_protocols = [Amqp10()]

    def __init__(self):
        super(Proton, self).__init__()
