import pytest
import sys
import logging

from typing import Optional

from plum.jobs.base_job import BaseJob

class LoopJob(BaseJob):

    def __init__(self, name: str, logger: logging.Logger):
        super().__init__(
            name = name,
            logger = logger
        )

    def _process(self) -> Optional[Exception]:
        sum: int = 0
        while sum < 100000000:
            sum = sum + 1

def test_logging():

    sysout_handler = logging.StreamHandler(sys.stdout)
    sysout_handler.setLevel(logging.DEBUG)
    sysout_handler.setFormatter(
        logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    )
    logger = logging.Logger(name = "Test_Logger")
    logger.addHandler(sysout_handler)

    job = LoopJob(
        name = "Test_Job",
        logger = logger
    )
    job.execute()
    assert True