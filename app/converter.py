import xml.etree.ElementTree as ET
import requests

class CurrencyConverter(object):

    def convert_amount(reference_date, amount, src_currency, dest_currency):

        URL = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist-90d.xml"
        response = requests.get(URL)
        with open('app/currency.xml', 'wb') as file:
             file.write(response.content)
        tree = ET.parse('app/currency.xml')
        root = tree.getroot()
        rate = 0
        for elem in root:
            for subelem in elem:
                if subelem.get('time') == reference_date:
                    time = subelem.get('time')
                    for subsubelem in subelem:
                        if subsubelem.get('currency') == dest_currency:
                            rate = subsubelem.get('rate')



        return round(amount * float(rate), 2)
