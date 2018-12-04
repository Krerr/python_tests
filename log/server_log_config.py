import logging
from logging.handlers import RotatingFileHandler
import __main__ as main

log = logging.getLogger("app.server")
log.setLevel(logging.DEBUG)

_format = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(name)s - %(message)s")

fh = RotatingFileHandler("log/server.log", maxBytes=20000, backupCount=10)
fh.setFormatter(_format)

log.addHandler(fh)
