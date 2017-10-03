from .execution import Execution
from .ansible import Ansible
from .executor import Executor


def not_supported():
    import inspect
    print("Execution method '%s' is not supported!" % inspect.stack()[1][3])
