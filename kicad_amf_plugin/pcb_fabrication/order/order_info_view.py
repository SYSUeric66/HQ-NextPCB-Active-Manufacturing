from .ui_order_info import UiOrderInfo
from kicad_amf_plugin.icon import GetImagePath

class OrderInfoView(UiOrderInfo):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)


    def GetImagePath( self, bitmap_path ):
        return  GetImagePath(bitmap_path)
