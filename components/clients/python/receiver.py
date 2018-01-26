from autologging import logged, traced
from odict import odict

import amom.client
from .client import Client


@logged
@traced
class Receiver(Client, amom.client.Receiver):
    """
    External Python-Proton receiver client
    """
    # client is installed from cli-rhea
    cli_command = odict([('python', 'cli-proton-python-receiver')])

    cli_params_transformation = odict([
        ('help', '--help'),
        # Control options
        ('timeout', '--timeout %s'),
        ('close_sleep', '--close-sleep %s'),
        ('broker_url',  '--broker-url %s'),
        ('sync_mode', '--sync-mode %s'),
        ('duration', '--duration %s'),
        ('duration_mode', '--duration-mode %s'),
        ('capacity', '--capacity %s'),
        ('dynamic', '--dynamic'),
        ('msg_cnt', '--count %s'),

        # Logging options
        ('log_lib', '--log-lib %s'),
        ('log_stats', '--log-stats %s'),
        ('log_msgs', '--log-msgs %s'),

        # Transaction options
        ('tx_size', '--tx-size %s'),
        ('tx_action', '--tx-action %s'),
        ('tx_endloop_action', '--tx-endloop-action %s'),

        # Connection options
        ('conn_urls', '--conn-urls %s'),
        ('conn_reconnect', '--conn-reconnect %s'),
        ('conn_reconnect_interval', '--conn-reconnect-interval %s'),
        ('conn_reconnect_limit', '--conn-reconnect-limit %s'),
        ('conn_reconnect_timeout', '--conn-reconnect-timeout %s'),
        ('conn_heartbeat', '--conn-heartbeat %s'),
        ('conn_ssl_domain_certificate', '--conn-ssl-certificate %s'),
        ('conn_ssl_domain_private_key', '--conn-ssl-private-key %s'),
        ('conn_ssl_domain_password', '--conn-ssl-password %s'),
        ('conn_ssl_domain_trust_store', '--conn-ssl-trust-store %s'),
        ('conn_ssl_domain_verify_peer', '--conn-ssl-verify-peer'),
        ('conn_ssl_domain_verify_peer_name', '--conn-ssl-verify-peer-name'),
        ('conn_handler', '--conn-handler %s'),
        ('conn_max_frame_size', '--conn-max-frame-size %s'),

        # Link options
        ('link_durable', '--link-durable'),
        ('link_at_least_once', '--link-at-least-once'),
        ('link_at_most_once', '--link-at-most-once'),
        ('link_dynamic_node_properties', '--link-dynamic-node-properties %s'),

        # Receiver options
        ('process_reply_to', '--process-reply-to'),
        ('action', '--action %s'),
        ('action_size', '--action-size %s'),
        ('recv_selector', '--recv-selector %s'),
        ('recv_browse', '--recv-browse'),
        ('recv_consume', '--recv-consume'),
        ('recv_filter', '--recv-filter %s'),
        ('recv_listen', '--recv-listen %s'),

        # Reactor options
        ('reactor_prefetch', '--reactor-prefetch %s'),
        ('reactor_auto_accept', '--reactor-auto-accept'),
        ('reactor_peer_close_is_error', '--reactor-peer-close-is-error'),
        ('reactor_auto_settle_off', '--reactor-auto-settle-off'),

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
        amom.client.Receiver.__init__(self)
        Client.__init__(self)
