"""Infix with basic presets. Usage:
# 'Hello' | iprint | 'world'
Read more about typing in Python 3: https://docs.python.org/3/library/typing.html
"""


# IMPORTS
# Basic
from typing import Self
from .ppretty import perror
# Math import
from math import copysign, ldexp, log, atan2
try:  # 3.2
    from math import isfinite, expm1, erf, erfc, gamma, lgamma
except ImportError as _ie_math:
    print(perror(module_name=__name__, error=_ie_math))
try:  # 3.5
    from math import gcd, isclose, inf, nan
except ImportError as _ie_math:
    print(perror(module_name=__name__, error=_ie_math))
try:  # 3.6
    from math import tau
except ImportError as _ie_math:
    print(perror(module_name=__name__, error=_ie_math))
try:  # 3.7
    from math import remainder
except ImportError as _ie_math:
    print(perror(module_name=__name__, error=_ie_math))
try:  # 3.8
    from math import isqrt, perm, prod, dist, comb
except ImportError as _ie_math:
    print(perror(module_name=__name__, error=_ie_math))
try:  # 3.9
    from math import lcm, nextafter, ulp
except ImportError as _ie_math:
    print(perror(module_name=__name__, error=_ie_math))
try:  # 3.11
    from math import cbrt, exp2
except ImportError as _ie_math:
    print(perror(module_name=__name__, error=_ie_math))
try:  # 3.12
    from math import sumprod
except ImportError as _ie_math:
    print(perror(module_name=__name__, error=_ie_math))


# ACCESSIBLE
# Functions in the module
__template = ['Infix']
__default_functions = ['iall', 'iany', 'iascii', 'ibreakpoint', 'ibytes', 'icallable', 'idelattr', 'idict',
                       'ienumerate', 'ifilter', 'iformat', 'ifrozenset', 'igetattr', 'ihasattr', 'iint',
                       'iisinstance', 'iissubclass', 'iiter', 'imap', 'inext', 'iopen', 'iprint', 'irange', 'iround',
                       'islice', 'ituple', 'imax', 'imin']
__basic_operators = ['iplus', 'iminus', 'imultiply', 'idivide', 'imod', 'ipower', 'ifloor_divide']
__math = ['icomb', 'icopysign', 'ildexp', 'inextafter', 'iperm', 'iremainder', 'isumprod', 'ilog', 'iatan2', 'idist']
# Make it accessible
__all__ = __template + __default_functions + __basic_operators + __math


# MAIN
# Template
class Infix:  # variable_1 | infix_here | variable_2
    """Template on creating infix class type for further creation of infixes.

Creating a new function:
1. Using lambda (recommended):
>>> infix_print: Infix = Infix(lambda var1, var2: print(var1, var2))
2. Function definition workaround:
>>> @Infix
... def infix_print(var1, var2):
...     Infix(print(var1, var2))

Usage example:
>>> 'Hello' | infix_print | 'world!'
Hello world!
"""

    # MAIN
    def __init__(self, func: callable) -> None:
        self.func = func

    def __ror__(self, other: any) -> Self:
        return Infix(lambda var: self.func(other, var))

    def __or__(self, other: any) -> any:
        return self.func(other)


# Presets
# 1. Default (built-in) functions
# Read more: https://docs.python.org/3/library/functions.html
iall: Infix = Infix(lambda iterable1, iterable2: all((iterable1, iterable2)))
iany: Infix = Infix(lambda iterable1, iterable2: any((iterable1, iterable2)))
iascii: Infix = Infix(lambda obj1, obj2: ascii(''.join(str(_) for _ in (obj1, obj2))))
ibreakpoint: Infix = Infix(lambda *args, **kws: breakpoint(*args, **kws))
ibytes: Infix = Infix(lambda x, y: bytes((int(x), int(y))))
icallable: Infix = Infix(lambda x, y: callable((x, y)))
idelattr: Infix = Infix(lambda obj, name: delattr(obj, name))
idict: Infix = Infix(lambda mapping_n_iterable, **kwarg: dict(mapping_n_iterable, **kwarg))
ienumerate: Infix = Infix(lambda iterable, start=0: enumerate(iterable, start))
ifilter: Infix = Infix(lambda function, iterable: filter(function, iterable))
iformat: Infix = Infix(lambda value, format_spec='': format(value, format_spec))
ifrozenset: Infix = Infix(lambda iterable1=set, iterable2=set: frozenset(iterable1.update(iterable2)))
igetattr: Infix = Infix(lambda obj, name: getattr(obj, name))
ihasattr: Infix = Infix(lambda obj, name: hasattr(obj, name))
iint: Infix = Infix(lambda x, base=10: int(x, base))
iisinstance: Infix = Infix(lambda obj, classinfo: isinstance(obj, classinfo))
iissubclass: Infix = Infix(lambda cls, classinfo: issubclass(cls, classinfo))
iiter: Infix = Infix(lambda obj, sentinel: iter(obj, sentinel))
imap: Infix = Infix(lambda func, iterable: map(func, iterable))
inext: Infix = Infix(lambda iterator, default: next(iterator, default))
iopen: Infix = Infix(lambda file, mode='r': open(file, mode))
iprint: Infix = Infix(lambda var1, var2: print(var1, var2))
irange: Infix = Infix(lambda start, stop: range(start, stop))
iround: Infix = Infix(lambda number, ndigits=None: round(number, ndigits))
islice: Infix = Infix(lambda start, stop: slice(start, stop))
ituple: Infix = Infix(lambda iterable1, iterable2: tuple(iterable1) + tuple(iterable2))
imax: Infix = Infix(lambda arg1, *arg2: max(arg1, *arg2))
imin: Infix = Infix(lambda arg1, *arg2: min(arg1, *arg2))
# 2. Basic operators
# Read more: https://docs.python.org/3/library/operator.html#mapping-operators-to-functions
iplus: Infix = Infix(lambda x, y: x + y)
iminus: Infix = Infix(lambda x, y: x - y)
imultiply: Infix = Infix(lambda x, y: x * y)
idivide: Infix = Infix(lambda x, y: int(x / y) if x / y == x // y else x / y)
imod: Infix = Infix(lambda x, y: x % y)
ipower: Infix = Infix(lambda x, y: x ** y)
ifloor_divide: Infix = Infix(lambda x, y: x // y)
# 3. Math
# Read more: https://docs.python.org/3/library/math.html
icomb: Infix = Infix(lambda x, y: comb(x, y))
icopysign: Infix = Infix(lambda x, y: copysign(x, y))
ildexp: Infix = Infix(lambda x, i: ldexp(x, i))
inextafter: Infix = Infix(lambda x, y: nextafter(x, y))
iperm: Infix = Infix(lambda n, k: perm(n, k))
iremainder: Infix = Infix(lambda x, y: remainder(x, y))
isumprod: Infix = Infix(lambda p, q: sumprod(p, q))
ilog: Infix = Infix(lambda x, base: log(x, base))
iatan2: Infix = Infix(lambda y, x: atan2(y, x))
idist: Infix = Infix(lambda p, q: dist(p, q))
