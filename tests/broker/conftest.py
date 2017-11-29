import pytest

from components.brokers.artemis import Artemis
from components.instance import IQAInstance

iqa_instance = IQAInstance()


########################
# Section: Fixtures    #
########################


master1 = iqa_instance.new_node(hostname='master1')


@pytest.fixture()
def master1():
    """
    Map Artemis broker 1 component
    :return: Broker object
    """

    return Artemis(node=master1)


slave1 = iqa_instance.new_node(hostname='slave1')


@pytest.fixture()
def slave1():
    """
    Map Artemis broker 2 component
    :return: Broker object
    """

    return Artemis(node=slave1)


slave2 = iqa_instance.new_node(hostname='slave2')


@pytest.fixture()
def slave2():
    """
    Map Artemis broker 2 component
    :return: Broker object
    """

    return Artemis(node=slave2)
