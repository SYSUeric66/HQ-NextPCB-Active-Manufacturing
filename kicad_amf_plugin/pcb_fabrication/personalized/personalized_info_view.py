
from .personalized_info_mdel import PersonalizedInfoModel
import wx
import wx.xrc
import wx.dataview
from .ui_personalized import UiPersonalizedService
from kicad_amf_plugin.utils.constraint import BOOLEAN_CHOICE
import gettext
_ = gettext.gettext


TEST_METHOD_CHOICE = [_(u"Sample Test Free"), _(
    u"AOI+Flying Test"), _(u"AOI+Fixture")]


REPORT_FORMAT_CHOICE = [_(u"Paper"), _(u"Electronic")]

UL_MARK_CHOICE = [_(u"No"), _(
    u"UL+Week/Year"), _(u"UL+Year/Week")]


class PersonalizedInfoView(UiPersonalizedService):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.special_process: PersonalizedInfoModel = None
        self.initUI()

    def getInfo(self):
        return self.special_process

    def initUI(self):

        for ctrl in (self.comb_test_method, self.comb_approve_gerber, self.comb_delivery_report, self.comb_film):
            ctrl.Append(TEST_METHOD_CHOICE)
            ctrl.SetSelection(0)

        self.comb_report_format.Append(REPORT_FORMAT_CHOICE)
        self.comb_report_format.SetSelection(1)

        self.comb_ul_mark.Append(UL_MARK_CHOICE)
        self.comb_ul_mark.SetSelection(0)
