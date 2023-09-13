# Tested configurations:
# - wxPython 4.0 on Windows/Mac/Linux
# - wxPython 3.0 on Windows/Mac
# - wxPython 2.8 on Linux
# - CEF Python v66.0+

from pypulse.Aplication import Vars
import wx
from cefpython3 import cefpython as cef
import platform
import sys
import os

# Platforms
WINDOWS = (platform.system() == "Windows")
LINUX = (platform.system() == "Linux")
MAC = (platform.system() == "Darwin")

if MAC:
    try:
        # noinspection PyUnresolvedReferences
        from AppKit import NSApp
    except ImportError:
        print("[PyPulse] Error: PyObjC package is missing, "
              "cannot fix Issue #371")
        print("[PyPulse] To install PyObjC type: "
              "pip install -U pyobjc")
        sys.exit(1)

# Configuration
WIDTH = None
HEIGHT = None
WINDOW_TITLE = None
DEBUG = None
ICON = None
DEBUG_FILE = None
BOREDER_LESS = None

# Globals
g_count_windows = 0


def Browser(title: str,
            debug: bool,
            debug_file_name: str,
            window_size_x: int,
            window_size_y: int,
            icon_path: str,
            border_less: bool):

    global WIDTH, HEIGHT, WINDOW_TITLE, DEBUG, ICON, DEBUG_FILE, BOREDER_LESS

    WIDTH = window_size_x
    HEIGHT = window_size_y
    WINDOW_TITLE = title
    DEBUG = debug
    ICON = icon_path
    DEBUG_FILE = debug_file_name
    BOREDER_LESS = border_less

    check_versions()
    sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error
    settings = {
        'product_version': 'PyPulse/10.00',
        'debug': DEBUG,
        'log_file': DEBUG_FILE,
    }

    if MAC:
        # Issue #442 requires enabling message pump on Mac
        # and calling message loop work in a timer both at
        # the same time. This is an incorrect approach
        # and only a temporary fix.
        settings["external_message_pump"] = True
    if WINDOWS:
        # noinspection PyUnresolvedReferences, PyArgumentList
        cef.DpiAware.EnableHighDpiSupport()

    cef.Initialize(settings=settings)
    app = CefApp(False)
    app.MainLoop()
    del app  # Must destroy before calling Shutdown
    if not MAC:
        # On Mac shutdown is called in OnClose
        cef.Shutdown()


def check_versions():
    print("[PyPulse] CEF Python {ver}".format(ver=cef.__version__))
    print("[PyPulse] Python {ver} {arch}".format(
        ver=platform.python_version(), arch=platform.architecture()[0]))
    print("[PyPulse] wxPython {ver}".format(ver=wx.version()))
    # CEF Python version requirement
    assert cef.__version__ >= "66.0", "CEF Python v66.0+ required to run this"


def scale_window_size_for_high_dpi(width, height):
    """Scale window size for high DPI devices. This func can be
    called on all operating systems, but scales only for Windows.
    If scaled value is bigger than the work area on the display
    then it will be reduced."""
    if not WINDOWS:
        return width, height
    (_, _, max_width, max_height) = wx.GetClientDisplayRect().Get()
    # noinspection PyUnresolvedReferences
    (width, height) = cef.DpiAware.Scale((width, height))
    if width > max_width:
        width = max_width
    if height > max_height:
        height = max_height
    return width, height


class MainFrame(wx.Frame):
    instance = None

    def __init__(self, parent, id=wx.ID_ANY, title="", pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE):
        super(MainFrame, self).__init__(parent, id, title, pos, size, style)
        Browser.instance = None
    
        # Must ignore X11 errors like 'BadWindow' and others by
        # installing X11 error handlers. This must be done after
        # wx was intialized.
        if LINUX:
            cef.WindowUtils.InstallX11ErrorHandlers()

        global g_count_windows
        g_count_windows += 1

        if WINDOWS:
            # noinspection PyUnresolvedReferences, PyArgumentList
            print("[PyPulse] System DPI settings: %s"
                  % str(cef.DpiAware.GetSystemDpi()))
        if hasattr(wx, "GetDisplayPPI"):
            print("[PyPulse] wx.GetDisplayPPI = %s" % wx.GetDisplayPPI())
        print("[PyPulse] wx.GetDisplaySize = %s" % wx.GetDisplaySize())

        print("[PyPulse] MainFrame declared size: %s"
              % str((WIDTH, HEIGHT)))
        size = scale_window_size_for_high_dpi(WIDTH, HEIGHT)
        print("[PyPulse] MainFrame DPI scaled size: %s" % str(size))

        wx.Frame.__init__(self, parent=None, id=wx.ID_ANY,
                          title=WINDOW_TITLE, size=size)
        # wxPython will set a smaller size when it is bigger
        # than desktop size.
        print("[PyPulse] MainFrame actual size: %s" % self.GetSize())

        self.setup_icon()
        self.Bind(wx.EVT_CLOSE, self.OnClose)

        # Set wx.WANTS_CHARS style for the keyboard to work.
        # This style also needs to be set for all parent controls.
        Browser.instance_panel = wx.Panel(self, style=wx.WANTS_CHARS)
        Browser.instance_panel.Bind(wx.EVT_SET_FOCUS, self.OnSetFocus)
        Browser.instance_panel.Bind(wx.EVT_SIZE, self.OnSize)

        if MAC:
            # Make the content view for the window have a layer.
            # This will make all sub-views have layers. This is
            # necessary to ensure correct layer ordering of all
            # child views and their layers. This fixes Window
            # glitchiness during initial loading on Mac (Issue #371).
            NSApp.windows()[0].contentView().setWantsLayer_(True)

        if LINUX:
            # On Linux must show before embedding browser, so that handle
            # is available (Issue #347).
            self.Show()
            # In wxPython 3.0 and wxPython 4.0 on Linux handle is
            # still not yet available, so must delay embedding browser
            # (Issue #349).
            if wx.version().startswith("3.") or wx.version().startswith("4."):
                wx.CallLater(100, self.embed_browser)
            else:
                # This works fine in wxPython 2.8 on Linux
                self.embed_browser()
        else:
            self.embed_browser()
            self.Show()

    def setup_icon(self):
        self.SetIcon(wx.Icon(ICON))

    def embed_browser(self):
        window_info = cef.WindowInfo()
        (width, height) = Browser.instance_panel.GetClientSize().Get()
        assert Browser.instance_panel.GetHandle(), "Window handle not available"
        window_info.SetAsChild(Browser.instance_panel.GetHandle(),
                               [0, 0, width, height])
        Browser.instance = cef.CreateBrowserSync(
            window_info, url=f'http://127.0.0.1:{Vars.INTERNAL_HTTP_SERVER_PORT}/')
        Browser.instance.SetClientHandler(FocusHandler())

    def OnSetFocus(self, _):
        if not Browser.instance:
            return
        if WINDOWS:
            cef.WindowUtils.OnSetFocus(Browser.instance_panel.GetHandle(),
                                       0, 0, 0)
        Browser.instance.SetFocus(True)

    def OnSize(self, _):
        if not Browser.instance:
            return
        if WINDOWS:
            cef.WindowUtils.OnSize(Browser.instance_panel.GetHandle(),
                                   0, 0, 0)
        elif LINUX:
            (x, y) = (0, 0)
            (width, height) = Browser.instance_panel.GetSize().Get()
            Browser.instance.SetBounds(x, y, width, height)
        Browser.instance.NotifyMoveOrResizeStarted()

    def OnClose(self, event):
        print("[PyPulse] OnClose called")
        from pypulse.Socket import stop_server
        stop_server()
        if not Browser.instance:
            # May already be closing, may be called multiple times on Mac
            return

        if MAC:
            # On Mac things work differently, other steps are required
            Browser.instance.CloseBrowser()
            self.clear_browser_references()
            self.Destroy()
            global g_count_windows
            g_count_windows -= 1
            if g_count_windows == 0:
                cef.Shutdown()
                wx.GetApp().ExitMainLoop()
                # Call _exit otherwise app exits with code 255 (Issue #162).
                # noinspection PyProtectedMember
                os._exit(0)
        else:
            # Calling browser.CloseBrowser() and/or self.Destroy()
            # in OnClose may cause app crash on some paltforms in
            # some use cases, details in Issue #107.
            Browser.instance.ParentWindowWillClose()
            event.Skip()
            self.clear_browser_references()

    def clear_browser_references(self):
        # Clear browser references that you keep anywhere in your
        # code. All references must be cleared for CEF to shutdown cleanly.
        Browser.instance = None


class FocusHandler(object):
    def OnGotFocus(self, browser, **_):
        # Temporary fix for focus issues on Linux (Issue #284).
        if LINUX:
            print("[PyPulse] FocusHandler.OnGotFocus:"
                  " keyboard focus fix (Issue #284)")
            browser.SetFocus(True)


class CefApp(wx.App):

    def __init__(self, redirect):
        self.timer = None
        self.timer_id = 1
        self.is_initialized = False
        super(CefApp, self).__init__(redirect=redirect)

    def OnPreInit(self):
        super(CefApp, self).OnPreInit()
        # On Mac with wxPython 4.0 the OnInit() event never gets
        # called. Doing wx window creation in OnPreInit() seems to
        # resolve the problem (Issue #350).
        if MAC and wx.version().startswith("4."):
            print("[PyPulse] OnPreInit: initialize here"
                  " (wxPython 4.0 fix)")
            self.initialize()

    def OnInit(self):
        self.initialize()
        return True

    def initialize(self):
        if self.is_initialized:
            return
        self.is_initialized = True
        self.create_timer()
        frame = MainFrame(None)
        self.SetTopWindow(frame)
        frame.Show()

    def create_timer(self):
        # See also "Making a render loop":
        # http://wiki.wxwidgets.org/Making_a_render_loop
        # Another way would be to use EVT_IDLE in MainFrame.
        self.timer = wx.Timer(self, self.timer_id)
        self.Bind(wx.EVT_TIMER, self.on_timer, self.timer)
        self.timer.Start(10)  # 10ms timer

    def on_timer(self, _):
        cef.MessageLoopWork()

    def OnExit(self):
        self.timer.Stop()
        return 0
