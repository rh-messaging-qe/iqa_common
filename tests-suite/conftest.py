import logging
import os
import xtlog.adapters
import pytest

xtlog.config.config_all_default()
xtlog.init()
logger = logging.getLogger(__name__)


def pytest_addoption(parser):
    """
    :param parser:
    :return:
    """
    iqa = parser.getgroup('iqa')

    # Inventory
    iqa.addoption('--inventory', action='store', dest='inventory', help='Inventory file.')


def pytest_configure(config):
    if not config.getvalue('inventory'):
        raise pytest.UsageError("value --inventory option is required")

    inventory_path = config.getvalue('inventory') if config.getvalue('inventory') else ''

    if not os.path.exists(inventory_path):
        raise pytest.UsageError("value of --inventory option ({}) is not accessible".format(inventory_path))


#####################
# Section: Logging #
###################

def pytest_logger_config(logger_config):
    pass


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
