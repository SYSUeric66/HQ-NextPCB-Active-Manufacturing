
from .special_process_model import SpecialProcessModel
import wx
import wx.xrc
import wx.dataview

import gettext
_ = gettext.gettext


class SpecialProcessView(wx.StaticBoxSizer):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.special_process: SpecialProcessModel = None
        self.initUI()

    def getBaseInfo(self):
        return self.special_process

    def initUI(self):
        m_fabSpecialProcessSizer = wx.GridBagSizer(0, 0)
        m_fabSpecialProcessSizer.SetFlexibleDirection(wx.BOTH)
        m_fabSpecialProcessSizer.SetNonFlexibleGrowMode(
            wx.FLEX_GROWMODE_SPECIFIED)

        self.m_impedanceLabel = wx.StaticText(self.GetStaticBox(
        ), wx.ID_ANY, _(u"Impedance:"), wx.DefaultPosition, wx.Size(100, -1), 0)
        self.m_impedanceLabel.Wrap(-1)

        m_fabSpecialProcessSizer.Add(
            self.m_impedanceLabel, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        m_impedanceCtrlChoices = [_(u"No"), _(u"Yes")]
        self.m_impedanceCtrl = wx.Choice(self.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.Size(100, -1), m_impedanceCtrlChoices, 0)
        self.m_impedanceCtrl.SetSelection(0)
        m_fabSpecialProcessSizer.Add(self.m_impedanceCtrl, wx.GBPosition(
            0, 1), wx.GBSpan(1, 3), wx.ALL | wx.EXPAND, 5)

        self.m_goldFingerLabel = wx.StaticText(self.GetStaticBox(
        ), wx.ID_ANY, _(u"Beveling of G/F:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_goldFingerLabel.Wrap(-1)

        m_fabSpecialProcessSizer.Add(
            self.m_goldFingerLabel, wx.GBPosition(1, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        m_goldFingerCtrlChoices = [_(u"No"), _(u"Yes")]
        self.m_goldFingerCtrl = wx.Choice(self.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.Size(100, -1), m_goldFingerCtrlChoices, 0)
        self.m_goldFingerCtrl.SetSelection(0)
        m_fabSpecialProcessSizer.Add(self.m_goldFingerCtrl, wx.GBPosition(
            1, 1), wx.GBSpan(1, 3), wx.ALL | wx.EXPAND, 5)

        self.m_halfHoleLabel = wx.StaticText(self.GetStaticBox(
        ), wx.ID_ANY, _(u"Plated Half Holes:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_halfHoleLabel.Wrap(-1)

        m_fabSpecialProcessSizer.Add(
            self.m_halfHoleLabel, wx.GBPosition(2, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        m_halfHoleCtrlChoices = [_(u"No"), _(u"Yes")]
        self.m_halfHoleCtrl = wx.Choice(self.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.Size(100, -1), m_halfHoleCtrlChoices, 0)
        self.m_halfHoleCtrl.SetSelection(0)
        m_fabSpecialProcessSizer.Add(self.m_halfHoleCtrl, wx.GBPosition(
            2, 1), wx.GBSpan(1, 3), wx.ALL | wx.EXPAND, 5)

        self.m_padHoleLabel = wx.StaticText(self.GetStaticBox(
        ), wx.ID_ANY, _(u"Pad Hole:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_padHoleLabel.Wrap(-1)

        m_fabSpecialProcessSizer.Add(
            self.m_padHoleLabel, wx.GBPosition(3, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        m_padHoleCtrlChoices = [_(u"No"), _(u"Yes")]
        self.m_padHoleCtrl = wx.Choice(self.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.Size(100, -1), m_padHoleCtrlChoices, 0)
        self.m_padHoleCtrl.SetSelection(0)
        m_fabSpecialProcessSizer.Add(self.m_padHoleCtrl, wx.GBPosition(
            3, 1), wx.GBSpan(1, 3), wx.ALL | wx.EXPAND, 5)

        self.m_blindViaLabel = wx.StaticText(self.GetStaticBox(), wx.ID_ANY, _(
            u"HDI(Buried/blind vias):"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_blindViaLabel.Wrap(-1)

        m_fabSpecialProcessSizer.Add(
            self.m_blindViaLabel, wx.GBPosition(4, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        m_blindViaCtrlChoices = [_(u"No"), _(u"Yes")]
        self.m_blindViaCtrl = wx.Choice(self.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_blindViaCtrlChoices, 0)
        self.m_blindViaCtrl.SetSelection(0)
        m_fabSpecialProcessSizer.Add(self.m_blindViaCtrl, wx.GBPosition(
            4, 1), wx.GBSpan(1, 3), wx.ALL | wx.EXPAND, 5)

        self.m_hdiStructureLabel = wx.StaticText(self.GetStaticBox(
        ), wx.ID_ANY, _(u"HDI Structure:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_hdiStructureLabel.Wrap(-1)

        m_fabSpecialProcessSizer.Add(
            self.m_hdiStructureLabel, wx.GBPosition(5, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        m_hdiStructureCtrlChoices = [_(u"Rank 1"), _(u"Rank 2"), _(u"Rank 3")]
        self.m_hdiStructureCtrl = wx.Choice(self.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.Size(100, -1), m_hdiStructureCtrlChoices, 0)
        self.m_hdiStructureCtrl.SetSelection(0)
        m_fabSpecialProcessSizer.Add(self.m_hdiStructureCtrl, wx.GBPosition(
            5, 1), wx.GBSpan(1, 3), wx.ALL | wx.EXPAND, 5)

        self.m_stackupLabel = wx.StaticText(self.GetStaticBox(
        ), wx.ID_ANY, _(u"Stack up:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_stackupLabel.Wrap(-1)

        m_fabSpecialProcessSizer.Add(
            self.m_stackupLabel, wx.GBPosition(6, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        m_stackupCtrlChoices = [_(u"No Requirement"), _(
            u"Customer Specified Stack up")]
        self.m_stackupCtrl = wx.Choice(self.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.Size(100, -1), m_stackupCtrlChoices, 0)
        self.m_stackupCtrl.SetSelection(0)
        m_fabSpecialProcessSizer.Add(self.m_stackupCtrl, wx.GBPosition(
            6, 1), wx.GBSpan(1, 3), wx.ALL | wx.EXPAND, 5)

        m_fabSpecialProcessSizer.AddGrowableCol(1)

        self.Add(m_fabSpecialProcessSizer, 1, wx.EXPAND, 5)
