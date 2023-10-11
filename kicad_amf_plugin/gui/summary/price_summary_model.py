from dataclasses import dataclass
import wx.dataview as dv
from .bom_price_model import BomPriceModel
from .pcb_price_model import PCBPriceModel
from .smt_price_model import SmtPriceModel

@dataclass
class OrderSummary:
    pcb_quantity: int = 0
    days: int = 0
    cost: int = 0


class OrderSummaryModel(dv.PyDataViewModel):
    def __init__(self):
        dv.PyDataViewModel.__init__(self)
        self.UseWeakRefs(True)        
        self.pcb = PCBPriceModel()
        self.smt = SmtPriceModel()
        self.bom = BomPriceModel()


    # Report how many columns this model provides data for.
    def GetColumnCount(self):
        return 6

    # Map the data column numbers to the data type
    def GetColumnType(self, col):
        mapper = { 0 : 'string',
                   1 : 'string',
                   2 : 'string',
                   3.: 'string', # the real value is an int, but the renderer should convert it okay
                   4 : 'datetime',
                   5 : 'bool',
                   }
        return mapper[col]


    def GetChildren(self, parent, children):
        # The view calls this method to find the children of any node in the
        # control. There is an implicit hidden root node, and the top level
        # item(s) should be reported as children of this node. A List view
        # simply provides all items as children of this hidden root. A Tree
        # view adds additional items as children of the other items, as needed,
        # to provide the tree hierarchy.
        ##self.log.write("GetChildren\n")

        # If the parent item is invalid then it represents the hidden root
        # item, so we'll use the genre objects as its children and they will
        # end up being the collection of visible roots in our tree.
        if not parent:
            for genre in self.data:
                children.append(self.ObjectToItem(genre))
            return len(self.data)

        # Otherwise we'll fetch the python object associated with the parent
        # item and make DV items for each of its child objects.
        node = self.ItemToObject(parent)
        if isinstance(node, Genre):
            for song in node.songs:
                children.append(self.ObjectToItem(song))
            return len(node.songs)
        return 0


    def IsContainer(self, item):
        # Return True if the item has children, False otherwise.
        ##self.log.write("IsContainer\n")

        # The hidden root is a container
        if not item:
            return True
        # and in this model the genre objects are containers
        node = self.ItemToObject(item)
        if isinstance(node, Genre):
            return True
        # but everything else (the song objects) are not
        return False


    #def HasContainerColumns(self, item):
    #    self.log.write('HasContainerColumns\n')
    #    return True


    def GetParent(self, item):
        # Return the item which is this item's parent.
        ##self.log.write("GetParent\n")

        if not item:
            return dv.NullDataViewItem

        node = self.ItemToObject(item)
        if isinstance(node, Genre):
            return dv.NullDataViewItem
        elif isinstance(node, Song):
            for g in self.data:
                if g.name == node.genre:
                    return self.ObjectToItem(g)


    def HasValue(self, item, col):
        # Overriding this method allows you to let the view know if there is any
        # data at all in the cell. If it returns False then GetValue will not be
        # called for this item and column.
        node = self.ItemToObject(item)
        if isinstance(node, Genre) and col > 0:
            return False
        return True


    def GetValue(self, item, col):
        # Return the value to be displayed for this item and column. For this
        # example we'll just pull the values from the data objects we
        # associated with the items in GetChildren.

        # Fetch the data object for this item.
        node = self.ItemToObject(item)

        if isinstance(node, Genre):
            # Due to the HasValue implementation above, GetValue should only
            # be called for the first column for Genre objects. We'll verify
            # that with this assert.
            assert col == 0, "Unexpected column value for Genre objects"
            return node.name

        elif isinstance(node, Song):
            mapper = { 0 : node.genre,
                       1 : node.artist,
                       2 : node.title,
                       3 : node.id,
                       4 : node.date,
                       5 : node.like,
                       }
            return mapper[col]

        else:
            raise RuntimeError("unknown node type")



    def GetAttr(self, item, col, attr):
        ##self.log.write('GetAttr')
        node = self.ItemToObject(item)
        if isinstance(node, Genre):
            attr.SetColour('blue')
            attr.SetBold(True)
            return True
        return False