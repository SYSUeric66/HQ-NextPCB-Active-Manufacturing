from .ui_order_info import UiOrderInfo
from kicad_amf_plugin.icon import GetImagePath
from kicad_amf_plugin.language.lang_setting_pop_menu import LangSettingPopMenu
import wx
from .order_summary_model import OrderSummary, OrderSummaryModel
from .price_summary_model import PriceSummaryModel, ItemPrice

import wx.dataview as dv
from kicad_amf_plugin.settings.setting_manager import SETTING_MANAGER


class OrderInfoView(UiOrderInfo):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.list_order_summary.AppendTextColumn(
            "ITEM",  1, width=-1, mode=dv.DATAVIEW_CELL_ACTIVATABLE, align=wx.ALIGN_LEFT)
        self.list_order_summary.AppendTextColumn(
            "QUANTITY",   2, width=-1, mode=dv.DATAVIEW_CELL_ACTIVATABLE, align=wx.ALIGN_CENTER)
        self.list_order_summary.AppendTextColumn(
            "UNIT",   3, width=-1, mode=dv.DATAVIEW_CELL_ACTIVATABLE, align=wx.ALIGN_LEFT)

        self.list_order_summary.SetMinSize(
            wx.Size(-1, OrderInfoView.GetLineHeight(self) * 3 + 30))
        self.model_order_summary = OrderSummaryModel(OrderSummary())
        self.list_order_summary.AssociateModel(self.model_order_summary)

        self.list_price_detail.AppendTextColumn(
            "Item",  1, width=-1, mode=dv.DATAVIEW_CELL_ACTIVATABLE, align=wx.ALIGN_LEFT)
        self.list_price_detail.AppendTextColumn(
            "Price",   2, width=-1, mode=dv.DATAVIEW_CELL_ACTIVATABLE, align=wx.ALIGN_CENTER)
        price = []
        for i in range(1, 10):
            price.append(ItemPrice(f'TestItem{i}', i * 100))
        self.model_price_summary = PriceSummaryModel(price)
        self.list_price_detail.AssociateModel(self.model_price_summary)

        self.btn_set_language.Bind(wx.EVT_BUTTON, self.on_set_lang_clicked)

        self.radio_box_order_region.Bind

    def GetImagePath(self, bitmap_path):
        return GetImagePath(bitmap_path)

    @staticmethod
    def GetLineHeight(parent):
        line = wx.TextCtrl(parent)
        _, height = line.GetSize()
        line.Destroy()
        return height

    def on_set_lang_clicked(self, evt):
        menu = LangSettingPopMenu(SETTING_MANAGER.language)
        self.PopupMenu(menu)
        menu.Destroy()
