"""
PPretty - Pretty-Pretty String Formatter
Formats most common-used string forms, decorations, etc. to the expected pretty form
Read more about formatting in Python 3:
https://docs.python.org/3/tutorial/inputoutput.html#fancier-output-formatting
"""


def pformat(string: str, decorator: str, count: int = 1) -> str:
    # pformat("{text} {and} {something}", '[]', count=2) -> "[{text}] [{and}] {something}"
    match decorator:
        case '(' | ')' | '()':
            _output = string.replace('{', '({', count).replace('}', '})', count)
        case '[' | ']' | '[]':
            _output = string.replace('{', '[{', count).replace('}', '}]', count)
        case '<' | '>' | '<>':
            _output = string.replace('{', '<{', count).replace('}', '}>', count)
        case _:
            _output = (string.replace('{', f'{decorator}{{', count).replace('}', f'}}{decorator}', count))
    return _output


def pmodule_name(name: any, decorator=None) -> str:  # gives "Module Name: {text}" where Module Name can be decorated
    _module_name_str = name.split('.')[-1].removeprefix('__').removesuffix('__').replace('_', ' ').title()
    _preset = "{module_name}: {{text}}"
    _title = decorator if decorator else ''
    _output = pformat(string=_preset, decorator=_title).format(module_name=_module_name_str)
    return _output


def perror(module_name: str, error: any) -> str:  # gives "[Module Name]: ERROR - {error}" where error is custom text
    _output = pmodule_name(name=module_name, decorator='[]').format(text=f"ERROR - {error}")
    return _output
