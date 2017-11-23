from amom.broker import Broker
from amom.node import Node


def test_isinstance(broker: Broker):
    assert isinstance(broker, Broker)


def test_node(broker: Broker):
    assert isinstance(broker.node, Node)


def test_exec_on_broker_node(broker: Broker):
    exec = broker.node.execute(['ls'])
    assert True if exec.get_ecode() == 0 else False