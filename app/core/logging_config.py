import logging
from logging.handlers import RotatingFileHandler

LOG_FORMAT = "%(levelprefix)s %(asctime)s %(message)s"
LOG_LEVEL = logging.INFO

logger = logging.getLogger("fastapi-connector")
logger.setLevel(LOG_LEVEL)

handler = RotatingFileHandler("app.log", maxBytes=10**6, backupCount=3)
formatter = logging.Formatter(LOG_FORMAT)
handler.setFormatter(formatter)
logger.addHandler(handler)
