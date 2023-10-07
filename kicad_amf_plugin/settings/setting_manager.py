
import wx

class _SettingManager(wx.EvtHandler) :
    def __init__(self) -> None:
        self.app : wx.App = None

    def set_language( self, lang : int):
        self
        pass

    def get_language(self, lang : int):
        self
        pass

    def register_app(self, app : wx.App):
        self.app = app




SETTING_MANAGER = _SettingManager()
