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

if __name__ == '__main__':
    app = wx.App ()
    dialog = wx.Frame(None, size= wx.Size(-1,-1))
    sizer = wx.BoxSizer()
    pcb_fab_scroll_wind = wx.ScrolledWindow(
    dialog, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1), wx.HSCROLL | wx.VSCROLL)
    pcb_fab_scroll_wind.SetScrollRate(10, 10)
    scroll_sizer = wx.BoxSizer(wx.VERTICAL)
    for i in range(1,30):
        box = ComboBoxIgnoreWheel(pcb_fab_scroll_wind, choices = ["1" , "2" , "3"])
        scroll_sizer.Add(box, 1, wx.ALL | wx.EXPAND, 5)
    pcb_fab_scroll_wind.SetSizer(scroll_sizer)
    pcb_fab_scroll_wind.Layout()
    sizer.Add(pcb_fab_scroll_wind ,1, wx.ALL | wx.EXPAND, 5)
    dialog.SetSizer(sizer)
    dialog.Layout()
    dialog.Show()
    app.MainLoop()
    