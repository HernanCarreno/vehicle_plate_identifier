import re
from lib.countries.base_country import BaseCountry

class Peru(BaseCountry):
    def __init__(self):
        region_formats = {
            "Automóvil": re.compile(r'^[A-Z]{3}-\d{3}$'),
            "Taxi": re.compile(r'^[A-Z]{3}-6\d{2}$'),
            "Bus Urbano": re.compile(r'^[A-Z]{3}-7\d{2}$'),
            "Bus Interprovincial": re.compile(r'^[A-Z]{3}-9[5-6]\d$'),
            "Gubernamental": re.compile(r'^EG\d-\d{3}$'),
            "Especial": re.compile(r'^E[A-Z0-9]{2}-\d{3}$')
        }

        vehicle_formats = region_formats  # Similares a los formatos de región

        self.region_map = {
            "H": "Áncash",
            "L": "Loreto",
            "M": "Amazonas, Cajamarca, Lambayeque",
            "P": "Tumbes, Piura",
            "S": "San Martín",
            "T": "La Libertad",
            "U": "Ucayali",
            "V": "Arequipa",
            "W": "Huánuco, Junín, Pasco",
            "X": "Apurímac, Cuzco, Madre de Dios",
            "Y": "Ayacucho, Ica, Huancavelica",
            "Z": "Moquegua, Puno, Tacna"
        }

        super().__init__("Perú", region_formats, vehicle_formats)

    def identify_region(self, plate):
        """Identifica la región con base en la primera letra."""
        if not self.is_valid_plate(plate):
            return "Unknown Region"
        region_code = plate[0].upper()  # Primera letra
        return self.region_map.get(region_code, "Unknown Region")
