
from kicad_amf_plugin.kicad.board_manager import BoardManager
from kicad_amf_plugin.order.order_region import SupportedRegion
from kicad_amf_plugin.settings.setting_manager import SETTING_MANAGER
from kicad_amf_plugin.utils.none_value_fitter import none_value_fitter
from .ui_special_process import UiSpecialProcess
from .special_process_model import SpecialProcessModel
import wx
import wx.xrc
import wx.dataview
from kicad_amf_plugin.utils.constraint import BOOLEAN_CHOICE
from .special_process_model import SpecialProcessModel
from kicad_amf_plugin.utils.form_panel_base import FormPanelBase
from kicad_amf_plugin.utils.validators import NumericTextCtrlValidator , FloatTextCtrlValidator

HDI_STRUCTURE_CHOICE = [_(u"Rank 1"), _(u"Rank 2"), _(u"Rank 3")]

STACKUP_CHOICE = [_(u"No Requirement"), _(
    u"Customer Specified Stack up")]


class SpecialProcessView(UiSpecialProcess,FormPanelBase):
    def __init__(self, parent, board_manager: BoardManager):
        super().__init__(parent)
        self.board_manager = board_manager

        self.initUI()
        self.combo_blind_via.Enabled = self.board_manager.board.GetCopperLayerCount() != 2
        self.combo_blind_via.Bind(wx.EVT_CHOICE, self.on_HDI_changed)


    def is_valid(self) -> bool:
        return True

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
        self.combo_baobian.Append([ str(i) for i in range(0 , 5)])
        self.combo_baobian.SetSelection(0)
        
    @none_value_fitter    
    def get_from(self) -> 'dict' :
        info = SpecialProcessModel(
            impendance= str(self.combo_impedance.GetSelection()),
            bankong= str(self.combo_halfHole.GetSelection()),
            blind=self.GetBlindValue(),
            via_in_pad='N/A' if self.combo_pad_hole.GetStringSelection() else 'Have',
            beveledge=str(self.combo_goldFinger.GetSelection()) ,
            baobian= self.combo_baobian.GetStringSelection(),
            bga= self.edit_bga.GetValue(),
            zknum= self.edit_turnhole_density.GetValue()
        )
        if self.layer_count > 2 and self.combo_stackup.GetSelection() != 0:
            info.pressing = 'Customer Specified Stack up'
        return  vars(info)

    @property
    def layer_count(self):
        return self.board_manager.board.GetCopperLayerCount()

    def on_HDI_changed(self, event):
        self.combo_hdi_structure.Enabled = self.combo_blind_via.GetSelection() == 1

    def on_layer_count_changed(self, event):
        self.combo_blind_via.Enabled = event.GetInt() > 2
        if not self.combo_blind_via.Enabled:
            self.combo_blind_via.SetSelection(0)
            self.combo_hdi_structure.Enabled = False

    def GetBlindValue(self):
        if self.combo_blind_via.GetSelection() == 0:
            return "0"
        elif self.combo_hdi_structure.GetSelection() == 0:
            return "1"
        elif self.combo_hdi_structure.GetSelection() == 1:
            return "2"
        elif self.combo_hdi_structure.GetSelection() == 2:
            return "3"
        
    def on_region_changed(self):
        pass
