'''
This is a submodule, in this case it's a class with 1 method.
'''

from python_package.logger_module.logger import Logger


class SomeClass:
    '''
    This is a class in the sub module.
    '''

    some_class_logger: Logger

    def __init__(self):
        # Get logger is run as part of instantiation, instead of when the submodule is imported
        logger: Logger = Logger()
        self.some_class_logger = logger.get_logger("some_class")


    def some_method_1(self) -> str:
        '''
        This is a method in the SomeClass class
        
        Args:
            None

        Returns:
            str
        '''

        self.some_class_logger.debug("Running some_method_1")

        return "The some_method_1 Method Says Hello"


    def some_method_2(self) -> str:
        '''
        This is a method in the SomeClass class
        
        Args:
            None

        Returns:
            str
        '''

        self.some_class_logger.debug("Running some_method_2")

        return "The some_method_2 Method Says Hello"
