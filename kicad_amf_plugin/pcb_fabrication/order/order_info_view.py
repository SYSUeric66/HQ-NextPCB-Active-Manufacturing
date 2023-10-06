from .ui_order_info import UiOrderInfo
from kicad_amf_plugin.icon import GetImagePath
from kicad_amf_plugin.language.lang_setting_pop_menu import LangSettingPopMenu
import wx
from kicad_amf_plugin.utils.platebtn import PlateButton ,PB_STYLE_SQUARE,PB_STYLE_GRADIENT ,AdjustColour


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
        self.btn_set_language.Bind(wx.EVT_BUTTON,self.OnTool )
        self.Bind(wx.EVT_BUTTON, self.OnTool, self.btn_set_language)

        self.list_price_detail.AppendTextColumn("Item")
        self.list_price_detail.AppendTextColumn("Price")

        self.list_price_detail.AppendItem(["AAAAAA" ,"$1000"])
        self.list_price_detail.AppendItem(["BBBBB" ,"$200000"])
        self.list_price_detail.AppendItem(["CCCCC" ,"$30000"])

    def GetImagePath( self, bitmap_path ):
        return  GetImagePath(bitmap_path)

    @staticmethod
    def GetLineHeight(parent):
        line = wx.TextCtrl(parent)
        _,height = line.GetSize()
        line.Destroy()
        return height

    def OnTool(self, evt):

        win = LangSettingPopMenu(self,
                                 wx.SIMPLE_BORDER
                            )

        # Show the popup right below or above the button
        # depending on available screen space...
        btn = evt.GetEventObject()
        pos = btn.ClientToScreen( (0,0) )
        sz =  btn.GetSize()
        win.Position(pos, (0, sz[1]))

        win.Popup()
