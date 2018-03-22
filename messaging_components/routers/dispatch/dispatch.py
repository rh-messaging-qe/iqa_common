from autologging import logged, traced

from messaging_components.routers import Router
from messaging_components.node.service import Service
from messaging_components.node import Node

from .management import QDManage, QDStat


@logged
@traced
class Dispatch(Router):
    """
    Dispatch router component
    """

    name = 'Qpid Dispatch Router'

    def __init__(self, node: Node, service='qdrouterd'):
        Router.__init__(self, node=node)
        self.qdmanage = QDManage()
        self.qdstat = QDStat()
        self.config = None
        self.service = Service(self, 'qdrouterd')

        self._service = service
        self.service = Service(node, self._service)
        self._version = None

    @staticmethod
    def config_refresh():
        """
        Read and save router config from remote
        :return:
        """
        pass

    @property
    def version(self):
        """
        Get qdrouterd version
        :return:
        """
        if self._version:
            return self._version
        else:
            cmd = self.node.execute(['qdrouterd', '-v'])
            return cmd
