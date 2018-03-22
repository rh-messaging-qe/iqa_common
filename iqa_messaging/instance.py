"""
    # TODO jstejska: Package description
"""

from autologging import logged, traced

import amom.router
import amom.broker
import amom.client

from components.node.node import Node
from components.node.executions.ansible import AnsibleCMD


@logged
@traced
class IQAInstance:
    """IQA helper class

    Store variables, node and related things
    """
    def __init__(self, inventory=''):
        self.inventory = inventory
        self.nodes = []
        self.components = []
        self.ansible = AnsibleCMD(inventory)

    def new_node(self, hostname, ip=None):
        """Create new node under iQA instance

        @TODO dlenoch Pass inventory by true way for Ansible
        # TODO jstejska: Description

        :param hostname:
        :type hostname:
        :param ip:
        :type ip:

        :return:
        :rtype:
        """
        node = Node(hostname=hostname, ip=ip, ansible=self.ansible)
        self.nodes.append(node)
        return node

    def new_component(self, node: Node, component):
        """Create new node under iQA instance

        @TODO Pass inventory by true way for Ansible
        # TODO jstejska: Description

        :param node:
        :type node:
        :param component:
        :type component:

        :return:
        :rtype:
        """
        new_component = node.new_component(component)
        self.components.append(new_component)
        return new_component

    def get_brokers(self):
        """Get all broker instances.

        :return:
        :rtype:
        """
        return [method_name for method_name in self.components
                if issubclass(method_name, amom.router.Router)]

    def get_clients(self):
        """Get all client instances.

        :return:
        :rtype:
        """
        return [method_name for method_name in self.components
                if issubclass(method_name, amom.client.Client)]

    def get_routers(self):
        """Get all router instances.

        :return:
        :rtype:
        """
        return [method_name for method_name in self.get_components
                if issubclass(method_name, amom.router.Router)]
