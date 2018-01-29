from inspect import stack
from odict import odict

from ..node import Node


class Client:
    """
    Abstract class for every messaging client
    """

    # Required variables
    supported_protocols = []
    name = ''
    version = ''

    ###

    def __init__(self):
        self.logs = None  # @TODO

    @property
    def get_supported_protocols(self):
        return self.supported_protocols

    @property
    def get_name(self):
        return self.name

    @property
    def get_version(self):
        return self.version

    @staticmethod
    def _not_supported():
        print("Function %s is not supported for this client." % stack()[1][3])
        raise NotImplemented


class NativeClient(Client):
    def __init__(self):
        Client.__init__(self)


class LocalhostClient(Client):
    def __init__(self):
        Client.__init__(self)


class ExternalClient(Client):
    """
    External CLI based clients

    @TODO move to components
    """

    # attribute-argument mapping dictionary
    cli_params_transformation = odict()
    attribute_prefix = "_c_"

    def __init__(self):
        Client.__init__(self)
        # self.node = node
        self._init_attributes(self)

    @staticmethod
    def _init_attributes(self):
        """
        Method for init class attributes based on clients attributes.
        :return:
        """
        for name, value in self.cli_params_transformation.items():
            name = self.attribute_prefix + name
            self.__setattr__(name, value)

    def _set_attr_values(self, **kwargs):
        """
        Method for set class attributes based on clients attributes.
        :param kwargs: dict of attributes with values
        :return:
        """
        for name, value in kwargs:
            name = self.attribute_prefix + name
            if hasattr(self, name):
                self.__setattr__(name, value)

    def _run(self):
        self._not_supported()

    def _execute(self, cmd):
        """
        Method for execute client's command.
        :param cmd: command
        :return:
        """
        self.node.execute(cmd)

    def _build_sender_command(self):
        """
        Method for create command for execute based on client's available attributes.
        :return: list with command attributes
        """
        attributes = filter(lambda a: a.startswith(self.attribute_prefix), dir(self))

        command = []

        for item in self.cli_params_transformation:
            value = getattr(self, item)
            if item in attributes and value is not None:
                if isinstance(value, bool):
                    command.append(self.cli_params_transformation[item])
                else:
                    command.append(self.cli_params_transformation[item] % value)

        return command
