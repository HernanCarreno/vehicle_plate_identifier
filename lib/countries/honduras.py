import re
from lib.countries.base_country import BaseCountry

class Honduras(BaseCountry):
    def __init__(self):
        region_formats = {
            "Vehículo Privado": re.compile(r'^H[A-Z]{2}\d{4}$'),  # H + dos letras + cuatro números
            "Motocicleta": re.compile(r'^B[A-Z]{2}\d{4}$')       # B + dos letras + cuatro números
        }

        vehicle_formats = region_formats  # Similares a los formatos de región

        super().__init__("Honduras", region_formats, vehicle_formats)
