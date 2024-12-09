import re
from lib.countries.base_country import BaseCountry

class Venezuela(BaseCountry):
    def __init__(self):
        # Mapeo de códigos de entidad federal
        self.region_codes = {
            'A': 'Ciudad de Caracas (Distrito Capital)',
            'B': 'Anzoátegui',
            'C': 'Apure',
            'D': 'Aragua',
            'E': 'Barinas',
            'F': 'Bolívar',
            'G': 'Carabobo',
            'H': 'Cojedes',
            'I': 'Falcón',
            'J': 'Guárico',
            'K': 'Lara',
            'L': 'Mérida',
            'M': 'Miranda',
            'N': 'Monagas',
            'O': 'Nueva Esparta',
            'P': 'Portuguesa',
            'R': 'Sucre',
            'S': 'Táchira',
            'T': 'Trujillo',
            'U': 'Yaracuy',
            'V': 'Zulia',
            'W': 'La Guaira',
            'X': 'Amazonas',
            'Y': 'Delta Amacuro',
        }
        
        # Formatos de placas
        region_formats = {
            "Particular": re.compile(r'^[A-Z]{2}[0-9]{3}[A-Z]{2}$'),
            "Transporte_Publico": re.compile(r'^PT[0-9]{3}[A-Z]{2}$'),
            "Diplomatico": re.compile(r'^CD[0-9]{3}$'),
            "Oficial": re.compile(r'^OA[0-9]{3}[A-Z]{2}$'),
            "Carga": re.compile(r'^CA[0-9]{3}[A-Z]{2}$'),
            "Taxi": re.compile(r'^7[A-Z][0-9][A-Z][0-9][A-Z]$'),
            "Transporte_Urbano": re.compile(r'^01[A-Z]{2}[0-9][A-Z]$')
        }

        vehicle_formats = {
            "Particular": re.compile(r'^[A-Z]{2}[0-9]{3}[A-Z]{2}$'),
            "Transporte_Publico": re.compile(r'^PT[0-9]{3}[A-Z]{2}$'),
            "Diplomatico": re.compile(r'^CD[0-9]{3}$'),
            "Oficial": re.compile(r'^OA[0-9]{3}[A-Z]{2}$'),
            "Carga": re.compile(r'^CA[0-9]{3}[A-Z]{2}$'),
            "Taxi": re.compile(r'^7[A-Z][0-9][A-Z][0-9][A-Z]$'),
            "Transporte_Urbano": re.compile(r'^01[A-Z]{2}[0-9][A-Z]$')
        }

        super().__init__("Venezuela", region_formats, vehicle_formats)

    def identify_region(self, plate):
        """Sobrescribe el método para identificar la región por la última letra de la placa."""
        if len(plate) < 1 or not plate[-1].isalpha():
            return "Unknown Region"
        
        # Última letra de la placa para región
        region_code = plate[-1].upper()
        return self.region_codes.get(region_code, "Unknown Region")
