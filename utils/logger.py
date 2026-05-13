import logging


logging.basicConfig(
    filename="logs/test_logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def log_message(message):

    logging.info(message)