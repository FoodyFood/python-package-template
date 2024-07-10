'''
    This is a sample python package.
'''

import sys

from python_package_module.logger_module.logger import Logger
from python_package_module.sub_module_1.some_class import SomeClass
from python_package_module.sub_module_2.some_module import some_function


# Create a instance of Logger, then create the log streams we need
logger: Logger = Logger(name="python_package")
default_logger = logger.get_logger()
application_logger = logger.get_logger("application")


def welcome_text() -> str:
    '''
        Returns welcome text.

        Args:
            None

        Returns:
            str: The welcome text
    '''

    return "Welcome to the python_package template"


def square(some_number: int) -> int:
    '''
        This functions takes an input and returns its square.

        Args:
            some_number (int): The number to be squared

        Returns:
            int: The square of the number
    '''

    return some_number * some_number


def main() -> None:
    '''
        When main is executed, we will instanciate a class from
        sub module 1 and call a method from it. Then call a method
        from sub module 2.

        Args:
            None

        Returns:
            None
    '''

    default_logger.info("Python Package Starting")


    # Using other functions in this module
    default_logger.info(welcome_text())
    application_logger.info(f"The square of 4 is {square(4)}")


    # Instanciate the classe from our first submoduule
    some_class: SomeClass = SomeClass()


    # Use the methods from our sub module 1 SomeClass class
    application_logger.info(some_class.some_method_1())
    application_logger.info(some_class.some_method_2())


    # Use a function from sub module 2
    application_logger.info(some_function())


def signal_handler(sig, frame): # pylint: disable=unused-argument # pragma: no cover
    '''
        If a user presses CTRL+C, this will catch it and exit gracefully without an error.
    '''

    sys.exit(0)


if __name__ == "__main__": # pragma: no cover
    main()
