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

    def send_message(self, **kwargs):
        """
        Method for send message.
        :param message: message
        :return:
        """
        self._add_message(kwargs)
        self._send_message(kwargs)
        self.sent_messages += 1

    def _send_message(self):
        """
        Method for yield unsoported send method.
        :return:
        """
        yield self._not_supported()

    def _add_message(self, **kwargs):
        """
        Method for get message from arguments.
        :param kwargs: dict with arguments
        :return:
        """
        message = ""
        if "msg_content" in kwargs:
            message = kwargs["msg_content"]

        if self.message_buffer:
            self.messages.append(message)
        else:
            self.messages = [message]

