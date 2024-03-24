import sys
from abc import ABC, abstractmethod
from enum import Enum
from platform import system

if system() == "Windows":
    import ctypes

from cefpython3 import cefpython


class Event(Enum):
    """
    List of all the events available for `abs` class CEF.
    """
    BROWSER_BEFORE = 1
    BROWSER_AFTER  = 2
    CLOSING        = 3
    INITIALIZING   = 4


class CEF(ABC):
    """
    Simplifies the CEF functions into a class.

    Start a CEF application:
    >>> _cef = CEF(url="https://example.com")
    >>> _cef.load()

    If you want to handle different events use:
    >>> def my_callback_for_event(app, type): 
    >>>    print(f"A event just happened! Type: {event}")
    >>> _cef.event = my_callback_for_event

    Its more recommended to inheritance this CEF class. 
    """
    # The current instance of the browser.
    # When its created will be automatically
    # assigned.
    instance = None

    def __init__(self, config: dict = {}, *args, **kwargs) -> None:
        self.config = config
        self.os = system()
        self.args = args
        self.kwargs = kwargs
    
    def __browser(self):
        self.event(Event.BROWSER_BEFORE)
        self.instance = cefpython.CreateBrowserSync(*self.args, 
                                                    **self.kwargs)
        
        self.event(Event.BROWSER_AFTER)

    def __initialize(self):
        self.event(Event.INITIALIZING)
        cefpython.Initialize(self.config)

        if self.os == 'Windows':
            ctypes.windll.shcore.SetProcessDpiAwareness(0)
            cefpython.DpiAware.EnableHighDpiSupport()

    def open(self):
        sys.excepthook = cefpython.ExceptHook
        
        self.__initialize()
        self.__browser()

    def close(self):
        self.event(Event.CLOSING)

        cefpython.MessageLoop()
        if self.os != "Darwin":
            cefpython.Shutdown()

    def load(self) -> None:
        """
        Load & open the browser.
        """
        self.open()
        self.close()

    @abstractmethod
    def event(self, type: Event) -> None: 
        """
        Some custom events added on top of CEF. You can modifythis 
        function however you want. Add the `type` argument. Necessary 
        to know what type of event you're handling
        """
        ...
 

class Browser(CEF):
    """
    A more friendly way to manage CEF browser.
    """
    window = cefpython.WindowInfo()
    config = {}

    def __init__(self, url: str, *args, **kwargs) -> None:
        super().__init__(config=self.config, 
                         window_info=self.window, 
                         url=url, 
                         *args, **kwargs)
        
    class Handler:
        """
        See [CEFPython handlers](https://github.com/cztomczak/cefpython/blob/master/api/API-categories.md#client-handlers-interfaces) if you want to check all the 
        handlers currently available.
        """
        def OnGotFocus(self, browser):
            if system() == 'Linux':
                browser.SetFocus(True)
                
    def event(self, type: Event) -> None:
        """
        Event handler for CEF.
        **Do not modify this function.**
        """
        if type is not Event.BROWSER_AFTER:
            return
        self.instance.SetClientHandler(self.Handler())
