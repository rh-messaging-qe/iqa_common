class ConfigOld(list):
    """
    List of ('section', {'name':'value', ...}).
    Fills in some default values automatically, see Qdrouterd.DEFAULTS
    Source qpid-dispatch/tests/system_test
    """

    DEFAULTS = {
        'listener': {
            'host': '0.0.0.0', 'saslMechanisms': 'ANONYMOUS', 'idleTimeoutSeconds': '120',
            'authenticatePeer': 'no', 'role': 'normal'
        },
        'connector': {
            'host': '127.0.0.1', 'saslMechanisms': 'ANONYMOUS', 'idleTimeoutSeconds': '120'
        },
        'router': {
            'mode': 'standalone', 'id': 'QDR', 'debugDump': 'qddebug.txt'
        }
    }

    def sections(self, name):
        """Return list of sections named name"""
        return [p for n, p in self if n == name]

    @property
    def router_id(self):
        return self.sections("router")[0]["id"]

    # def defaults(self):
    #     """Fill in default values in gconfiguration"""
    #     for name, props in self:
    #         if name in Config.DEFAULTS:
    #             for n, p in Config.DEFAULTS[name].iteritems():
    #                 props.setdefault(n, p)

    def __str__(self):
        """Generate config file content. Calls default() first."""

        def props(p):
            return "".join(["    %s: %s\n" % (k, v) for k, v in p.iteritems()])

        self.defaults()
        return "".join(["%s {\n%s}\n" % (n, props(p)) for n, p in self])


#
# class ConfigNew(list):
#     def add_section(self):
#


class Section:
    def __init__(self, name):
        name = name
        items = []


class Sections:
    def __init__(self):
        pass


