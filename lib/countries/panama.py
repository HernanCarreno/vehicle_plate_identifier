from lib.countries.base_country import BaseCountry
import re

class Panama(BaseCountry):
    def __init__(self):
        region_formats = {
            "Placa Numérica": re.compile(r'^\d{6}$'),       # Seis números
            "Placa Alfanumérica": re.compile(r'^[A-Z]{2}\d{4}$')  # Dos letras + cuatro números
        }

        region_map = {
            "01": "Panamá",
            "02": "Colón",
            "03": "Chiriquí",
            "04": "Coclé",
            "05": "Veraguas",
            "06": "Los Santos",
            "07": "Herrera",
            "08": "Bocas del Toro",
            "09": "Darién",
            "10": "Guna Yala"
        }

        super().__init__("Panamá", region_formats)

    def identify_region(self, plate):
        """
        Identifica la región basándose en los dos primeros números para las placas numéricas.
        """
        if re.match(r'^\d{6}$', plate):  # Placa Numérica
            region_code = plate[:2]
            return self.region_map.get(region_code, "Unknown Region")
        return "Formato Alfanumérico (No aplica región)"
