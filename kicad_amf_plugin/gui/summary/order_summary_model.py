from dataclasses import dataclass
import wx.dataview as dv
from kicad_amf_plugin.settings.setting_manager import SETTING_MANAGER ,TRANSLATED_PRICE_UNIT


@dataclass
class OrderSummary:
    pcb_quantity: int = 0
    days: int = 0
    cost: int = 0


ORDER_SUMMARY_ROW_COUNT = 3
ORDER_SUMMARY_COL_COUNT = 3


PCB_QUANTITY = 0
DAYS = 1
COST = 2


DESC = 1
VALUE = DESC + 1
UNIT = VALUE + 1


class OrderSummaryModel(dv.DataViewIndexListModel):
    def __init__(self, data: OrderSummary):
        dv.DataViewIndexListModel.__init__(self, ORDER_SUMMARY_ROW_COUNT)
        self.summary = data

    # This method is called to provide the data object for a
    # particular row,col
    def GetValueByRow(self, row, col):
        if PCB_QUANTITY == row:
            if DESC == col:
                return _("PCB Quantity")
            elif VALUE == col:
                return f'{self.summary.pcb_quantity}' if self.summary.pcb_quantity else "-"
            elif UNIT == col:
                return _("pcs")

        elif DAYS == row:
            if DESC == col:
                return _("Time")
            elif VALUE == col:
                return f'{self.summary.days}' if self.summary.pcb_quantity else "-"
            elif UNIT == col:
                return _("days")

        elif COST == row:
            if DESC == col:
                return _("Cost")
            elif VALUE == col:
                return f'{self.summary.cost}' if self.summary.pcb_quantity else "-"
            elif UNIT == col:
                return SETTING_MANAGER.get_price_unit(True)

    # Report how many columns this model provides data for.
    def GetColumnCount(self):
        return ORDER_SUMMARY_COL_COUNT

    # Specify the data type for a column
    def GetColumnType(self, col):
        return "string"

    def SetValueByRow(self, value, row, col):
        return False

    # Report the number of rows in the model
    def GetCount(self):
        # self.log.write('GetCount')
        return ORDER_SUMMARY_ROW_COUNT

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
        self.summary = data
        self.Cleared()
