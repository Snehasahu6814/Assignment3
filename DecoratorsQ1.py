import logging
from functools import wraps
from datetime import datetime
def log_function_calls(logger_name):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logger = logging.getLogger(logger_name)
            logger.setLevel(logging.INFO)
            log_file = datetime.now().strftime("%Y%m%d") + ".log"
            fh = logging.FileHandler(log_file)
            fh.setLevel(logging.INFO)
            
            # Create formatter and add it to the handler
            formatter = logging.Formatter('%(module)s %(funcName)s %(asctime)s %(message)s')
            fh.setFormatter(formatter)
            
            # Add the handler to the logger
            logger.addHandler(fh)
            logger.info(f"{func.__module__} {func.__name__} {datetime.now().strftime('%d-%m-%y %H:%M:%S')} {args}, {kwargs}")
            return func(*args, **kwargs)
        
        return wrapper
    
    return decorator
 
# Example usage
@log_function_calls("function_logger")
def example_function(x, y):
    return x + y
 
example_function(3, 5)