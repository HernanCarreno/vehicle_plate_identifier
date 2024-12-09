from lib.countries.base_country import BaseCountry
import re
class Brasil(BaseCountry):
    def __init__(self):
        region_formats = {
            "Particular": re.compile(r'^(?!CD)[A-Z]{3}[0-9][A-Z][0-9]{2}$'),
            "Taxi": re.compile(r'^(?!CD)[A-Z]{3}[0-9][A-Z][0-9]{2}$'),
            "Oficial": re.compile(r'^(?!CD)[A-Z]{3}[0-9][A-Z][0-9]{2}$'),
            "Diplomatico": re.compile(r'^CD[0-9]{5}$'),
            "Prueba": re.compile(r'^(?!CD)[A-Z]{3}[0-9][A-Z][0-9]{2}$')
        }
        vehicle_formats = {
            "Particular": re.compile(r'^(?!CD)[A-Z]{3}[0-9][A-Z][0-9]{2}$'),
            "Taxi": re.compile(r'^(?!CD)[A-Z]{3}[0-9][A-Z][0-9]{2}$'),
            "Oficial": re.compile(r'^(?!CD)[A-Z]{3}[0-9][A-Z][0-9]{2}$'),
            "Diplomatico": re.compile(r'^CD[0-9]{5}$'),
            "Prueba": re.compile(r'^(?!CD)[A-Z]{3}[0-9][A-Z][0-9]{2}$')
        }
        super().__init__("Brasil", region_formats, vehicle_formats)
