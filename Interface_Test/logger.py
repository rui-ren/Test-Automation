import json, logging

logger = logging.getLogger('test')
logger.setLevel(logging.DEBUG)

# Set the logging file format
fmt = logging.Formatter('[%(filename)-6s]: [%(levelname)-6s] [%(asctime)s]: %(message)s')
stream_hdl = logging.StreamHandler()
stream_hdl.setFormatter(fmt)
stream_hdl.setLevel(logging.DEBUG)
logger.addHandler(stream_hdl)


if __name__ == "__main__":
    logger.info("this is info")

