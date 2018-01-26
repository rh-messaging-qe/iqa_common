from autologging import logged, traced
from odict import odict

import amom.client
from .client import Client


@logged
@traced
class Sender(Client, amom.client.Sender):
    """
    External Python-Proton sender client
    """
    # client is installed from cli-rhea, node_app is there only for backward compability
    cli_command = odict([('python', 'cli-proton-python-sender')])
    # Client-sender params for build execute command
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
        ('conn_ssl_certificate', '--conn-ssl-certificate %s'),
        ('conn_ssl_private_key', '--conn-ssl-private-key %s'),
        ('conn_ssl_password', '--conn-ssl-password %s'),
        ('conn_ssl_trust_store', '--conn-ssl-trust-store %s'),
        ('conn_ssl_verify_peer', '--conn-ssl-verify-peer'),
        ('conn_ssl_verify_peer_name', '--conn-ssl-verify-peer-name'),
        ('conn_handler', '--conn-handler %s'),
        ('conn_max_frame_size', '--conn-max-frame-size %s'),

        # Link options
        ('link_durable', '--link-durable'),
        ('link_at_least_once', '--link-at-least-once'),
        ('link_at_most_once', '--link-at-most-once'),

        # Message options
        ('msg_id', '--msg-id %s'),
        ('msg_subject', '--msg-subject %s'),
        ('msg_reply_to', '--msg-reply-to %s'),
        ('msg_durable', '--msg-durable %s'),
        ('msg_ttl', '--msg-ttl %s'),
        ('msg_priority', '--msg-priority %s'),
        ('msg_correlation_id', '--msg-correlation-id %s'),
        ('msg_user_id', '--msg-user-id %s'),
        ('msg_group-id', '--msg-group-id %s'),
        ('msg_property', '--msg-property %s'),
        ('msg_content_map_item', '--msg-content-map-item %s'),
        ('msg_content_list_item', '--msg-content-list-item %s'),
        ('msg_content_from_file', '--msg-content-from-file %s'),
        ('msg_content', '--msg-content %s'),
        ('msg_content_type', '--msg-content-type %s'),
        ('content_type', '--content-type %s'),

        # Reactor options
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
        Methd for init Python sender.
        """
        amom.client.Sender.__init__(self)
        Client.__init__(self)

    def _send_message(self, **kwargs):
        """
        Method for send message.
        :return:
        """
        self._set_attr_values(kwargs)
        cmd = self._build_sender_command()
        self._execute(cmd)
