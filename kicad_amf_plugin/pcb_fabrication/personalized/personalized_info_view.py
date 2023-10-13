
from kicad_amf_plugin.order.order_region import OrderRegion, SupportedRegion
from kicad_amf_plugin.settings.setting_manager import SETTING_MANAGER
from kicad_amf_plugin.utils.none_value_fitter import none_value_fitter
from .personalized_info_model import PersonalizedInfoModel
import wx.xrc
import wx.dataview
from .ui_personalized import UiPersonalizedService , BOX_SP_REQUEST
from kicad_amf_plugin.utils.constraint import BOOLEAN_CHOICE
from .personalized_info_model import PersonalizedInfoModel
from kicad_amf_plugin.utils.form_panel_base import FormPanelBase
from kicad_amf_plugin.utils.roles import EditDisplayRole


REVIEW_FILE_OPTION = [
    EditDisplayRole(0,_('Need') ),
    EditDisplayRole(1,_('Need & Auto Confirm') ),
    EditDisplayRole(2,_('Need & Manual Confirm') ),
]

CROSS_BOARD = [
    EditDisplayRole(1,_('Accept') ),
    EditDisplayRole(2,_('Reject') ),
]


PAPER = [
    EditDisplayRole(1,_('Need') ),
    EditDisplayRole(2,_("No need") ),
]

USER_STAMP = [
    EditDisplayRole(1,_('Add customer stamp') ),
    EditDisplayRole(2,_("Add it to specified location") ),
    EditDisplayRole(2,_("Don't add customer stamp") ),
]

HQ_PACK = [
    EditDisplayRole(1,_('Yes') ),
    EditDisplayRole(0,_("No") ),
]



TEST_METHOD_CHOICE = {
    _(u"Sample Test Free"): "Sample Test Free",
    _(u"AOI+Flying Test"): "Batch Flying Probe Test",
    _(u"AOI+Fixture"): "Batch Fixture Test"
}


REPORT_FORMAT_CHOICE = [_(u"Paper"), _(u"Electronic")]

UL_MARK_CHOICE = [_(u"No"), _(
    u"UL+Week/Year"), _(u"UL+Year/Week")]


class PersonalizedInfoView(UiPersonalizedService ,FormPanelBase):
    def __init__(self, parent , _):
        super().__init__(parent)
        self.special_process: PersonalizedInfoModel = None
        self.initUI()

    def initUI(self):
        self.comb_test_method.Append([ i for i in   TEST_METHOD_CHOICE])
        self.comb_test_method.SetSelection(0)
        for ctrl in ( self.combo_microsection_report, self.comb_film, self.comb_delivery_report):
            for i in BOOLEAN_CHOICE:
                ctrl.Append(_(i))
            ctrl.SetSelection(0)

        self.comb_report_format.Append(REPORT_FORMAT_CHOICE)
        self.comb_report_format.SetSelection(1)

        self.comb_ul_mark.Append(UL_MARK_CHOICE)
        self.comb_ul_mark.SetSelection(0)

        map = {
            self.comb_approve_gerber : REVIEW_FILE_OPTION,
             self.combo_cross_board : CROSS_BOARD,
             self.combo_paper : PAPER ,
             self.combo_user_stamp : USER_STAMP,
             self.combo_hq_pack : HQ_PACK
        }
        map = {
            self.comb_approve_gerber : REVIEW_FILE_OPTION,
             self.combo_cross_board : CROSS_BOARD,
             self.combo_paper : PAPER ,
             self.combo_user_stamp : USER_STAMP,
             self.combo_hq_pack : HQ_PACK
        }
        for comb in map:
            comb.Append([i.DisplayRole for i in map[comb]])
            comb.SetSelection(0)        
        
    @none_value_fitter    
    def get_from(self) -> 'dict' :
        info = PersonalizedInfoModel(
            test=TEST_METHOD_CHOICE[self.comb_test_method.StringSelection],
            shipment_report=str(self.comb_delivery_report.GetSelection()),
            slice_report=str(self.combo_microsection_report.GetSelection()),
            report_type=str(self.GetReportType()),
            review_file=REVIEW_FILE_OPTION[int(self.comb_approve_gerber.GetSelection())].EditRole,
            has_period=str(self.GetHasPeriod()),
            period_format=self.GetPeriodFormat() if self.comb_ul_mark.GetSelection() else None,
            film_report=str(self.comb_film.GetSelection()),
            cross_board= CROSS_BOARD[self.combo_cross_board.GetSelection()].EditRole,
            paper = PAPER[self.combo_paper.GetSelection()].EditRole,
            user_stamp= USER_STAMP[self.combo_user_stamp.GetSelection()].EditRole,

            hq_pack= HQ_PACK[int(self.combo_hq_pack.GetSelection())].EditRole  if self.combo_hq_pack.Shown else None,
            pcb_note=self.edit_special_request.GetValue() if self.edit_special_request.Shown else None,

        )
        return vars(info)

    def GetReportType(self):
        if self.comb_delivery_report.GetSelection() == 0 and self.combo_microsection_report.GetSelection() == 0:
            return 0
        elif self.comb_report_format.GetSelection() == 0:
            return 2
        elif self.comb_report_format.GetSelection() == 1:
            return 1

    def GetHasPeriod(self):
        if self.comb_ul_mark.GetSelection() == 0:
            return '2'
        else:
            return '6'
    @property
    def sp_box(self):
        return self.FindWindowById(BOX_SP_REQUEST)

    def GetPeriodFormat(self):
        if self.comb_ul_mark.GetSelection() == 1:
            return '2'
        elif self.comb_ul_mark.GetSelection() == 2:
            return '1'
        
    def on_region_changed(self):
        for i in self.combo_hq_pack , self.label_hq_pack:
            i.Show(SETTING_MANAGER.order_region == SupportedRegion.CHINA_MAINLAND)
        self.sp_box.Show(SETTING_MANAGER.order_region != SupportedRegion.CHINA_MAINLAND)
        if SETTING_MANAGER.get_main_wind() is not None:
            SETTING_MANAGER.get_main_wind().adjust_size()        