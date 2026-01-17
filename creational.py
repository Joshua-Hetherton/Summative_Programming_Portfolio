"""
Creational Design Pattern Module:
Prototyping Rocket Engines
"""
import copy
class RocketEngine:
    """
    This class is the basis for the Prototype Design Pattern.
    It represents a default rocket engine, which can contain various features and attributes 
    that can later be cloned to create new rocket engines with similar properties
    """
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
        """
        Clones the given Object (in this case Rocket Engine), and a copy is returned.

        Returns:
            RocketEngine: A copy of the current RocketEngine Object
        """
        return copy.deepcopy(self)

    def add_features(self, feature):
        """
        Adds a new feature to the Rocket Engine.

        Args:
            feature (str): Description of the feature to be added
        """

        self.features.append(feature)

    def list_features(self):
        """
        Lists all the features of the Rocket Engine.
        
        Returns:
            str: A formatted string that lists all the features of the Rocket Engine.
        """
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
    """
    The main class which manages all the prototypes of the rocket Engines.
    It initialises a set of the default Rocket Engines, and allows for cloning and creating of any custom engines.
    """
    def __init__(self):
        self.prototypes={}
        self.initialise_engines()

    def initialise_engines(self):
        """
        Provides a default set of Rocket Engines to be used for Prototyping.
        Currently, it Include both Liquid Fuel and Solid Fuel Rocket Engines(Also known as SRB's if attached radially/to the side).
        """
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
        """
        Lists all available engine types for the Prototype Manager.
        
        Returns:
            list: A list of all available engine types.
        """
        return list(self.prototypes.keys())
    
    def create_engine(self, engine_type):
        """
        Creates a clone of a given engine type.
        This then allows it to be customised further.

        Args:
            engine_type (str): The type of engine to clone.
        Returns:
            RocketEngine | None: A cloned RocketEngine Objects based on the engine type provided, or None if the engine doesnt exist
        """

        if engine_type in self.prototypes:
            return self.prototypes[engine_type].clone()
        else:
            return None
        
    def create_custom_engine(self, new_engine, engine_type, features):
        """
        Creates a custom Rocket Engine given all the facts provided by the user.
        
        Args:
            new_engine (str): The name of the new custom engine.
            engine_type (str): The type of engine to clone.
            features (list): A list of features to be added to the new engine.
        Returns:
            RocketEngine | None: A customised RocketEngine Object based on the engine type provided, or None if the engine doesnt exist
        """
        engine=self.create_engine(engine_type)
        if engine is not None:
            engine.name=new_engine
            for feature in features:
                engine.add_features(feature)
            return engine
        else:
            return None
        
        

