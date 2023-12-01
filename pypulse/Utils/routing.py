def repl(string: str,
         character: str,
         index: int,
         condition: bool = None) -> str:

    if condition != None and not condition:
        return string

    string = list(string)
    string[index] = character
    string = ''.join(string)

    return string


def variable_info(text: str):
    text = repl(text, '', 0)
    text = repl(text, '', -1)

    type, name = text.split(':')
    return type, name


def is_variable(text: str):
    if not text.startswith('<') or not text.endswith('>'):
        return False

    text = repl(text, '', 0)
    text = repl(text, '', -1)

    text = text.split(':')
    if len(text) != 2:
        raise ValueError('You tried to add more than one argument or none.')

    return True
