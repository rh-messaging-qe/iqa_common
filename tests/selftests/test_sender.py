from amom.client import Sender
from odict import odict



def test_isinstance(sender: Sender):
    assert isinstance(sender, Sender)


def test_name(sender: Sender):
    clients = ['Internal core client','NodeJS RHEA client']
    assert (sender.name in clients) == True


def test_attributes(sender: Sender):
    output = False

    for name, value in sender.cli_params_transformation.items():
        name = sender.attribute_prefix + name
        output = hasattr(sender, name)

    assert output == True