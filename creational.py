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

    def add_features(self):
        pass

    def list_features(self):
        pass
