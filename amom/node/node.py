from inspect import stack


class Node:
    """
    Represents virtual destination/service aka node.
    In a case of interconnect vm with qdrouterd is represented as a Router node.
    When there is a sender present on such node, it is a Sender node.
    All future representations should inherit from this class.
    """

    def __init__(self, hostname=None, ip=None):
        self.hostname = hostname
        self.ip = ip

    def execute(self, command):
        """
        Execute command on remote node
        :param command: list
        :return:
        """
        return self._not_supported()

    def ping(self):
        return self._not_supported()

    @staticmethod
    def _not_supported():
        print("Function %s is not supported for this node." % stack()[1][3])

