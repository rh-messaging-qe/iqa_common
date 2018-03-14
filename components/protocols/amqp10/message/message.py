import amom.message


class Message(amom.message.Message):
    """
    AMQP10 Message
    """
    def __init__(self):
        amom.message.Message.__init__(self)
