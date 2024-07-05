'''
    This tests class methods in the sub_module_1 module
'''

from python_package_module.sub_module_1.some_class import SomeClass


def test_some_method_1() -> None:
    '''
        Tests the SomeClass Methods.
    '''

    some_class: SomeClass = SomeClass()

    assert some_class.some_method_1() == "The some_method_1 Method Says Hello"


def test_some_method_2() -> None:
    '''
        Tests the SomeClass Methods.
    '''

    some_class: SomeClass = SomeClass()

    assert some_class.some_method_2() == "The some_method_2 Method Says Hello"
