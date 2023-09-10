import sys
import platform
import ctypes

from cefpython3 import cefpython as cef


class Load():
    def __init__(self, title: str = 'PyPulse App',
                 debug: bool = True,
                 debug_file_name: str = 'debug.log',
                 window_size_y: int = 1270,
                 window_size_x: int = 720,
                 ) -> None:

        self.check_versions()
        sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error

        settings = {
            'product_version': 'PyPulse/10.00',
            'debug': debug,
            'log_severity': cef.LOGSEVERITY_INFO,
            'log_file': debug_file_name,
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
        browser = cef.CreateBrowserSync(
            url="https://www.google.com/", window_title=title, window_info=window_info)

        if platform.system() == "Windows":
            window_handle = browser.GetOuterWindowHandle()
            insert_after_handle = 0
            # X and Y parameters are ignored by setting the SWP_NOMOVE flag
            SWP_NOMOVE = 0x0002
            # noinspection PyUnresolvedReferences
            ctypes.windll.user32.SetWindowPos(window_handle, insert_after_handle,
                                              0, 0, window_size_y, window_size_x, SWP_NOMOVE)

        browser.SetClientHandler(LoadHandler())

        cef.MessageLoop()
        del browser
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


class LoadHandler(object):
    def OnLoadingStateChange(self, browser, is_loading, **_):
        """For detecting if page loading has ended it is recommended
        to use OnLoadingStateChange which is most reliable. The OnLoadEnd
        callback also available in LoadHandler can sometimes fail in
        some cases e.g. when image loading hangs."""
        if not is_loading:
            self._OnPageComplete(browser)

    def _OnPageComplete(self, browser):
        print("[PyPulse] Aplication Loaded")
        # browser.ExecuteFunction("alert", "Message from Python: Page loading"
        #                                  " is complete!")
