from autologging import logged
from components.nodes.executions import not_supported

# @TODO implement execution base class
# Why we need have more different execution method?
# - Will be easy and supported to switch into another execution.


@logged
class Execution:
    def __init__(self):
        pass

    def execute(self, command):
        self.__log.debug('Call execute "%s"' % command)
        self.__execute(command)

    @staticmethod
    def execute():
        not_supported()
