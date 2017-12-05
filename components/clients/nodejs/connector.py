from autologging import logged, traced
from odict import odict

import amom.client
from .client import Client


@logged
@traced
class Connector(Client, amom.client.Connector):
    """
    External NodeJS connector client
    """
    # client is installed from cli-rhea, node_app is there only for backward compability
    cli_command = odict([('nodejs', 'cli-rhea-connector')])

    cli_params_transformation = odict([
        # TODO
        ('help', '--help'),

        ('broker-url', "--broker %s"),
        ('transport', None),
        ('host', None),
        ('port', None),
        ('username', None),
        ('password', None),
        ('address', '--address "%s"'),

        ('count', '--count %s'),
        ('close-sleep', '--close-sleep %s'),

        ('log-lib', '--log-lib %s'),
        ('log-stats', '--log-stats %s'),

        ('conn-urls', '--conn-urls %s'),
        ('conn-reconnect', '--conn-reconnect %s'),
        ('conn-heartbeat', '--conn-heartbeat %s'),
        ('conn-ssl-domain', '--conn-ssl-domain %s'),
        ('conn-handler', '--conn-handler %s'),

        ('obj-ctrl', '--obj-ctrl %s'),
        ('sync-mode', '--sync-mode %s')
    ])

    def __init__(self):
        amom.client.Connector.__init__(self)
        Client.__init__(self)
