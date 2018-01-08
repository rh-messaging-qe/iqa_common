import pytest

import components.clients.core as core
# from components.nodes import Node
from components.brokers.artemis import Artemis
from components.routers.dispatch.dispatch import Dispatch
from components.instance import IQAInstance

iqa_instance = IQAInstance()


def pytest_namespace():
    return {'iqa_instance': iqa_instance}


@pytest.fixture
def iqa():
    """
    IQA instance with accessible nodes, components
    :return:
    """
    return pytest.iqa


########################
# Section: Add option  #
########################
def pytest_addoption(parser):
    components = parser.getgroup('iqa-components')

    # Senders
    components.addoption("--sender", action="append", default=[], help="Define sender client [native, nodejs]")

    # Brokers
    components.addoption("--receiver", action="append", default=[], help="Define receiver client []")

    # Routers
    components.addoption("--router", action="append", default=[], help="Define which router [dispatch, interconnect]")

    # Brokers
    components.addoption("--broker", action="append", default=[], help="Define which broker [amq7, artemis, rabitmq]")

    # TLS
    components.addoption("--tls", action="append", default=[], help="TLS option [tls10,tls11,tls12,tls13]")


def pytest_configure(config):
    iqa_instance.inventory = config.getvalue('inventory')


##############################
# Section: Parametrization  #
#############################
def pytest_generate_tests(metafunc):
    if 'sender' in metafunc.fixturenames:
        senders = list(metafunc.config.option.sender)
        metafunc.parametrize('sender', senders, indirect=True)

    if 'receiver' in metafunc.fixturenames:
        receivers = list(metafunc.config.option.receiver)
        metafunc.parametrize('receiver', receivers, indirect=True)

    if 'broker' in metafunc.fixturenames:
        brokers = list(metafunc.config.option.broker)
        metafunc.parametrize('broker', brokers, indirect=True)

    if 'router' in metafunc.fixturenames:
        routers = list(metafunc.config.option.router)
        metafunc.parametrize('router', routers, indirect=True)

    if 'tls' in metafunc.fixturenames:
        tls = list(metafunc.config.option.tls)
        metafunc.parametrize('tls', tls, indirect=True)


########################
# Section: Fixtures    #
########################
@pytest.fixture()
def sender(request):
    if 'native' in request.param:
        return core.Sender()
    elif 'nodejs' in request.param:
        return core.Sender()
    elif 'python' in request.param:
        return core.Sender()


@pytest.fixture()
def receiver(request):
    if 'native' in request.param:
        return core.Receiver()
    elif 'nodejs' in request.param:
        return core.Receiver()
    elif 'python' in request.param:
        return core.Receiver()


broker_node = iqa_instance.new_node(hostname='ic01-r6i')

@pytest.fixture()
def broker(request):
    """
    Iteration objects for broker
    :return: Broker object
    """

    if 'artemis' in request.param:
        return Artemis(node=broker_node)
    elif 'amq7' in request.param:
        return Artemis(node=broker_node)
    elif 'amq6' in request.param:
        return Artemis(node=broker_node)


router_node = iqa_instance.new_node(hostname='ic01-r6i')


@pytest.fixture()
def router(request):
    """
    Iteration objects for router
    :param request:
    :return: Router object
    """
    if 'dispatch' in request.param:
        return Dispatch(node=router_node)
    elif 'interconnect' in request.param:
        return Dispatch(node=router_node)


@pytest.fixture()
def tls(request):
    """
    Iteration object for TLS settings
    :param request:
    :return:
    """
    if 'tls10' in request.param:
        return 'settings for tls10'
    elif 'tls11' in request.param:
        return 'settings for tls11'
    elif 'tls12' in request.param:
        return 'settings for tls12'
    elif 'tls13' in request.param:
        return 'settings for tls13'


@pytest.fixture()
def sasl(request):
    """
    SASL Authentication fixture
    :param request:
    :return:
    """
    if 'sasl_user' in request.param and 'sasl_password':
        return None
    else:
        return None