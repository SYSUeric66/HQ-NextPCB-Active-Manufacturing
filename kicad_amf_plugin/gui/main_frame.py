
import os
import sys
import wx
import wx.lib.sized_controls as sc
import wx.xrc


class AppI18N(wx.Dialog):
    def __init__(self, parent, **kwds):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString,
                           pos=wx.DefaultPosition, size=wx.Size(852, 571), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel1 = wx.Panel(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        m_radioBox1Choices = [u"Radio Button"]
        self.m_radioBox1 = wx.RadioBox(self.m_panel1, wx.ID_ANY, u"wxRadioBox",
                                       wx.DefaultPosition, wx.DefaultSize, m_radioBox1Choices, 1, wx.RA_SPECIFY_COLS)
        self.m_radioBox1.SetSelection(0)
        bSizer2.Add(self.m_radioBox1, 0, wx.ALL, 5)

        self.m_radioBtn1 = wx.RadioButton(
            self.m_panel1, wx.ID_ANY, u"RadioBtn", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.m_radioBtn1, 0, wx.ALL, 5)

        self.m_staticline1 = wx.StaticLine(
            self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizer2.Add(self.m_staticline1, 0, wx.EXPAND | wx.ALL, 5)

        self.m_gauge1 = wx.Gauge(self.m_panel1, wx.ID_ANY, 100,
                                 wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL)
        self.m_gauge1.SetValue(0)
        bSizer2.Add(self.m_gauge1, 0, wx.ALL, 5)

        self.m_slider1 = wx.Slider(self.m_panel1, wx.ID_ANY, 50, 0,
                                   100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL)
        bSizer2.Add(self.m_slider1, 0, wx.ALL, 5)

        self.m_radioBtn2 = wx.RadioButton(
            self.m_panel1, wx.ID_ANY, u"RadioBtn", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.m_radioBtn2, 0, wx.ALL, 5)

        self.m_panel1.SetSizer(bSizer2)
        self.m_panel1.Layout()
        bSizer2.Fit(self.m_panel1)
        bSizer1.Add(self.m_panel1, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel2 = wx.Panel(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer1.Add(self.m_panel2, 1, wx.EXPAND | wx.ALL, 5)

        self.m_collapsiblePane1 = wx.CollapsiblePane(
            self, wx.ID_ANY, u"collapsible", wx.DefaultPosition, wx.DefaultSize, wx.CP_DEFAULT_STYLE)
        self.m_collapsiblePane1.Collapse(False)

        bSizer1.Add(self.m_collapsiblePane1, 1, wx.EXPAND | wx.ALL, 5)

        self.m_checkBox1 = wx.CheckBox(
            self, wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.m_checkBox1, 0, wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

    def createOtherCtrls(self):
        sizer = wx.BoxSizer()
        pane = sc.SizedFrame(None)
        sizer.Add(pane)
        cPane = sc.SizedPanel(pane)
        cPane.SetSizerType("grid", options={"cols": 2})
        st = wx.StaticText(cPane, wx.ID_ANY,
                           _(u"A nice label for the TextCtrl"))
        st.SetSizerProps(valign='center')
        tc = wx.TextCtrl(cPane, wx.ID_ANY)

        searchSt = wx.StaticText(cPane, wx.ID_ANY,
                                 _(u"a search control"))
        searchSt.SetSizerProps(valign='center')
        searchC = wx.SearchCtrl(cPane, wx.ID_ANY)

        # sline = wx.StaticLine(pane, wx.ID_ANY)
        # sline.SetSizerProps(expand=True)
        bPane = sc.SizedPanel(pane)
        fB = wx.Button(bPane, wx.ID_ANY, _(u"Open a file dialog"))
        fB.SetSizerProps(align="center")
        fB.Bind(wx.EVT_BUTTON, self.onFbButton)
        self.SetSizer(sizer)
        self.Layout()

    def onFbButton(self, event):
        wildcard = "Python source (*.py)|*.py|"     \
                   "Compiled Python (*.pyc)|*.pyc|" \
                   "SPAM files (*.spam)|*.spam|"    \
                   "Egg file (*.egg)|*.egg|"        \
                   "All files (*.*)|*.*"

        with wx.FileDialog(
            self, message=_(u"Choose a file"),
            defaultDir=os.getcwd(),
            defaultFile="",
            wildcard=wildcard,
            style=wx.FD_OPEN | wx.FD_MULTIPLE | wx.FD_CHANGE_DIR
        ) as dlg:

            # Show the dialog and retrieve the user response. If it is the
            # OK response,
            # process the data.
            if dlg.ShowModal() == wx.ID_OK:
                # This returns a Python list of files that were selected.
                paths = dlg.GetPaths()

    def onClose(self, event):
        event.Skip()

    def doEditSomething(self, event):
        event.Skip()

    def doAboutBox(self, event):
        event.Skip()


if __name__ == '__main__':
    import app_base as ab
    app = ab.BaseApp(redirect=False)
    frame = AppI18N(None)
    frame.Show()
    sys.exit(app.MainLoop())
