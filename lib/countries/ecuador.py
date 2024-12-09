import re
from lib.countries.base_country import BaseCountry

class Ecuador(BaseCountry):
    def __init__(self):
        region_formats = {
            "Particular": re.compile(r'^[A-Z]{3}-\d{4}$'),
            "Público/Comercial": re.compile(r'^U[A-Z]{2}-\d{4}$'),
            "Gubernamental": re.compile(r'^G[A-Z]{2}-\d{4}$'),
            "Diplomático": re.compile(r'^CD-\d{4}$')
        }

        vehicle_formats = region_formats  # Similares a los formatos de región

        self.region_map = {
            "A": "Azuay",
            "B": "Bolívar",
            "C": "Carchi",
            "E": "Esmeraldas",
            "G": "Guayas",
            "H": "Chimborazo",
            "I": "Imbabura",
            "J": "Santo Domingo de los Tsáchilas",
            "K": "Sucumbíos",
            "L": "Loja",
            "M": "Manabí",
            "N": "Napo",
            "O": "El Oro",
            "P": "Pichincha",
            "Q": "Orellana",
            "R": "Los Ríos",
            "S": "Pastaza",
            "T": "Tungurahua",
            "U": "Cañar",
            "V": "Morona-Santiago",
            "W": "Galápagos",
            "X": "Cotopaxi",
            "Z": "Zamora-Chinchipe"
        }

        super().__init__("Ecuador", region_formats, vehicle_formats)

    def identify_region(self, plate):
        """Identifica la región con base en la primera letra."""
        if not self.is_valid_plate(plate):
            return "Unknown Region"
        region_code = plate[0].upper()  # Primera letra
        return self.region_map.get(region_code, "Unknown Region")
