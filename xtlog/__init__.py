""" Custom logging overlay on the python logging
"""
import logging
import config

logger = logging.getLogger(__name__)


def init():
    """ Used to suppress unused import warning
    @return: None
    """
    logger.debug('Logger initialized')
    pass

