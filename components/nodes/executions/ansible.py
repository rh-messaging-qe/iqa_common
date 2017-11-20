from autologging import logged, traced
import subprocess
from .execution import Execution


# @TODO implement Ansible execution

@logged
@traced
class AnsibleCMD(Execution):
    def __init__(self, hostname):
        Execution.__init__(self, hostname=hostname)

    def execute(self, command):
        """
        Execute command on node by using Ansible command module
        :param command:
        :return:
        """
        AnsibleCMD.__log.info('Executing command on node %s..' % self.hostname)
        AnsibleCMD.__log.debug('Executing command "%s" on node %s..' % (*command, self.hostname))
        process = self._ansible_cmd(moduleargs=command, host=self.hostname, module='command')
        AnsibleCMD.__log.debug(process.stdout)
        return process

    def ping(self):
        """
        Run Ansible ping module for ping node
        :return:
        """
        AnsibleCMD.__log.info('Pinging node %s..' % self.hostname)
        process = subprocess.run(['ansible', self.hostname, '-m', 'ping'], stdout=subprocess.PIPE)

        AnsibleCMD.__log.info('Ping for node %s %s.' % (self.hostname,
                                                        'passed' if process.returncode == 0 else 'failed'))
        return True if process.returncode == 0 else False

    @staticmethod
    def _ansible_cmd(moduleargs, host, module):
        command = ['ansible', host, '-m', module, '-a', *moduleargs]
        AnsibleCMD.__log.debug(command)

        process = subprocess.run(command, stdout=subprocess.PIPE)
        AnsibleCMD.__log.debug(process.stdout)
        return process


class AnsibleAPI(Execution):
    def __init__(self, hostname):
        Execution.__init__(self, hostname=hostname)

