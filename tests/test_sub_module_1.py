"""
This tests class methods in the sub_module_1 module
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from python_package.sub_module_1.some_class import SomeClass


class TestSubModule1(unittest.TestCase):
    """
    Tests the sub_module_1 module.
    """

    def test_some_method_1(self) -> None:
        """
        Tests the SomeClass Methods.
        """

        some_class: SomeClass = SomeClass()

        self.assertTrue(some_class.some_method_1() == "The some_method_1 Method Says Hello")


    def test_some_method_2(self) -> None:
        """
        Tests the SomeClass Methods.
        """

        some_class: SomeClass = SomeClass()

        self.assertTrue(some_class.some_method_2() == "The some_method_2 Method Says Hello")


if __name__ == '__main__':
    unittest.main()
