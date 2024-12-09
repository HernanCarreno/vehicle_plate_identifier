from lib.countries.mexico import Mexico
from lib.countries.colombia import Colombia
from lib.countries.guatemala import Guatemala
from lib.countries.el_salvador import El_salvador
from lib.countries.chile import Chile
from lib.countries.costa_rica import CostaRica
from lib.countries.panama import Panama
from lib.countries.argentina import Argentina
from lib.countries.venezuela import Venezuela
from lib.countries.bolivia import Bolivia
from lib.countries.uruguay import Uruguay
from lib.countries.brasil import Brasil
from lib.countries.ecuador import Ecuador
from lib.countries.peru import Peru
from lib.countries.paraguay import Paraguay
from lib.countries.cuba import Cuba


class PlateIdentifier:
    def __init__(self):
        self.countries = [Mexico(), Colombia(), Guatemala(), El_salvador(), Chile(), CostaRica(),
                          Panama(),Argentina(),Venezuela(),Brasil(),Bolivia(),Uruguay(),Brasil(),  
                          Peru(),Ecuador(),Paraguay(),Cuba()                        ]

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