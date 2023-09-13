import threading

from pypulse.Aplication import Vars
from pypulse.Socket import run_socket

from .browser import Browser


class LoadBrowser():
    def __init__(self, title: str = 'PyPulse App', debug: bool = True, debug_file_name: str = 'debug.log', window_size_x: int = 1270, window_size_y: int = 720, icon_path: str = None) -> None:

        ts = threading.Thread(target=run_socket)
        ts.start()

        t = threading.Thread(target=Browser, args=(
            title, debug, debug_file_name, window_size_x, window_size_y, icon_path))
        t.start()

        ts.join()
        t.join()

        while (not Browser.instance):
            pass

    @staticmethod
    def go_to_path(path: str):
        if Browser.instance:
            Browser.instance.GetMainFrame().LoadUrl(
                f'http://127.0.0.1:{Vars.INTERNAL_HTTP_SERVER_PORT}/{path}')
