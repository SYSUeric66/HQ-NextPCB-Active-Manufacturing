from .base_info_model import BaseInfoModel
from .ui_base_info import UiBaseInfo
import wx
import wx.xrc
import wx.dataview

import gettext
_ = gettext.gettext


AVAILABLE_MATERIAL_TYPES = [_(u"FR-4")]

AVAILABLE_LAYER_COUNTS = [_(u"1"), _(u"2"), _(u"4"), _(u"6"), _(
    u"8"), _(u"10"), _(u"12"), _(u"14"), _(u"16"), _(u"18"), _(u"20")]

PCB_PACKAGE_KIND = [_(u"Single Piece"), _(
    u"Panel by Customer"), _(u"Panel by NextPCB")]


AVAILABLE_QUANTITY = [_(u"5"), _(u"10"), _(u"15"), _(u"20"), _(u"25"), _(u"30"), _(u"40"), _(u"50"), _(u"75"), _(u"100"), _(u"125"), _(u"150"), _(u"200"), _(u"250"), _(u"300"), _(u"350"), _(u"400"), _(u"450"), _(u"500"), _(u"600"), _(
    u"700"), _(u"800"), _(u"900"), _(u"1000"), _(u"1500"), _(u"2000"), _(u"2500"), _(u"3000"), _(u"3500"), _(u"4000"), _(u"4500"), _(u"5000"), _(u"5500"), _(u"6000"), _(u"6500"), _(u"7000"), _(u"7500"), _(u"8000"), _(u"9000"), _(u"10000")]

MARGIN_MODE_CHOICE = [
    _(u"N/A"), _(u"Left & Right"), _(u"Top & Bottom"), _(u"All 4 sides")]


class BaseInfoView(UiBaseInfo):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.base_info = None
        self.initUI()

    def getBaseInfo(self):
        return self.base_info

    def initUI(self):
        self.combo_material_type.Append(AVAILABLE_MATERIAL_TYPES)
        self.combo_material_type.SetSelection(0)

        self.combo_layer_count.AppendItems(AVAILABLE_LAYER_COUNTS)
        self.combo_layer_count.SetSelection(1)

        self.pcb_package_kind.Append(PCB_PACKAGE_KIND)
        self.pcb_package_kind.SetSelection(0)

        self.combo_quantity.Append(AVAILABLE_QUANTITY)
        self.combo_quantity.SetSelection(0)

        self.comb_margin_mode.Append(MARGIN_MODE_CHOICE)
        self.comb_margin_mode.SetSelection(0)
