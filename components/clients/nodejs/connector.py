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
    # client is installed from cli-rhea, node_app is there only for backward compatibility
    cli_command = odict([('nodejs', 'cli-rhea-connector')])

    cli_params_transformation = odict([
        ('help', '--help'),
        # Control options
        ('timeout', '--timeout %s'),
        ('close_sleep', '--close-sleep %s'),
        ('broker_url', '--broker %s'),
        ('broker_address', '--address %s'),
        ('count', '--count %s'),
        ('link_durable', '--link-durable %s'),

        # Logging options
        ('log-lib', '--log-lib %s'),
        ('log-stats', '--log-stats %s'),

        # Connection options
        ('conn_urls', '--conn-urls %s'),
        ('conn_reconnect', '--conn-reconnect %s'),
        ('conn_reconnect_interval', '--conn-reconnect-interval %s'),
        ('conn_reconnect_limit', '--conn-reconnect-limit %s'),
        ('conn_reconnect_timeout', '--conn-reconnect-timeout %s'),
        ('conn_heartbeat', '--conn-heartbeat %s'),
        ('conn_ssl', '--conn-ssl %s'),
        ('conn_ssl_certificate', '--conn-ssl-certificate %s'),
        ('conn_ssl_private_key', '--conn-ssl-private-key %s'),
        ('conn_ssl_password', '--conn-ssl-password %s'),
        ('conn_ssl_trust_store', '--conn-ssl-trust-store %s'),
        ('conn_ssl_verify_peer', '--conn-ssl-verify-peer'),
        ('conn_ssl_verify_peer_name', '--conn-ssl-verify-peer-name'),
        ('conn_max_frame_size', '--conn-max-frame-size %s'),
        ('conn_web_socket', '--conn-web-socket %s'),

        # Connector options
        ('obj-ctrl', '--obj-ctrl %s'),

        # Other
        ('transport', None),
        ('host', None),
        ('port', None),
        ('username', None),
        ('password', None),
        ('address', None)
    ])

    def __init__(self):
        """
        Method for init receiver.
        """
        amom.client.Connector.__init__(self)
        Client.__init__(self)
