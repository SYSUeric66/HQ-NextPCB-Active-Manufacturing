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
    units: str = '2'  # Board Type
    layoutx: str = None  # X
    layouty: str = None  # Y
    sidewidth: str = None  # Break-away Rail
    
    testpoint : str = None  # 测试点数，默认为0 
    pbnum : str = None # 拼版款数，指文件内不同款的板子个数， 不传默认为1
    board_tg: str = None  # 4层及以上可选TG值，TG130、TG150、TG170

