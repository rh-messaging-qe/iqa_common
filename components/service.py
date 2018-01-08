from autologging import logged, traced


@logged
@traced
class Service:
    """
    Class for service handling.
    """
    def __init__(self, service, name):
        """

        :param service:
        :param name:
        """
        self.service = service
        self.name = name

    @property
    def status(self):
        """
        Get service status
        :return:
        """
        status = self.service.node.execute('service %s status' % self.name)

        for line in status.get_stdout():
            if 'running' in line:
                return 'running'
            elif '(running)' in line:
                return 'running'
            elif 'stopped' in line:
                return 'stopped'
            elif 'failed' in line:
                return 'failed'
        return 'unknown'

    def enable(self):
        """
        Service enable.
        :return: executed process
        """
        return self.service.node.ansible.ansible_cmd.cli_cmd(module='service', host=self.service.node.hostname,
                                                         args=['name=%s enabled=yes' % self.name])

    def disable(self):
        """
        Service enable.
        :return: executed process
        """
        return self.service.node.ansible.ansible_cmd.cli_cmd(module='service', host=self.service.node.hostname,
                                                         args=['name=%s enabled=no' % self.name])

    def restart(self):
        """
        Service restart.
        :return: executed process
        """
        return self.service.node.ansible.ansible_cmd.cli_cmd(module='service', host=self.service.node.hostname,
                                                         args=['name=%s state=restarted' % self.name])

    def start(self):
        """
        Service start.
        :return: executed process
        """
        return self.service.node.ansible.ansible_cmd.cli_cmd(module='service', host=self.service.node.hostname,
                                                         args=['name=%s state=started' % self.name])

    def stop(self):
        """
        Service stop.
        :return: executed process
        """
        return self.service.node.ansible.ansible_cmd.cli_cmd(module='service', host=self.service.node.hostname,
                                                         args=['name=%s state=stopped' % self.name])
