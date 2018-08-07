from . import Anycast, Multicast


class Mixed(Anycast, Multicast):
    def __init__(self, value):
        Anycast.__init__(self, value)
        Multicast.__init__(self, value)

