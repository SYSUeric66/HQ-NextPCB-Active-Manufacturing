
from kicad_amf_plugin.icon import GetImagePath
from kicad_amf_plugin.pcb_fabrication.base.base_info_view import BaseInfoView
from kicad_amf_plugin.pcb_fabrication.process.process_info_view import ProcessInfoView
from kicad_amf_plugin.pcb_fabrication.special_process.special_process_view import SpecialProcessView
from kicad_amf_plugin.pcb_fabrication.personalized.personalized_info_view import PersonalizedInfoView
from kicad_amf_plugin.pcb_fabrication.order.order_info_view import OrderInfoView

import wx
import wx.xrc
import wx.dataview

import gettext
_ = gettext.gettext


class MainWindow (wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=_(u"HQ NextPCB Active Manufacturing"),
                           pos=wx.DefaultPosition, size=wx.Size(800, 700), style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)
        wx.SizerFlags.DisableConsistencyChecks()
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        main_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # m_topSizer = wx.BoxSizer(wx.HORIZONTAL)

        left_sizer = wx.BoxSizer(wx.VERTICAL)

        self.stack_widget = wx.Notebook(
            self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.pcb_fab_panel = wx.ScrolledWindow(
            self.stack_widget, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1), wx.HSCROLL | wx.VSCROLL)
        self.pcb_fab_panel.SetScrollRate(10, 10)
        lay_fab_left = wx.BoxSizer(wx.VERTICAL)

        # Section the info views
        m_fabBaseInfo = BaseInfoView(self.pcb_fab_panel)
        lay_fab_left.Add(m_fabBaseInfo, 0, wx.ALL | wx.EXPAND, 5)

        m_fabProcessInfo = ProcessInfoView(self.pcb_fab_panel)
        lay_fab_left.Add(m_fabProcessInfo, 0, wx.ALL | wx.EXPAND, 5)

        m_fabSpecialProcess = SpecialProcessView(self.pcb_fab_panel)
        lay_fab_left.Add(m_fabSpecialProcess, 0, wx.ALL | wx.EXPAND, 5)

        m_fabServiceInfo = PersonalizedInfoView(
            self.pcb_fab_panel)
        lay_fab_left.Add(m_fabServiceInfo, 0, wx.ALL | wx.EXPAND, 5)

        lay_fab_main =  wx.BoxSizer(wx.HORIZONTAL)
        lay_fab_main.Add(lay_fab_left ,1 , wx.ALL | wx.EXPAND, 5)

        self.pcb_fab_panel.SetSizer(lay_fab_left)
        self.pcb_fab_panel.Layout()

        self.stack_widget.AddPage(self.pcb_fab_panel, _(u"PCB Fabrication"), False)

        left_sizer.Add(self.stack_widget, 1,
                           wx.ALIGN_CENTER | wx.EXPAND | wx.TOP, 12)

        # m_topSizer.Add(top_left_sizer, 6, wx.ALL | wx.EXPAND, 5)

        # m_topRightSizer = wx.BoxSizer(wx.VERTICAL)

        # m_totalSummarySizer = wx.GridBagSizer(0, 0)
        # m_totalSummarySizer.SetFlexibleDirection(wx.BOTH)
        # m_totalSummarySizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        # self.m_huaqiuLogo = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(GetImagePath(
        #     u"Huaqiu.png"), wx.BITMAP_TYPE_ANY), wx.DefaultPosition, wx.DefaultSize, 0)
        # m_totalSummarySizer.Add(self.m_huaqiuLogo, wx.GBPosition(
        #     0, 0), wx.GBSpan(3, 1), wx.ALL | wx.EXPAND | wx.RIGHT | wx.TOP, 5)

        # self.m_amountLabel = wx.StaticText(self, wx.ID_ANY, _(
        #     u"PCB Qty:"), wx.DefaultPosition, wx.DefaultSize, 0)
        # self.m_amountLabel.Wrap(-1)

        # m_totalSummarySizer.Add(self.m_amountLabel, wx.GBPosition(
        #     0, 1), wx.GBSpan(1, 1), wx.LEFT | wx.TOP, 5)

        # self.m_amountCtrl = wx.StaticText(self, wx.ID_ANY, _(
        #     u"-"), wx.DefaultPosition, wx.DefaultSize, 0)
        # self.m_amountCtrl.Wrap(-1)

        # m_totalSummarySizer.Add(self.m_amountCtrl, wx.GBPosition(
        #     0, 2), wx.GBSpan(1, 1), wx.TOP, 5)

        # self.m_amountUnit = wx.StaticText(self, wx.ID_ANY, _(
        #     u"pcs"), wx.DefaultPosition, wx.DefaultSize, 0)
        # self.m_amountUnit.Wrap(-1)

        # m_totalSummarySizer.Add(self.m_amountUnit, wx.GBPosition(
        #     0, 3), wx.GBSpan(1, 1), wx.LEFT | wx.TOP, 5)

        # self.m_dueDateLabel = wx.StaticText(self, wx.ID_ANY, _(
        #     u"Time:"), wx.DefaultPosition, wx.DefaultSize, 0)
        # self.m_dueDateLabel.Wrap(-1)

        # m_totalSummarySizer.Add(self.m_dueDateLabel, wx.GBPosition(
        #     1, 1), wx.GBSpan(1, 1), wx.LEFT, 5)

        # self.m_dueDateCtrl = wx.StaticText(self, wx.ID_ANY, _(
        #     u"-"), wx.DefaultPosition, wx.DefaultSize, 0)
        # self.m_dueDateCtrl.Wrap(-1)

        # m_totalSummarySizer.Add(
        #     self.m_dueDateCtrl, wx.GBPosition(1, 2), wx.GBSpan(1, 1), 0, 5)

        # self.m_dueDateUnit = wx.StaticText(self, wx.ID_ANY, _(
        #     u"Days"), wx.DefaultPosition, wx.DefaultSize, 0)
        # self.m_dueDateUnit.Wrap(-1)

        # m_totalSummarySizer.Add(self.m_dueDateUnit, wx.GBPosition(
        #     1, 3), wx.GBSpan(1, 1), wx.LEFT, 5)

        # self.m_priceLabel = wx.StaticText(self, wx.ID_ANY, _(
        #     u"Cost:"), wx.DefaultPosition, wx.DefaultSize, 0)
        # self.m_priceLabel.Wrap(-1)

        # m_totalSummarySizer.Add(self.m_priceLabel, wx.GBPosition(
        #     2, 1), wx.GBSpan(1, 1), wx.LEFT | wx.TOP, 5)

        # self.m_priceCtrl = wx.StaticText(self, wx.ID_ANY, _(
        #     u"-"), wx.DefaultPosition, wx.DefaultSize, 0)
        # self.m_priceCtrl.Wrap(-1)

        # m_totalSummarySizer.Add(self.m_priceCtrl, wx.GBPosition(
        #     2, 2), wx.GBSpan(1, 1), wx.TOP, 5)

        # self.m_priceUnit = wx.StaticText(self, wx.ID_ANY, _(
        #     u"$"), wx.DefaultPosition, wx.DefaultSize, 0)
        # self.m_priceUnit.Wrap(-1)

        # m_totalSummarySizer.Add(self.m_priceUnit, wx.GBPosition(
        #     2, 3), wx.GBSpan(1, 1), wx.LEFT | wx.TOP, 5)

        # self.m_updatePriceButton = wx.Button(self, wx.ID_ANY, _(
        #     u"Update Price"), wx.DefaultPosition, wx.DefaultSize, 0)
        # m_totalSummarySizer.Add(self.m_updatePriceButton, wx.GBPosition(
        #     2, 4), wx.GBSpan(1, 1), wx.BOTTOM | wx.EXPAND | wx.RIGHT, 5)

        # self.m_placeOrderButton = wx.Button(self, wx.ID_ANY, _(
        #     u"Place Order"), wx.DefaultPosition, wx.DefaultSize, 0)
        # m_totalSummarySizer.Add(self.m_placeOrderButton, wx.GBPosition(
        #     0, 4), wx.GBSpan(1, 1), wx.EXPAND | wx.RIGHT | wx.TOP, 5)

        # m_totalSummarySizer.AddGrowableCol(2)
        # m_totalSummarySizer.AddGrowableCol(3)

        # m_topRightSizer.Add(m_totalSummarySizer, 0, wx.EXPAND, 5)

        # self.m_priceDetailsViewListCtrl = wx.dataview.DataViewListCtrl(
        #     self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        # self.m_priceDescriptionColumn = self.m_priceDetailsViewListCtrl.AppendTextColumn(
        #     _(u"Item"), wx.dataview.DATAVIEW_CELL_INERT, 200, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE)
        # self.m_priceColumn = self.m_priceDetailsViewListCtrl.AppendTextColumn(
        #     _(u"Price"), wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE)
        # m_topRightSizer.Add(self.m_priceDetailsViewListCtrl,
        #                     1, wx.ALL | wx.EXPAND, 5)

        # self.m_drcPanel = wx.Panel(
        #     self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_SIMPLE | wx.TAB_TRAVERSAL)
        # m_drcPanelSizer = wx.BoxSizer(wx.VERTICAL)

        # self.m_drcPanel.SetSizer(m_drcPanelSizer)
        # self.m_drcPanel.Layout()
        # m_drcPanelSizer.Fit(self.m_drcPanel)
        # m_topRightSizer.Add(self.m_drcPanel, 1, wx.ALL | wx.EXPAND, 5)

        # m_topSizer.Add(m_topRightSizer, 5, wx.ALL | wx.EXPAND, 5)

        content_sizer = wx.BoxSizer(wx.VERTICAL)
        content_sizer.Add(left_sizer,1,wx.EXPAND)
        order_info_view = OrderInfoView(self)
        content_sizer.Add(order_info_view ,1 ,  wx.EXPAND)

        main_sizer.Add(content_sizer, 1, wx.EXPAND, 8)
        self.SetSizer(main_sizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        # self.m_template.Bind(wx.EVT_CHOICE, self.OnTemplateChanged)
        # self.m_pcbPackaingCtrl.Bind(wx.EVT_CHOICE, self.OnPcbPackagingChanged)
        # self.edit_panel_x.Bind(wx.EVT_TEXT, self.OnPanelizeXChanged)
        # self.edit_panel_y.Bind(wx.EVT_TEXT, self.OnPanelizeYChanged)
        # self.m_quantityCtrl.Bind(wx.EVT_CHOICE, self.OnPcbQuantityChanged)
        # self.comb_margin_mode.Bind(wx.EVT_CHOICE, self.OnMarginModeChanged)
        # self.combo_surface_process.Bind(
        #     wx.EVT_CHOICE, self.OnSurfaceProcessChanged)
        # self.combo_blind_via.Bind(wx.EVT_CHOICE, self.OnHDIChanged)
        # self.m_deliveryReportCtrl.Bind(wx.EVT_CHOICE, self.OnReportChanged)
        # self.comb_delivery_report.Bind(wx.EVT_CHOICE, self.OnReportChanged)
        # self.m_updatePriceButton.Bind(wx.EVT_BUTTON, self.OnUpdatePrice)
        # self.m_placeOrderButton.Bind(wx.EVT_BUTTON, self.OnPlaceOrder)
        # self.combo_solder_color.Bind(wx.EVT_CHOICE, self.OnMaskColorChange)
        # # self.combo_layer_count.Bind( wx.EVT_CHOICE, self.OnTGChangebyLayer )
        # self.combo_layer_count.Bind(
        #     wx.EVT_CHOICE, self.OnThicknessChangebyLayer)

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
