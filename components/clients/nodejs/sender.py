from autologging import logged, traced
from odict import odict

import amom.client
from components.nodes.node import Node
from .client import Client


@logged
@traced
class Sender(Client, amom.client.Sender):
    """
    External NodeJS sender client
    """
    # client is installed from cli-rhea, node_app is there only for backward compatibility
    cli_command = ['cli-rhea-sender']

    # Client-receiver params for build execute command
    cli_params_transformation = odict([
        ('help', '--help'),
        # Control options
        ('capacity', '--capacity %s'),
        ('reactor_auto_settle_off', '--reactor-auto-settle-off %s'),
        ('anonymous', '--anonymous %s'),
        ('duration', '--duration %s'),
        ('broker_url', '--broker %s'),
        ('broker_address', '--address "%s"'),
        ('msg_cnt', '--count %s'),
        ('close_sleep', '--close-sleep %s'),
        ('timeout', '--timeout %s'),

        # Message options
        ('msg_id', '--msg-id %s'),
        ('msg_subject', '--msg-subject %s'),
        ('msg_reply_to', '--msg-reply-to %s'),
        ('msg_reply_to_group_id', '--msg-reply-to-group-id %s'),
        ('msg_durable', '--msg-durable %s'),
        ('msg_ttl', '--msg-ttl %s'),
        ('msg_priority', '--msg-priority %s'),
        ('msg_correlation_id', '--msg-correlation-id %s'),
        ('msg_user_id', '--msg-user-id %s'),
        ('msg_group-id', '--msg-group-id %s'),
        ('msg_group-seq', '--msg-group-seq %s'),
        ('msg_property', '--msg-property %s'),
        ('property_type', '--property-type %s'),
        ('msg_content_map_item', '--msg-content-map-item %s'),
        ('msg_content_list_item', '--msg-content-list-item %s'),
        ('msg_content_from_file', '--msg-content-from-file %s'),
        ('msg_content', '--msg-content %s'),
        ('msg_anotation', '--msg-anotation %s'),
        ('msg_content_type', '--msg-content-type %s'),
        ('content_type', '--content-type %s'),

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

        # Other options
        ('transport', None),
        ('host', None),
        ('port', None),
        ('username', None),
        ('password', None),
        ('address', None)
    ])

    def __init__(self, node: Node):
        """
        Method for init NodeJS sender.
        """
        amom.client.Sender.__init__(self)
        Client.__init__(self, node)

    def _send_message(self, **kwargs):
        """
        Method for send message.
        :return:
        """
        self._set_attr_values(kwargs)
        cmd = self._build_sender_command()
        self._execute(cmd)
