class EmergencyModule:
    def __init__(self, name):
        self.name = name
        self.mode = "normal"

    def activate_emergency(self):
        self.mode = "emergency"
        print(f"{self.name} is in emergency mode.")
        # Implement decision-making and rapid response here

    def respond(self, context):
        if self.mode == "emergency":
            return f"{self.name} responds quickly to {context}."
        else:
            return f"{self.name} is in normal mode."

class DefensiveRestModule:
    def __init__(self, name):
        self.name = name
        self.mode = "normal"

    def switch_to_defensive(self):
        self.mode = "defensive"
        print(f"{self.name} is in defensive mode.")
        # Implement environmental scanning here

    def switch_to_rest(self):
        self.mode = "rest"
        print(f"{self.name} is in rest mode.")
        # Implement rest mode behavior here

    def respond(self, context):
        if self.mode == "defensive":
            return f"{self.name} is scanning the environment for {context}."
        elif self.mode == "rest":
            return f"{self.name} is in rest mode, blocking everything out."
        else:
            return f"{self.name} is in normal mode."

# Example usage
emergency_module = EmergencyModule("EM")
defensive_rest_module = DefensiveRestModule("DRM")

# Activate emergency mode
emergency_module.activate_emergency()
print(emergency_module.respond("critical situation"))

# Switch to defensive mode
defensive_rest_module.switch_to_defensive()
print(defensive_rest_module.respond("possible threat"))

# Switch to rest mode
defensive_rest_module.switch_to_rest()
print(defensive_rest_module.respond("time to rest"))
