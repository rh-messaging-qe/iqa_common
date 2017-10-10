from autologging import logged, traced

from .executions import Execution
from .executions import Ansible
from .executions import Executor
import amom.node


@logged
@traced
class Node(amom.node.Node):
    """
    Node component
     - Complete implementation of node
     -
    """
    def __init__(self, hostname, execution=None):
        amom.node.Node.__init__(self, hostname=hostname)
        self.ansible = Ansible(hostname)
        self.executor = Executor(hostname)

        # Execution, by default is used Ansible
        self.execution = self.ansible
        if execution is 'Executor':
            self.execution = self.executor

        self.components = None

    def execute(self, command):
        self.execution.execute(command)

    def get_components(self):
        """
        Get all instances on this node
        @TODO complete this method for usability, it's just idea now
        :return: list of objects which use this Node object
        """
        return [method_name for method_name in dir(self)
                if callable(getattr(self, method_name))]

    def get_brokers(self):
        """
        Get all broker instances on this node
        :return:
        """
        return [method_name for method_name in self.get_components()
                if callable(getattr(self, method_name))]

    def get_clients(self):
        """
        Get all client instances on this node
        @TODO
        :return:
        """
        return [method_name for method_name in self.get_components()
                if callable(getattr(self, method_name))]

    def get_routers(self):
        """
        Get all router instances on this node
        @TODO
        :return:
        """
        return [method_name for method_name in self.get_components()
                if callable(getattr(self, method_name))]
