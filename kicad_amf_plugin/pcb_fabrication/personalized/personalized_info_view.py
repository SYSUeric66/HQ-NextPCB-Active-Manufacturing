
from .personalized_info_mdel import PersonalizedInfoModel
import wx
import wx.xrc
import wx.dataview
from .ui_personalized import UiPersonalizedService
from kicad_amf_plugin.utils.constraint import BOOLEAN_CHOICE




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

    def initUI(self):
        self.comb_test_method.Append(TEST_METHOD_CHOICE)
        self.comb_test_method.SetSelection(0)
        for ctrl in (self.comb_approve_gerber, self.combo_microsection_report, self.comb_film, self.comb_delivery_report):
            for i in BOOLEAN_CHOICE:
                ctrl.Append(_(i))
            ctrl.SetSelection(0)

        self.comb_report_format.Append(REPORT_FORMAT_CHOICE)
        self.comb_report_format.SetSelection(1)

        self.comb_ul_mark.Append(UL_MARK_CHOICE)
        self.comb_ul_mark.SetSelection(0)
