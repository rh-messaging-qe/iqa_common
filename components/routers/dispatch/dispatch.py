from autologging import logged, traced

from amom.router import Router
from amom.node import Node

from .management import QDManage, QDStat
from ...service import Service


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
