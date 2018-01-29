from autologging import logged, traced

import os

from .execution import Execution
from .local_exec import LocalExec


@logged
@traced
class AnsibleCMD:
    """
    Ansible program abstraction
    """

    def __init__(self, inventory):
        """
        :param inventory:
        """
        self.inventory = inventory

    @staticmethod
    def cli_cmd(host, module, args):
        """
        Execute command on node by using Ansible.
        :param args:
        :param host:
        :param module:
        :param args:
        :return:
        """
        command = ['ansible', host, '-m', module, '-a', *args]
        process = LocalExec(command)
        process.run_and_wait()
        return process

    @staticmethod
    def cli_playbook(playbook, inventory, args):
        """
        Execute command on node by using Ansible.
        :param playbook:
        :param module:
        :param inventory:
        :param args:
        :return:
        """
        # Check if Ansible playbook exists
        if not os.path.exists(playbook):
            AnsibleCMD.__log.debug('Wrong playbook: %s' % playbook)

        command = ['ansible-playbook', '-i', inventory, playbook, '-a', '-f', '10', *args]
        process = LocalExec(command)
        process.run_and_wait()
        return process


@logged
@traced
class AnsibleExecution(Execution):
    """
    Ansible CLI Ad-Hoc Commands
    """

    def __init__(self, hostname, ansible_cmd: AnsibleCMD):
        Execution.__init__(self, hostname=hostname)
        self.ansible_cmd = ansible_cmd

    def _execute(self, command):
        """
        Execute command on node by using Ansible command module.
        :param command:
        :return:
        """
        if isinstance(command, str):
            command = [command]

        process = self.ansible_cmd.cli_cmd(host=self.hostname, module='shell', args=command)
        return process

    def ping(self):
        """
        Run Ansible ping module for ping node
        :return:
        """
        AnsibleCMD.__log.info('Pinging node %s..' % self.hostname)

        command = ['ansible', self.hostname, '-m', 'ping']
        process = LocalExec(command)
        process.run_and_wait()
        self.ansible_cmd.cli_cmd(host=self.hostname, module='ping', args='data=pong')

        # Logs
        result = 'passed' if process.get_ecode() == 0 else 'failed'
        AnsibleExecution.__log.info('Ping for node %s %s.' % (self.hostname, result))

        return True if process.get_ecode() == 0 else False


@logged
@traced
class AnsibleAPI(Execution):
    """
    @TODO Ansible API Usage
    """

    def __init__(self, hostname):
        Execution.__init__(self, hostname=hostname)
