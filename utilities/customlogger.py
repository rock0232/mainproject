import logging
from pathlib import Path

def get_project_root() -> Path:
    return Path(__file__).parent.parent

class Logger:
    @staticmethod
    def logen():
        path = get_project_root()
        logging.basicConfig(filename=f'{path}/Logs//automation.log',
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', force=True, level=logging.INFO)
        logger = logging.getLogger()
        return logger

inpl = 1
for j in range(0,inpl):
    if j == inpl:
        print("helo")