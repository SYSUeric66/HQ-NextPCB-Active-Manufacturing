from .ui_order_info import UiOrderInfo
from kicad_amf_plugin.icon import GetImagePath
import wx

class OrderInfoView(UiOrderInfo):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.list_order_summary.AppendTextColumn("Text")
        self.list_order_summary.AppendTextColumn("Text")
        self.list_order_summary.AppendTextColumn("Text")
        self.list_order_summary.AppendItem(["PCB Quantity" ,"NA","pcs"])
        self.list_order_summary.AppendItem(["Time" ,"NA","days"])
        self.list_order_summary.AppendItem(["Cost" ,"NA","$"])
        self.list_order_summary.SetMinSize(wx.Size(-1 , OrderInfoView.GetLineHeight(self) *3 + 30))

    def GetImagePath( self, bitmap_path ):
        return  GetImagePath(bitmap_path)

    @staticmethod
    def GetLineHeight(parent):
        line = wx.TextCtrl(parent)
        _,height = line.GetSize()
        line.Show(False)
        del line
        return height
