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


run:
	export PYTHONPATH="$(PWD):$$PYTHONPATH"; \
	python3 python_package/main_module.py

run-package:
	python_package

lint:
	export PYTHONPATH="$(PWD):$$PYTHONPATH"; \
	pylint ./python_package/

test:
	export PYTHONPATH="$(PWD):$$PYTHONPATH"; \
	pytest

coverage:
	export PYTHONPATH="$(PWD):$$PYTHONPATH"; \
	coverage run -m pytest; coverage report

# Cleanup by uninstalling the WHL
uninstall:
	pip3 uninstall -y python_package


# Time savers
rebuildinstall: build uninstall install
rebuildinstallrun: build uninstall install run