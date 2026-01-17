class MissionState:
    def next_state(self,spacecraft):
        raise NotImplementedError("Subclasses must be implemented")
    def name(self):
        raise NotImplementedError("Subclasses must be implemented")
    def description(self):
        raise NotImplementedError("Subclasses must be implemented")
    pass

class PrelaunchState(MissionState):
    pass

class LaunchState(MissionState):
    pass

class OrbitState(MissionState):
    pass

class ReEntryState(MissionState):
    pass

class Spacecraft:
    pass