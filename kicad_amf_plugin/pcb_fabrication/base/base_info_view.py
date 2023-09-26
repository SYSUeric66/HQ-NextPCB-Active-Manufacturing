from .base_info_model import BaseInfoModel
import wx
import wx.xrc
import wx.dataview

import gettext
_ = gettext.gettext


class BaseInfoView(wx.StaticBoxSizer):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.base_info = None
        self.initUI()

    def getBaseInfo(self):
        return self.base_info

    def initUI(self):
        m_fabBaseInfoSizer = wx.GridBagSizer(0, 0)
        m_fabBaseInfoSizer.SetFlexibleDirection(wx.BOTH)
        m_fabBaseInfoSizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        self.m_baseMaterialLabel = wx.StaticText(self.GetStaticBox(), wx.ID_ANY, _(
            u"Material Type:"), wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.m_baseMaterialLabel.Wrap(-1)

        self.m_baseMaterialLabel.SetToolTip(_(u"Non-conductive base material"))

        m_fabBaseInfoSizer.Add(self.m_baseMaterialLabel,
                               wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        m_baseMaterialCtrlChoices = [_(u"FR-4")]
        self.m_baseMaterialCtrl = wx.Choice(self.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.Size(100, -1), m_baseMaterialCtrlChoices, 0)
        self.m_baseMaterialCtrl.SetSelection(0)
        m_fabBaseInfoSizer.Add(self.m_baseMaterialCtrl, wx.GBPosition(
            0, 1), wx.GBSpan(1, 2), wx.ALL | wx.EXPAND, 5)

        self.m_layerCountLabel = wx.StaticText(self.GetStaticBox(), wx.ID_ANY, _(
            u"Layer Count:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_layerCountLabel.Wrap(-1)

        self.m_layerCountLabel.SetToolTip(_(u"Number of copper layers"))

        m_fabBaseInfoSizer.Add(self.m_layerCountLabel, wx.GBPosition(
            1, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        m_layerCountCtrlChoices = [_(u"1"), _(u"2"), _(u"4"), _(u"6"), _(
            u"8"), _(u"10"), _(u"12"), _(u"14"), _(u"16"), _(u"18"), _(u"20")]
        self.m_layerCountCtrl = wx.Choice(self.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.Size(100, -1), m_layerCountCtrlChoices, 0)
        self.m_layerCountCtrl.SetSelection(1)
        m_fabBaseInfoSizer.Add(self.m_layerCountCtrl, wx.GBPosition(
            1, 1), wx.GBSpan(1, 2), wx.ALL | wx.EXPAND, 5)

        self.m_pcbPackaingLabel = wx.StaticText(self.GetStaticBox(), wx.ID_ANY, _(
            u"Board Type:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_pcbPackaingLabel.Wrap(-1)

        self.m_pcbPackaingLabel.SetToolTip(
            _(u"The finished PCB are by single or by panel"))

        m_fabBaseInfoSizer.Add(self.m_pcbPackaingLabel,
                               wx.GBPosition(2, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        m_pcbPackaingCtrlChoices = [_(u"Single Piece"), _(
            u"Panel by Customer"), _(u"Panel by NextPCB")]
        self.m_pcbPackaingCtrl = wx.Choice(self.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.Size(100, -1), m_pcbPackaingCtrlChoices, 0)
        self.m_pcbPackaingCtrl.SetSelection(0)
        m_fabBaseInfoSizer.Add(self.m_pcbPackaingCtrl, wx.GBPosition(
            2, 1), wx.GBSpan(1, 2), wx.ALL | wx.EXPAND, 5)

        self.m_panelizeRuleLbel = wx.StaticText(self.GetStaticBox(), wx.ID_ANY, _(
            u"Panel Type:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_panelizeRuleLbel.Wrap(-1)

        m_fabBaseInfoSizer.Add(self.m_panelizeRuleLbel,
                               wx.GBPosition(3, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_panelizeXLabel = wx.StaticText(self.GetStaticBox(), wx.ID_ANY, _(
            u"X:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_panelizeXLabel.Wrap(-1)

        m_fabBaseInfoSizer.Add(self.m_panelizeXLabel, wx.GBPosition(
            4, 0), wx.GBSpan(1, 1), wx.ALIGN_RIGHT | wx.ALL, 5)

        self.m_panelizeXCtrl = wx.TextCtrl(self.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(100, -1), wx.TE_READONLY)
        self.m_panelizeXCtrl.SetMaxLength(0)
        m_fabBaseInfoSizer.Add(self.m_panelizeXCtrl, wx.GBPosition(
            4, 1), wx.GBSpan(1, 1), wx.ALL | wx.EXPAND, 5)

        self.m_panelizeXUnit = wx.StaticText(self.GetStaticBox(), wx.ID_ANY, _(
            u"pcs"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_panelizeXUnit.Wrap(-1)

        m_fabBaseInfoSizer.Add(self.m_panelizeXUnit, wx.GBPosition(
            4, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_panelizeYCtrl = wx.TextCtrl(self.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(100, -1), wx.TE_READONLY)
        self.m_panelizeYCtrl.SetMaxLength(0)
        m_fabBaseInfoSizer.Add(self.m_panelizeYCtrl, wx.GBPosition(
            5, 1), wx.GBSpan(1, 1), wx.ALL | wx.EXPAND, 5)

        self.m_panelizeYLabel = wx.StaticText(self.GetStaticBox(), wx.ID_ANY, _(
            u"Y:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_panelizeYLabel.Wrap(-1)

        m_fabBaseInfoSizer.Add(self.m_panelizeYLabel, wx.GBPosition(
            5, 0), wx.GBSpan(1, 1), wx.ALIGN_RIGHT | wx.ALL, 5)

        self.m_panelizeYUnit = wx.StaticText(self.GetStaticBox(), wx.ID_ANY, _(
            u"pcs"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_panelizeYUnit.Wrap(-1)

        m_fabBaseInfoSizer.Add(self.m_panelizeYUnit, wx.GBPosition(
            5, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_sizeLabel = wx.StaticText(self.GetStaticBox(), wx.ID_ANY, _(
            u"Size (single):"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_sizeLabel.Wrap(-1)

        m_fabBaseInfoSizer.Add(self.m_sizeLabel, wx.GBPosition(
            6, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_sizeXLabel = wx.StaticText(self.GetStaticBox(), wx.ID_ANY, _(
            u"X:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_sizeXLabel.Wrap(-1)

        m_fabBaseInfoSizer.Add(self.m_sizeXLabel, wx.GBPosition(
            7, 0), wx.GBSpan(1, 1), wx.ALIGN_RIGHT | wx.ALL, 5)

        self.m_sizeXCtrl = wx.TextCtrl(self.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(100, -1), wx.TE_READONLY)
        self.m_sizeXCtrl.SetMaxLength(0)
        m_fabBaseInfoSizer.Add(self.m_sizeXCtrl, wx.GBPosition(
            7, 1), wx.GBSpan(1, 1), wx.ALL | wx.EXPAND, 5)

        self.m_sizeXUnit = wx.StaticText(self.GetStaticBox(), wx.ID_ANY, _(
            u"mm"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_sizeXUnit.Wrap(-1)

        m_fabBaseInfoSizer.Add(self.m_sizeXUnit, wx.GBPosition(
            7, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_sizeYLabel1 = wx.StaticText(self.GetStaticBox(), wx.ID_ANY, _(
            u"Y:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_sizeYLabel1.Wrap(-1)

        m_fabBaseInfoSizer.Add(self.m_sizeYLabel1, wx.GBPosition(
            8, 0), wx.GBSpan(1, 1), wx.ALIGN_RIGHT | wx.ALL, 5)

        self.m_sizeYCtrl = wx.TextCtrl(self.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(100, -1), wx.TE_READONLY)
        self.m_sizeYCtrl.SetMaxLength(0)
        m_fabBaseInfoSizer.Add(self.m_sizeYCtrl, wx.GBPosition(
            8, 1), wx.GBSpan(1, 1), wx.ALL | wx.EXPAND, 5)

        self.m_sizeYUnit = wx.StaticText(self.GetStaticBox(), wx.ID_ANY, _(
            u"mm"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_sizeYUnit.Wrap(-1)

        m_fabBaseInfoSizer.Add(self.m_sizeYUnit, wx.GBPosition(
            8, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_quantityLbel = wx.StaticText(self.GetStaticBox(), wx.ID_ANY, _(
            u"Qty(single):"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_quantityLbel.Wrap(-1)

        m_fabBaseInfoSizer.Add(self.m_quantityLbel, wx.GBPosition(
            9, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        m_quantityCtrlChoices = [_(u"5"), _(u"10"), _(u"15"), _(u"20"), _(u"25"), _(u"30"), _(u"40"), _(u"50"), _(u"75"), _(u"100"), _(u"125"), _(u"150"), _(u"200"), _(u"250"), _(u"300"), _(u"350"), _(u"400"), _(u"450"), _(u"500"), _(u"600"), _(
            u"700"), _(u"800"), _(u"900"), _(u"1000"), _(u"1500"), _(u"2000"), _(u"2500"), _(u"3000"), _(u"3500"), _(u"4000"), _(u"4500"), _(u"5000"), _(u"5500"), _(u"6000"), _(u"6500"), _(u"7000"), _(u"7500"), _(u"8000"), _(u"9000"), _(u"10000")]
        self.m_quantityCtrl = wx.Choice(self.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.Size(100, -1), m_quantityCtrlChoices, 0)
        self.m_quantityCtrl.SetSelection(0)
        m_fabBaseInfoSizer.Add(self.m_quantityCtrl, wx.GBPosition(
            9, 1), wx.GBSpan(1, 1), wx.ALL | wx.EXPAND, 5)

        self.m_quantityUnit = wx.StaticText(self.GetStaticBox(), wx.ID_ANY, _(
            u"Pcs"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_quantityUnit.Wrap(-1)

        m_fabBaseInfoSizer.Add(self.m_quantityUnit, wx.GBPosition(
            9, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_marginLabel = wx.StaticText(self.GetStaticBox(), wx.ID_ANY, _(
            u"Break-away Rail:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_marginLabel.Wrap(-1)

        m_fabBaseInfoSizer.Add(self.m_marginLabel, wx.GBPosition(
            10, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        m_marginModeCtrlChoices = [
            _(u"N/A"), _(u"Left & Right"), _(u"Top & Bottom"), _(u"All 4 sides")]
        self.m_marginModeCtrl = wx.Choice(self.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.Size(100, -1), m_marginModeCtrlChoices, 0)
        self.m_marginModeCtrl.SetSelection(0)
        m_fabBaseInfoSizer.Add(self.m_marginModeCtrl, wx.GBPosition(
            10, 1), wx.GBSpan(1, 1), wx.ALL | wx.EXPAND, 5)

        self.m_marginValueCtrl = wx.TextCtrl(self.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(100, -1), wx.TE_READONLY)
        self.m_marginValueCtrl.SetMaxLength(0)
        m_fabBaseInfoSizer.Add(self.m_marginValueCtrl, wx.GBPosition(
            11, 1), wx.GBSpan(1, 1), wx.ALL | wx.EXPAND, 5)

        self.m_marginValueUnit = wx.StaticText(self.GetStaticBox(), wx.ID_ANY, _(
            u"mm"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_marginValueUnit.Wrap(-1)

        m_fabBaseInfoSizer.Add(self.m_marginValueUnit, wx.GBPosition(
            11, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        m_fabBaseInfoSizer.AddGrowableCol(1)
        self.Add(m_fabBaseInfoSizer, 1, wx.EXPAND, 5)
