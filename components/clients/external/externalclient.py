"""
    # TODO jstejska: Package description
"""

from amom.client.client import Client
from components.node import Node


class ExternalClient(Client):
    """External CLI based clients."""

    # attribute-argument mapping dictionary
    cli_params_transformation = []
    cli_command = []
    data = set()

    def __init__(self, node: Node):
        super(ExternalClient, self).__init__()
        self.node = node

    def _run(self):
        """ # TODO jstejska: Description

        :return: # TODO jstejska: Description
        :rtype: # TODO jstejska: type
        """
        assert NotImplementedError

    def _execute(self, cmd):
        """Method for execute client's command.

        :param cmd: command
        :type cmd: # TODO jstejska: type

        :return: # TODO jstejska: Description
        :rtype: # TODO jstejska: type
        """
        self.node.execute(cmd)

    def build_command(self):
        """Method for create command for execute based on client's available attributes.

        :return: list with command attributes
        :rtype: # TODO jstejska: type
        """

        cmd = [
            opt.generate(self.data)
            for opt in self.cli_params_transformation
            if opt.satisfied(self.data)
        ]

        cmd = self.cli_command + cmd

        print(cmd)

        return " ".join(filter(None, cmd)), cmd

#
# class ExternalClientOld(Client):
#     """
#     External CLI based clients
#
#
#     @MOVED FROM AMOM
#     """
#
#     # attribute-argument mapping dictionary
#     cli_params_transformation = odict()
#     attribute_prefix = "_c_"
#
#     def __init__(self, node: Node):
#         Client.__init__(self)
#         self.node = node
#         self._init_attributes(self)
#
#     @staticmethod
#     def _init_attributes(self):
#         """
#         Method for init class attributes based on clients attributes.
#
#         :return:
#         """
#         for name, value in self.cli_params_transformation.items():
#             name = self.attribute_prefix + name
#             self.__setattr__(name, value)
#
#     def _set_attr_values(self, **kwargs):
#         """
#         Method for set class attributes based on clients attributes.
#
#         :param kwargs: dict of attributes with values
#         :return:
#         """
#         for name, value in kwargs:
#             name = self.attribute_prefix + name
#             if hasattr(self, name):
#                 self.__setattr__(name, value)
#
#     def _run(self):
#         self._not_supported()
#
#     def _execute(self, cmd):
#         """
#         Method for execute client's command.
#
#         :param cmd: command
#         :return:
#         """
#         self.node.execute(cmd)
#
#     def _build_sender_command(self):
#         """
#         Method for create command for execute based on client's available attributes.
#
#         :return: list with command attributes
#         """
#         attributes = filter(lambda a: a.startswith(self.attribute_prefix), dir(self))
#
#         command = []
#
#         for item in self.cli_params_transformation:
#             value = getattr(self, item)
#             if item in attributes and value is not None:
#                 if isinstance(value, bool):
#                     command.append(self.cli_params_transformation[item])
#                 else:
#                     command.append(self.cli_params_transformation[item] % value)
#
#         return command
