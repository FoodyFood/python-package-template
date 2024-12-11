"""
This is another submodule, in this case it's a module with 1 function.
"""

from python_package.logger_module.logger import Logger


# Logger is configured inside the logger module
logger: Logger = Logger()
some_module_logger = logger.get_logger("some_module")


def some_function() -> str:
    """
    This is some function in sub_module_2 
    
    Args:
        None

    Returns:
        str
    """

    some_module_logger.debug("Running some_function")

    return "The some_function Function Says Hello"
