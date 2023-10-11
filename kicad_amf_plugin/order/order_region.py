from enum import Enum
import wx
class URL_KIND(Enum):
    QUERY_PRICE =0
    PLACE_ORDER =1



class OrderRegion :
    CHINA_MAINLAND  = 0    
    JAPAN  = CHINA_MAINLAND + 1
    EUROPE_USA = JAPAN + 1 

    AVAILABLE_URLS = {
        CHINA_MAINLAND :{
            URL_KIND.PLACE_ORDER : 'https://www.nextpcb.com/Upfile/kiCadUpFile',
            URL_KIND.QUERY_PRICE : 'https://www.nextpcb.com/ajax/valuation'
        },
        JAPAN : {
            URL_KIND.PLACE_ORDER : None,
            URL_KIND.QUERY_PRICE : None
        },
        EUROPE_USA : {
            URL_KIND.PLACE_ORDER : None,
            URL_KIND.QUERY_PRICE : None
        }
    }    

    @staticmethod
    def get_url(region : int , kind : URL_KIND):
        if region in OrderRegion.AVAILABLE_URLS:
            return OrderRegion.AVAILABLE_URLS[region][kind]
