import wx
from main_frame import AppI18N


class MainWindow(wx.Dialog):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.mainPanel = wx.Button(self)
        mysizer = wx.BoxSizer()
        mysizer.Add(self.mainPanel, 1, wx.EXPAND)
        self.SetSizer(mysizer)
        self.Layout()


if __name__ == '__main__':
    import app_base as ab
    app = ab.BaseApp(redirect=False)
    frame = MainWindow(None)
    frame.Show()
    app.MainLoop()
