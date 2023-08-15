import logging
from logging.handlers import RotatingFileHandler

from mltd.servers.config import log_level

logger = logging.getLogger()
logger.setLevel(log_level)
handler = RotatingFileHandler('mltd-relive.log', maxBytes=50_000_000,
                              backupCount=3, encoding='utf-8')
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
