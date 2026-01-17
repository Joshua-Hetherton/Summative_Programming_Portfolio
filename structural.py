"""Structural Design Pattern: Adapter Pattern Example"""
class Measurement:
    """
    The Target Interface
    This is where the client interacts with the desired interface
    """
    
    def get_meters_measurement(self):
        raise NotImplementedError("Subclass Must be used")

class OriginalMeasurement:
    """
    This is the Class which will be adapted to the target interface
    """
    def __init__ (self, measurement,unit):
        self.measurement=measurement
        self.unit=unit

    def get_measurement(self):
        return self.measurement

    def get_unit(self):
        return self.unit
    
    pass

class MeasurementAdapter(Measurement):
    """
    The adapter class
    This class adapts the OriginalMeasurement Class to the Target Interface class "Measurement"
    """
    def __init__ (self, original_measurement):
        self.original_measurement=original_measurement


    def get_meters_measurement(self):
        """
        Where the adaptation happens
        
        Args:
            original_measurement (OriginalMeasurement): The original measurement object to be adapted
        
        Returns:
            float: The measurement in meters
        """
        value=self.original_measurement.get_measurement()
        unit=self.original_measurement.get_unit()
        if unit=="meters":
            return value
        
        elif unit=="kilometers":
            return value * 1000
        
        elif unit=="gigameters":
            return value * 1e9
        
        elif unit=="miles":
            return value * 1609.34
        
        elif unit=="feet":
            return value * 0.3048
        
        elif unit=="inches":
            return value * 0.0254
    
        else:
            return None

    