
from kicad_amf_plugin.icon import GetImagePath
from kicad_amf_plugin.pcb_fabrication.base.base_info_view import BaseInfoView
from kicad_amf_plugin.pcb_fabrication.process.process_info_view import ProcessInfoView
from kicad_amf_plugin.pcb_fabrication.special_process.special_process_view import SpecialProcessView
from kicad_amf_plugin.pcb_fabrication.personalized.personalized_info_view import PersonalizedInfoView
from kicad_amf_plugin.pcb_fabrication.order.order_info_view import OrderInfoView
from kicad_amf_plugin.utils.platebtn import PlateButton ,PB_STYLE_GRADIENT ,AdjustColour



import wx
import wx.xrc
import wx.dataview

import gettext
_ = gettext.gettext


class MainWindow (wx.Dialog):

    def __init__(self, parent):

        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=_(u"HQ NextPCB Active Manufacturing"),
                           pos=wx.DefaultPosition, size=wx.Size(900, 600), style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)
        wx.SizerFlags.DisableConsistencyChecks()
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        main_sizer = wx.BoxSizer(wx.HORIZONTAL)

        pcb_fab_panel = wx.ScrolledWindow(
            self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1), wx.HSCROLL | wx.VSCROLL)
        pcb_fab_panel.SetScrollRate(10, 10)
        lay_pcb_fab_panel = wx.BoxSizer(wx.VERTICAL)

        m_fabBaseInfo = BaseInfoView(pcb_fab_panel)
        lay_pcb_fab_panel.Add(m_fabBaseInfo, 0, wx.ALL | wx.EXPAND, 5)

        m_fabProcessInfo = ProcessInfoView(pcb_fab_panel)
        lay_pcb_fab_panel.Add(m_fabProcessInfo, 0, wx.ALL | wx.EXPAND, 5)

        m_fabSpecialProcess = SpecialProcessView(pcb_fab_panel)
        lay_pcb_fab_panel.Add(m_fabSpecialProcess, 0, wx.ALL | wx.EXPAND, 5)

        m_fabServiceInfo = PersonalizedInfoView(
            pcb_fab_panel)
        lay_pcb_fab_panel.Add(m_fabServiceInfo, 0, wx.ALL | wx.EXPAND, 5)

        pcb_fab_panel.SetSizer(lay_pcb_fab_panel)
        pcb_fab_panel.Layout()


        order_info_view = OrderInfoView(self)

        main_sizer.Add(pcb_fab_panel, 1, wx.EXPAND, 8)

        main_sizer.Add(order_info_view, 0, wx.EXPAND, 8)

        # main_sizer.Add(PlateButton(self,
        #                            bmp= wx.Bitmap( GetImagePath( u"language.png" ),wx.BITMAP_TYPE_ANY ),
        #                            style= PB_STYLE_GRADIENT
        #                            ), 0)

        self.SetSizer(main_sizer)
        self.Layout()

        self.Centre(wx.BOTH)


    def __del__(self):
        pass


    # Virtual event handlers, override them in your derived class
    def OnTemplateChanged(self, event):
        event.Skip()

    def OnPcbPackagingChanged(self, event):
        event.Skip()

    def OnPanelizeXChanged(self, event):
        event.Skip()

    def OnPanelizeYChanged(self, event):
        event.Skip()

    def OnPcbQuantityChanged(self, event):
        event.Skip()

    def OnMarginModeChanged(self, event):
        event.Skip()

    def OnSurfaceProcessChanged(self, event):
        event.Skip()

    def OnHDIChanged(self, event):
        event.Skip()

    def OnReportChanged(self, event):
        event.Skip()

    def OnUpdatePrice(self, event):
        event.Skip()

    def OnPlaceOrder(self, event):
        event.Skip()

    def OnMaskColorChange(self, event):
        event.Skip()

    def OnThicknessChangebyLayer(self, event):
        event.Skip()
