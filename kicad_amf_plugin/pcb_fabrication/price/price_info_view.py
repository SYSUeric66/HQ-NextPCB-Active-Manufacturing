
from kicad_amf_plugin.icon import GetImagePath
import wx
import wx.xrc
import wx.dataview

import gettext
_ = gettext.gettext


class PriceInfoView(wx.GridBagSizer):
    def __init__(self, vgap=0, hgap=0):
        super().__init__(vgap, hgap)
        self.initUI()

    def initUI(self):
        self.SetFlexibleDirection(wx.BOTH)
        self.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        # self.m_huaqiuLogo = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(GetImagePath(
        #     u"Huaqiu.png"), wx.BITMAP_TYPE_ANY), wx.DefaultPosition, wx.DefaultSize, 0)
        # self.Add(self.m_huaqiuLogo, wx.GBPosition(
        #     0, 0), wx.GBSpan(3, 1), wx.ALL | wx.EXPAND | wx.RIGHT | wx.TOP, 5)

        self.m_amountLabel = wx.StaticText(self, wx.ID_ANY, _(
            u"PCB Qty："), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_amountLabel.Wrap(-1)

        self.Add(self.m_amountLabel, wx.GBPosition(
            0, 1), wx.GBSpan(1, 1), wx.LEFT | wx.TOP, 5)

        self.m_amountCtrl = wx.StaticText(self, wx.ID_ANY, _(
            u"-"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_amountCtrl.Wrap(-1)

        self.Add(self.m_amountCtrl, wx.GBPosition(
            0, 2), wx.GBSpan(1, 1), wx.TOP, 5)

        self.m_amountUnit = wx.StaticText(self, wx.ID_ANY, _(
            u"pcs"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_amountUnit.Wrap(-1)

        self.Add(self.m_amountUnit, wx.GBPosition(
            0, 3), wx.GBSpan(1, 1), wx.LEFT | wx.TOP, 5)

        self.m_dueDateLabel = wx.StaticText(self, wx.ID_ANY, _(
            u"Time："), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_dueDateLabel.Wrap(-1)

        self.Add(self.m_dueDateLabel, wx.GBPosition(
            1, 1), wx.GBSpan(1, 1), wx.LEFT, 5)

        self.m_dueDateCtrl = wx.StaticText(self, wx.ID_ANY, _(
            u"-"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_dueDateCtrl.Wrap(-1)

        self.Add(
            self.m_dueDateCtrl, wx.GBPosition(1, 2), wx.GBSpan(1, 1), 0, 5)

        self.m_dueDateUnit = wx.StaticText(self, wx.ID_ANY, _(
            u"Days"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_dueDateUnit.Wrap(-1)

        self.Add(self.m_dueDateUnit, wx.GBPosition(
            1, 3), wx.GBSpan(1, 1), wx.LEFT, 5)

        self.m_priceLabel = wx.StaticText(self, wx.ID_ANY, _(
            u"Cost："), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_priceLabel.Wrap(-1)

        self.Add(self.m_priceLabel, wx.GBPosition(
            2, 1), wx.GBSpan(1, 1), wx.LEFT | wx.TOP, 5)

        self.m_priceCtrl = wx.StaticText(self, wx.ID_ANY, _(
            u"-"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_priceCtrl.Wrap(-1)

        self.Add(self.m_priceCtrl, wx.GBPosition(
            2, 2), wx.GBSpan(1, 1), wx.TOP, 5)

        self.m_priceUnit = wx.StaticText(self, wx.ID_ANY, _(
            u"$"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_priceUnit.Wrap(-1)

        self.Add(self.m_priceUnit, wx.GBPosition(
            2, 3), wx.GBSpan(1, 1), wx.LEFT | wx.TOP, 5)

        self.m_updatePriceButton = wx.Button(self, wx.ID_ANY, _(
            u"Update Price"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.Add(self.m_updatePriceButton, wx.GBPosition(
            2, 4), wx.GBSpan(1, 1), wx.BOTTOM | wx.EXPAND | wx.RIGHT, 5)

        self.m_placeOrderButton = wx.Button(self, wx.ID_ANY, _(
            u"Place Order"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.Add(self.m_placeOrderButton, wx.GBPosition(
            0, 4), wx.GBSpan(1, 1), wx.EXPAND | wx.RIGHT | wx.TOP, 5)

        self.AddGrowableCol(2)
        self.AddGrowableCol(3)
