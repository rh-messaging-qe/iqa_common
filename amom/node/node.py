from inspect import stack as stack


class Node(object):
    """
    Represents virtual destination/service aka node.
    In a case of interconnect vm with qdrouterd is represented as a Router node.
    When there is a sender present on such node, it is a Sender node.
    All future representations should inherit from this class.
    """

    def __init__(self, hostname):
        self.hostname = hostname

    def run_command(self):
        yield self._not_supported()

    @staticmethod
    def _not_supported():
        print("Function '%s' is not supported for this client." % stack()[1][3])

