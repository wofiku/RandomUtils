"""PPretty - Pretty-Pretty String Formatter
Formats most common-used string forms, decorations, etc. to the expected pretty form
Read more about formatting in Python 3:
https://docs.python.org/3/tutorial/inputoutput.html#fancier-output-formatting
"""


# ACCESSIBLE
# Make functions in the module accessible
__all__ = ['pformat', 'pmodule_name', 'perror']


# MAIN
def pformat(string: str, decorator: str, count: int = 1, remove_original_brackets: bool = False) -> str:
    """Pretty Format - adds brackets to your not formatted text for further formatting

Usage example:
>>> pformat("{text} {and} {something} else", '[]')
[{text}] {and} {something} else
"""

    # MAIN
    match decorator:
        case '(' | ')' | '()':
            _output = string.replace('{', '({', count).replace('}', '})', count)
        case '[' | ']' | '[]':
            _output = string.replace('{', '[{', count).replace('}', '}]', count)
        case '<' | '>' | '<>':
            _output = string.replace('{', '<{', count).replace('}', '}>', count)
        case _:
            _output = (string.replace('{', f'{decorator}{{', count).replace('}', f'}}{decorator}', count))

    # OUTPUT with remove_original_brackets HANDLER
    return _output.replace('{', '', count).replace('}', '', count) if remove_original_brackets else _output


def pmodule_name(name: any, decorator: str = None, remove_underscores: bool = True, make_title: bool = True) -> str:
    """Module name string from module name - returns "<Module Name>: {text}", where <module name> \
can be decorated

Usage example:
>>> pmodule_name(name=__name__, decorator='[').format(text='Hello there')
[Main]: Hello there
"""

    # VARS
    _preset = "{module_name}: {{text}}"
    name = name.split('.')[-1]
    name = name.removeprefix('__').removesuffix('__').replace('_', ' ') if remove_underscores else name
    name = name.title() if make_title else name

    # MAIN
    _output = pformat(string=_preset, decorator=decorator or '').format(module_name=name)

    # OUTPUT
    return _output


def perror(module_name: str, error: any) -> str:
    """ Returns error string in a "[<Module Name>]: ERROR - {error}" variation, where {error} is custom formattable text

Usage example:
>>> print(perror(module_name=__name__, error='test text'))
[Main]: ERROR - test text
"""

    # MAIN
    _output = pmodule_name(name=module_name, decorator='[]').format(text=f"ERROR - {error}")

    # OUTPUT
    return _output
