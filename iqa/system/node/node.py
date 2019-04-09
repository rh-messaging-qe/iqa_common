"""
Interface for Node element. A node holds a running messaging component and it
must provide some basic behaviors, like ping, get_ip and execute command.
"""
import abc

from iqa.system.command.command_base import Command
from iqa.system.executor import Executor, Execution


class Node:
    """Node component."""

    def __init__(self, hostname: str, executor: Executor, ip: str=None):
        self.hostname = hostname
        self.executor = executor
        self.ip = ip

    def execute(self, command: Command) -> Execution:
        """Execute command using Node's executor"""
        return self.executor.execute(command)

    @abc.abstractmethod
    def ping(self) -> bool:
        pass

    @abc.abstractmethod
    def get_ip(self) -> str:
        pass
