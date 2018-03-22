from .route_type import RouteType


class Anycast(RouteType):
    """
    Any-cast routing type
    A single queue within the matching address, in a point-to-point manner.
    """
    def __init__(self):
        RouteType.__init__(self)
