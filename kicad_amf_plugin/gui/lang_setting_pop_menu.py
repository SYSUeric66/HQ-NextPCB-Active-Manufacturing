import wx

class LangSettingPopMenu(wx.PopupTransientWindow):
    """Adds a bit of text and mouse movement to the wx.PopupWindow"""
    def __init__(self, parent, style):
        wx.PopupTransientWindow.__init__(self, parent, style)
        panel = wx.Panel(self)
        panel.SetBackgroundColour("#FFB6C1")

        st = wx.StaticText(panel, -1,
                          "wx.PopupTransientWindow is a\n"
                          "wx.PopupWindow which disappears\n"
                          "automatically when the user\n"
                          "clicks the mouse outside it or if it\n"
                          "(or its first child) loses focus in \n"
                          "any other way.")
        btn = wx.Button(panel, -1, "Press Me")
        spin = wx.SpinCtrl(panel, -1, "Hello")
        btn.Bind(wx.EVT_BUTTON, self.OnButton)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(st, 0, wx.ALL, 5)
        sizer.Add(btn, 0, wx.ALL, 5)
        sizer.Add(spin, 0, wx.ALL, 5)
        panel.SetSizer(sizer)

        sizer.Fit(panel)
        sizer.Fit(self)
        self.Layout()


    def ProcessLeftDown(self, evt):
        return wx.PopupTransientWindow.ProcessLeftDown(self, evt)

    def OnDismiss(self):
        pass

    def OnButton(self, evt):
        btn = evt.GetEventObject()
        if btn.GetLabel() == "Press Me":
            btn.SetLabel("Pressed")
        else:
            btn.SetLabel("Press Me")