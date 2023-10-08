from kicad_amf_plugin.kicad.board_manager import BoardManager
from .base_info_model import BaseInfoModel
from .ui_base_info import UiBaseInfo
import pcbnew




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
        self.edit_size_x.SetEditable(False)
        self.edit_size_y.SetValue(str(boardHeight))
        self.edit_size_y.SetEditable(False)

    def initUI(self):
        self.combo_material_type.Append(AVAILABLE_MATERIAL_TYPES)
        self.combo_material_type.SetSelection(0)

        self.combo_layer_count.AppendItems( [ str(i) for i in AVAILABLE_LAYER_COUNTS] )
        self.combo_layer_count.SetSelection(1)

        self.pcb_package_kind.Append(PCB_PACKAGE_KIND)
        self.pcb_package_kind.SetSelection(0)

        self.combo_quantity.Append([  str(i)  for i in AVAILABLE_QUANTITY ])
        self.combo_quantity.SetSelection(0)

        self.comb_margin_mode.Append(MARGIN_MODE_CHOICE)
        self.comb_margin_mode.SetSelection(0)
