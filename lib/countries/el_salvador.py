from lib.countries.base_country import BaseCountry
import re

class El_salvador(BaseCountry):
    def __init__(self):
        region_formats = {
            "General": re.compile(r"^(A \d{2} \d{3}|P\d{3} \d{3}|MB \d{1} \d{3}|MB\d{2} \d{3}|AB\d{2} \d{3})$")
        }
        vehicle_formats = {
            "Vehículo de Servicio Publico": re.compile(r"^(A \d{2} \d{3}|MB \d{1} \d{3}|MB\d{2} \d{3}|AB\d{2} \d{3})$"),
            "Vehículo Particular": re.compile(r"^P\d{3} \d{3}$"),
        }
        super().__init__("El Salvador", region_formats, vehicle_formats)