"""
    # TODO jstejska: Package description
"""

from autologging import logged, traced

import messaging_abstract.router
import messaging_abstract.broker
import messaging_abstract.client

from messaging_components.node.node import Node
from messaging_components.node.executions.ansible import AnsibleCMD


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

    @property
    def brokers(self):
        """Get all broker instances.

        :return:
        :rtype:
        """
        return [method_name for method_name in self.components
                if issubclass(method_name, messaging_abstract.router.Router)]

    @property
    def clients(self):
        """Get all client instances.

        :return:
        :rtype:
        """
        return [method_name for method_name in self.components
                if issubclass(method_name, messaging_abstract.client.Client)]

    @property
    def routers(self):
        """Get all router instances.

        :return:
        :rtype:
        """
        return [method_name for method_name in self.componentsb
                if issubclass(method_name, messaging_abstract.router.Router)]
