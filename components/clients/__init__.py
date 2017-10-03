from components.clients import core


def not_supported():
    import inspect
    print("Function '%s' is not supported for this client." % inspect.stack()[1][3])
