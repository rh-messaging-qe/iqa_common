from .client import Client


class Sender(Client):
    def __init__(self, message_buffer=False):
        Client.__init__(self)
        # Sender settings
        self.message_buffer = message_buffer

        self.messages = []
        self.last_messages = lambda: self.messages[-1] if not self.messages else None
        self.sent_messages = 0

    def send_message(self, message):
        if self.message_buffer:
            self.messages.append(message)
        else:
            self.messages = [message]

        self._send_message()
        self.sent_messages += 1

    def _send_message(self):
        yield self._not_supported()

