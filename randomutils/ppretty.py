"""
pPretty - Pretty Pretty String Formatter.
Formats most common-used string forms, decorations, etc. to the expected pretty form.
"""


def pformat(string: str, decorator: str, count=1):  # pformat("{text} {and} {something}", '[]', 2) gives
    # "[{text}] [{and}] {something}"
    match decorator:
        case '(' | ')' | '()':
            string = string.replace('{', '({', count).replace('}', '})', count)
        case '[' | ']' | '[]':
            string = string.replace('{', '[{', count).replace('}', '}]', count)
        case '<' | '>' | '<>':
            string = string.replace('{', '<{', count).replace('}', '}>', count)
        case _:
            string = (string.replace('{', f'{decorator}{{', count).replace('}', f'}}{decorator}', count))
    return string


def pmodule_name(name: any, decorator=None):  # gives "Module Name: {text} where "Module Name" can be decorated
    __module_name_str = name.split('.')[-1].removeprefix('__').removesuffix('__').replace('_', ' ').title()
    __preset = "{module_name}: {{text}}"
    __title = decorator if decorator else None
    __module_name_str = pformat(string=__preset, decorator=__title).format(module_name=__module_name_str)
    return __module_name_str


def perror(module_name, error):  # gives "[Module Name]: ERROR - error text"
    _err_str = pmodule_name(name=module_name, decorator='[]').format(text=f"ERROR - {error}")
    return _err_str
