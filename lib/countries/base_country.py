import re

class BaseCountry:
    def __init__(self, name, region_formats=None, vehicle_formats=None):
        self.name = name
        self.region_formats = region_formats or {}
        self.vehicle_formats = vehicle_formats or {}

    def is_valid_plate(self, plate):
        """Validates the plate based on the country's general patterns or regions."""
        for pattern in self.region_formats.values():
            if pattern.match(plate):
                return True
        return False

    def identify_region(self, plate):
        """Identifies the region of the plate."""
        for region, pattern in self.region_formats.items():
            if pattern.match(plate):
                return region
        return "Unknown Region"

    def identify_vehicle_type(self, plate):
        """Identifies the type of vehicle."""
        for vehicle_type, pattern in self.vehicle_formats.items():
            if pattern.match(plate):
                return vehicle_type
        return "Unknown Vehicle Type"