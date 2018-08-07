from .route_type import RouteType


class Multicast(RouteType):
    """
    Multi-cast routing type
    Every queue within the matching address, in a publish-subscribe manner.
    """
    def __init__(self):
        RouteType.__init__(self)
