from dataclasses import dataclass
import wx.dataview as dv
from kicad_amf_plugin.settings.setting_manager import SETTING_MANAGER
from enum import Enum

from collections import namedtuple


AVAILABLE_TIME_UNIT = {
    'days':   _('days'),
    'hours' : _('hours')
}

BuildTime = namedtuple('BuildTime' ,['Time' ,'Unit'])


class OrderSummaryCol(Enum):
    BUILD_TIME = 0
    QUANTITY = BUILD_TIME + 1
    PRICE = QUANTITY + 1

    COL_COUNT =  PRICE + 1


@dataclass
class OrderSummary:
    pcb_quantity : int
    build_time: BuildTime 
    price: float 


class OrderSummaryModel(dv.DataViewIndexListModel):
    def __init__(self):
        dv.DataViewIndexListModel.__init__(self, 0)
        self.orders_summary : 'list[OrderSummary]' = []

    # This method is called to provide the data object for a
    # particular row,col
    def GetValueByRow(self, row  : int , col : int):
        order = self.orders_summary[row]
        map = {
            OrderSummaryCol.BUILD_TIME : SETTING_MANAGER.get_build_time_formatter().format(time  = order.build_time.Time , unit = order.build_time.Unit),
            OrderSummaryCol.QUANTITY : order.pcb_quantity,
            OrderSummaryCol.PRICE :  f'{SETTING_MANAGER.get_price_unit(True)}{order.price}'
        }
        return map[col]
    
    # Report how many columns this model provides data for.
    def GetColumnCount(self):
        return OrderSummaryCol.COL_COUNT

    # Specify the data type for a column
    def GetColumnType(self, col):
        return "string"

    def SetValueByRow(self, value, row, col):
        return False

    # Report the number of rows in the model
    def GetCount(self):
        # self.log.write('GetCount')
        return len(self.orders_summary)

    # Called to check if non-standard attributes should be used in the
    # cell at (row, col)
    def GetAttrByRow(self, row, col, attr):
        # self.log.write('GetAttrByRow: (%d, %d)' % (row, col))
        # if col == 3:
        #     attr.SetColour('red')
        #     attr.SetBold(True)
        #     return True
        return False

    def update_order_info(self, data: OrderSummary):
        self.orders_summary = data
        self.Cleared()
