'''
    This is the setup.py for a sample package.
'''

from setuptools import setup, find_packages

# with open('README.md', 'r') as fh:
#     long_description = fh.read()

def read_version() -> str:
    """
        Reads the version that will be applied to the python whl from the VERSION file

        Args:
            None

        Returns:
            str
    """

    with open("VERSION", "r", encoding="utf-8") as version_file:
        return version_file.read().strip()


setup(
    name='python_package',
    version=read_version(),
    author='FoodyFood',
    description='An example python_package',
    # long_description=long_description,
    # long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    python_requires='>=3.9',
    install_requires=[
    ],
    entry_points={
        'console_scripts': [
            'python_package = python_package.main_module:main',
        ],
    },
    # package_data={
    #     'assets': ['assets/*.yaml'],
    # },
)
