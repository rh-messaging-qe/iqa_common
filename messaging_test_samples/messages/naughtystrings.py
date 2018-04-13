import os

"""Path to the file"""

path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def naughty_strings():
    """
    Get the list of naughty_strings.

    https://github.com/minimaxir/big-list-of-naughty-string

    :returns: The list of naughty strings
    """
    naughty = _naughty_strings_read(os.path.join(path, 'messages/assets/blns.txt'))
    return naughty


def naughty_strings_base64():
    """
    Get the list of naughty_strings in base64.

    https://github.com/minimaxir/big-list-of-naughty-string

    :returns: The list of naughty strings
    """
    naughty = _naughty_strings_read(os.path.join(path, 'messages/assets/blns.base64.txt'))
    return naughty


def _naughty_strings_read(file):
    """
    Parse file to list

    :returns: The list of strings
    """


    strings = []

    with open(file, 'r') as f:
        strings = f.readlines()

        # above line leaves trailing newline characters; strip them out
        strings = [x.strip(u'\n') for x in strings]

        # remove empty-lines and comments
        strings = [x for x in strings if x and not x.startswith(u'#')]

        # insert empty string since all are being removed
        strings.insert(0, u"")

    return strings