from __future__ import print_function
from amom.node import Node


class Client:
    """
    Abstract class for every messaging client
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


class ExternalClient(Client):
    def __init__(self, node: Node):
        Client.__init__(self)
        self.node = node

