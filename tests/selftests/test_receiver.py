from pip._vendor.distlib._backport.shutil import ReadError

from amom.client import Receiver
from components.nodes.node import Node


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
    clients = ['Internal core client', 'NodeJS RHEA client', 'Python Proton client']
    assert (receiver.name in clients) is True


def test_attributes(receiver: Receiver):
    """
    Check if all internal attributes are created.
    :param receiver:
    """
    output = False

    for name, value in receiver.cli_params_transformation.items():
        name = receiver.attribute_prefix + name
        output = hasattr(receiver, name)

    assert output is True


def test_execute(receiver: Receiver):
    """
    Check remote command exec.
    :param receiver:
    """
    receiver._c_help = True
    receiver._c_timeout = 5
    command = receiver._build_sender_command()

    result = receiver.node.execute(command)
    assert result.get_ecode() == 0
