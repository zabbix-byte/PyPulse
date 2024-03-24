from dataclasses import dataclass
from datetime import datetime
from enum import Enum


@dataclass
class Colors:
    RESET = '\033[0m'

    BOLD = '\033[1m'

    BRIGHT_CYAN = '\033[96m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_RED = '\033[91m'
    YELLOW = '\033[1;33m'


class LogTypes(Enum):
    INFO = 'INFO'
    LOADING = 'LOADING'
    SUCCESS = 'SUCCESS'
    WARNING = 'WARNING'
    DEBUG = 'DEBUG'


def log(type: LogTypes, message: str, **settings):
    prefix = f'{Colors.BRIGHT_CYAN}[{datetime.now()}]'

    if type is LogTypes.LOADING:
        prefix += f' {Colors.YELLOW}LOADING  '

    elif type is LogTypes.SUCCESS:
        prefix += f' {Colors.BRIGHT_GREEN}SUCCESS  '

    elif type is LogTypes.INFO:
        prefix += f' {Colors.BRIGHT_BLUE}INFO     '

    elif type is LogTypes.WARNING:
        prefix += f' {Colors.BRIGHT_RED}WARNING  '
    
    elif type is LogTypes.DEBUG:
        prefix += f' {Colors.BOLD}DEBUG    '

    message_color = Colors.RESET

    if isinstance(settings.get('message_color'), Colors):
        message_color = settings.get('message_color')

    print(prefix + f'{message_color}{message} {Colors.RESET}')
