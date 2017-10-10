import pytest

from amom.broker import Broker
from amom.node import Node


def test_isinstance(broker: Broker):
    assert isinstance(broker, Broker)


def test_node(broker: Broker):
    assert isinstance(broker.node, Node)
