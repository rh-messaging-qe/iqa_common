import pytest


def pytest_addoption(parser):
#     # In node
#     parser.addoption("--in_node", action="store", default="localhost", help="node for ingress connection")
#
#     # Out node
#     parser.addoption("--out_node", action="store", default="localhost", help="node for egress connection")
#
#     # Sender
    parser.addoption("--senders", action="store", default="localhost", help="node where sender is running", )

#     # Receiver
#    parser.addoption("--receiver_node", action="store", default="localhost", help="node where receiver is running")
#
#     # Network model
#     parser.addoption("--network_model", action="store", default="localhost", help="path to network_model file")


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
class A:
    def __init__(self,b):
        self.b = b

a = A(b=[])

@pytest.fixture
def senders_1(request):
    args = request.config.getoption("senders")
    clients = args.split(",")
    a.b = clients

# @pytest.fixture(scope="module", autouse=True)
# def receiver_node(request):
#     #return Receiver(request.config.getoption("receiver_node"))
#     pass


import pytest
import itertools
import components.clients as client

# @TODO These lists replace with "addoptions"
senders = ['python', 'c']
receivers = ['python', 'c']


@pytest.fixture(params=senders, scope='module')
def sender(request):
    clients = {
        'native': client.core.Sender(),
        # 'python': Client(name='Python'),
        # 'c': Client(name='C'),
    }
    yield clients.get(request.param)


@pytest.fixture(params=receivers, scope='module')
def receiver(request):
    clients = {
        'native': client.core.Receiver(),
        # 'python': Client(name='Python'),
        # 'c': Client(name='C'),
    }
    yield clients.get(request.param)


@pytest.fixture(params=['artemis', 'amq7'])
def broker2(request):
    brokers = {
        'artemis': broker.artemis(),
        # 'amq7': broker.Amq7(name='Python'),
        # 'qpid': broker.qpid(name='C'),
    }
    yield brokers.get(request.param)


c_c = Client('c_client')
j_client = Client('j_client')

topologies = ['x', 'y']
clients = [c_c.name, j_client.name]
receivers = clients
senders = clients
brokers = ['artemis', 'amq7', 'amq6', 'qpid', 'rabitmq']
routers = ['qpid-dispatch', 'interconnect']


def pytest_generate_tests(metafunc):
    if hasattr(metafunc.function, 'iterate'):
        metafunc.function.parametrize = [calculate_second_parametrize()]


def calculate_second_parametrize():
    return pytest.mark.parametrize('topology,sender,receiver,broker,router',
                                   itertools.product(topologies, senders, receivers, brokers, routers))

