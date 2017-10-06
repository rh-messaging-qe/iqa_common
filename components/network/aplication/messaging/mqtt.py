from autologging import logged, traced
from amom.protocol.protocol import Protocol


@logged
@traced
class Mqtt(Protocol):
    def __init__(self, default_port=5672):
        super(Mqtt, self).__init__(default_port)
