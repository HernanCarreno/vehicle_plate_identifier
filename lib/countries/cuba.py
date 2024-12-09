import re
from lib.countries.base_country import BaseCountry

class Cuba(BaseCountry):
    def __init__(self):
        region_format = re.compile(r'^[A-Z] \d{3} \d{3}$')
        vehicle_types = {
            "A": "Administración",
            "C": "Cuerpo Consular",
            "D": "Cuerpo Diplomático",
            "E": "Embajada",
            "F": "Fuerzas Armadas",
            "K": "Personal Extranjero",
            "M": "Ministerio del Interior (Policía)",
            "T": "Turista",
            "P": "Vehículo Privado",
            "B": "Vehículo Privado",
            "G": "Vehículo Privado",
            "H": "Vehículo Privado",
            "J": "Vehículo Privado",
            "L": "Vehículo Privado",
            "N": "Vehículo Privado",
            "R": "Vehículo Privado",
            "U": "Vehículo Privado",
            "V": "Vehículo Privado",
            "X": "Vehículo Privado",
            "Y": "Vehículo Privado",
        }
        super().__init__("Cuba", region_format)
        self.vehicle_types = vehicle_types

    def identify_vehicle_type(self, plate):
        """
        Identifica el tipo de vehículo según la primera letra de la placa.
        """
        first_letter = plate[0]
        return self.vehicle_types.get(first_letter, "Desconocido")
