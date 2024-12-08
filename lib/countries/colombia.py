from lib.countries.base_country import BaseCountry
import re

class Colombia(BaseCountry):
    def __init__(self):
        region_formats = {
            "General": re.compile(r"^[A-Z]{3}-\d{3}$")
        }
        vehicle_formats = {
            "Automobile": re.compile(r"^[A-Z]{3}-\d{3}$"),
            "Motorcycle": re.compile(r"^[A-Z]{3}\d{2}[A-Z]$"),
            "Truck": re.compile(r"^T[A-Z]{3}-\d{3}$"),
        }
        super().__init__("Colombia", region_formats, vehicle_formats)