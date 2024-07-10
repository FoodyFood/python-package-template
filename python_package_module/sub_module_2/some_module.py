'''
    This is another submodule, in this case it's a module with 1 function.
'''

from python_package_module.logger_module.logger import Logger


# Get the Logger instance, then get the log streams we need in this module
logger: Logger = Logger(name="python_package")
application_logger = logger.get_logger("application")


def some_function() -> str:
    '''
        This is some function in sub_module_2 
        
        Args:
            None

        Returns:
            str
    '''

    application_logger.debug("Running some_function")

    return "The some_function Function Says Hello"
