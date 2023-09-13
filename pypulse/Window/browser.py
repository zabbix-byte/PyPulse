import sys
import platform
import ctypes

from cefpython3 import cefpython as cef
from pypulse.Aplication import Vars
from .request_hander import LoadHandler


class Browser():
    instance = None

    def __init__(self, title: str,
                 debug: bool,
                 debug_file_name: str,
                 window_size_x: int,
                 window_size_y: int
                 ) -> None:

        self.title = title
        self.debug = debug
        self.debug_file_name = debug_file_name
        self.window_size_y = window_size_y
        self.window_size_x = window_size_x

        self.check_versions()

        sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error

        settings = {
            'product_version': 'PyPulse/10.00',
            'debug': self.debug,
            'log_severity': cef.LOGSEVERITY_INFO,
            'log_file': self.debug_file_name
        }

        switches = {
            'enable-media-stream': '',
            'disable-gpu': '',
        }

        parent_handle = 0
        window_info = cef.WindowInfo()
        window_info.SetAsChild(
            parent_handle, [0, 0, window_size_y, window_size_x])
        cef.Initialize(settings=settings, switches=switches)
        cef.DpiAware.EnableHighDpiSupport()
        Browser.instance = cef.CreateBrowserSync(url=f'http://127.0.0.1:{Vars.INTERNAL_HTTP_SERVER_PORT}/',
                                                 window_title=self.title, window_info=window_info)

        if platform.system() == "Windows":
            window_handle = Browser.instance.GetOuterWindowHandle()
            insert_after_handle = 0
            # X and Y parameters are ignored by setting the SWP_NOMOVE flag
            SWP_NOMOVE = 0x0002
            # noinspection PyUnresolvedReferences
            ctypes.windll.user32.SetWindowPos(window_handle, insert_after_handle,
                                              0, 0, self.window_size_x, self.window_size_y, SWP_NOMOVE)

        Browser.instance.SetClientHandler(LoadHandler())

        cef.MessageLoop()
        cef.Shutdown()

    def check_versions(self) -> None:
        ver = cef.GetVersion()
        print('[PyPulse] CEF Python {ver}'.format(ver=ver['version']))
        print('[PyPulse] Chromium {ver}'.format(ver=ver['chrome_version']))
        print('[PyPulse] CEF {ver}'.format(ver=ver['cef_version']))
        print('[PyPulse] Python {ver} {arch}'.format(
            ver=platform.python_version(),
            arch=platform.architecture()[0]))
        assert cef.__version__ >= '57.0', 'CEF Python v57.0+ required to run this'
