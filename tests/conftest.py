import sys
import os
import logging
import xtlog
import xtlog.adapters

import pytest
import itertools

from components.nodes import Node
import components.clients.core as core
from components.brokers.artemis import Artemis
from components.routers.dispatch.dispatch import Dispatch

#####################
# Section: Logging #
###################


def pytest_logger_config(logger_config):
    xtlog.config.config_all_default()
    xtlog.init()
    # logging.basicConfig(
    #     level=TRACE, stream=sys.stdout,
    #     format="%(levelname)s:%(name)s:%(funcName)s:%(message)s"
    # )
    logger_config.add_loggers(['foo', 'bar', 'baz'], stdout_level='debug')
    logger_config.set_log_option_default('foo,bar')


#def pytest_logger_logdirlink(config):
#    return os.path.join(os.path.dirname(__file__), 'mylogs')


########################
# Section: Add option #
######################


def pytest_addoption(parser):
    """

    :param parser:
    :return:
    """
#     # In node
    parser.addoption("--in_node", action="store", default="localhost", help="node for ingress connection")
#
#     # Out node
    parser.addoption("--out_node", action="store", default="localhost", help="node for egress connection")
#
#
#     # Receiver node
    parser.addoption("--receiver_node", action="store", default="localhost", help="node where receiver is running")
#
#     # Sender node
    parser.addoption("--sender_node", action="store", default="localhost", help="node where receiver is running")
#

    # Sender
    parser.addoption("--sender", action="append", default=[], help="node where sender is running")

    # Brokers
    parser.addoption("--receiver", action="append", default=[], help="node where sender is running")

    # Routers
    parser.addoption("--router", action="append", default=[], help="node where sender is running")

    # Brokers
    parser.addoption("--broker", action="append", default=[], help="node where sender is running")


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
    broker_node = Node(hostname='broker_node')
    if 'artemis' in request.param:
        return Artemis(node=broker_node)  # @TODO Node
    elif 'amq7' in request.param:
        return Artemis(node=broker_node)  # @TODO Node


@pytest.fixture()
def router(request):
    router_node = Node(hostname='router_node')
    if 'dispatch' in request.param:
        return Dispatch(node=router_node)  # @TODO Node
    elif 'interconnect' in request.param:
        return Dispatch(node=router_node)  # @TODO Node


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


