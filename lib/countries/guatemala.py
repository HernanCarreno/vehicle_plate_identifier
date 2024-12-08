from lib.countries.base_country import BaseCountry
import re

class Guatemala(BaseCountry):
    def __init__(self):
        region_formats = {
            "General": re.compile(r"^[PAU]\d{3}[B-DF-HJ-NP-TV-Z]{3}$")
        }
        vehicle_formats = {
            "Vehiculo Particular": re.compile(r"^P\d{3}[B-DF-HJ-NP-TV-Z]{3}$"),
            "Vehiculo Servicio Publico": re.compile(r"^[AU]\d{3}[B-DF-HJ-NP-TV-Z]{3}$")
        }
        super().__init__("Guatemala", region_formats, vehicle_formats)