from amom.protocol import Protocol


class TLS11(Protocol):
    def __init__(self):
        Protocol.__init__(self)
        self.name = 'TLS 1.1'
