class Protocol:
    """ Protocol abstraction"""
    def __init__(self, transaction, transport, default_port=None):
        self.name = type(self).__name__
        self.default_port = default_port
        self.transaction = transaction
        self.transport = transport
