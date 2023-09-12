from cefpython3 import cefpython as cef
from .browser import Browser
from pypulse import View
from pypulse import Aplication
from pypulse.Utils import execute_ast_view_request

import threading


class LoadBrowser():
    def __init__(self, title: str = 'PyPulse App', debug: bool = True, debug_file_name: str = 'debug.log', window_size_x: int = 1270, window_size_y: int = 720) -> None:
        t = threading.Thread(target=Browser, args=(
            title, debug, debug_file_name, window_size_x, window_size_y))
        t.start()

        while (not Browser.instance):
            pass

        primary_aplication = Aplication.GetAplication.primary()

        current_view = View.CallView(
            f'{primary_aplication.name}___{primary_aplication.primary_view_name}')
        
        execute_ast_view_request(node_body=current_view.view, request="testequest")

    @staticmethod
    def go_to_html_string(string: str):
        if Browser.instance:
            Browser.instance.GetMainFrame().LoadUrl(f'data:text/html,{str.join(" ", string.splitlines())}')
