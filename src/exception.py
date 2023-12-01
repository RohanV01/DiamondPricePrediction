import sys
from logger import logging  # Assuming logger.py and exception.py are in the same directory

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail
    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = "Error occurred in python script [{0}] line no [{1}] error message[{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message


class CustomException(Exception):

    def __init__(self, error, error_detail: sys):
        super().__init__(error_message_detail(error, error_detail=error_detail))
        self.error_message = error_message_detail(error, error_detail=error_detail)

    def __str__(self):
        return self.error_message


if __name__ == "__main__":
    logging.info("Logging has started")

    try:
        a = 1 / 0
    except Exception as e:
        logging.error("Division by zero")
        raise CustomException(e, sys.exc_info())
