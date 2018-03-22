import messaging_abstraction.message


class Message(messaging_abstraction.message.Message):
    """
    AMQP10 Message
    """
    def __init__(self):
        messaging_abstraction.message.Message.__init__(self)
