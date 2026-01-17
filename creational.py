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
        self.prototypes["Liquid Fuel Rocket Engine"]=LF_engine

        #Solid Fuel Rocket Engine (SRB's)
        SRB_engine=RocketEngine("SRB-1", "Solid Fuel", 750)
        SRB_engine.burn_time=120
        SRB_engine.specific_impulse=170.0
        SRB_engine.fuel_type="Composite Propellant"
        SRB_engine.oxidiser_type="Ammonium"
        SRB_engine.mixture_ratio=1.8
        self.prototypes["Solid Fuel Rocket Engine"]=SRB_engine

    def get_engine_types(self):
        return list(self.prototypes.keys())
    
    def create_engine(self, engine_type):
        if engine_type in self.prototypes:
            return self.prototypes[engine_type].clone()
        else:
            return None
        
    def create_custom_engine(self, new_engine, engine_type, features):
        engine=self.create_engine(engine_type)
        if engine is not None:
            engine.name=new_engine
            for feature in features:
                engine.add_features(feature)
            return engine
        else:
            return None
        
        

