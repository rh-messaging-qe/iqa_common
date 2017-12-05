from autologging import logged, traced
from odict import odict

import amom.client
from .client import Client


@logged
@traced
class Sender(Client, amom.client.Sender):
    """
    External NodeJS sender client
    """

    # client is installed from cli-rhea, node_app is there only for backward compability
    cli_command = odict([('nodejs', 'cli-rhea-sender')])
    # Client-sender params for build execute command
    cli_params_transformation = odict([
        ('help', '--help'),
        ('timeout', '--timeout %s'),
        ('close_sleep', '--close-sleep %s'),

        ('broker_url', '--broker %s'),
        ('transport', None),  # TODO Proc je tu None?
        ('host', None),
        ('port', None),
        ('username', None),
        ('password', None),
        ('address', '--address %s'),

        ('log_msgs', '--log-msgs %s'),
        ('log_lib', '--log-lib %s'),
        ('log_stats', '--log-stats %s'),

        ('msg_cnt', '--count %s'),
        ('msg_id', '--msg-id %s'),
        ('msg_subject', '--msg-subject "%s"'),
        ('msg_reply_to', '--msg-reply-to "%s"'),
        ('msg_property', "--msg-property"),
        ('msg_content_list', "--msg-content-list-item"),
        ('msg_content_map', "--msg-content-map-item"),
        ('msg_content', '--msg-content "%s"'),
        ('msg_content_from_file', '--msg-content-from-file'),
        ('msg_durable', '--msg-durable %s'),
        ('msg_ttl', '--msg-ttl %s'),
        ('msg_correlation_id', '--msg-correlation-id %s'),
        ('msg_user_id', '--msg-user-id %s'),
        ('msg_priority', '--msg-priority %s'),
        ('msg_group_id', '--msg-group-id %s'),
        ('msg_group_seq', '--msg-group-seq %s'),
        ('msg_reply_to_group_id', '--msg-reply-to-group-id %s'),

        ('anonymous', '--anonymous'),

        ('duration', '--duration %s'),
        ('duration_mode', '--duration-mode %s'),

        ('conn_urls', '--conn-urls %s'),
        ('conn_reconnect', '--conn-reconnect %s'),
        ('conn_heartbeat', '--conn-heartbeat %s'),
        ('conn_ssl_domain', '--conn-ssl-domain %s'),
        ('conn_max_frame_size', '--conn-max-frame-size %s'),

        ('auto_settle_off', '--reactor-auto-settle-off'),
        ('capacity', '--capacity %s')
    ])

    def __init__(self):
        """

        """
        amom.client.Sender.__init__(self)
        Client.__init__(self)



    def _send_message(self):
        """

        :return:
        """
        cmd = self._build_sender_command()
        self._execute(cmd)
