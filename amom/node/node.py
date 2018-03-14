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
        Execute command on node
        :param command:
        :return:
        """
        raise NotImplementedError

    def ping(self):
        """
        Ping node
        :return:
        """
        raise NotImplementedError


