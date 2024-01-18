"""
Import It (Modules)!
Tries to replicate a case of dynamically importing modules from given lists or tuples. Python 3.1+
If wanted in direct modules as like usual imported ones, please use similar to those lines:
(warning: NoQA! Highly NOT recommended!)
# locals().update(import_it(('modules', 'here')))
"""

# IMPORTS
from .types_converter import force_to_tuple
from .ppretty import perror, pmodule_name
from importlib import import_module  # Invented in Python 3.1
try:  # importlib find module handler
    from importlib import util as _find_module
    _find_module = _find_module.find_spec
except ImportError:  # Python 3.3 or less
    try:
        from importlib import find_loader as _find_module
    except ImportError as _ie_main:  # never usually achievable, but if so, throw an error
        def _find_module(*args): return
        print(perror(module_name=__name__, error=_ie_main))


# MAIN
def check_availability(name: any, tuplify=False) -> bool | tuple | dict:
    name, _output = force_to_tuple(name), {} if not tuplify else ()
    if tuplify:
        _output = tuple(True if _find_module(_mod) else False for _mod in name)
        _output = _output if len(name) > 1 else _output[0]
    else:
        for _mod in name:
            _output[_mod] = True if _find_module(_mod) else False
    return _output


def import_it(check: tuple or list, output_full: bool = False, return_status: bool = False) -> dict:
    check, _output, _success, _failed = force_to_tuple(check), {}, [], {}
    def __dot_split_last(var: str) -> str: return force_to_tuple(var, split='.')[-1]  # 'randomutils.ptime' -> 'ptime'
    # MAIN + output_full handle
    for _mod in check:
        try:
            if output_full:  #
                _output[_mod] = import_module(_mod)
                _success.append(_mod)
            else:
                _output[__dot_split_last(_mod)] = import_module(_mod)
                _success.append(f"{_mod} as {__dot_split_last(_mod)}" if len(_mod.split('.')) > 1 else _mod)
        except ImportError as _ie:
            _failed[_mod] = _ie
    # return_status handle
    if return_status:
        _prefix = pmodule_name(name=__name__, decorator='[]').format(text='Importing {stat}')
        _success = _prefix.format(stat=f"Successful: {' & '.join(_e for _e in _success)}")
        _failed = _prefix.format(stat=f"Failed: " + ' & '.join(f'{__dot_split_last(_m)} - {_r}' for _m, _r in _failed.items())) if _failed.keys() else None
        _final_status = f'{_success}\n{_failed}' if _failed else _success
        print(_final_status)
    # output
    return _output
