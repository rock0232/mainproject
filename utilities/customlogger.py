import logging

class Logger:
    @staticmethod
    def logen():
        logging.basicConfig(filename="..//Logs//automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', force=True, level=logging.INFO)
        logger = logging.getLogger()
        return logger
