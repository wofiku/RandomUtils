"""
isexist - module to check if paths and files exists, if no, module contain functions to create it
Usage:
# to_path(path='./test_path') -> *creates path* -> 'Path "./test_path" has been created'
"""


# IMPORTS
from os import makedirs
from os.path import exists, isfile
from .ppretty import perror


# MAIN
# Checks
def is_path(path: str) -> bool: return exists(path)
def is_file(file_path: str) -> bool: return isfile(file_path)


# Creators
def to_path(path: str, print_output: bool = False) -> str:  # creates path if it doesn't exist
    try:
        _output = f"Path \"{path}\" "
        _output += ("have been created", makedirs(path))[0] if not is_path(path) else "already exists"
    except Exception as _err:
        _output = perror(module_name=__name__, error=_err)
    print(_output) if print_output else None
    return _output


def to_file(file_path: str, print_output: bool = False) -> str:  # creates file (with path) if it doesn't exist
    _output = f"File {file_path} "
    try:
        with open(file_path, 'x') as _f:
            _output += "has been created"
    except FileExistsError:
        _output += "already exists"
    except Exception as _err:
        _output = perror(module_name=__name__, error=_err)
    print(_output) if print_output else None
    return _output
