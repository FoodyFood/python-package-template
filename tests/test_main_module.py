"""
This tests functions in the main_module module
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from python_package.main_module import main, welcome_text, square


class TestMainModule(unittest.TestCase):
    """
    Tests the main_module module.
    """

    def test_main(self) -> None:
        """
            Tests the main function.
        """

        self.assertTrue(main() is None)


    def test_welcome_text(self) -> None:
        """
        Tests the welcome_text function.
        """

        self.assertTrue(welcome_text() == "Welcome to the python_package template")


    def test_square(self) -> None:
        """
        Tests the square function.
        """

        self.assertTrue(square(4) == 16)


if __name__ == '__main__':
    unittest.main()
