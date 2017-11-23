from amom.client import Receiver


def test_isinstance(receiver: Receiver):
    assert isinstance(receiver, Receiver)


def test_name(receiver: Receiver):
    assert receiver.name == 'Internal core client'
