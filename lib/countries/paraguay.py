import re
from lib.countries.base_country import BaseCountry

class Paraguay(BaseCountry):
    def __init__(self):
        region_formats = {
            "Vehículo General": re.compile(r'^[A-Z]{4}\d{3}$'),  # AAAA nnn
            "Motocicleta": re.compile(r'^\d{3}[A-Z]{4}$')       # nnn AAAA
        }

        vehicle_formats = region_formats  # Similares a los formatos de región

        self.region_map = {
            "A": "Concepción",
            "B": "San Pedro",
            "C": "Cordillera",
            "D": "Guairá",
            "E": "Caaguazú",
            "F": "Caazapá",
            "G": "Itapúa",
            "H": "Misiones",
            "I": "Paraguarí",
            "J": "Alto Paraná",
            "K": "Central",
            "L": "Ñeembucú",
            "M": "Amambay",
            "N": "Canindeyú",
            "Q": "Presidente Hayes",
            "R": "Alto Paraguay",
            "S": "Boquerón"
        }

        super().__init__("Paraguay", region_formats, vehicle_formats)

    def identify_region(self, plate):
        """
        Identifica la región con base en la primera letra de placas antiguas municipales.
        Esto no aplica para las placas Mercosur (AAAA nnn o nnn AAAA).
        """
        if not self.is_valid_plate(plate):
            return "Unknown Region"
        
        # Verificar si es formato de placas municipales antiguas
        if re.match(r'^[A-Z]\d+$', plate):  # Formato "A12345"
            region_code = plate[0].upper()  # Primera letra
            return self.region_map.get(region_code, "Unknown Region")
        
        return "Mercosur (No aplica región)"

    def is_valid_plate(self, plate):
        """
        Valida la placa con los formatos definidos.
        Adicionalmente, incluye validación para placas antiguas municipales.
        """
        # Validar Mercosur (AAAA nnn o nnn AAAA)
        for pattern in self.region_formats.values():
            if pattern.match(plate):
                return True

        # Validar formato antiguo municipal
        if re.match(r'^[A-Z]\d+$', plate):  # Ejemplo: A12345
            return True

        return False
