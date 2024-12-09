import re
from lib.countries.base_country import BaseCountry

class Argentina(BaseCountry):
    def __init__(self):
        # Formatos de placas para diferentes tipos de vehículos
        region_formats = {
            "Particular": re.compile(r'^(?!TQ\s|XT\s|CD\s|OF)[A-Z]{2}\s[0-9]{3}\s[A-Z]{2}$'),
            "Transporte_Publico": re.compile(r'^TQ\s[0-9]{3}\s[A-Z]{2}$'),
            "Comercial": re.compile(r'^XT\s[0-9]{3}\s[A-Z]{2}$'),
            "Diplomatico": re.compile(r'^CD\s[0-9]{3}$'),
            "Oficial": re.compile(r'^[A-Z]{2}\s[0-9]{3}\sOF$'),
            "Provisional": re.compile(r'^PROV\s[0-9]{3}$'),
            "Motocicleta": re.compile(r'^[A-Z]\s[0-9]{2}\s[A-Z]{2}$')
        }
        vehicle_formats = region_formats  # Los formatos de vehículo coinciden con los de región

        # Mapeo de prefijos a fechas para cálculo de año
        self.plate_date_map = [
            ("AA000AA", "2016-04"),
            ("AA860AA", "2017-01"),
            ("AB000AA", "2017-02"),
            ("AC000AA", "2017-10"),
            ("AC195AA", "2018-01"),
            ("AD000AA", "2018-07"),
            ("AD385AA", "2019-01"),
            ("AE000AA", "2019-10"),
            ("AE070AA", "2020-01"),
        ]

        super().__init__("Argentina", region_formats, vehicle_formats)

    def calculate_year(self, plate):
        """Calcula el año aproximado basado en el prefijo de la matrícula."""
        normalized_plate = plate.replace(" ", "").upper()
        for i, (prefix, date) in enumerate(self.plate_date_map):
            if normalized_plate >= prefix:
                if i == len(self.plate_date_map) - 1 or normalized_plate < self.plate_date_map[i + 1][0]:
                    return date.split("-")[0]  # Retorna solo el año
        return "Unknown Year"

    def identify_region(self, plate):
        """Extiende la región para incluir el cálculo del año."""
        region = super().identify_region(plate)
        if region != "Unknown Region":
            # Calcular el año si aplica
            year = self.calculate_year(plate)
            return f"{region} (Year: {year})" if year != "Unknown Year" else region
        return "Unknown Region"
