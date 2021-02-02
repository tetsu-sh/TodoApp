import logging


def get_logger(logger):
    LOG_FORMAT = (
        "time:%(asctime)s "
        + "level:[%(levelname)s] "
        + "thread:%(thread)d "
        + "name:%(name)s "
        + "funcName:%(funcName)s "
        + "lineno:%(lineno)d "
        + "message:%(message)s"
    )
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter(LOG_FORMAT))
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger