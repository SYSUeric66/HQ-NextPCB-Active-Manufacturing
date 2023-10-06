import wx
import wx.xrc
import wx.dataview
from wx import Plat

class OrderSummaryModel(wx.dataview.DataViewModel):
    def __init__(self):
        super().__init__()
