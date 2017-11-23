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



##################################
# Section: Run before/after test #
##################################


@pytest.yield_fixture(scope='function', autouse=True)
def run_around_tests(request):
    test_name = request.node.name
    logger.info("Starting: %s" % test_name)

    def fin():
        logger.info("Ending: %s" % test_name)
        if request.node.rep_setup.failed:
            logger.error("Setting up a test failed!")
        elif request.node.rep_setup.passed:
            logger.info("Setting up a test passed!")
            if request.node.rep_call.failed:
                logger.test_fail(request.node.nodeid)
            elif request.node.rep_call.passed:
                logger.test_pass(request.node.nodeid)

    request.addfinalizer(fin)

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
