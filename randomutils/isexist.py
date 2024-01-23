"""IsExist - module to check if paths and files exists and, if not, create it

Usage:
# to_path(path='./test_path') -> *creates path* -> 'Path "./test_path" has been created'
"""


# IMPORTS
from os import makedirs
from os.path import exists, isfile
from .ppretty import perror


# ACCESSIBLE
# Make functions in the module accessible
__all__ = ['is_path', 'is_file', 'to_path', 'to_file']


# MAIN
# Checks
def is_path(path: str) -> bool: return exists(path)
def is_file(file_path: str) -> bool: return isfile(file_path)


# Creators
def to_path(path: str, print_output: bool = False) -> str:
    """Creates the path if it doesn't exist
Returns results of the operation, forcefully prints output if print_output set to True

Usage example:
>>> to_path(path='test', print_output=True)
# is equivalent to
>>> aaa = to_path(path='test')
>>> print(aaa)
Output example:
Path "test" has been created
"""

    # VARS
    _output = f"Path \"{path}\" "

    # MAIN
    try:
        _output += ("has been created", makedirs(path))[0] if not is_path(path) else "already exists"
    except Exception as _err:
        _output += f'- {perror(module_name=__name__, error=_err)}'

    # OUTPUT
    print(_output) if print_output else None
    return _output


def to_file(file_path: str, print_output: bool = False) -> str:
    """Creates the file (with its path) if it doesn't exist
Returns results of the operation, forcefully prints output if print_output set to True
Usage example:
>>> to_file(path='test.txt', print_output=True)
# is equivalent to
>>> bbb = to_file(path='test.txt')
>>> print(bbb)
Output example:
File "test.txt" has been created
"""

    # VARS
    _output = f"File \"{file_path}\" "
    try:
        with open(file_path, 'x') as _f:
            _output += "has been created"
    except FileExistsError:
        _output += "already exists"
    except Exception as _err:
        _output += f'- {perror(module_name=__name__, error=_err)}'

    # OUTPUT
    print(_output) if print_output else None
    return _output
