from autologging import logged, traced
from amom.protocol import Protocol


@logged
@traced
class TLS13(Protocol):
    def __init__(self):
        Protocol.__init__(self)
        self.name = 'TLS 1.3'
