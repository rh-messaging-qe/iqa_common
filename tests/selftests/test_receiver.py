from amom.client import Receiver


def test_isinstance(receiver: Receiver):
    """
    Check if created receiver is instance of Receiver class.
    :param receiver:
    """
    assert isinstance(receiver, Receiver)


def test_name(receiver: Receiver):
    """
    Check if created receiver is available in the test-suite.
    :param receiver:
    """
    clients = ['Internal core client','NodeJS RHEA client']
    assert (receiver.name in clients) == True


def test_attributes(receiver: Receiver):
    """
    Check if all internal attributes are created.
    :param receiver:
    """
    output = False

    for name, value in receiver.cli_params_transformation.items():
        name = receiver.attribute_prefix + name
        output = hasattr(receiver, name)

    assert output == True