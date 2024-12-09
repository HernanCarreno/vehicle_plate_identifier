from lib.countries.base_country import BaseCountry
import re

class CostaRica(BaseCountry):
    def __init__(self):
        region_formats = {
            "Vehículo General": re.compile(r'^[BCDFGHJKLMNPQRSTVWXYZ]{3}-\d{3}$'),  # Tres letras (sin vocales) + guion + tres números
            "Taxi": re.compile(r'^TSJ-\d{3}$'),  # Taxis con el prefijo TSJ
            "Bus Interprovincial": re.compile(r'^AB-\d{3}$'),  # AB para buses interprovinciales
            "Bus Interurbano": re.compile(r'^SJB-\d{3}$')     # SJB para buses interurbanos
        }

        vehicle_formats = region_formats  # Similares a los formatos de región

        super().__init__("Costa Rica", region_formats, vehicle_formats)
