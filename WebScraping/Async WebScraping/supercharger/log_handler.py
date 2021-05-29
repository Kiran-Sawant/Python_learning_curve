import logging as log
import structlog

def set_arsenic_log_level(level=log.WARNING):
    # Create logger
    logger = log.getLogger('arsenic')

    def logger_factory():
        return logger

    structlog.configure(logger_factory=logger_factory)
    logger.setLevel(level)

