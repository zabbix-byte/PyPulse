from cefpython3 import cefpython as cef
from urllib.parse import urlparse

# TODO: i need to handle the path howwwwwwwwwwwwwwww
class LoadHandler(object):
    def OnLoadingStateChange(self, browser, is_loading, **_):
        if not is_loading:

            print(browser.GetUrl())

            self._OnPageComplete(browser)
            
    def _OnPageComplete(self, browser):
        print("[PyPulse] Page Loaded")
