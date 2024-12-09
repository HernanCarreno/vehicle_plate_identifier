from lib.countries.base_country import BaseCountry
import re
class Bolivia(BaseCountry):
    def __init__(self):
        region_formats = {
            "Particular": re.compile(r'^(?!CD-|[0-9]{4}-[A-Z]{2}T|[0-9]{4}-[A-Z]{2}O)[0-9]{4}-[A-Z]{3}$'),
            "Transporte_Publico": re.compile(r'^[0-9]{4}-[A-Z]{2}T$'),
            "Oficial": re.compile(r'^[0-9]{4}-[A-Z]{2}O$'),
            "Diplomatico": re.compile(r'^CD-[0-9]{3}$')
        }
        vehicle_formats = {
            "Particular": re.compile(r'^(?!CD-|[0-9]{4}-[A-Z]{2}T|[0-9]{4}-[A-Z]{2}O)[0-9]{4}-[A-Z]{3}$'),
            "Transporte_Publico": re.compile(r'^[0-9]{4}-[A-Z]{2}T$'),
            "Oficial": re.compile(r'^[0-9]{4}-[A-Z]{2}O$'),
            "Diplomatico": re.compile(r'^CD-[0-9]{3}$')
        }
        super().__init__("Bolivia", region_formats, vehicle_formats)