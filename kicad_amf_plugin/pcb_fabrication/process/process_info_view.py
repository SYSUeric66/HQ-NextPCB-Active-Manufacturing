
from .process_info_model import ProcessInfoModel

from .ui_process_info import UiProcessInfo

import gettext
_ = gettext.gettext

BOARD_THICKNESS_CHOICE = [_(u"0.6"), _(u"0.8"), _(u"1.0"), _(
    u"1.2"), _(u"1.6"), _(u"2.0"), _(u"2.5"), _(u"3.0"), _(u"3.2")]

OUTER_THICKNESS_CHOICE = [_(u"1oz"), _(u"2oz")]


INNER_COPPER_THICKNESS_CHOICE = [_(u"0.5oz"), _(u"1oz"), _(u"2oz")]


MIN_TRACE_WIDTH_CLEARANCE_CHOICE = [
    _(u"10/10mil"), _(u"8/8mil"), _(u"6/6mil"), _(u"5/5mil"), _(u"4/4mil"), _(u"3.5/3.5mil")]


MIN_HOLE_SIZE_CHOICE = [_(u"0.3mm"), _(
    u"0.25mm"), _(u"0.2mm"), _(u"0.15mm")]


SOLDER_COLOR_CHOICE = [_(u"Green"), _(u"Red"), _(u"Yellow"), _(
    u"Blue"), _(u"White"), _(u"Matte Black"), _(u"Black")]


SILK_SCREEN_COLOR_CHOICE = [_(u"White")]


SOLDER_COVER_CHOICE = [_(u"Tenting Vias"), _(u"Vias not covered"), _(
    u"Solder Mask Plug (IV-B)"), _(u"Non-Conductive Fill")]

SURFACE_PROCESS_CHOICE = [_(u"HASL"), _(
    u"Lead free HASL"), _(u"ENIG"), _(u"OSP")]

GOLD_THICKNESS_CHOICE = [_(u"1µm"), _(u"2µm"), _(u"3µm")]


class ProcessInfoView(UiProcessInfo):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.info: ProcessInfoModel = None
        self.initUI()
        self.Fit()


    def getInfo(self):
        return self.info

    def initUI(self):
        self.combo_board_thickness.Append(BOARD_THICKNESS_CHOICE)
        self.combo_board_thickness.SetSelection(4)

        self.combo_outer_copper_thickness.Append(OUTER_THICKNESS_CHOICE)
        self.combo_outer_copper_thickness.SetSelection(0)

        self.combo_inner_copper_thickness.Append(INNER_COPPER_THICKNESS_CHOICE)
        self.combo_inner_copper_thickness.SetSelection(0)

        self.combo_min_trace_width_clearance.Append(
            MIN_TRACE_WIDTH_CLEARANCE_CHOICE)
        self.combo_min_trace_width_clearance.SetSelection(2)

        self.combo_min_hole_size.Append(MIN_HOLE_SIZE_CHOICE)
        self.combo_min_hole_size.SetSelection(0)

        self.combo_solder_color.Append(SOLDER_COLOR_CHOICE)
        self.combo_solder_color.SetSelection(0)

        self.combo_silk_screen_color.Append(SILK_SCREEN_COLOR_CHOICE)
        self.combo_silk_screen_color.SetSelection(0)

        self.combo_solder_cover.Append(SOLDER_COVER_CHOICE)
        self.combo_solder_cover.SetSelection(0)

        self.combo_surface_process.Append(SURFACE_PROCESS_CHOICE)
        self.combo_surface_process.SetSelection(0)

        self.combo_gold_thickness.Append(GOLD_THICKNESS_CHOICE)
        self.combo_gold_thickness.SetSelection(0)
