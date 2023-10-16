import wx

class  ComboBoxIgnoreWheel(wx.Choice):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.EventHandler 

    def ProcessEvent(self, evt : wx.Event):
            if evt.EventType  == wx.wxEVT_MOUSEWHEEL:
                evt.Skip(True)
                return True
            return super().ProcessEvent(evt)