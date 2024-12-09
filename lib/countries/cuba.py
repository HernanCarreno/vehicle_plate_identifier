from lib.countries.base_country import BaseCountry
import re

class Cuba(BaseCountry):
    def __init__(self):
        # Define el formato general de las placas de Cuba
        region_formats = {
            "Cuba": re.compile(r"^[A-Z]{1} \d{6}$"),  # Una letra y seis números
        }

        # Formatos de placas por tipo de vehículo
        vehicle_formats = {
            "Vehículos de la administración": re.compile(r"^A \d{6}$"),
            "Cuerpo Consular": re.compile(r"^C \d{6}$"),
            "Cuerpo Diplomático": re.compile(r"^D \d{6}$"),
            "Vehículo de embajada": re.compile(r"^E \d{6}$"),
            "Fuerzas Armadas": re.compile(r"^F \d{6}$"),
            "Personal extranjero": re.compile(r"^K \d{6}$"),
            "Ministerio del Interior (Policía)": re.compile(r"^M \d{6}$"),
            "Turista": re.compile(r"^T \d{6}$"),
            "Vehículo privado": re.compile(r"^[PBHGJLNRTUVXY] \d{6}$"),  # Letras válidas para vehículos privados
        }

        # Inicializa la clase base con los datos de Cuba
        super().__init__("Cuba", region_formats, vehicle_formats)
