"""
This is a sample python package.
"""

import sys
import importlib.metadata
import argparse

from python_package.logger_module.logger import Logger
from python_package.sub_module_1.some_class import SomeClass
from python_package.sub_module_2.some_module import some_function


# Constants
PACKAGE_NAME: str = "python_package"

# Get the loggers used in main
logger = Logger()
default_logger = logger.get_logger()
application_logger = logger.get_logger("application")


def welcome_text() -> str:
    """
    Returns welcome text.

    Args:
        None

    Returns:
        str: The welcome text
    """

    return "Welcome to the python_package template"


def square(some_number: int) -> int:
    """
    This functions takes an input and returns its square.

    Args:
        some_number (int): The number to be squared

    Returns:
        int: The square of the number
    """

    return some_number * some_number


def main() -> None:
    """
    When main is executed, we will instantiate a class from
    sub module 1 and call a method from it. Then call a function
    from sub module 2.

    Args:
        None

    Returns:
        None
    """

    # Create an arg parser so we can pass arguments to the package
    parser = argparse.ArgumentParser(description=PACKAGE_NAME)


    # Add any arguments we want
    parser.add_argument('--version', action='store_true', help='Print the version of the package')
    parser.add_argument('--number', type=int, help='Specify a number to be squared', default=4)
    args = parser.parse_args()


    # Use the args that were parsed to determine actions, or to store any variables that were passed
    if args.version:
        version = importlib.metadata.version(PACKAGE_NAME)
        print(f"Version: {version}")
        return


    # Print the installed package version for easier debugging once installed in the wild
    try:
        version = importlib.metadata.version(PACKAGE_NAME)
        default_logger.info(f"Installed Package Version: {version}")
    except importlib.metadata.PackageNotFoundError as e:
        default_logger.info(f"No package version available for: {e}")


    # Using other functions in this module
    application_logger.info(welcome_text())
    application_logger.info(f"The square of {args.number} is {square(args.number)}")


    # Instantiate the class from our first submodule
    some_class: SomeClass = SomeClass()


    # Use the methods from our sub module 1 SomeClass class
    application_logger.info(some_class.some_method_1())
    application_logger.info(some_class.some_method_2())


    # Use a function from sub module 2
    application_logger.info(some_function())


def signal_handler(sig, frame): # pylint: disable=unused-argument # pragma: no cover
    """
    If a user presses CTRL+C, this will catch it and exit gracefully without an error.
    """

    sys.exit(0)


if __name__ == "__main__": # pragma: no cover
    main()
