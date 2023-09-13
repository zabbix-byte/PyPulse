import threading

from pypulse.Aplication import Vars
from pypulse.Socket import run_socket

from .browser import Browser, MainFrame


class LoadBrowser():
    def __init__(self, title: str = 'PyPulse App',
                 debug: bool = True,
                 debug_file_name: str = 'debug.log',
                 window_size_x: int = 1270,
                 window_size_y: int = 720,
                 icon_path: str = None,
                 border_less: bool = False
                 ) -> None:

        server_thread = threading.Thread(target=run_socket)
        server_thread.daemon = True
        server_thread.start()

        Browser(title, debug, debug_file_name, window_size_x, window_size_y, icon_path, border_less)

        while (not MainFrame.instance):
            pass

    @staticmethod
    def go_to_path(path: str):
        if MainFrame.instance:
            MainFrame.instance.GetMainFrame().LoadUrl(
                f'http://127.0.0.1:{Vars.INTERNAL_HTTP_SERVER_PORT}/{path}')
