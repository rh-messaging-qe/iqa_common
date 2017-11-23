from amom.client import Sender, Receiver
from amom.broker import Broker
from amom.router import Router


def test_1(receiver: Receiver, sender: Sender, broker: Broker, router: Router, tls):
    # assert broker.node.execute(['ls'])
    assert broker.node.ping()
