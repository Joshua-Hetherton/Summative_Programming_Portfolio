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
        self.oxidiser_type=""
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
self.oxidiser_type: {self.oxidiser_type}
self.mixture_rati: {self.mixture_ratio}
==========================
Additional Features:
{", ".join(self.features)}

"""

class PrototypeManager:
    def __init__(self):
        self.prototypes={}
        self.initialise_engines()
    def intialise_engines(self):
        #Liquid Fuel Rocket Engine
        LF_engine=RocketEngine("LF-1", "Liquid Fuel", 500)
        LF_engine.burn_time=230
        LF_engine.specific_impulse=205.5
        LF_engine.fuel_type="Refined Petroleum"
        LF_engine.oxidiser_type="Liquid Oxygen"
        LF_engine.mixture_ratio=2.5

