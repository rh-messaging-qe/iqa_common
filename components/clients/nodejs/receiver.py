from autologging import logged, traced
from odict import odict

import amom.client
from .client import Client


@logged
@traced
class Receiver(Client, amom.client.Receiver):
    """
    External NodeJS receiver client
    """
    # client is installed from cli-rhea
    cli_command = odict([('nodejs', 'cli-rhea-receiver')])

    cli_params_transformation = odict([
        ('help', '--help'),
        ('timeout', '--timeout %s'),
        ('close_sleep', '--close-sleep %s'),

        ('broker_url',  '--broker %s'),
        ('transport', None),
        ('host', None),
        ('port', None),
        ('username', None),
        ('password', None),
        ('address', '--address "%s"'),

        ('log_msgs', '--log-msgs %s'),
        ('log_lib', '--log-lib %s'),
        ('log_stats', '--log-stats %s'),

        ('msg_cnt', '--count %s'),
        ('msg_accept', '--action %s'),
        ('recv_msg_selector', '--recv-selector "%s"'),

        ('duration', '--duration %s'),
        ('duration_mode', '--duration-mode %s'),

        ('conn_urls', '--conn-urls %s'),
        ('conn_reconnect', '--conn-reconnect %s'),
        ('conn_heartbeat', '--conn-heartbeat %s'),
        ('conn_ssl_domain', '--conn-ssl-domain %s'),
        ('conn_max_frame_size', '--conn-max-frame-size %s'),

        ('at_most_once', '--link-at-most-once'),
        ('at_least_once', '--link-at-least-once'),
        ('recv_listen', '--recv-listen %s'),
        ('recv_listen_port', '--recv-listen-port %s'),

        ('process_reply_to', '--process-reply-to'),
        ('selector', '--recv-selector %s'),
        ('recv_browse', '--recv-browse'),

        ('capacity', '--capacity %s')
    ])

    def __init__(self):
        amom.client.Receiver.__init__(self)
        Client.__init__(self)
