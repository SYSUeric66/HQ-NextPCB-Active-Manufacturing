
from .personalized_info_model import PersonalizedInfoModel
import wx.xrc
import wx.dataview
from .ui_personalized import UiPersonalizedService
from kicad_amf_plugin.utils.constraint import BOOLEAN_CHOICE
from .personalized_info_model import PersonalizedInfoModel


TEST_METHOD_CHOICE = {
    _(u"Sample Test Free"): "Sample Test Free",
    _(u"AOI+Flying Test"): "Batch Flying Probe Test",
    _(u"AOI+Fixture"): "Batch Fixture Test"
}


REPORT_FORMAT_CHOICE = [_(u"Paper"), _(u"Electronic")]

UL_MARK_CHOICE = [_(u"No"), _(
    u"UL+Week/Year"), _(u"UL+Year/Week")]


class PersonalizedInfoView(UiPersonalizedService):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.special_process: PersonalizedInfoModel = None
        self.initUI()

    def initUI(self):
        self.comb_test_method.Append([ i for i in   TEST_METHOD_CHOICE])
        self.comb_test_method.SetSelection(0)
        for ctrl in (self.comb_approve_gerber, self.combo_microsection_report, self.comb_film, self.comb_delivery_report):
            for i in BOOLEAN_CHOICE:
                ctrl.Append(_(i))
            ctrl.SetSelection(0)

        self.comb_report_format.Append(REPORT_FORMAT_CHOICE)
        self.comb_report_format.SetSelection(1)

        self.comb_ul_mark.Append(UL_MARK_CHOICE)
        self.comb_ul_mark.SetSelection(0)

    @property
    def personalized_info(self):
        info = PersonalizedInfoModel(
            test=TEST_METHOD_CHOICE[self.comb_test_method.StringSelection],
            shipment_report=str(self.comb_delivery_report.GetSelection()),
            slice_report=str(self.combo_microsection_report.GetSelection()),
            report_type=str(self.GetReportType()),
            review_file=str(self.GetReviewFile()),
            has_period=str(self.GetHasPeriod()),
            period_format=self.GetPeriodFormat() if self.comb_ul_mark.GetSelection() else None,
            film_report=str(self.comb_film.GetSelection()),
            pcb_note=self.edit_special_request.GetValue()
        )
        return info

    def GetReportType(self):
        if self.comb_delivery_report.GetSelection() == 0 and self.combo_microsection_report.GetSelection() == 0:
            return 0
        elif self.comb_report_format.GetSelection() == 0:
            return 2
        elif self.comb_report_format.GetSelection() == 1:
            return 1

    def GetReviewFile(self):
        if self.comb_approve_gerber.GetSelection() == 0:
            return '0'
        else:
            return '2'

    def GetHasPeriod(self):
        if self.comb_ul_mark.GetSelection() == 0:
            return '2'
        else:
            return '6'

    def GetPeriodFormat(self):
        if self.comb_ul_mark.GetSelection() == 1:
            return '2'
        elif self.comb_ul_mark.GetSelection() == 2:
            return '1'
