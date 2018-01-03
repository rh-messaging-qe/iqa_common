# -*- coding: utf-8 -*-

from autologging import logged, traced
import inspect

# @TODO implement execution base class
# Why we need have more different execution method?
# - Will be easy and supported to switch into another execution.


@logged
@traced
class Execution:
    """
    Abstract of execution
    """
    def __init__(self, hostname):
        self.hostname = hostname

    def execute(self, command):
        """
        Execute command on node
        """
        Execution.__log.info('Executing command on node %s..' % self.hostname)
        return self._execute(command)

    def _execute(self, command):
        print("Execution method '%s' is not supported!" % inspect.stack()[1][3])
