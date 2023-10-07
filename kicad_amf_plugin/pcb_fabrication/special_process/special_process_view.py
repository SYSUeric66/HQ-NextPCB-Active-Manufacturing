
from .ui_special_process import UiSpecialProcess
from .special_process_model import SpecialProcessModel
import wx
import wx.xrc
import wx.dataview
from kicad_amf_plugin.utils.constraint import BOOLEAN_CHOICE





HDI_STRUCTURE_CHOICE = [_(u"Rank 1"), _(u"Rank 2"), _(u"Rank 3")]

STACKUP_CHOICE = [_(u"No Requirement"), _(
    u"Customer Specified Stack up")]


class SpecialProcessView(UiSpecialProcess):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.special_process: SpecialProcessModel = None
        self.initUI()

    def getBaseInfo(self):
        return self.special_process

    def initUI(self):
        for ctrl in self.combo_impedance, self.combo_goldFinger, self.combo_halfHole,  self.combo_pad_hole, self.combo_blind_via:
            for i in BOOLEAN_CHOICE:
                ctrl.Append(_(i))
            ctrl.SetSelection(0)

        self.combo_hdi_structure.Append(HDI_STRUCTURE_CHOICE)
        self.combo_hdi_structure.SetSelection(0)

        self.combo_stackup.Append(STACKUP_CHOICE)
        self.combo_stackup.SetSelection(0)
