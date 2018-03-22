from .address import Address

from ..route import Multicast as MulticastRoute


class Multicast(Address, MulticastRoute):
    """
    Every queue within the matching address, in a publish-subscribe manner.
    """
    def __init__(self, value):
        Address.__init__(self, value)
        MulticastRoute.__init__(self)

