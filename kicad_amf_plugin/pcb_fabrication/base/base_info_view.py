from kicad_amf_plugin.kicad.board_manager import BoardManager
from .base_info_model import BaseInfoModel
from .ui_base_info import UiBaseInfo , BOX_SIZE_SETTING , BOX_PANEL_SETTING ,BOX_BREAK_AWAY
import pcbnew

import wx


AVAILABLE_MATERIAL_TYPES = ["FR-4"]

AVAILABLE_LAYER_COUNTS = [1, 2, 4, 6,
    8, 10, 12, 14, 16, 18, 20]


PCB_PACKAGE_KIND = [_(u"Single Piece"),
    _(u"Panel by Customer"), _(u"Panel by NextPCB")]


AVAILABLE_QUANTITY = [5, 10, 15, 20, 25, 30, 40, 50, 75, 100, 125, 150, 200, 250, 300, 350, 400, 450, 500, 600,
    700, 800, 900, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 9000, 10000]

MARGIN_MODE_CHOICE = [
    _(u"N/A"), _(u"Left & Right"), _(u"Top & Bottom"), _(u"All 4 sides")]


class BaseInfoView(UiBaseInfo):
    def __init__(self, parent, board_manager : BoardManager  ):
        super().__init__(parent)
        self.base_info = None
        self.board_manager = board_manager
        self.initUI()
        self.loadBoardInfo()
        self.Fit()

        self.combo_pcb_package_kind.Bind(wx.EVT_CHOICE, self.OnPcbPackagingChanged)
        self.comb_margin_mode.Bind(wx.EVT_CHOICE, self.OnMarginModeChanged)


    @property
    def board(self):
        return self.board_manager.board

    def getBaseInfo(self):
        return self.base_info
        
    def loadBoardInfo(self):
        boardWidth = pcbnew.ToMM(
            self.board.GetBoardEdgesBoundingBox().GetWidth())
        boardHeight = pcbnew.ToMM(
            self.board.GetBoardEdgesBoundingBox().GetHeight())
        layerCount = self.board.GetCopperLayerCount()
        self.combo_layer_count.SetSelection(
            self.combo_layer_count.FindString(str(layerCount)))
        self.combo_layer_count.Enabled = False
        self.edit_size_x.SetValue(str(boardWidth))
        self.edit_size_y.SetValue(str(boardHeight))
        for i in self.edit_panel_x  , self.edit_panel_y:
            i.SetEditable(False)
        self.edit_margin_size.Enabled = False
        self.box_panel_setting.Enabled = False

    def initUI(self):
        self.combo_material_type.Append(AVAILABLE_MATERIAL_TYPES)
        self.combo_material_type.SetSelection(0)

        self.combo_layer_count.AppendItems( [ str(i) for i in AVAILABLE_LAYER_COUNTS] )
        self.combo_layer_count.SetSelection(1)

        self.combo_pcb_package_kind.Append(PCB_PACKAGE_KIND)
        self.combo_pcb_package_kind.SetSelection(0)

        self.combo_quantity.Append([  str(i)  for i in AVAILABLE_QUANTITY ])
        self.combo_quantity.SetSelection(0)

        self.comb_margin_mode.Append(MARGIN_MODE_CHOICE)
        self.comb_margin_mode.SetSelection(0)

    @property
    def box_piece_or_panel_size(self):
        return  self.FindWindowById(BOX_SIZE_SETTING)
    
    @property
    def box_panel_setting(self):
        return  self.FindWindowById(BOX_PANEL_SETTING)
    
    @property
    def box_break_away(self):
        return  self.FindWindowById(BOX_BREAK_AWAY)    


    def OnPcbPackagingChanged(self , evt = None):
        if self.combo_pcb_package_kind.GetSelection() == 0:
            self.box_piece_or_panel_size.SetLabelText(_('Size (single)'))
            self.label_quantity.SetLabel(_('Qty(single)'))
            self.label_quantity_unit.SetLabel(_('Pcs'))
        else:
            self.box_piece_or_panel_size.SetLabelText(_('Size (set)'))
            self.label_quantity.SetLabel(_('Qty(Set)'))
            self.label_quantity_unit.SetLabel(_('Set'))
        
        self.box_panel_setting.Enabled = self.combo_pcb_package_kind.GetSelection() == 2 # Only while the option is by HuaQiu
        self.box_break_away.Enabled = self.combo_pcb_package_kind.GetSelection() != 1  # Only Disabled while the option is by customer
        self.OnMarginModeChanged()
   
    def OnMarginModeChanged(self, event = None):
        self.edit_margin_size.Enabled = self.comb_margin_mode.GetSelection() != 0