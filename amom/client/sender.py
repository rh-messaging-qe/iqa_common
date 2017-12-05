from .client import Client


class Sender(Client):
    """
    Abstract class of client's senders.
    """
    def __init__(self, message_buffer=False):
        """

        :param message_buffer:
        """
        Client.__init__(self)
        # Sender settings
        self.message_buffer = message_buffer

        self.messages = []
        self.sent_messages = 0


    @property
    def last_message(self):
        """
        Method for pickup sent last message.
        :return: message
        """
        return self.messages[-1] if not self.messages else None

    def send_message(self, message):
        """
        Method for send message.
        :param message: message
        :return:
        """
        if self.message_buffer:
            self.messages.append(message)
        else:
            self.messages = [message]

        self.msg_content = message
        self._send_message()
        self.sent_messages += 1

    def _send_message(self):
        """
        Method for yield unsoported send method.
        :return:
        """
        yield self._not_supported()

