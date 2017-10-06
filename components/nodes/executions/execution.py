from autologging import logged, traced
import inspect

# @TODO implement execution base class
# Why we need have more different execution method?
# - Will be easy and supported to switch into another execution.


@logged
@traced
class Execution:
    def __init__(self, hostname):
        self.hostname = hostname

    def execute(self, command):
        self.__execute(command)

    @staticmethod
    def __execute(self):
        print("Execution method '%s' is not supported!" % inspect.stack()[1][3])
