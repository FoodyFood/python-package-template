"""
This tests functions in the sub_module_2 module
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from python_package.sub_module_2.some_module import some_function


class TestSubModule2(unittest.TestCase):
    """
    Tests the sub_module_2 module.
    """

    def test_some_function(self) -> None:
        """
        Tests some_function.
        """

        self.assertTrue(some_function() == "The some_function Function Says Hello")


if __name__ == '__main__':
    unittest.main()
