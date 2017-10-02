# Thos class is probably obsolete
class Topology(object):
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is not None:
            return cls.instance
        else:
            cls.instance = super(Topology, cls).__new__(args, kwargs)
            return cls.instance

    def __init__(self, in_node=None, out_node=None, sender_node=None, receiver_node=None):
        self.in_node = in_node
        self.out_node = out_node
        self.sender_node = sender_node
        self.receiver_node = receiver_node
