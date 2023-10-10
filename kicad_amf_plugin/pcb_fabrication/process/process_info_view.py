
from kicad_amf_plugin.kicad.board_manager import BoardManager
from kicad_amf_plugin.utils.roles import EditDisplayRole
from .process_info_model import ProcessInfoModel
from kicad_amf_plugin.utils.two_step_setup import TwoStepSetup

from .ui_process_info import UiProcessInfo
import wx
import pcbnew


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

SOLDER_COVER_CHOICE = [_(u"Tenting Vias"), _(u"Vias not covered"), _(
    u"Solder Mask Plug (IV-B)"), _(u"Non-Conductive Fill")]

SURFACE_PROCESS_CHOICE = [_(u"HASL"), _(
    u"Lead free HASL"), _(u"ENIG"), _(u"OSP")]

GOLD_THICKNESS_CHOICE = [1, 2, 3]

GOLD_THICKNESS_CHOICE_UNIT = "µm"

SILK_SCREEN_COLOR_BY_SOLDER_COLOR = {
    _("Green") :[_("White")],
    _("Red"):[_("White")],
    _("Yellow"):[_("White")],
    _("Blue"):[_("White")],
    _("White"):[_("Black")],
    _("Matte Black"):[_("White")],
    _("Black"):[_("White")]
}

class ProcessInfoView(UiProcessInfo ,TwoStepSetup):
    def __init__(self, parent , board_manager : BoardManager ):
        super().__init__(parent)
        self.board_manager = board_manager

        self.combo_surface_process.Bind(wx.EVT_CHOICE  , self.on_surface_process_changed)
        self.combo_solder_color.Bind(wx.EVT_CHOICE, self.OnMaskColorChange)

        self.Fit()

    @property
    def process_info(self):
        info = ProcessInfoModel(
            bheight = self.combo_board_thickness.GetStringSelection(),
            copper= str(self.combo_outer_copper_thickness.GetStringSelection()).removesuffix(OZ) ,
            lineweight= str(self.combo_min_trace_width_clearance.GetStringSelection()).split('/')[0],
            vias=str(self.combo_min_hole_size.GetStringSelection()).removesuffix(MM),

            color = self.combo_solder_color.GetStringSelection(),
            charcolor= self.combo_silk_screen_color.GetStringSelection(),
            cover= self.combo_solder_cover.GetStringSelection(),
            spray= self.combo_surface_process.GetStringSelection(),

        )

        if(self.layer_count > 2):
            info.insidecopper = str(self.combo_inner_copper_thickness.GetStringSelection()).removesuffix(OZ)
        
        if(self.combo_surface_process.GetCurrentSelection() == 2):
            info.cjh =  str(self.combo_gold_thickness.GetCurrentSelection() + 1)


    def init(self):
        self.initUI()
        self.loadBoardInfo()


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

        self.combo_silk_screen_color.Append(SILK_SCREEN_COLOR_BY_SOLDER_COLOR[self.combo_solder_color.GetStringSelection()])
        self.combo_silk_screen_color.SetSelection(0)

        self.combo_solder_cover.Append(SOLDER_COVER_CHOICE)
        self.combo_solder_cover.SetSelection(0)

        self.combo_surface_process.Append(SURFACE_PROCESS_CHOICE)
        self.combo_surface_process.SetSelection(0)

        self.combo_gold_thickness.Append([f'{i}{GOLD_THICKNESS_CHOICE_UNIT}'  for i in GOLD_THICKNESS_CHOICE ])
        self.combo_gold_thickness.SetSelection(0) 
              
    @property
    def layer_count(self):
        return self.board_manager.board.GetCopperLayerCount()

    def loadBoardInfo(self):
        for i in self.label_immersion_gold , self.combo_gold_thickness : 
            i.Enabled = False    
        designSettings = self.board_manager.board.GetDesignSettings()
        boardThickness = designSettings.GetBoardThickness()
        minTraceWidth = designSettings.m_TrackMinWidth
        minTraceClearance = designSettings.m_MinClearance
        minHoleSize = designSettings.m_MinThroughDrill
        self.combo_inner_copper_thickness.Enabled = self.layer_count > 2

        self.set_board_thickness(pcbnew.ToMM(boardThickness))
        self.set_min_trace(pcbnew.ToMils(minTraceWidth),
                         pcbnew.ToMils(minTraceClearance))
        self.set_min_hole(pcbnew.ToMM(minHoleSize))

    def on_layer_count_changed(self, event):
        layer_count =  event.GetInt()
        self.combo_board_thickness.Clear()
        val_list =THICKNESS_SETTING[str(layer_count)]
        self.combo_board_thickness.Append(val_list)
        self.combo_board_thickness.SetSelection(0)

    def on_surface_process_changed(self , evt = None  ):
        for i in self.label_immersion_gold , self.combo_gold_thickness : 
            i.Enabled = self.combo_surface_process.GetSelection() == 2


    def set_board_thickness(self, thickness):
        for i in range(self.combo_board_thickness.GetCount()):
            if thickness <= float(self.combo_board_thickness.GetString(i)):
                self.combo_board_thickness.SetSelection(i)
                break

    def set_min_trace(self, minTraceWidth, minTraceClearance):
        if minTraceWidth == 0 and minTraceClearance == 0:
            minTrace = 6
        elif minTraceWidth == 0:
            minTrace = minTraceClearance
        elif minTraceClearance == 0:
            minTrace = minTraceWidth
        else:
            minTrace = min(minTraceWidth, minTraceClearance)

        if minTrace == 0:
            minTrace = 6
            self.combo_min_trace_width_clearance.SetSelection(2)
        elif minTrace >= 10:
            minTrace = 10
            self.combo_min_trace_width_clearance.SetSelection(0)
        elif minTrace >= 8:
            minTrace = 8
            self.combo_min_trace_width_clearance.SetSelection(1)
        elif minTrace >= 6:
            minTrace = 6
            self.combo_min_trace_width_clearance.SetSelection(2)
        elif minTrace >= 5:
            minTrace = 5
            self.combo_min_trace_width_clearance.SetSelection(3)
        elif minTrace >= 4:
            minTrace = 4
            self.combo_min_trace_width_clearance.SetSelection(4)
        else:
            minTrace = 3.5
            self.combo_min_trace_width_clearance.SetSelection(5)

    def set_min_hole(self, minHoleSize):
        if minHoleSize == 0:
            minHoleSize = 0.3
            self.combo_min_hole_size.SetSelection(0)
        elif minHoleSize >= 0.3:
            minHoleSize = 0.3
            self.combo_min_hole_size.SetSelection(0)
        elif minHoleSize >= 0.25:
            minHoleSize = 0.25
            self.combo_min_hole_size.SetSelection(1)
        elif minHoleSize >= 0.2:
            minHoleSize = 0.2
            self.combo_min_hole_size.SetSelection(2)
        else:
            minHoleSize = 0.15
            self.combo_min_hole_size.SetSelection(3)

    def OnMaskColorChange(self, event):
        self.combo_silk_screen_color.Clear()
        self.combo_silk_screen_color.Append(SILK_SCREEN_COLOR_BY_SOLDER_COLOR[self.combo_solder_color.GetStringSelection()])
        self.combo_silk_screen_color.SetSelection(0)