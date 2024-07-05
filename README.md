# Python Library Template

This doesn't do much on it's own, it's a reference for myself for future for how to build a python package.
<br>

## Description

Once you build this, it will create a dist folder containing a whl that you can install.

If you pip install the whl file you can run `python_package` from your terminal and see the output.


## Development Environment Setup (Optional)

As a developer you will need to be able to run the build command in the [Makefile](./makefile). This command will build a whl file that can be distributed and installed using pip.

Bash:
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Windows:
```
python -m venv .venv
source .\.venv\scripts\activate
pip install -r requirements.txt
```

## Building The WHL File

To build the wheel you can either do it manually by using these commands, or if you have `make` innstalled you can just `make build`.

```bash
rm -rf build *.egg-info
python3 setup.py sdist bdist_wheel
```

## Tests

Running `pytest` from the root directory of this repository will run PyTest which will test the main module as well as the sub modules.


