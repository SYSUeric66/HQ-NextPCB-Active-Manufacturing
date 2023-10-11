import logging

class OrderRegion :
    CHINA_MAINLAND  = 0    
    JAPAN  = CHINA_MAINLAND + 1
    EUROPE_USA = JAPAN + 1 

    QUERY_PRICE_URLS = {
        CHINA_MAINLAND : 'https://www.nextpcb.com/ajax/valuation',
        JAPAN : "",
        EUROPE_USA : "", 
    }


    PLACE_ORDER_URLS = {
        CHINA_MAINLAND : 'https://www.nextpcb.com/Upfile/kiCadUpFile',
        JAPAN : "",
        EUROPE_USA : "", 
    }    

    @staticmethod
    def get_query_price_url(region : int):
        if region in OrderRegion.QUERY_PRICE_URLS:
            return OrderRegion.QUERY_PRICE_URLS[region]
        logging.error(f'No available url for region {region}')

    @staticmethod
    def get_place_order_url(region : int):
        if region in OrderRegion.PLACE_ORDER_URLS:
            return OrderRegion.PLACE_ORDER_URLS[region]
        logging.error(f'No available url for region {region}')        


