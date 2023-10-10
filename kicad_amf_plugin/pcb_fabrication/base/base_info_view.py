from kicad_amf_plugin.kicad.board_manager import BoardManager
from kicad_amf_plugin.utils.two_step_setup import TwoStepSetup
from .base_info_model import BaseInfoModel
from kicad_amf_plugin.gui.event.pcb_fabrication_evt_list import LayerCountChange
from .ui_base_info import UiBaseInfo , BOX_SIZE_SETTING , BOX_PANEL_SETTING ,BOX_BREAK_AWAY
from kicad_amf_plugin.utils.validators  import  NumericTextCtrlValidator
from kicad_amf_plugin.utils.roles import EditDisplayRole
import pcbnew
import wx

def convert_pcb_geometry( base = 10, digit = 2):
    def decorate(fn):
        def wrapper(*args, **kwargs):
            return  round( fn(*args, **kwargs) / base ,digit)
        return wrapper
    return decorate



AVAILABLE_MATERIAL_TYPES = ["FR-4"]

AVAILABLE_BOARD_TG_TYPES = ["TG130"]

AVAILABLE_LAYER_COUNTS = [1, 2, 4, 6,
    8, 10, 12, 14, 16, 18, 20]


class PcbPackageKind:
    SINGLE_PIECE = 1 
    PANEL_BY_CUSTOMER =  3
    PANEL_BY_NEXT_PCB = 2

    PCB_PACKAGE_KIND = (  
        EditDisplayRole(SINGLE_PIECE,_(u"Single Piece") ),
        EditDisplayRole(PANEL_BY_CUSTOMER,_(u"Panel by Customer") ),
        EditDisplayRole(PANEL_BY_NEXT_PCB,_(u"Panel by NextPCB") )
    )

class MarginMode:
    NA = "N/A"
    LEFT_RIGHT =  "X" 
    TOP_BOTTOM =  "Y" 
    ALL_4_SIDE = "XY"

    MARGIN_MODE_CHOICE = [  
        EditDisplayRole(NA,  _(u"N/A") ),
        EditDisplayRole(LEFT_RIGHT, _(u"Left & Right")),
        EditDisplayRole(TOP_BOTTOM,  _(u"Top & Bottom") ),
        EditDisplayRole(ALL_4_SIDE,  _(u"All 4 sides") )
    ]


AVAILABLE_QUANTITY = [5, 10, 15, 20, 25, 30, 40, 50, 75, 100, 125, 150, 200, 250, 300, 350, 400, 450, 500, 600,
    700, 800, 900, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 9000, 10000]


class BaseInfoView(UiBaseInfo,TwoStepSetup):
    def __init__(self, parent, board_manager : BoardManager  ):
        super().__init__(parent)
        self.board_manager = board_manager

        self.combo_pcb_package_kind.Bind(wx.EVT_CHOICE, self.on_pcb_packaging_changed)
        self.comb_margin_mode.Bind(wx.EVT_CHOICE, self.on_margin_mode_changed)
        self.combo_layer_count.Bind(wx.EVT_CHOICE , self.on_layer_count_changed)
        for editor in self.edit_panel_x , self.edit_panel_y ,self.edit_margin_size:
            editor.SetValidator(NumericTextCtrlValidator())

    @property
    def box_piece_or_panel_size(self):
        return  self.FindWindowById(BOX_SIZE_SETTING)
    
    @property
    def box_panel_setting(self):
        return  self.FindWindowById(BOX_PANEL_SETTING)
    
    @property
    def box_break_away(self):
        return  self.FindWindowById(BOX_BREAK_AWAY)
    
    @property
    def pcb_package_kind(self):
        return  PcbPackageKind.PCB_PACKAGE_KIND[int(self.combo_pcb_package_kind.GetSelection())].EditRole    

    @property
    def margin_mode(self):
        return  MarginMode.MARGIN_MODE_CHOICE[int(self.comb_margin_mode.GetSelection())].EditRole         

    @convert_pcb_geometry()
    def get_pcb_length(self):
        if self.pcb_package_kind == PcbPackageKind.SINGLE_PIECE:
            if self.margin_mode in ( MarginMode.LEFT_RIGHT , MarginMode.ALL_4_SIDE ):
                return float(self.edit_size_x.GetValue()) + float(self.edit_margin_size.GetValue()) * 2
            else:
                return float(self.edit_size_x.GetValue())
        else:
            if self.margin_mode in (  MarginMode.LEFT_RIGHT , MarginMode.ALL_4_SIDE ):
                return float(self.edit_size_x.GetValue()) * int(self.edit_panel_x.GetValue()) + float(self.edit_margin_size.GetValue()) * 2
            else:
                return float(self.edit_size_x.GetValue()) * int(self.edit_panel_x.GetValue())       
             
    @convert_pcb_geometry()
    def get_pcb_width(self):
        if self.pcb_package_kind == PcbPackageKind.SINGLE_PIECE:
            if self.margin_mode in (  MarginMode.LEFT_RIGHT , MarginMode.ALL_4_SIDE ):
                return float(self.edit_size_y.GetValue()) + float(self.edit_margin_size.GetValue()) * 2
            else:
                return float(self.edit_size_y.GetValue())
        else:
            if self.margin_mode in (  MarginMode.LEFT_RIGHT , MarginMode.ALL_4_SIDE ):
                return float(self.edit_size_y.GetValue()) * int(self.edit_panel_y.GetValue()) + float(self.edit_margin_size.GetValue()) * 2
            else:
                return float(self.edit_size_y.GetValue()) * int(self.edit_panel_y.GetValue())                    

    @property
    def base_info(self):
        data = BaseInfoModel(
            blayer=  self.combo_layer_count.GetStringSelection() ,
            plate_type=AVAILABLE_MATERIAL_TYPES[0] , 
            board_tg =AVAILABLE_BOARD_TG_TYPES[0],
            units = str(self.pcb_package_kind),
            blength = str(self.get_pcb_length()),
            bwidth= str(self.get_pcb_width()),
            bcount= self.combo_quantity.GetStringSelection(),
            sidedirection= str(self.margin_mode)
        )

        if self.pcb_package_kind in (PcbPackageKind.PANEL_BY_CUSTOMER , PcbPackageKind.PANEL_BY_NEXT_PCB) :
            data.layoutx = self.edit_panel_x.GetValue()
            data.layouty  =self.edit_panel_y.GetValue()

        if self.margin_mode != MarginMode.NA:
            data.sidewidth = self.edit_margin_size.GetValue()
    
        return data


    def init(self):
        self.initUI()
        self.loadBoardInfo()

    def getBaseInfo(self):
        return self.base_info
        
    def initUI(self):
        self.combo_material_type.Append(AVAILABLE_MATERIAL_TYPES)
        self.combo_material_type.SetSelection(0)

        self.combo_layer_count.AppendItems( [ str(i) for i in AVAILABLE_LAYER_COUNTS] )
        self.combo_layer_count.SetSelection(1)

        self.combo_pcb_package_kind.Append([ i.DisplayRole for i in PcbPackageKind.PCB_PACKAGE_KIND ])
        self.comb_margin_mode.Append( [i.DisplayRole for i in MarginMode.MARGIN_MODE_CHOICE ])


        self.combo_quantity.Append([  str(i)  for i in AVAILABLE_QUANTITY ])
        self.combo_quantity.SetSelection(0)

        self.comb_margin_mode.SetSelection(0)
        self.combo_pcb_package_kind.SetSelection(0)

        for i in self.edit_size_x  , self.edit_size_y:
            i.SetEditable(False)
        self.edit_margin_size.Enabled = False
        self.box_panel_setting.Enabled = False  

    def loadBoardInfo(self):
        boardWidth = pcbnew.ToMM(
            self.board_manager.board.GetBoardEdgesBoundingBox().GetWidth())
        boardHeight = pcbnew.ToMM(
            self.board_manager.board.GetBoardEdgesBoundingBox().GetHeight())
        layerCount = self.board_manager.board.GetCopperLayerCount()
        self.combo_layer_count.SetSelection(
            self.combo_layer_count.FindString(str(layerCount)))
        self.combo_layer_count.Enabled = False
        self.edit_size_x.SetValue(str(boardWidth))
        self.edit_size_y.SetValue(str(boardHeight))              


    def on_pcb_packaging_changed(self , evt = None):
        if self.pcb_package_kind == PcbPackageKind.SINGLE_PIECE:
            self.box_piece_or_panel_size.SetLabelText(_('Size (single)'))
            self.label_quantity.SetLabel(_('Qty(single)'))
            self.label_quantity_unit.SetLabel(_('Pcs'))
        else:
            self.box_piece_or_panel_size.SetLabelText(_('Size (set)'))
            self.label_quantity.SetLabel(_('Qty(Set)'))
            self.label_quantity_unit.SetLabel(_('Set'))
        
        self.box_panel_setting.Enabled = self.pcb_package_kind  == PcbPackageKind.PANEL_BY_NEXT_PCB # Only while the option is by HuaQiu
        self.box_break_away.Enabled = self.pcb_package_kind  != PcbPackageKind.PANEL_BY_CUSTOMER  # Only Disabled while the option is by customer
        self.on_margin_mode_changed()
   
    def on_margin_mode_changed(self, event = None):
        self.edit_margin_size.Enabled = self.margin_mode != MarginMode.NA

    def on_layer_count_changed(self, evt):
        evt = LayerCountChange(id = -1)
        evt.SetInt(int(self.combo_layer_count.GetStringSelection()))
        wx.PostEvent(self.Parent ,evt)



