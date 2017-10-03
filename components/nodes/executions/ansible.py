# @TODO implement Ansible execution

from .execution import Execution


class Ansible(Execution):
    def __init__(self):
        Execution.__init__(self)
