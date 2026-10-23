import logging

logging.basicConfig(
    level=logging.WARNING,
    format="%(levelname)s - %(message)s"
)

logging.debug("Checking debug")
logging.info("Checking info")
logging.warning("Checking warning")
logging.error("Checking error")
logging.critical("Checking critical")

try:
    result = 10 / 0
except ZeroDivisionError:
    logging.exception("Calculation failed")