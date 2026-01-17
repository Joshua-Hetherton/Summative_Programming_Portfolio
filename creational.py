"""
Creational Design Pattern Module:
Prototyping Rocket Engines
"""
import copy
class RocketEngine:
    def __init__(self, name, engine_type,thrust):
        self.name=name
        self.engine_type=engine_type
        self.thrust=thrust
        self.burn_time=0
        self.specific_impulse=0.0

        self.fuel_type=""
        self.oxidizer_type=""
        self.mixture_ratio=0.0

        self.features=[]

        pass
    
    def clone(self):
        return copy.deepcopy(self)

    def add_features(self, feature):
        self.features.append(feature)

    def list_features(self):
        return f"""
Amount of Features: {len(self.features)}
==========================
{self.name} has the following Attributes:
self.engine_type: {self.engine_type}
self.thrust: {self.thrust} kN
self.burn_time: {self.burn_time} seconds
self.specific_impulse: {self.specific_impulse} seconds
self.fuel_type: {self.fuel_type}
self.oxidizer_type: {self.oxidizer_type}
self.mixture_rati: {self.mixture_ratio}
==========================
Additional Features:
{", ".join(self.features)}

"""
        pass
