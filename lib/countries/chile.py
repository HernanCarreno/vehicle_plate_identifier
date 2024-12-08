from lib.countries.base_country import BaseCountry
import re

class Chile(BaseCountry):
    def __init__(self):
        region_formats = {
            "General": re.compile(r"^[A-Z]{2}·[A-Z]{2} [1-9][0-9]$")
        }
        vehicle_formats = {
            "No Aplica": re.compile(r"^[A-Z]{2}·[A-Z]{2} [1-9][0-9]$")
        }
        super().__init__("Chile", region_formats, vehicle_formats)