# coding=utf-8
from autologging import logged, traced
from .nodes.node import Node
from .nodes.executions.ansible import AnsibleCMD


@logged
@traced
class IQAInstance:
    """
    iQA helper class

    Store variables, nodes and related things
    """
    def __init__(self, inventory=''):
        self.inventory = inventory
        self.nodes = []
        self.ansible = AnsibleCMD(inventory)

    def new_node(self, hostname):
        """
        Create new node under iQA instance

        @TODO Pass inventory by true way for Ansible

        :param hostname
        :return:
        """
        node = Node(hostname=hostname)
        self.nodes.append(node)
        return node
