import pytest

from amom.client import Sender, Receiver, Connector
from amom.broker import Broker
from amom.router import Router


# @pytest.mark.iterate
# def test(topology, sender, receiver, broker, router):
#     print('\n%s %s %s %s %s' % (topology, sender, receiver, broker, router))
#     pass


def test_2(receiver: Receiver, sender: Sender, broker: Broker, router: Router):
    print(sender.name)
    print(receiver.name)
    print(broker.supported_protocols)
    print(router.node.hostname)
    pass
