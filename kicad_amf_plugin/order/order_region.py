import logging

class OrderRegion :
    CHINA_MAINLAND  = 0    
    JAPAN  = CHINA_MAINLAND + 1
    EUROPE_USA = JAPAN + 1 

    ORDER_URLS = {
        CHINA_MAINLAND : 'https://www.nextpcb.com/ajax/valuation',
        JAPAN : "",
        EUROPE_USA : "", 
    }

    @staticmethod
    def get_order_url(region : int):
        if region in OrderRegion.ORDER_URLS:
            return OrderRegion.ORDER_URLS[region]
        logging.error(f'No available order url for region {region}')


