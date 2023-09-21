from dataclasses import dataclass


@dataclass
class BaseInfo:
    plate_type: str = 'Fr-4'  # Material Type
    blayer: str  # Layer Count
    board_tg: str = 'TG130'  # TODO
    units: str = '2'  # Board Type
    blength: str  # GetPcbLength
    bwidth: str  # GetPcbWidth
    layoutx: str or None  # X
    layouty: str or None  # Y
    bcount: str  # Qty(single)
    sidedirection: str  # Decided by the marginMode automatically
    sidewidth: str or None  # Break-away Rail
