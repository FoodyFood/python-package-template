'''
This is another submodule, in this case it's a module with 1 function.
'''

from python_package.logger_module.logger import Logger


def some_function() -> str:
    '''
    This is some function in sub_module_2 
    
    Args:
        None

    Returns:
        str
    '''

    logger: Logger = Logger()
    application_logger = logger.get_logger("application")

    application_logger.debug("Running some_function")

    return "The some_function Function Says Hello"
