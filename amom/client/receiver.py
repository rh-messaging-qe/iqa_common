from .client import Client


class Receiver(Client):
    def __init__(self, message_buffer=True):
        Client.__init__(self)
        # Sender settings
        self.message_buffer = message_buffer

        self.messages = []
        self.last_messages = lambda: self.messages[-1] if not self.messages else None
        self.received_messages = 0

    def receive_messages(self, message=None):
        self.start_receive()

    def start_receive(self):
        yield self._not_supported()

