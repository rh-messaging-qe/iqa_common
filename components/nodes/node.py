from autologging import logged, traced

import amom.node

from .executions import AnsibleCMD
from .executions import Executor


@logged
@traced
class Node(amom.node.Node):
    """
    Node component
    """
    def __init__(self, hostname, execution=None):
        amom.node.Node.__init__(self, hostname=hostname)
        Node.__log.info('Initialization of node %s..' % self.hostname)
        self.ansible = AnsibleCMD(hostname)
        self.executor = Executor(hostname)

        # Execution, by default is used Ansible
        self.execution = self.ansible

        if 'Executor' == execution:
            self.execution = self.executor

        self.ip = self._get_ip()
        self.components = None

    def execute(self, command):
        """Execute command on node"""
        return self.execution.execute(command)

    def ping(self):
        """Send ping to node"""
        return self.ansible.ping()

    def _get_ip(self):
        """Get ip of node"""
        cmd_ip = 'ip route | grep ^default | grep -oE [0-9]+\.[0-9]+\.[0-9]+\.[0-9]+'
        process = self.execute(cmd_ip)
        return process.get_stdout()[1]

    # def get_components(self):
    #     """
    #     Get all instances on this node
    #     @TODO complete this method for usability, it's just idea now
    #     :return: list of objects which use this Node object
    #     """
    #     return [method_name for method_name in dir(self)
    #             if callable(getattr(self, method_name))]
    #
    # def get_brokers(self):
    #     """
    #     Get all broker instances on this node
    #     :return:
    #     """
    #     return [method_name for method_name in self.get_components()
    #             if callable(getattr(self, method_name))]
    #
    # def get_clients(self):
    #     """
    #     Get all client instances on this node
    #     @TODO
    #     :return:
    #     """
    #     return [method_name for method_name in self.get_components()
    #             if callable(getattr(self, method_name))]
    #
    # def get_routers(self):
    #     """
    #     Get all router instances on this node
    #     @TODO
    #     :return:
    #     """
    #     return [method_name for method_name in self.get_components()
    #             if callable(getattr(self, method_name))]
