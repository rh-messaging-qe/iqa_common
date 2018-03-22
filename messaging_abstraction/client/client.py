"""
    # TODO jstejska: Package description
"""


class Client:
    """
    Abstract class for every messaging client
    """

    # Required variables
    supported_protocols = []
    name = ''
    version = ''

    def __init__(self):
        self.logs = None  # @TODO

    @property
    def get_supported_protocols(self):
        return self.supported_protocols

    @property
    def get_name(self):
        return self.name

    @property
    def get_version(self):
        return self.version
