from dataclasses import dataclass


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
