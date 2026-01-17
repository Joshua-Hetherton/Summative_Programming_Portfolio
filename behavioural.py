class MissionState:
    """
    The abstract base class for the different states the spacecraft will go through during "the mission".
    """
    def next_state(self,spacecraft):
        """
        This function transitions the spacecraft to the next state.

        """

        raise NotImplementedError("Subclasses must be implemented")
    
    def name(self):
        """
        Returns the name of the current state.

        """

        raise NotImplementedError("Subclasses must be implemented")
    
    def description(self):
        """
        Returns the current description of the state.
        
        """

        raise NotImplementedError("Subclasses must be implemented")

class PrelaunchState(MissionState):
    def next_state(self,spacecraft):
        if spacecraft.get_fuel_level() >=50:
            spacecraft.fuel=spacecraft.get_fuel_level()-20
            spacecraft.state=LaunchState()
    def name(self):
        return "Prelaunch"
    
    def description(self):
        return "Spacecraft is in a prelaunch state, and is ready for lift-off if fuel levels are sufficient."

class LaunchState(MissionState):
    def next_state(self,spacecraft):
        spacecraft.fuel=spacecraft.get_fuel_level()-50
        spacecraft.state=OrbitState()
    def name(self):
        return "Launch"
    
    def description(self):
        return "Spacecraft is launching, consuming fuel. It is now going to get to orbit."
    

class OrbitState(MissionState):
    def next_state(self,spacecraft):
        spacecraft.fuel=spacecraft.get_fuel_level()-30
        spacecraft.state=ReEntryState()
    def name(self):
        return "Orbit"
    
    def description(self):
        return "Spacecraft is in orbit, orbiting round Earth. It is now ready to burn fuel to re-enter the atmospehre"

class ReEntryState(MissionState):
    def next_state(self,spacecraft):
        spacecraft.fuel=0


    def name(self):
        return "Re-Entry"
    
    def description(self):
        return "Spacecraft is now rentering the atmosphere, all fuel has been consumed and the engine and fuel are jettisoned."

class Spacecraft:
    def __init__(self):
        self.state= PrelaunchState()
        self.fuel=100
    
    def transition_to_next_state(self):
        self.state.next_state(self)
    
    def get_fuel_level(self):
        return self.fuel
    
    def get_description(self):
        return self.state.description()

    def get_status(self):
        return f"Current State: {self.state.name()} \n Description: {self.get_description()} \n Fuel Level is: {self.get_fuel_level()}%"
    