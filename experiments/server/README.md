# Server

This is the main host server.  We're wriging this in Python for now, but later
it will move to C++ and run on the game server.  For now we're focused on
the interfaces between the modules and writing the simplest thing that will work
so we're using Python.

* [Wasmer](https://pypi.org/project/wasmer/)
* [Wasmer-Python](https://github.com/wasmerio/wasmer-python/)

## Getting started
```
cd experiments\assembly-script
python -m venv venv
venv\scripts\activate
pip install -r requirements.txt
```