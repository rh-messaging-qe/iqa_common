import logging
import xtlog
import xtlog.adapters

import pytest


import components.clients.core as core
from components.nodes import Node
from components.brokers.artemis import Artemis
from components.routers.dispatch.dispatch import Dispatch


#####################
# Section: Logging #
###################


def pytest_logger_config(logger_config):
    xtlog.config.config_all_default()
    xtlog.init()
    logger_config.add_loggers(['foo', 'bar', 'baz'], stdout_level='debug')
    logger_config.set_log_option_default('foo,bar')


logger = logging.getLogger(__name__)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


########################
# Section: Add option  #
########################


def pytest_addoption(parser):
    """

    :param parser:
    :return:
    """
    # In node
    parser.addoption("--in_node", action="store", default="localhost", help="node for ingress connection")

    # Out node
    parser.addoption("--out_node", action="store", default="localhost", help="node for egress connection")

    # Receiver node
    parser.addoption("--receiver_node", action="store", default="localhost", help="node where receiver is running")

    # Sender node
    parser.addoption("--sender_node", action="store", default="localhost", help="node where receiver is running")

    # Senders
    parser.addoption("--sender", action="append", default=[], help="Define which sender client")

    # Brokers
    parser.addoption("--receiver", action="append", default=[], help="Define which receiver client")

    # Routers
    parser.addoption("--router", action="append", default=[], help="Define which router [dispatch, interconnect]")

    # Brokers
    parser.addoption("--broker", action="append", default=[], help="Define which broker [amq7, artemis, rabitmq]")


#############################
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


########################
# Section: Fixtures    #
########################


@pytest.fixture()
def sender(request):
    if 'native' in request.param:
        return core.Sender()


@pytest.fixture()
def receiver(request):
    if 'native' in request.param:
        return core.Receiver()


@pytest.fixture()
def broker(request):
    broker_node = Node(hostname='ic02')
    if 'artemis' in request.param:
        return Artemis(node=broker_node)
    elif 'amq7' in request.param:
        return Artemis(node=broker_node)


@pytest.fixture()
def router(request):
    router_node = Node(hostname='ic02')
    if 'dispatch' in request.param:
        return Dispatch(node=router_node)
    elif 'interconnect' in request.param:
        return Dispatch(node=router_node)


@pytest.fixture()
def tls(request):
    if 'tls10' in request.param:
        return core.Sender()
    if 'tls11' in request.param:
        return core.Sender()
    if 'tls12' in request.param:
        return core.Sender()
    if 'tls13' in request.param:
        return core.Sender()


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


##################################
# Section: Run before/after test #
##################################


@pytest.yield_fixture(scope='function', autouse=True)
def run_around_tests(request):
    test_name = request.node.name
    print("Starting ", test_name)
    yield
    print("Ending: %s" % test_name)

    if request.node.rep_setup.failed:
        print("Setting up a test failed!", request.node.nodeid)
    elif request.node.rep_setup.passed:
        print("Setting up a test passed!", request.node.nodeid)
        if request.node.rep_call.failed:
            # print("Executing test failed!", request.node.nodeid)
            logger.test_fail(request.node.nodeid)
        elif request.node.rep_call.passed:
            # print("Executing test passed!", request.node.nodeid)
            logger.test_pass(request.node.nodeid)


#########################################
# Section: Try overloading parametrize #
#######################################
# i_topologies = ['x', 'y']

# def calculate_second_parametrize():
#     parametrize = \
#         pytest.mark.parametrize(
#             'topology,'
#             'sender,'
#             'receiver,'
#             'broker,'
#             'router',
#             itertools.product(
#                 i_topologies,
#                 i_sender,
#                 i_receiver,
#                 i_brokers,
#                 i_routers
#             )
#         )
#     return parametrize
