import logging

logger = logging.getLogger(__name__)


def log(msg):
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('[%(levelname)-4s] %(message)s')
    ch.setFormatter(formatter)

    if logger.hasHandlers():
        logger.handlers.clear()

    logger.addHandler(ch)
    return logger.info(msg)
