"""
Types Converter - convert one type to another
This script converts tries to convert any variable to the called one
Including functions preset according to the basic Built-in types
"""


# IMPORTS
from .ppretty import perror


# ACCESSIBLE
# Functions in the module
__template = ['converter']
__force_to = ['force_to_tuple', 'force_to_list', 'force_to_str', 'force_to_dict', 'force_to_set']
__basic_types_to = ['to_int', 'to_float', 'to_complex', 'to_bool', 'to_list', 'to_tuple', 'to_range', 'to_str',
                    'to_bytes', 'to_bytearray', 'to_memoryview', 'to_set', 'to_frozenset', 'to_dict']
__basic_types_is = ['is_int', 'is_float', 'is_complex', 'is_bool', 'is_list', 'is_tuple', 'is_range', 'is_str',
                    'is_bytes', 'is_bytearray', 'is_memoryview', 'is_set', 'is_frozenset', 'is_dict']
# Make it accessible
__all__ = __template + __force_to + __basic_types_to + __basic_types_is


# MAIN
# Template. Custom types included!
def converter(anything: any, to_type: type) -> any:
    """Tries to convert any type to the expected type "to_type" and returns the result, or outputs inputted type \
in case if conversion wasn't succeeded

Usage example:
>>> some_var = converter(anything='1', to_type=int)
>>> some_var, type(some_var)
1
<class 'int'>
"""

    # MAIN
    try:
        _output = anything if isinstance(anything, to_type) else to_type(anything)
    except Exception as _err:
        print(perror(module_name=__name__, error=_err))
        _output = anything

    # OUTPUT
    return _output


# Forceful convert
def force_to_tuple(var: any, split: str = ' ') -> tuple:
    """Forcefully converts any type "var" variable to tuple

Usage example:
>>> force_to_tuple(var='this, and this string', split=', ')
('this', 'and this string')
"""

    # MAIN
    match var:
        case int() | float():
            _output = tuple(int(_digit) if _digit.isnumeric() else str(_digit) for _digit in str(var))
        case complex():
            _output = tuple((var.real, var.imag))
        case str():  # str (using sep as separator) -> tuple
            _output = tuple(var.split(split))
        case bytes() | bytearray():
            _output = tuple(str(var).removeprefix('b\'').removeprefix('\\x').removesuffix('\'')
                            .replace('\\x', ' ').split(split))  # b'\xd0\xb2' -> ('d0', 'b2')
        case dict():  # dict keys -> tuple
            _output = tuple(var.keys())
        case _:  # anything else -> tuple
            _output = tuple(var)

    # OUTPUT
    return _output


def force_to_list(var: any, split: str = ' ') -> list:
    """Forcefully converts any type "var" variable to list

Usage example:
>>> force_to_list(var='this, and this string', split=', ')
['this', 'and this string']
"""

    # MAIN
    match var:
        case int() | float():
            _output = list(int(_digit) if _digit.isnumeric() else str(_digit) for _digit in str(var))
        case complex():
            _output = list((var.real, var.imag))
        case str():
            _output = var.split(split)
        case bytes() | bytearray():
            _output = list(str(var).removeprefix('b\'').removeprefix('\\x').removesuffix('\'')
                           .replace('\\x', ' ').split(split))  # b'\xd0\xb2' -> ['d0', 'b2']
        case dict():
            _output = list(var.keys())
        case _:
            _output = list(var)

    # OUTPUT
    return _output


def force_to_str(var: any, split: str = ' ') -> str:
    """Forcefully converts any type "var" variable to string

Usage example:
>>> force_to_str(var=['this', 'and this string'], split=', ')
this, and this string
"""

    # MAIN
    match var:
        case complex():  # complex(1, 2) -> '1<split>2'
            _output = f'{var.real}{split}{var.imag}'
        case list() | tuple() | range() | set() | frozenset():
            _output = split.join(var)
        case dict():
            _output = split.join(f'{_k}{split}{_v}' for _k, _v in var.items())
        case _:
            _output = str(var)

    # OUTPUT
    return _output


def force_to_dict(var: any, split: str = ' ') -> dict:
    """Forcefully converts any type "var" variable to dict and filling the keys, but leaving empty None values

Usage example:
>>> force_to_dict(var=['this', 'and this string'], split=', ')
{'this': None, 'and this string': None}
"""

    # VARS
    _output = {}

    # MAIN
    match var:
        case int() | float():
            for _digit in str(var):
                if _digit.isnumeric():
                    _output[(int(_digit))] = None
                else:
                    _output[(str(_digit))] = None
        case complex():
            _output['real'], _output['imag'] = var.real, var.imag
        case list() | tuple() | range() | set() | frozenset():
            for _element in var:
                _output[_element] = None
        case str():
            for _element in var.split(split):
                _output[_element] = None
        case bytes() | bytearray():
            for _element in str(var).removeprefix('b\'').removeprefix('\\x').removesuffix('\'')\
                    .replace('\\x', ' ').split(split):
                _output[_element] = None
        case dict():
            _output = var
        case _:
            _output[var] = None

    # OUTPUT
    return _output


def force_to_set(var: any, split: str = ' ') -> set:
    """Forcefully converts any type "var" variable to set\n
Usage example:
>>> force_to_set(var=['this', 'and this string'], split=', ')
(this, 'and this string')
"""
    # MAIN & OUTPUT
    return set(force_to_dict(var=var, split=split).keys())


# Basic Python 3 types
# For more info about the basic types, please refer to the official Python 3 documentation:
# https://docs.python.org/3/library/stdtypes.html
# 1. Numeric
def to_int(var: any) -> any: return converter(anything=var, to_type=int)
def is_int(var: any) -> bool: return isinstance(var, int)
def to_float(var: any) -> any: return converter(anything=var, to_type=float)
def is_float(var: any) -> bool: return isinstance(var, float)
def to_complex(var: any) -> any: return converter(anything=var, to_type=complex)
def is_complex(var: any) -> bool: return isinstance(var, complex)
# 2. Boolean
def to_bool(var: any) -> any: return converter(anything=var, to_type=bool)
def is_bool(var: any) -> bool: return isinstance(var, bool)
# 3. Sequence
def to_list(var: any) -> any: return converter(anything=var, to_type=list)
def is_list(var: any) -> bool: return isinstance(var, list)
def to_tuple(var: any) -> any: return converter(anything=var, to_type=tuple)
def is_tuple(var: any) -> bool: return isinstance(var, tuple)
def to_range(var: any) -> any: return converter(anything=var, to_type=range)
def is_range(var: any) -> bool: return isinstance(var, range)
# 4. Text Sequence
def to_str(var: any) -> any: return converter(anything=var, to_type=str)
def is_str(var: any) -> bool: return isinstance(var, str)
# 5. Binary Sequence
def to_bytes(var: any) -> any: return converter(anything=var, to_type=bytes)
def is_bytes(var: any) -> bool: return isinstance(var, bytes)
def to_bytearray(var: any) -> any: return converter(anything=var, to_type=bytearray)
def is_bytearray(var: any) -> bool: return isinstance(var, bytearray)
def to_memoryview(var: any) -> any: return converter(anything=var, to_type=memoryview)
def is_memoryview(var: any) -> bool: return isinstance(var, memoryview)
# 6. Set
def to_set(var: any) -> any: return converter(anything=var, to_type=set)
def is_set(var: any) -> bool: return isinstance(var, set)
def to_frozenset(var: any) -> any: return converter(anything=var, to_type=frozenset)
def is_frozenset(var: any) -> bool: return isinstance(var, frozenset)
# 7. Mapping
def to_dict(var: any) -> any: return converter(anything=var, to_type=dict)
def is_dict(var: any) -> bool: return isinstance(var, dict)
