from .address import Address
from ..route.anycast import Anycast as AnycastRoute


class Anycast(Address, AnycastRoute):
    """
    A single queue within the matching address, in a point-to-point manner.
    """
    def __init__(self, value):
        Address.__init__(self, value)
        AnycastRoute.__init__(self)
