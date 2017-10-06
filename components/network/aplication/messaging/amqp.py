from autologging import logged, traced
from amom.protocol.protocol import Protocol


@logged
@traced
class Amqp(Protocol):
    def __init__(self, default_port=5672):
        super(Amqp, self).__init__(default_port)
        self.name = "AMQP 1.0"


class Amqp10(Amqp):
    def __init__(self, default_port=5672):
        super(Amqp10, self).__init__(default_port)
        self.name = "AMQP 1.0"


class Amqp091(Amqp):
    def __init__(self, default_port=5672):
        super(Amqp091, self).__init__(default_port)
        self.name = "AMQP 0.9.1"
