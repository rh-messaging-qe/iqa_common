import inspect


def get_func_name():
    return inspect.stack()[1][3]  # return caller's name


# For understand please follow: http://www.diveintopython.net/power_of_introspection/index.html
def get_class(cls):
    parts = cls.split('.')
    mod = ".".join(cls.split('.')[:-1])
    m = __import__(mod)
    for comp in parts[1:]:
        m = getattr(m, comp)
    return m

