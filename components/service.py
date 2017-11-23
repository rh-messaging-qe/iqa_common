class Service:
    """
    Class for service handling.
    """
    def __init__(self, service, name):
        self.service = service
        self.name = name

    def _restart(self):
        """
        Service restart.
        :return: executed process
        """
        return self.service.node.ansible.cli_cmd(module='service', host=self.service.node.hostname,
                                                 moduleargs=['name=%s state=restarted' % self.name])
    def _start(self):
        """
        Service start.
        :return: executed process
        """
        return self.service.node.ansible.cli_cmd(module='service', host=self.service.node.hostname,
                                                 moduleargs=['name=%s state=started' % self.name])

    def _stop(self):
        """
        Service stop.
        :return: executed process
        """
        return self.service.node.ansible.cli_cmd(module='service', host=self.service.node.hostname,
                                                 moduleargs=['name=%s state=stopped' % self.name])
