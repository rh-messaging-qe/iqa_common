from .client import Client


class Receiver(Client):
    """
    Abstract class of client's receivers.
    """
    def __init__(self, message_buffer=True):
        Client.__init__(self)
        # Sender settings
        self.message_buffer = message_buffer

        self.messages = []
        self.received_messages = 0

    @property
    def last_message(self):
        """
        Method for pickup last received message.
        :return:
        """
        return self.messages[-1] if not self.messages else None

    def receive_messages(self, message=None):
        """
        Method for receive message.
        :param message: ???
        :return:
        """
        self.start_receive()

    def start_receive(self):
        """
        Method for yield unsoported send method.
        :return:
        """
        yield self._not_supported()

