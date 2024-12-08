from lib.countries.base_country import BaseCountry
import re

class Honduras(BaseCountry):j
    def __init__(self):
        region_formats = {
            "General": re.compile(r"^(H [A-NO-Z]{2} \d{4})$")
        }
        vehicle_formats = {
            "Vehículo de Servicio Publico": re.compile(r"^(A \d{2} \d{3}|MB \d{1} \d{3}|MB\d{2} \d{3}|AB\d{2} \d{3})$"),
            "Vehículo Particular": re.compile(r"^H [A-NO-Z]{2} \d{4}$"),
        }
        super().__init__("Honduras", region_formats, vehicle_formats)