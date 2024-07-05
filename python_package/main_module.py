'''
    This is a sample python package.
'''

import sys
from python_package.sub_module_1.some_class import SomeClass
from python_package.sub_module_2.some_module import some_function


def welcome_text() -> str:
    '''
        Returns welcome text.

        Args:
            None

        Returns:
            Str: The welcome text
    '''

    return "Welcome to the python_package template"


def square(some_number: int) -> int:
    '''
        This functions takes an input and returns its square.

        Args:
            int: The number to be squared

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


    # Using other functions in this module
    print(welcome_text())
    print(f"The square of 4 is {square(4)}")


    # Instanciate the classe from our first submoduule
    some_class: SomeClass = SomeClass()


    # Use a method from our sub module 1 SomeClass class
    print(some_class.some_method())


    # Use a function from sub module 2
    print(some_function())


def signal_handler(sig, frame): # pylint: disable=unused-argument
    '''
        If a user presses CTRL+C, this will catch it and exit gracefully without an error.
    '''

    sys.exit(0)


if __name__ == "__main__":
    main()
