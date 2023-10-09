from dataclasses import dataclass

'''
from dataclasses import dataclass
import json

@dataclass
class AAA:
    a : int = 1
    b  : int = 2

@dataclass
class CC:
    c : str = '3w2'
    d : str = '3w3e'


a = AAA( ).__dict__
b = CC().__dict__

c = { ** a , ** b}

s = json.dumps(c, indent=4)
j = json.loads(s)
print(j)

'''

@dataclass
class BaseInfoModel:
    blayer: str  # Layer Count
    blength: str  # GetPcbLength
    bwidth: str  # GetPcbWidth
    bcount: str  # Qty(single)
    sidedirection: str  # Decided by the marginMode automatically

    plate_type: str = 'Fr-4'  # Material Type
    board_tg: str = 'TG130'  # TODO
    units: str = '2'  # Board Type
    layoutx: str = None  # X
    layouty: str = None  # Y
    sidewidth: str = None  # Break-away Rail
