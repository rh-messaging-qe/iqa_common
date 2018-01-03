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
        return self.messages[-1] if self.messages else None

    def receive_messages(self, message=None):
        """
        Method for receive message.
        :param message: ???
        """
        if self.message_buffer:
            self.messages.append(message)
        else:
            self.messages = [message]

        self.start_receive()
        self.received_messages += 1

    def start_receive(self):
        """
        Start receive messages
        :return:
        """
        # if self.message_buffer:
        #     while True:
        #         self.messages.append(message)
        # else:
        #     while True:
        #         self.messages = [message]
        # self.received_messages += 1

        yield self._not_supported()

