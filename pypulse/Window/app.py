import wx

from pypulse.Aplication.vars import Vars

from .frames import BrowserFrame
from .logger import LogTypes, log


class App(wx.App):
    def __init__(self, *args, **kwargs):
        self.kwargs = kwargs
        super().__init__()

    def OnInit(self):
        frame = BrowserFrame(url=f"localhost:{Vars.INTERNAL_HTTP_SERVER_PORT}",
                             title=self.kwargs['title'],
                             icon=self.kwargs['icon_path'],
                             size=(self.kwargs.get('window_size_x'),
                                   self.kwargs.get('window_size_y')),
                             debug=self.kwargs.get('debug'),
                             log_file=self.kwargs.get('debug_file_name'),
                             border_less=self.kwargs.get('border_less'))

        log(LogTypes.SUCCESS, 'CEF initialized')
        print()

        frame.Show()
        frame.browser.close()

        return True
