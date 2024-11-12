import logging
from datetime import datetime

logging.basicConfig(filename="summation.log", level=logging.debug, filemode="a")


def summation(a: float, b: float) -> float:
    logging.debug(f"{a} and {b} - {datetime.now()}")
    result: float = a + b
    logging.debug(f"Result: {result} - {datetime.now()}")
    print(result)
    return result


summation(1.5, 3.5)
