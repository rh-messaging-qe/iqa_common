"""
    # TODO jstejska: Package description
"""

from .client import Client
from ..message import Message


class Sender(Client):
    """Abstract class of client's senders."""

    def __init__(self, message_buffer=False):
        """Init

        :param message_buffer: # TODO jstejska: description
        :type message_buffer: # TODO jstejska: type
        """
        super(Sender, self).__init__()
        # Sender settings
        self.message_buffer = message_buffer

        self.messages = []
        self.sent_messages = 0

    @property
    def last_message(self):
        """Method for pickup sent last message.

        :return: message
        :rtype: # TODO jstejska: type
        """
        return self.messages[-1] if self.messages else None

    def send_message(self, message: Message, **kwargs):
        """Method for send message.

        :param message: # TODO jstejska: descritpion
        :type: # TODO jstejska: type

        :return: # TODO jstejska: description
        :rtype  # TODO jstejska: type
        """
        if self.message_buffer:
            self.messages.append(message)
        else:
            self.messages = [message]

        self.sent_messages += 1
        self._add_message(**kwargs)
        self._send_message(**kwargs)
        self.sent_messages += 1

    def _send_message(self, **kwargs):
        """Method for yield unsoported send method.

        :return: # TODO jstejska: description
        :rtype: # TODO jstejska: type
        """
        yield self._not_supported()

    def _add_message(self, **kwargs):
        """Method for get message from arguments.

        :param kwargs: dict with arguments
        :type kwargs: # TODO jstejska: type

        :return: # TODO jstejska: description
        :rtype: # TODO jstejska: type
        """
        message = ""
        if "msg_content" in kwargs:
            message = kwargs["msg_content"]

        if self.message_buffer:
            self.messages.append(message)
        else:
            self.messages = [message]

