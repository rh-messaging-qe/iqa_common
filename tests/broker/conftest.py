import pytest

from components.brokers.artemis import Artemis
from components.instance import IQAInstance

iqa_instance = IQAInstance()


########################
# Section: Fixtures    #
########################


master1 = iqa_instance.new_node(hostname='master1')


@pytest.fixture()
def master1(request):
    """
    Map Artemis broker 1 component
    :return: Broker object
    """

    if 'artemis' in request.param:
        return Artemis(node=master1)


slave1 = iqa_instance.new_node(hostname='master1')


@pytest.fixture()
def slave1(request):
    """
    Map Artemis broker 2 component
    :return: Broker object
    """

    if 'artemis' in request.param:
        return Artemis(node=slave1)


slave2 = iqa_instance.new_node(hostname='master1')


@pytest.fixture()
def slave2(request):
    """
    Map Artemis broker 2 component
    :return: Broker object
    """

    if 'artemis' in request.param:
        return Artemis(node=slave2)
