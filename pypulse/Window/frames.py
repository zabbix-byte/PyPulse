import os
import platform
from sys import exit

import wx
from cefpython3 import cefpython

from .cef import Browser
from .logger import LogTypes, log

if platform.system() == 'Darwin':
    try:
        from AppKit import NSApp
    except ImportError:
        log(LogTypes.WARNING, 'You need AppKit installed.')
        log(LogTypes.INFO, 'Use `pip install AppKit`.')
        exit(1)

WINDOWS = 0


def scale_window_size_for_high_dpi(os, width, height):
    if os == 'Windows':
        return width, height

    _, _, max_width, max_height = wx.GetClientDisplayRect().Get()
    width, height = cefpython.DpiAware.Scale((width, height))

    if width > max_width:
        width = max_width

    if height > max_height:
        height = max_height

    return width, height


class BrowserFrame(wx.Frame):
    browser = None

    def __init__(self,
                 url='about:blank',
                 title: str = "PyPulse",
                 size: tuple = (1000, 600),
                 icon: str = None,
                 debug: bool = False,
                 log_file: bool = None,
                 border_less: bool = True,
                 maximize: bool = None,
                 minimize: bool = None,
                 caption = None) -> None:

        self.title = title
        self.icon = icon
        self.url = url
        self.width, self.height = size

        self.browser = Browser(self.url)

        self.browser.config['product_version'] = 'PyPulse/0.1.9'
        self.browser.config['debug'] = debug
        if log_file:
            self.browser.config['log_file'] = log_file

        self.adapt_width, self.adapt_height = scale_window_size_for_high_dpi(self.browser.os,
                                                                             self.width,
                                                                             self.height)

        wx.Frame.__init__(
            self,
            parent=None,
            id=wx.ID_ANY,

            title=title,
        )
        width, height = self.FromDIP(wx.Size(self.width, self.height))
        self.SetClientSize(width, height)

        style = wx.DEFAULT_FRAME_STYLE
        if maximize:
            style = style & (~wx.MAXIMIZE_BOX)

        if minimize:
            style = style & (~wx.MINIMIZE_BOX)
        
        self.SetWindowStyle(style)

        if caption:
            self.SetWindowStyle(wx.CAPTION)

        if border_less:
            self.SetWindowStyle(wx.NO_BORDER)

        if self.browser.os == 'Linux':
            cefpython.WindowUtils.InstallX11ErrorHandlers()

        self.panel = wx.Panel(self)
        self.browser.window.SetAsChild(self.panel.GetHandle(),
                                       [0, 0, width, height])

        self.SetBackgroundColour(wx.BLACK)

        if self.icon:
            self.icon_img = wx.Icon(self.icon)
            self.SetIcon(self.icon_img)

        global WINDOWS
        WINDOWS += 1

        log(LogTypes.SUCCESS, 'Window added')

        self.browser.open()
        # os.system('clear' if self.browser.os != 'Windows' else 'cls')

        log(LogTypes.INFO, 'Browser open')

        self.Bind(wx.EVT_CLOSE, self.OnExit)
        self.panel.Bind(wx.EVT_SET_FOCUS, self.OnSetFocus)
        self.panel.Bind(wx.EVT_SIZE, self.OnSize)

    def OnSetFocus(self, _):
        if self.browser.os == 'Windows':
            cefpython.WindowUtils.OnSetFocus(self.panel.GetHandle(),
                                             0, 0, 0)

        self.browser.instance.SetFocus(True)

    def OnSize(self, *args, **kwargs):
        if self.browser.os == 'Windows':
            cefpython.WindowUtils.OnSize(self.panel.GetHandle(),
                                         0, 0, 0)

        if self.browser.os == 'Linux':
            x, y = 0, 0
            width, height = self.panel.GetSize().Get()
            self.browser.instance.SetBounds(x, y, width, height)

        self.browser.instance.NotifyMoveOrResizeStarted()

    def OnExit(self, _):
        print()
        log(LogTypes.WARNING, 'Closing application...')

        self.Destroy()

        if self.browser.os == 'Darwin':
            self.browser.instance.CloseBrowser()

            self.Destroy()

            global windows
            windows -= 1

            if windows == 0:
                self.browser.close()
                wx.GetApp().ExitMainLoop()
                os._exit(0)
            return

        self.browser.instance.ParentWindowWillClose()
        self.browser.instance = None
        exit(0)
