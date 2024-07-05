# Define a variable to store the version read from the VERSION file
VERSION := $(shell cat VERSION)

# Build a WHL from our module
.PHONY: build
build:
	rm -rf build *.egg-info
	python3 setup.py sdist bdist_wheel


# Install the WHL we built
install:
	pip3 install ./dist/python_package-${VERSION}-py3-none-any.whl


# Cleanup by uninstalling the WHL
uninstall:
	pip3 uninstall -y python_package


# Time saver
rebuildinstall: build uninstall install