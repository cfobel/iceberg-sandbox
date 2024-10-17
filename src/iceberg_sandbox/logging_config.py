import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def log_example():
    logger.info("🔍 This is a log message with an emoji prefix")
