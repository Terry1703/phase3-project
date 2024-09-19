import logging


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_info(message):
    """Log an info message."""
    logging.info(message)
    
def log_debug(message):
    """Log a debug message."""
    logging.debug(message)  
    
def log_warning(message):
    """Log a warning message."""
    logging.warning(message)     
    
def log_exception  (exc) :
    """Log an exception with traceback."""
    logging.exception(exc)
    
def check_variable(name, value):
    """Print the variable name and its value for debugging.""" 
    logging.debug(f"{name} = {value}")

def sanity_check(condition, message):
    """Check a condition and log a message if it's False.""" 
    if not condition:
        logging.warning(f"Sanity check failed: {message}")        