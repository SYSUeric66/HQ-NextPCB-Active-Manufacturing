
from .process_info_model import ProcessInfoModel

from .ui_process_info import UiProcessInfo




BOARD_THICKNESS_CHOICE = [0.6, 0.8, 1.0,
    1.2, 1.6, 2.0, 2.5, 3.0, 3.2]

OZ = "oz"

OUTER_THICKNESS_CHOICE = [1 ,2]


INNER_COPPER_THICKNESS_CHOICE = [0.5 ,1 ,2]

MIL = "mil"

MIN_TRACE_WIDTH_CLEARANCE_CHOICE = [10 , 8 ,6 , 5 ,4 , 3.5]
MIN_HOLE_SIZE_CHOICE = [0.3, 0.25, 0.2, 0.15]

MM="mm"

SOLDER_COLOR_CHOICE = [_(u"Green"), _(u"Red"), _(u"Yellow"), _(
    u"Blue"), _(u"White"), _(u"Matte Black"), _(u"Black")]

SILK_SCREEN_COLOR_CHOICE = [_(u"White")]


SOLDER_COVER_CHOICE = [_(u"Tenting Vias"), _(u"Vias not covered"), _(
    u"Solder Mask Plug (IV-B)"), _(u"Non-Conductive Fill")]

SURFACE_PROCESS_CHOICE = [_(u"HASL"), _(
    u"Lead free HASL"), _(u"ENIG"), _(u"OSP")]

GOLD_THICKNESS_CHOICE = [1, 2, 3]

GOLD_THICKNESS_CHOICE_UNIT = "µm"


class ProcessInfoView(UiProcessInfo):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.info: ProcessInfoModel = None
        self.initUI()
        self.Fit()


    def getInfo(self):
        return self.info

    def initUI(self):
        self.combo_board_thickness.Append([str(i) for i in BOARD_THICKNESS_CHOICE])
        self.combo_board_thickness.SetSelection(4)

        self.combo_outer_copper_thickness.Append( [f'{i}{OZ}' for i in OUTER_THICKNESS_CHOICE])
        self.combo_outer_copper_thickness.SetSelection(0)

        self.combo_inner_copper_thickness.Append([f'{i}{OZ}' for i in INNER_COPPER_THICKNESS_CHOICE])
        self.combo_inner_copper_thickness.SetSelection(0)

        self.combo_min_trace_width_clearance.Append(
     [ f'{i}/{i}{MIL}'  for i in      MIN_TRACE_WIDTH_CLEARANCE_CHOICE])
        self.combo_min_trace_width_clearance.SetSelection(2)

        self.combo_min_hole_size.Append( [ f'{i}{MM}' for i in  MIN_HOLE_SIZE_CHOICE])
        self.combo_min_hole_size.SetSelection(0)

        self.combo_solder_color.Append(SOLDER_COLOR_CHOICE)
        self.combo_solder_color.SetSelection(0)

        self.combo_silk_screen_color.Append(SILK_SCREEN_COLOR_CHOICE)
        self.combo_silk_screen_color.SetSelection(0)

        self.combo_solder_cover.Append(SOLDER_COVER_CHOICE)
        self.combo_solder_cover.SetSelection(0)

        self.combo_surface_process.Append(SURFACE_PROCESS_CHOICE)
        self.combo_surface_process.SetSelection(0)

        self.combo_gold_thickness.Append([f'{i}{GOLD_THICKNESS_CHOICE_UNIT}'  for i in GOLD_THICKNESS_CHOICE ])
        self.combo_gold_thickness.SetSelection(0)
