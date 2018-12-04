import logging
import __main__ as main

log = logging.getLogger("app.client")
log.setLevel(logging.DEBUG)

_format = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(name)s - %(message)s")

fh = logging.FileHandler("log/client.log", encoding="utf-8")
fh.setFormatter(_format)

log.addHandler(fh)
