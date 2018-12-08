from functools import wraps
import logging

log = logging.getLogger("app.funcLogger")
log.setLevel(logging.DEBUG)

_format = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(name)s - %(message)s")

fh = logging.FileHandler("log/func.log", encoding="utf-8")
fh.setFormatter(_format)

log.addHandler(fh)

def log_decorator(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        log.info("Вызов %s: с аргументами %s, %s\n" % (func.__name__, args, kwargs))
        return func(*args, **kwargs)
    return decorator