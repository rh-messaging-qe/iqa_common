from autologging import logged, traced
from odict import odict

import amom.client
from components.nodes.node import Node
from .client import Client


@logged
@traced
class Receiver(Client, amom.client.Receiver):
    """
    External NodeJS receiver client
    """
    # client is installed from cli-rhea, node_app is there only for backward compatibility
    cli_command = ['cli-rhea-receiver']

    # Client-sender params for build execute command
    cli_params_transformation = odict([
        ('help', '--help'),
        # Control options
        ('recv_msg_selector', '--recv-selector "%s"'),
        ('recv_browse', '--recv-browse'),
        ('action', '--action %s'),
        ('capacity', '--capacity %s'),
        ('process_reply_to', '--process-reply-to'),
        ('recv_listen', '--recv-listen %s'),
        ('recv_listen_port', '--recv-listen-port %s'),
        ('duration', '--duration %s'),
        ('broker_url', '--broker %s'),
        ('broker_address', '--address "%s"'),
        ('msg_cnt', '--count %s'),
        ('close_sleep', '--close-sleep %s'),
        ('timeout', '--timeout %s'),

        # Logging options
        ('log_msgs', '--log-msgs %s'),
        ('log_lib', '--log-lib %s'),
        ('log_stats', '--log-stats %s'),

        # Link options
        ('link_at_most_once', '--link-at-most-once'),
        ('link_at_least_once', '--link-at-least-once'),
        ('link_durable', '--link-durable %s'),

        # Connection options
        ('conn_urls', '--conn-urls %s'),
        ('conn_reconnect', '--conn-reconnect %s'),
        ('conn_reconnect_interval', '--conn-reconnect-interval %s'),
        ('conn_reconnect_limit', '--conn-reconnect-limit %s'),
        ('conn_reconnect_timeout', '--conn-reconnect-timeout %s'),
        ('conn_heartbeat', '--conn-heartbeat %s'),
        ('conn_ssl', '--conn-ssl %s'),
        ('conn_ssl_certificate', '--conn-ssl-certificate %s'),
        ('conn_ssl_password', '--conn-ssl-password %s'),
        ('conn_ssl_trust_store', '--conn-ssl-trust-store %s'),
        ('conn_ssl_verify_peer', '--conn-ssl-verify-peer %s'),
        ('conn_ssl_verify-peer-name', '--conn-ssl-verify-peer-name %s'),
        ('conn_web_socket', '--conn-web-socket %s'),
        ('conn_max_frame_size', '--conn-max-frame-size %s'),

    ])

    def __init__(self, node: Node):
        """
        Method for init receiver.
        """
        amom.client.Receiver.__init__(self)
        Client.__init__(self, node)
