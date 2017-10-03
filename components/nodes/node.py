from .executions import Execution
from .executions import Ansible
from .executions import Executor
import amom.node


class Node(amom.node.Node):
    def __init__(self, execution=Execution()):
        amom.node.Node.__init__(self)
        self.execution = execution
        self.ansible = Ansible()
        self.executor = Executor()

    def execute(self, command):
        self.execution.execute()
