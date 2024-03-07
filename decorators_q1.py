"""import logger"""
import logging
from functools import wraps
import datetime
def log_function_call(log):
    """use logger to log the file"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            log.info(f"{func.__module__} {func.__name__} {current_time} {kwargs}")
            return func(*args, **kwargs)
        return wrapper
    return decorator
# Configure logging
log_filename = f"{__name__}_{datetime.datetime.now().strftime('%Y%m%d')}.log"
logging.basicConfig(filename=log_filename, level=logging.INFO)
# Create logger
logger=logging.getLogger(__name__)
# Example usage
@log_function_call(logger)
def example_function(x,y):
    """ add function"""
    return x + y
example_function(4, 8)
