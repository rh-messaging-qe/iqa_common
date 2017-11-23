from autologging import logged, traced
from .execution import Execution
from .local_exec import LocalExec


@logged
@traced
class AnsibleCMD(Execution):
    def __init__(self, hostname):
        Execution.__init__(self, hostname=hostname)

    def _execute(self, command):
        """
        Execute command on node by using Ansible command module.
        :param command:
        :return:
        """
        if isinstance(command, str):
            command = [command]

        AnsibleCMD.__log.info('Executing command on node %s..' % self.hostname)
        AnsibleCMD.__log.debug('Executing command "%s" on node %s..' % (*command, self.hostname))
        process = self._ansible_cmd(moduleargs=command, host=self.hostname, module='command')
        AnsibleCMD.__log.debug(process.get_stdout())
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
        AnsibleCMD.__log.info('Ping for node %s %s.' % (self.hostname,
                                                        'passed' if process.get_ecode() == 0 else 'failed'))

        return True if process.get_ecode() == 0 else False

    @staticmethod
    def _ansible_cmd(moduleargs, host, module):
        """
        Execute command on node by using Ansible.
        :param moduleargs:
        :param host:
        :param module:
        :return:
        """
        command = ['ansible', host, '-m', module, '-a', *moduleargs]
        AnsibleCMD.__log.debug(command)

        process = LocalExec(command)
        process.run_and_wait()
        AnsibleCMD.__log.debug(process.get_stdout())

        return process


class AnsibleAPI(Execution):
    def __init__(self, hostname):
        Execution.__init__(self, hostname=hostname)
