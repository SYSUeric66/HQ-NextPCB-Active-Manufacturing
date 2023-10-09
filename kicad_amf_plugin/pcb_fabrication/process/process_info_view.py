
from kicad_amf_plugin.kicad.board_manager import BoardManager
from .process_info_model import ProcessInfoModel

from .ui_process_info import UiProcessInfo
import wx


THICKNESS_SETTING = {
            "1":["0.6","0.8","1.0","1.2","1.6"],
            "2":["0.6","0.8","1.0","1.2","1.6"],
            "4":["0.6","0.8","1.0","1.2","1.6","2.0","2.5"],
            "6":["1.0","1.2","1.6","2.0","2.5"],
            "8":["1.2","1.6","2.0","2.5"],
            "10":["1.2","1.6","2.0","2.5"],
            "12":["1.6","2.0","2.5"],
            "14":["1.6","2.0","2.5","3.0"],
            "16":["2.0","2.5","3.0"],
            "18":["2.0","2.5","3.0","3.2"],
            "20":["2.0","2.5","3.0","3.2"]
}

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
    def __init__(self, parent , board_manager : BoardManager ):
        super().__init__(parent)
        self.info: ProcessInfoModel = None
        self.board_manager = board_manager

        self.initUI()
        self.combo_surface_process.Bind(wx.EVT_CHOICE  , self.on_surface_process_changed)



        self.loadBoardInfo()
        self.Fit()


    def initUI(self):
        self.combo_board_thickness.Append(THICKNESS_SETTING["1"])
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

      

    def loadBoardInfo(self):
        for i in self.label_immersion_gold , self.combo_gold_thickness : 
            i.Enabled = False  

    def on_layer_count_changed(self, event):
        layer_count =  event.GetInt()
        self.combo_board_thickness.Clear()
        val_list =THICKNESS_SETTING[str(layer_count)]
        self.combo_board_thickness.Append(val_list)
        self.combo_board_thickness.SetSelection(0)

    def on_surface_process_changed(self , evt = None  ):
        for i in self.label_immersion_gold , self.combo_gold_thickness : 
            i.Enabled = self.combo_surface_process.GetSelection() == 2