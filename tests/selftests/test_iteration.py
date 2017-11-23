from amom.client import Sender, Receiver
from amom.broker import Broker
from amom.router import Router


def test_1(receiver: Receiver, sender: Sender, broker: Broker, router: Router):
    broker.node.execute(['ls'])
    assert broker.node.ping()

def test_restart(receiver: Receiver, sender: Sender, broker: Broker, router: Router):
    assert router.service._restart().get_ecode() == 0

def test_stop(receiver: Receiver, sender: Sender, broker: Broker, router: Router):
    assert router.service._stop().get_ecode() == 0

def test_start(receiver: Receiver, sender: Sender, broker: Broker, router: Router):
    assert router.service._start().get_ecode() == 0
