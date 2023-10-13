import wx

class  ComboBoxIgnoreWheel(wx.Choice):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

    