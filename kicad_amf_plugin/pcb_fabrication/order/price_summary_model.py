from dataclasses import dataclass
import wx
import wx.dataview as dv
import gettext
_ = gettext.gettext

@dataclass
class ItemPrice:
    desc : str
    cost : int

PRICE_SUMMARY_COL_COUNT = 2



DESC = 1
PRICE = DESC + 1




class PriceSummaryModel(dv.DataViewIndexListModel):
    def __init__(self, price : 'list[ItemPrice]' ):
        dv.DataViewIndexListModel.__init__(self, len(price))
        self.item_price = price

    # This method is called to provide the data object for a
    # particular row,col
    def GetValueByRow(self, row : int, col):
        current = self.item_price[row]
        if DESC == col:
            return _(current.desc)
        elif PRICE == col:
            return f'${current.cost}'

    # Report how many columns this model provides data for.
    def GetColumnCount(self):
        return PRICE_SUMMARY_COL_COUNT

    # Specify the data type for a column
    def GetColumnType(self, col):
        return "string"

    def SetValueByRow(self, value, row, col):
        return False

    # Report the number of rows in the model
    def GetCount(self):
        #self.log.write('GetCount')
        return len(self.item_price)

    # Called to check if non-standard attributes should be used in the
    # cell at (row, col)
    def GetAttrByRow(self, row, col, attr):
        ##self.log.write('GetAttrByRow: (%d, %d)' % (row, col))
        # if col == 3:
        #     attr.SetColour('red')
        #     attr.SetBold(True)
        #     return True
        return False
    def Update(self , price : 'list[ItemPrice]' ):
        self.item_price = price
        self.Reset(len(price))
