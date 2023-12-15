import threading

from pypulse.Socket import run_socket

from .app import App


class LoadBrowser:
    def __init__(*args, **kwargs) -> None:
        server_thread = threading.Thread(target=run_socket)
        server_thread.daemon = True
        server_thread.start()

        App(**kwargs)
