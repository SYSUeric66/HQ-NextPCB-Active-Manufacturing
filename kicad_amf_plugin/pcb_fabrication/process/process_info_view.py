
from .process_info_model import ProcessInfoModel
import wx
import wx.xrc
import wx.dataview

import gettext
_ = gettext.gettext


class ProcessInfoView(wx.StaticBoxSizer):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.info: ProcessInfoModel = None
        self.initUI()

    def getInfo(self):
        return self.info

    def initUI(self):
        m_fabProcessInfoSizer = wx.GridBagSizer(0, 0)
        m_fabProcessInfoSizer.SetFlexibleDirection(wx.BOTH)
        m_fabProcessInfoSizer.SetNonFlexibleGrowMode(
            wx.FLEX_GROWMODE_SPECIFIED)

        self.m_boardThicknessLabel = wx.StaticText(self.GetStaticBox(
        ), wx.ID_ANY, _(u"PCB Thickness:"), wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.m_boardThicknessLabel.Wrap(-1)

        m_fabProcessInfoSizer.Add(self.m_boardThicknessLabel, wx.GBPosition(
            0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        m_boardThicknessCtrlChoices = [_(u"0.6"), _(u"0.8"), _(u"1.0"), _(
            u"1.2"), _(u"1.6"), _(u"2.0"), _(u"2.5"), _(u"3.0"), _(u"3.2")]
        self.m_boardThicknessCtrl = wx.Choice(self.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.Size(100, -1), m_boardThicknessCtrlChoices, 0)
        self.m_boardThicknessCtrl.SetSelection(4)
        m_fabProcessInfoSizer.Add(self.m_boardThicknessCtrl, wx.GBPosition(
            0, 1), wx.GBSpan(1, 1), wx.ALL | wx.EXPAND, 5)

        self.m_boardThicknessUnit = wx.StaticText(self.GetStaticBox(
        ), wx.ID_ANY, _(u"mm"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_boardThicknessUnit.Wrap(-1)

        m_fabProcessInfoSizer.Add(self.m_boardThicknessUnit, wx.GBPosition(
            0, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_outerCopperThicknessLabel = wx.StaticText(self.GetStaticBox(
        ), wx.ID_ANY, _(u"Finished Copper Weight:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_outerCopperThicknessLabel.Wrap(-1)

        m_fabProcessInfoSizer.Add(self.m_outerCopperThicknessLabel, wx.GBPosition(
            1, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        m_outerCopperThicknessCtrlChoices = [_(u"1oz"), _(u"2oz")]
        self.m_outerCopperThicknessCtrl = wx.Choice(self.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.Size(100, -1), m_outerCopperThicknessCtrlChoices, 0)
        self.m_outerCopperThicknessCtrl.SetSelection(0)
        m_fabProcessInfoSizer.Add(self.m_outerCopperThicknessCtrl, wx.GBPosition(
            1, 1), wx.GBSpan(1, 2), wx.ALL | wx.EXPAND, 5)

        self.m_innerCopperThicknessLabel = wx.StaticText(self.GetStaticBox(
        ), wx.ID_ANY, _(u"Inner Copper Weight:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_innerCopperThicknessLabel.Wrap(-1)

        m_fabProcessInfoSizer.Add(self.m_innerCopperThicknessLabel, wx.GBPosition(
            2, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        m_innerCopperThicknessCtrlChoices = [_(u"0.5oz"), _(u"1oz"), _(u"2oz")]
        self.m_innerCopperThicknessCtrl = wx.Choice(self.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.Size(100, -1), m_innerCopperThicknessCtrlChoices, 0)
        self.m_innerCopperThicknessCtrl.SetSelection(0)
        m_fabProcessInfoSizer.Add(self.m_innerCopperThicknessCtrl, wx.GBPosition(
            2, 1), wx.GBSpan(1, 2), wx.ALL | wx.EXPAND, 5)

        self.m_minTraceWidthClearanceLabel = wx.StaticText(self.GetStaticBox(
        ), wx.ID_ANY, _(u"Min Trace/Space Outer:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_minTraceWidthClearanceLabel.Wrap(-1)

        m_fabProcessInfoSizer.Add(self.m_minTraceWidthClearanceLabel, wx.GBPosition(
            3, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        m_minTraceWidthClearanceCtrlChoices = [
            _(u"10/10mil"), _(u"8/8mil"), _(u"6/6mil"), _(u"5/5mil"), _(u"4/4mil"), _(u"3.5/3.5mil")]
        self.m_minTraceWidthClearanceCtrl = wx.Choice(self.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.Size(100, -1), m_minTraceWidthClearanceCtrlChoices, 0)
        self.m_minTraceWidthClearanceCtrl.SetSelection(2)
        m_fabProcessInfoSizer.Add(self.m_minTraceWidthClearanceCtrl, wx.GBPosition(
            3, 1), wx.GBSpan(1, 2), wx.ALL | wx.EXPAND, 5)

        self.m_minHoleSizeLabel = wx.StaticText(self.GetStaticBox(
        ), wx.ID_ANY, _(u"Min Drilled Hole:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_minHoleSizeLabel.Wrap(-1)

        m_fabProcessInfoSizer.Add(self.m_minHoleSizeLabel, wx.GBPosition(
            4, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        m_minHoleSizeCtrlChoices = [_(u"0.3mm"), _(
            u"0.25mm"), _(u"0.2mm"), _(u"0.15mm")]
        self.m_minHoleSizeCtrl = wx.Choice(self.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.Size(100, -1), m_minHoleSizeCtrlChoices, 0)
        self.m_minHoleSizeCtrl.SetSelection(0)
        m_fabProcessInfoSizer.Add(self.m_minHoleSizeCtrl, wx.GBPosition(
            4, 1), wx.GBSpan(1, 2), wx.ALL | wx.EXPAND, 5)

        self.m_solderColorLabel = wx.StaticText(self.GetStaticBox(
        ), wx.ID_ANY, _(u"Solder Mask Color:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_solderColorLabel.Wrap(-1)

        m_fabProcessInfoSizer.Add(self.m_solderColorLabel, wx.GBPosition(
            5, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        m_solderColorCtrlChoices = [_(u"Green"), _(u"Red"), _(u"Yellow"), _(
            u"Blue"), _(u"White"), _(u"Matte Black"), _(u"Black")]
        self.m_solderColorCtrl = wx.Choice(self.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.Size(100, -1), m_solderColorCtrlChoices, 0)
        self.m_solderColorCtrl.SetSelection(0)
        m_fabProcessInfoSizer.Add(self.m_solderColorCtrl, wx.GBPosition(
            5, 1), wx.GBSpan(1, 2), wx.ALL | wx.EXPAND, 5)

        self.m_silkscreenColorLabel = wx.StaticText(self.GetStaticBox(
        ), wx.ID_ANY, _(u"Silkscreen:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_silkscreenColorLabel.Wrap(-1)

        m_fabProcessInfoSizer.Add(self.m_silkscreenColorLabel, wx.GBPosition(
            6, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        m_silkscreenColorCtrlChoices = [_(u"White")]
        self.m_silkscreenColorCtrl = wx.Choice(self.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.Size(100, -1), m_silkscreenColorCtrlChoices, 0)
        self.m_silkscreenColorCtrl.SetSelection(0)
        m_fabProcessInfoSizer.Add(self.m_silkscreenColorCtrl, wx.GBPosition(
            6, 1), wx.GBSpan(1, 2), wx.ALL | wx.EXPAND, 5)

        self.m_solderCoverLabel = wx.StaticText(self.GetStaticBox(
        ), wx.ID_ANY, _(u"Via Process:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_solderCoverLabel.Wrap(-1)

        m_fabProcessInfoSizer.Add(self.m_solderCoverLabel, wx.GBPosition(
            7, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        m_solderCoverCtrlChoices = [_(u"Tenting Vias"), _(u"Vias not covered"), _(
            u"Solder Mask Plug (IV-B)"), _(u"Non-Conductive Fill")]
        self.m_solderCoverCtrl = wx.Choice(self.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.Size(100, -1), m_solderCoverCtrlChoices, 0)
        self.m_solderCoverCtrl.SetSelection(0)
        m_fabProcessInfoSizer.Add(self.m_solderCoverCtrl, wx.GBPosition(
            7, 1), wx.GBSpan(1, 2), wx.ALL | wx.EXPAND, 5)

        self.m_surfaceProcessLabel = wx.StaticText(self.GetStaticBox(
        ), wx.ID_ANY, _(u"Surface Finish:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_surfaceProcessLabel.Wrap(-1)

        m_fabProcessInfoSizer.Add(self.m_surfaceProcessLabel, wx.GBPosition(
            8, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        m_surfaceProcessCtrlChoices = [_(u"HASL"), _(
            u"Lead free HASL"), _(u"ENIG"), _(u"OSP")]
        self.m_surfaceProcessCtrl = wx.Choice(self.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.Size(100, -1), m_surfaceProcessCtrlChoices, 0)
        self.m_surfaceProcessCtrl.SetSelection(0)
        m_fabProcessInfoSizer.Add(self.m_surfaceProcessCtrl, wx.GBPosition(
            8, 1), wx.GBSpan(1, 2), wx.ALL | wx.EXPAND, 5)

        self.m_goldThicknessLabel = wx.StaticText(self.GetStaticBox(), wx.ID_ANY, _(
            u"Immersion Gold Thickness:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_goldThicknessLabel.Wrap(-1)

        m_fabProcessInfoSizer.Add(self.m_goldThicknessLabel, wx.GBPosition(
            9, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        m_goldThicknessCtrlChoices = [_(u"1µm"), _(u"2µm"), _(u"3µm")]
        self.m_goldThicknessCtrl = wx.Choice(self.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.Size(100, -1), m_goldThicknessCtrlChoices, 0)
        self.m_goldThicknessCtrl.SetSelection(0)
        m_fabProcessInfoSizer.Add(self.m_goldThicknessCtrl, wx.GBPosition(
            9, 1), wx.GBSpan(1, 2), wx.ALL | wx.EXPAND, 5)

        m_fabProcessInfoSizer.AddGrowableCol(1)

        self.Add(m_fabProcessInfoSizer, 1, wx.EXPAND, 5)
