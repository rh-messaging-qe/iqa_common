from autologging import logged, traced
from amom.router import Router
from amom.node import Node
from .management import QDManage, QDStat


@logged
@traced
class Dispatch(Router):
    """
    Qpid Dispatch component
    """
    def __init__(self, node: Node):
        Router.__init__(self, node=node)
        self.qdmanage = QDManage()
        self.qdstat = QDStat()
        self.config = None
