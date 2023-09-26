
from .personalized_info_mdel import PersonalizedInfoModel
import wx
import wx.xrc
import wx.dataview

import gettext
_ = gettext.gettext


class personalized_info_view(wx.StaticBoxSizer):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.special_process: PersonalizedInfoModel = None
        self.initUI()

    def getInfo(self):
        return self.special_process

    def initUI(self):
        m_fabServiceInfoSizer = wx.GridBagSizer(0, 0)
        m_fabServiceInfoSizer.SetFlexibleDirection(wx.BOTH)
        m_fabServiceInfoSizer.SetNonFlexibleGrowMode(
            wx.FLEX_GROWMODE_SPECIFIED)

        self.m_testMethodLabel = wx.StaticText(self.GetStaticBox(
        ), wx.ID_ANY, _(u"Electrical Test:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_testMethodLabel.Wrap(-1)

        m_fabServiceInfoSizer.Add(self.m_testMethodLabel, wx.GBPosition(
            0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        m_testMethodCtrlChoices = [_(u"Sample Test Free"), _(
            u"AOI+Flying Test"), _(u"AOI+Fixture")]
        self.m_testMethodCtrl = wx.Choice(self.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.Size(100, -1), m_testMethodCtrlChoices, 0)
        self.m_testMethodCtrl.SetSelection(0)
        m_fabServiceInfoSizer.Add(self.m_testMethodCtrl, wx.GBPosition(
            0, 1), wx.GBSpan(1, 3), wx.ALL | wx.EXPAND, 5)

        self.m_approveWorkingGerberLabel = wx.StaticText(self.GetStaticBox(
        ), wx.ID_ANY, _(u"Approve Working Gerber:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_approveWorkingGerberLabel.Wrap(-1)

        m_fabServiceInfoSizer.Add(self.m_approveWorkingGerberLabel, wx.GBPosition(
            1, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        m_approveWorkingGerberCtrlChoices = [_(u"No"), _(u"Yes")]
        self.m_approveWorkingGerberCtrl = wx.Choice(self.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.Size(100, -1), m_approveWorkingGerberCtrlChoices, 0)
        self.m_approveWorkingGerberCtrl.SetSelection(0)
        m_fabServiceInfoSizer.Add(self.m_approveWorkingGerberCtrl, wx.GBPosition(
            1, 1), wx.GBSpan(1, 3), wx.ALL | wx.EXPAND, 5)

        self.m_deliveryReportLabel = wx.StaticText(self.GetStaticBox(
        ), wx.ID_ANY, _(u"Delivery Report:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_deliveryReportLabel.Wrap(-1)

        m_fabServiceInfoSizer.Add(self.m_deliveryReportLabel, wx.GBPosition(
            2, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        m_deliveryReportCtrlChoices = [_(u"No"), _(u"Yes")]
        self.m_deliveryReportCtrl = wx.Choice(self.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.Size(100, -1), m_deliveryReportCtrlChoices, 0)
        self.m_deliveryReportCtrl.SetSelection(0)
        m_fabServiceInfoSizer.Add(self.m_deliveryReportCtrl, wx.GBPosition(
            2, 1), wx.GBSpan(1, 3), wx.ALL | wx.EXPAND, 5)

        self.m_analysisReportLabel = wx.StaticText(self.GetStaticBox(), wx.ID_ANY, _(
            u"Microsection Analysis Report:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_analysisReportLabel.Wrap(-1)

        m_fabServiceInfoSizer.Add(self.m_analysisReportLabel, wx.GBPosition(
            3, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        m_analysisReportCtrlChoices = [_(u"No"), _(u"Yes")]
        self.m_analysisReportCtrl = wx.Choice(self.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.Size(100, -1), m_analysisReportCtrlChoices, 0)
        self.m_analysisReportCtrl.SetSelection(0)
        m_fabServiceInfoSizer.Add(self.m_analysisReportCtrl, wx.GBPosition(
            3, 1), wx.GBSpan(1, 3), wx.ALL | wx.EXPAND, 5)

        self.m_reportFormatLabel = wx.StaticText(self.GetStaticBox(
        ), wx.ID_ANY, _(u"Report Format:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_reportFormatLabel.Wrap(-1)

        m_fabServiceInfoSizer.Add(self.m_reportFormatLabel, wx.GBPosition(
            4, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        m_reportFormatCtrlChoices = [_(u"Paper"), _(u"Electronic")]
        self.m_reportFormatCtrl = wx.Choice(self.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.Size(100, -1), m_reportFormatCtrlChoices, 0)
        self.m_reportFormatCtrl.SetSelection(1)
        m_fabServiceInfoSizer.Add(self.m_reportFormatCtrl, wx.GBPosition(
            4, 1), wx.GBSpan(1, 3), wx.ALL | wx.EXPAND, 5)

        self.m_ulMarkLabel = wx.StaticText(self.GetStaticBox(
        ), wx.ID_ANY, _(u"UL Mark:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_ulMarkLabel.Wrap(-1)

        m_fabServiceInfoSizer.Add(self.m_ulMarkLabel, wx.GBPosition(
            5, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        m_ulMarkCtrlChoices = [_(u"No"), _(
            u"UL+Week/Year"), _(u"UL+Year/Week")]
        self.m_ulMarkCtrl = wx.Choice(self.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.Size(100, -1), m_ulMarkCtrlChoices, 0)
        self.m_ulMarkCtrl.SetSelection(0)
        m_fabServiceInfoSizer.Add(self.m_ulMarkCtrl, wx.GBPosition(
            5, 1), wx.GBSpan(1, 3), wx.ALL | wx.EXPAND, 5)

        self.m_filmLabel = wx.StaticText(self.GetStaticBox(
        ), wx.ID_ANY, _(u"Film:"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_filmLabel.Wrap(-1)

        m_fabServiceInfoSizer.Add(self.m_filmLabel, wx.GBPosition(
            6, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        m_filmCtrlChoices = [_(u"No"), _(u"Yes")]
        self.m_filmCtrl = wx.Choice(self.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.Size(100, -1), m_filmCtrlChoices, 0)
        self.m_filmCtrl.SetSelection(0)
        m_fabServiceInfoSizer.Add(self.m_filmCtrl, wx.GBPosition(
            6, 1), wx.GBSpan(1, 3), wx.ALL | wx.EXPAND, 5)

        self.m_specialRequestsLabel = wx.StaticText(self.GetStaticBox(
        ), wx.ID_ANY, _(u"Special Requests:"), wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.m_specialRequestsLabel.Wrap(-1)

        m_fabServiceInfoSizer.Add(self.m_specialRequestsLabel, wx.GBPosition(
            7, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_specialRequestsCtrl = wx.TextCtrl(self.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(100, -1), 0)
        m_fabServiceInfoSizer.Add(self.m_specialRequestsCtrl, wx.GBPosition(
            7, 1), wx.GBSpan(5, 3), wx.ALL | wx.EXPAND, 5)

        m_fabServiceInfoSizer.AddGrowableCol(1)

        self.Add(m_fabServiceInfoSizer, 1, wx.EXPAND, 5)
