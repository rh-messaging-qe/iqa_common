from sultan.api import Sultan

from src.components import *
from src.components.node import Node


# TODO This ist just an idea, not doing anything really - implement it

class Router(Node):
    """
    Class representing a routers on the physical node.
    This class should contain an API to start, stop, restart routers and get basic analytics
    Note:
        Uses sultan as an example project -- py wrapper around shell -- this could be a pythonic way for further API implementation.
    """

    def __init__(self, hostname="localhost", configuration=None, configuration_path=DEFAULT_CONFIG_PATH):
        super(Router, self).__init__(hostname)
        self.configuration = configuration
        self.configuration_path = configuration_path
        self.sultan = Sultan()

    def start(self):  # example uf sultan's usage -- RUNNING ONLY ON LOCALHOST
        self.sultan.qdrouterd.run("-c %s -d" % self.configuration_path)

    def stop(self):
        pass

    def restart(self):
        self.start()
        self.stop()
