from .Anycast import Anycast
from .Multicast import Multicast


class Mixed(Anycast, Multicast):
    """
    Mixed Multi-cast and Any-cast (Booth) type
    """
    def __init__(self):
        Anycast.__init__(self)
        Multicast.__init__(self)
