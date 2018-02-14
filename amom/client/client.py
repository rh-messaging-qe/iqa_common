"""
    # TODO jstejska: Package description
"""

from inspect import stack


class Client:
    """Abstract class for every messaging client."""

    # Required variables
    supported_protocols = []
    name = ''
    version = ''

    def __init__(self):
        self.logs = None

    @property
    def get_supported_protocols(self):
        return self.supported_protocols

    @property
    def get_name(self):
        return self.name

    @property
    def get_version(self):
        return self.version

    @staticmethod
    def _not_supported():
        print("Function %s is not supported for this client." % stack()[1][3])
        raise NotImplementedError


class NativeClient(Client):
    """Abstract class for Native client."""
    def __init__(self):
        super(NativeClient, self).__init__()


class LocalhostClient(Client):
    """Abstract class for Localhost client."""
    def __init__(self):
        super(LocalhostClient, self).__init__()


