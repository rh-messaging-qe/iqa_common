from amom.client import Receiver


def test_isinstance(receiver: Receiver):
    assert isinstance(receiver, Receiver)


def test_name(receiver: Receiver):
    clients = ['Internal core client','NodeJS RHEA client']
    assert (receiver.name in clients) == True


def test_attributes(receiver: Receiver):
    output = False

    for name, value in receiver.cli_params_transformation.items():
        name = receiver.attribute_prefix + name
        output = hasattr(receiver, name)

    assert output == True