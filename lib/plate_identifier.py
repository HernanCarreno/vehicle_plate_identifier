from lib.countries.mexico import Mexico
from lib.countries.colombia import Colombia
from lib.countries.guatemala import Guatemala
from lib.countries.el_salvador import El_salvador
from lib.countries.chile import Chile
from lib.countries.costa_rica import Costa_Rica
from lib.countries.panama import Panama

class PlateIdentifier:
    def __init__(self):
        self.countries = [Mexico(), Colombia(), Guatemala(), El_salvador(), Chile(), Costa_Rica(),
                          Panama()]

    def identify(self, plate):
        matches = []
        for country in self.countries:
            if country.is_valid_plate(plate):
                region = country.identify_region(plate)
                vehicle_type = country.identify_vehicle_type(plate)
                matches.append({
                    "country": country.name,
                    "region": region,
                    "vehicle_type": vehicle_type
                })
        return matches if matches else [{"country": "Desconocido", "region": "Desconocido", "vehicle_type": "Desconocido"}]