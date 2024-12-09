import re
from lib.countries.base_country import BaseCountry

class Mexico(BaseCountry):
    def __init__(self):
        # Formatos de placas
        region_formats = {
            "Vehículo Privado": re.compile(r'^[A-Z]{3}-\d{2}-\d{2}$|^[A-Z]{3}-\d{3}-[A-Z]$'),  # AAA-00-00 o AAA-000-A
            "Vehículo Público": re.compile(r'^[A-Z]-\d{3}-[A-Z]{3}$'),  # A-000-AAA
            "Ciudad de México Privado": re.compile(r'^\d{3}-[A-Z]{3}$|^[A-Z]-\d{2}-[A-Z]{3}$')  # 000-AAA o A-00-AAA
        }

        # Map de entidades y códigos fiscales
        state_map = {
            "AGS": "01", "BC": "02", "BCS": "03", "CAMP": "04", "COAH": "05", "COL": "06",
            "CHIS": "07", "CHIH": "08", "CDMX": "09", "DGO": "10", "GTO": "11", "GRO": "12",
            "HGO": "13", "JAL": "14", "MEX": "15", "MICH": "16", "MOR": "17", "NAY": "18",
            "NL": "19", "OAX": "20", "PUE": "21", "QRO": "22", "QR": "23", "SLP": "24",
            "SIN": "25", "SON": "26", "TAB": "27", "TAMPS": "28", "TLAX": "29", "VER": "30",
            "YUC": "31", "ZAC": "32"
        }

        super().__init__("México", region_formats)
        self.state_map = state_map

    def identify_state(self, plate):
        """
        Identifica el estado emisor basándose en los códigos presentes en la placa.
        """
        for state, code in self.state_map.items():
            if code in plate or state in plate:
                return state
        return "Unknown State"

    def is_valid_plate(self, plate):
        """
        Valida la placa según los formatos establecidos.
        """
        for format_name, regex in self.region_formats.items():
            if regex.match(plate):
                return True, format_name
        return False, "Formato Inválido"


#mexico = Mexico()

# Validar placas
#print(mexico.is_valid_plate("ABC-12-34"))  # (True, "Vehículo Privado")
#print(mexico.is_valid_plate("A-123-DEF"))  # (True, "Vehículo Público")
#print(mexico.is_valid_plate("CDMX-09-AAA"))  # (False, "Formato Inválido")

# Identificar estados
#print(mexico.identify_state("AGS-01-ABC"))  # AGS
#print(mexico.identify_state("123-CDMX"))  # CDMX
