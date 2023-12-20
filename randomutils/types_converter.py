"""
Python Types Converter.
This script converts tries to convert any variable to the called one.
Including function presets as per as to the basic Built-in types.
For more info about the basic types, please refer to the official Python 3 documentation:
https://docs.python.org/3/library/stdtypes.html
"""

# IMPORT
from .ppretty import perror as _perror


# MAIN
# Template. Custom types included!
def template(anything: any, to_type: type):
    try:
        output = anything if isinstance(anything, to_type) else to_type(anything)
    except Exception as _err:
        print(_perror(module_name=__name__, error=_err))
        output = anything
    return output


# Basic Python 3 types
# Numeric
def to_int(var: any):
    output = template(anything=var, to_type=int)
    return output


def to_float(var: any):
    output = template(anything=var, to_type=float)
    return output


def to_complex(var: any):
    output = template(anything=var, to_type=complex)
    return output


# Boolean
def to_bool(var: any):
    output = template(anything=var, to_type=bool)
    return output


# Sequence
def to_list(var: any):
    output = template(anything=var, to_type=list)
    return output


def to_tuple(var: any):
    output = template(anything=var, to_type=tuple)
    return output


def to_range(var: any):
    output = template(anything=var, to_type=range)
    return output


# Text Sequence
def to_str(var: any):
    output = template(anything=var, to_type=str)
    return output


# Binary Sequence
def to_bytes(var: any):
    output = template(anything=var, to_type=bytes)
    return output


def to_bytearray(var: any):
    output = template(anything=var, to_type=bytearray)
    return output


def to_memoryview(var: any):
    output = template(anything=var, to_type=memoryview)
    return output


# Set
def to_set(var: any):
    output = template(anything=var, to_type=set)
    return output


def to_frozenset(var: any):
    output = template(anything=var, to_type=frozenset)
    return output


# Mapping
def to_dict(var: any):
    output = template(anything=var, to_type=dict)
    return output
