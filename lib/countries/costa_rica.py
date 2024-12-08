from lib.countries.base_country import BaseCountry
import re

class Costa_Rica(BaseCountry):
    def __init__(self):
        region_formats = {
            "General": re.compile(r"^([B_DF-HJ-NP-TV-Z]{3}-\d{3})$")
        }
        vehicle_formats = {
            "Vehículo Particular": re.compile(r"^[B_DF-HJ-ÑP-TV-Z]{3}-\d{3}$")
        }
        super().__init__("Costa Rica", region_formats, vehicle_formats)