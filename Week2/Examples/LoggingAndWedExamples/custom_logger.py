import logging

#default logging level was WARNING before set to DEBUG
logging.basicConfig(filename='app.log', filemode="a",\
    format="%(process)d - %(asctime)s - %(name)s - %(message)s", \
        datefmt= "%d-%b-%y %H:%M:%S",level = logging.DEBUG)
logger = logging.getLogger("customLogger")
logger.warning("this is a warning")
logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")        # ← you're already using this
logger.error("Error message")
logger.critical("Critical message")

