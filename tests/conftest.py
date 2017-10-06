import os
import pytest
import itertools
from components.nodes import Node

#####################
# Section: Logging #
###################


def pytest_logger_config(logger_config):
    logger_config.add_loggers(['foo', 'bar', 'baz'], stdout_level='debug')
    logger_config.set_log_option_default('foo,bar')


def pytest_logger_logdirlink(config):
    return os.path.join(os.path.dirname(__file__), 'mylogs')

########################
# Section: Add option #
######################

# def pytest_addoption(parser):
#     # In node
#     parser.addoption("--in_node", action="store", default="localhost", help="node for ingress connection")
#
#     # Out node
#     parser.addoption("--out_node", action="store", default="localhost", help="node for egress connection")
#
#     # Sender
#    parser.addoption("--senders", action="store", default="localhost", help="node where sender is running", )
#
#     # Receiver
#    parser.addoption("--receiver_node", action="store", default="localhost", help="node where receiver is running")
#
#     # Network model
#     parser.addoption("--network_model", action="store", default="localhost", help="path to network_model file")
#
#
# @pytest.fixture(scope="module", autouse=True)
# def in_node(request):
#     #return Router(request.config.getoption("in_node"))
#     pass
#
# @pytest.fixture(scope="module", autouse=True)
# def out_node(request):
#     #return Router(request.config.getoption("out_node"))
#     pass
#


def parse_senders(request):
    return request.config.getoption("senders").split(",")

######################
# Section: Fixtures #
####################

# @pytest.fixture(scope="module", autouse=True)
# def receiver_node(request):
#     #return Receiver(request.config.getoption("receiver_node"))
#     pass

##
i_clients = ['native']
i_brokers = ['artemis', 'amq7']
i_routers = ['dispatch', 'interconnect']
i_sender = i_clients
i_receiver = i_clients


@pytest.fixture(params=i_sender, scope='module')
def sender(request):
    if request.param is 'native':
        import components.clients.core as core
        return core.Sender()
    # yield s


@pytest.fixture(params=i_receiver, scope='module')
def receiver(request):
    if request.param is 'native':
        import components.clients.core as core
        return core.Receiver()

broker_node = Node(hostname='broker_node')


@pytest.fixture(params=['artemis', 'amq7'])
def broker(request):
    from components.brokers.artemis.artemis import Artemis
    if request.param is 'artemis':
        return Artemis(node=broker_node)  # @TODO Node
    elif request.param is 'amq7':
        return Artemis(node=broker_node)  # @TODO Node

router_node = Node(hostname='router_node')


@pytest.fixture(params=['dispatch', 'interconnect'])
def router(request):
    from components.routers.dispatch.dispatch import Dispatch
    if request.param is 'dispatch':
        return Dispatch(node=router_node)  # @TODO Node
    elif request.param is 'interconnect':
        return Dispatch(node=router_node)  # @TODO Node


#########################################
# Section: Try overloading parametrize #
#######################################
i_topologies = ['x', 'y']


def pytest_generate_tests(metafunc):
    if hasattr(metafunc.function, 'iterate'):
        metafunc.function.parametrize = [calculate_second_parametrize()]


def calculate_second_parametrize():
    parametrize = \
        pytest.mark.parametrize(
            'topology,'
            'sender,'
            'receiver,'
            'broker,'
            'router',
            itertools.product(
                i_topologies,
                i_sender,
                i_receiver,
                i_brokers,
                i_routers
            )
        )
    return parametrize


