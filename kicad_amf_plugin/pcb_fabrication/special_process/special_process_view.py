
from kicad_amf_plugin.kicad.board_manager import BoardManager
from .ui_special_process import UiSpecialProcess
from .special_process_model import SpecialProcessModel
import wx
import wx.xrc
import wx.dataview
from kicad_amf_plugin.utils.constraint import BOOLEAN_CHOICE
from .special_process_model import SpecialProcessModel



HDI_STRUCTURE_CHOICE = [_(u"Rank 1"), _(u"Rank 2"), _(u"Rank 3")]

STACKUP_CHOICE = [_(u"No Requirement"), _(
    u"Customer Specified Stack up")]


class SpecialProcessView(UiSpecialProcess):
    def __init__(self, parent, board_manager : BoardManager ):
        super().__init__(parent)
        self.board_manager = board_manager
        self.special_process: SpecialProcessModel = None

        self.initUI()

        self.combo_blind_via.Enabled = self.board_manager.board.GetCopperLayerCount() != 2
        self.combo_blind_via.Bind(wx.EVT_CHOICE, self.on_HDI_changed)

    
    def special_process(self):
        info = SpecialProcessModel(

        )
        if self.layer_count > 2 and self.combo_stackup.GetSelection() != 0:
            info.pressing =  'Customer Specified Stack up'
        return info

    @property
    def layer_count(self):
        return self.board_manager.board.GetCopperLayerCount()

    def initUI(self):
        for ctrl in self.combo_impedance, self.combo_goldFinger, self.combo_halfHole,  self.combo_pad_hole, self.combo_blind_via:
            for i in BOOLEAN_CHOICE:
                ctrl.Append(_(i))
            ctrl.SetSelection(0)

        self.combo_hdi_structure.Append(HDI_STRUCTURE_CHOICE)
        self.combo_hdi_structure.SetSelection(0)

        self.combo_stackup.Append(STACKUP_CHOICE)
        self.combo_stackup.SetSelection(0)
        self.combo_hdi_structure.Enabled = False

    
    def on_HDI_changed(self, event):
        self.combo_hdi_structure.Enabled = self.combo_blind_via.GetSelection() == 1

    def on_layer_count_changed(self, event):
        self.combo_blind_via.Enabled = event.GetInt() > 2 
        if not  self.combo_blind_via.Enabled :
            self.combo_blind_via.SetSelection(0)
            self.combo_hdi_structure.Enabled = False
                