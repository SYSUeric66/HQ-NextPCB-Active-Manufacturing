from enum import Enum
import wx
class URL_KIND(Enum):
    QUERY_PRICE =0
    PLACE_ORDER =1



class SupportedRegion:
    CHINA_MAINLAND = 0
    JAPAN = 1
    EUROPE_USA = 2


class OrderRegion :

    AVAILABLE_URLS = {
        SupportedRegion.CHINA_MAINLAND :{
            URL_KIND.PLACE_ORDER : None,
            URL_KIND.QUERY_PRICE : None
        },
        SupportedRegion.JAPAN : {
            URL_KIND.PLACE_ORDER : None,
            URL_KIND.QUERY_PRICE : None
        },
        SupportedRegion.EUROPE_USA : {
            URL_KIND.PLACE_ORDER : 'https://www.nextpcb.com/Upfile/kiCadUpFile',
            URL_KIND.QUERY_PRICE : 'https://www.nextpcb.com/ajax/valuation'
        }
    }    

    @staticmethod
    def get_url(region : SupportedRegion , kind : URL_KIND):
        if region in OrderRegion.AVAILABLE_URLS:
            return OrderRegion.AVAILABLE_URLS[region][kind]
