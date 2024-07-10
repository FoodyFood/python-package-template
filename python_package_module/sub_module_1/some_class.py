'''
    This is a submodule, in this case it's a class with 1 method.
'''

from python_package_module.logger_module.logger import Logger


# Get the Logger instance, then get the log streams we need in this module
logger: Logger = Logger(name="python_package")
application_logger = logger.get_logger("application")


class SomeClass:
    '''
        This is a class in the sub module.
    '''

    def some_method_1(self) -> str:
        '''
            This is a method in the SomeClass class
            
            Args:
                None

            Returns:
                str
        '''

        application_logger.debug("Running some_method_1")

        return "The some_method_1 Method Says Hello"


    def some_method_2(self) -> str:
        '''
            This is a method in the SomeClass class
            
            Args:
                None

            Returns:
                str
        '''

        application_logger.debug("Running some_method_2")

        return "The some_method_2 Method Says Hello"
