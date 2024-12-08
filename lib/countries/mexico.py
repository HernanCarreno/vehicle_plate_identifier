from lib.countries.base_country import BaseCountry
import re

class Mexico(BaseCountry):
    def __init__(self):
        region_formats = {
            "CDMX": re.compile(r"^A\d{2}-\d{3}$"),
            "Jalisco": re.compile(r"^J[A-Z]{1}-\d{3}$"),
            "Nuevo León": re.compile(r"^N[L|M]\d{3}[A-Z]{2}$"),
        }
        vehicle_formats = {
            "Automobile": re.compile(r"^[A-Z]{1,3}\d{1,4}[A-Z]{0,2}$"),
            "Motorcycle": re.compile(r"^[A-Z]{2}\d{3}[A-Z]$"),
            "Truck": re.compile(r"^T\d{2}-\d{4}$"),
        }
        super().__init__("Mexico", region_formats, vehicle_formats)