from amom.protocol.protocol import Protocol


class Stomp(Protocol):
    def __init__(self, default_port=5672):
        super(Stomp, self).__init__(default_port)