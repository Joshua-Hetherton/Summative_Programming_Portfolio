class MissionState:
    def next_state(self,spacecraft):
        raise NotImplementedError("Subclasses must be implemented")
    def name(self):
        raise NotImplementedError("Subclasses must be implemented")
    def description(self):
        raise NotImplementedError("Subclasses must be implemented")
    pass

class PrelaunchState(MissionState):
    def next_state(self,spacecraft):
        if spacecraft.get_fuel_level() >=50:
            spacecraft.state=LaunchState()
    def name(self):
        return "Prelaunch"
    
    def description(self):
        return "Spacecraft is in a prelaunch state, and is ready for lift-off if fuel levels are sufficient."

class LaunchState(MissionState):
    pass

class OrbitState(MissionState):
    pass

class ReEntryState(MissionState):
    pass

class Spacecraft:
    def __init__(self):
        self.state=None
        self.fuel=100
    
    def transition_to_next_state(self):
        self.state.next_state(self)
    
    def get_fuel_level(self):
        return self.fuel
    
    def get_description(self):
        return self.state.description()

    def get_status(self):
        return f"Current State: {self.state.name()} \n Description: {self.get_description()} \n Fuel Level is: {self.get_fuel_level()}%"
    


    pass