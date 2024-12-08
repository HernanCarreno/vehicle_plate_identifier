from lib.countries.base_country import BaseCountry
import re

class Panama(BaseCountry):
    def __init__(self):
        region_formats = {
            "General": re.compile(r"^(\d{6}|[A-Z]{2}\d{4})$")
        }
        vehicle_formats = {
            "Desconocido": re.compile(r"^\d{6}$")
        }
        super().__init__("Panamá", region_formats, vehicle_formats)