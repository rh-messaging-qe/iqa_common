import pytest

from components.brokers.artemis import Artemis
from components.instance import IQAInstance

iqa_instance = IQAInstance()


def pytest_addoption(parser):
    components = parser.getgroup('iqa-components')

    # Senders
    components.addoption("--master1", action="append", default=['master1'])

    # Brokers
    components.addoption("--slave1", action="append", default=['slave1'])

    # Routers
    components.addoption("--slave2", action="append", default=['slave2'])



def pytest_configure(config):
    # iqa_instance = IQAInstance(inventory=config.getvalue('inventory'))
    iqa_instance.inventory = config.getvalue('inventory')

#############################
# Section: Parametrization  #
#############################

def pytest_generate_tests(metafunc):
    if 'master1' in metafunc.fixturenames:
        master1 = list(metafunc.config.option.sender)
        metafunc.parametrize('master1', master1, indirect=True)

    if 'slave1' in metafunc.fixturenames:
        slave1 = list(metafunc.config.option.receiver)
        metafunc.parametrize('slave1', slave1, indirect=True)

    if 'slave2' in metafunc.fixturenames:
        slave2 = list(metafunc.config.option.broker)
        metafunc.parametrize('slave2', slave2, indirect=True)

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
