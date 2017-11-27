class Service:
    """
    Class for service handling.
    """
    def __init__(self, service, name):
        self.service = service
        self.name = name
    # @TODO status, enable, disable
    #     self.status = self._status()
    #
    # def _status(self):
    #     status = self.service.node.execute('service %s status' % self.service)
    #     if 'running' in status.get_stdout():
    #         return 'running'
    #     if 'stopped' in status.get_stdout():
    #         return 'stopped'
    #     if 'failed' in status.get_stdout():
    #         return 'failed'
    #
    # def _enable(self):
    #     """
    #     Service enable.
    #     :return: executed process
    #     """
    #     return self.service.node.ansible.cli_cmd(module='service', host=self.service.node.hostname,
    #                                              moduleargs=['name=%s state=disabled' % self.name])
    #
    # def _disable(self):
    #     """
    #     Service enable.
    #     :return: executed process
    #     """
    #     return self.service.node.ansible.cli_cmd(module='service', host=self.service.node.hostname,
    #                                              moduleargs=['name=%s state=disabled' % self.name])
    #

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
