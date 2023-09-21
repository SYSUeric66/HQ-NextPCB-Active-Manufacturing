from dataclasses import dataclass
from kicad_amf_plugin.pcb_fabrication.price.price_info_request import PriceInfoRequest


@dataclass
class PlaceOrderRequest(PriceInfoRequest):
    blength: str
    bwidth: str
    type: str = 'pcbfile'
