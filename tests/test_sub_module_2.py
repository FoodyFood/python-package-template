'''
    This tests functions in the sub_module_2 module
'''

from python_package_module.sub_module_2.some_module import some_function


def test_some_function() -> None:
    '''
        Tests some_function.
    '''

    assert some_function() == "The some_function Function Says Hello"
