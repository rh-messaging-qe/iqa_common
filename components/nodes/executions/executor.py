# @TODO implement @mlesko Executor

from .execution import Execution


class Executor(Execution):
    def __init__(self, hostname):
        Execution.__init__(self, hostname=hostname)
