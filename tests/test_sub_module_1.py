'''
    This tests class methods in the sub_module_1 module
'''

from python_package.sub_module_1.some_class import SomeClass


def test_some_method() -> None:
    '''
        Tests the SomeClass Methods.
    '''

    some_class: SomeClass = SomeClass()

    assert some_class.some_method() == "The some_method Method Says Hello"
