from lib.countries.base_country import BaseCountry
import re
from lib.countries.base_country import BaseCountry
import re

class Uruguay(BaseCountry):
    def __init__(self):
        region_formats = {
            "Particular": re.compile(r'^(?!TX|TC|TI)([A-Z]{3})\s[0-9]{4}$'),
            "Taxi": re.compile(r'^[A-Z]{3}TX\s[0-9]{4}$'),
            "Bus": re.compile(r'^[A-Z]{3}TC\s[0-9]{4}$'),
            "Bus Interurbano": re.compile(r'^[A-Z]{3}TI\s[0-9]{4}$')
        }
        vehicle_formats = {
            "Particular": re.compile(r'^(?!TX|TC|TI)([A-Z]{3})\s[0-9]{4}$'),
            "Taxi": re.compile(r'^[A-Z]{3}TX\s[0-9]{4}$'),
            "Bus": re.compile(r'^[A-Z]{3}TC\s[0-9]{4}$'),
            "Bus Interurbano": re.compile(r'^[A-Z]{3}TI\s[0-9]{4}$')
        }
        super().__init__("Uruguay", region_formats, vehicle_formats)
        
        # Mapeo de departamentos
        self.departments = {
            'A': 'Canelones',
            'B': 'Maldonado',
            'C': 'Rocha',
            'D': 'Treinta y Tres',
            'E': 'Cerro Largo',
            'F': 'Rivera',
            'G': 'Artigas',
            'H': 'Salto',
            'I': 'Paysandú',
            'J': 'Río Negro',
            'K': 'Soriano',
            'L': 'Colonia',
            'M': 'San José',
            'N': 'Flores',
            'O': 'Florida',
            'P': 'Lavalleja',
            'Q': 'Durazno',
            'R': 'Tacuarembó',
            'S': 'Montevideo'
        }
    
    def identify_region(self, plate):
        """
        Identify the specific region for a Uruguayan license plate
        """
        # Remove spaces from the plate
        cleaned_plate = plate.replace(' ', '')
        
        # Check if the plate starts with a valid department letter
        if len(cleaned_plate) >= 3 and cleaned_plate[0] in self.departments:
            return self.departments[cleaned_plate[0]]
        
        return super().identify_region(plate)