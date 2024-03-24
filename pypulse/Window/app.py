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
                             icon=self.kwargs.get('icon_path'),
                             size=(self.kwargs['window_size_x'],
                                   self.kwargs['window_size_y']),
                             debug=self.kwargs.get('debug'),
                             log_file=self.kwargs.get('debug_file_name'),
                             border_less=self.kwargs.get('border_less'),
                             caption = self.kwargs.get('titlebar_caption'),
                             maximize = self.kwargs.get('titlebar_no_button_maximize'),
                             minimize = self.kwargs.get('titlebar_no_button_minimize'))

        log(LogTypes.SUCCESS, 'CEF initialized')
        print()

        frame.Show()
        frame.browser.close()

        return True
