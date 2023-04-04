import logging


def test_logging():
    logger = logging.getLogger(__name__)
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    filehandler = logging.FileHandler('logfile.log')
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)
    logger.setLevel(logging.INFO)
    logger.debug("this is debug")
    logger.info("this is info")
    logger.error("this is error")
    logger.warning("this is warning")
    logger.critical("this is critical")
