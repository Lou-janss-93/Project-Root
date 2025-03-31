def bereken_kern(WY, WP, WS, YYY, PPP, SSS):
    # Bereken de kern als een gewogen gemiddelde
    kern = (WY * YYY + WP * PPP + WS * SSS) / (WY + WP + WS)
    return kern

# Voorbeeldwaarden voor gewichten en outputs
WY = 0.3
WP = 0.4
WS = 0.3
YYY = 50
PPP = 70
SSS = 60

# Bereken de kern
kern_waarde = bereken_kern(WY, WP, WS, YYY, PPP, SSS)
print(f"De berekende kernwaarde is: {kern_waarde}")

# Voeg de kernberekening toe aan je bestaande modules
class Rest_NeedModule:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.rest = 0
        self.log = []

    def get_emotion(self):
        return "neutral"

    def get_status(self):
        return "stable"

    def adjust_balance(self, adjustment):
        self.balance += 1 if adjustment == "positief/goed" else -1

    def adjust_balance_dynamic(self, adjustment, amount):
        self.balance += amount if adjustment == "positief/goed" else -amount

    def adjust_rest(self, rest_state):
        self.rest = 1 if rest_state == "rest" else -1

class Intent_Module(Rest_NeedModule):
    def __init__(self, name):
        super().__init__(name)
        self.intentions = {"critical": False}

    def set_intention(self, intention, value):
        self.intentions[intention] = value

    def respond(self, trigger, WY, WP, WS, YYY, PPP, SSS):
        """ Generate response based on current balance, rest level, intention, and trigger input """
        emotion = self.get_emotion()
        status = self.get_status()
        intent_status = "critical" if self.intentions.get("critical") else "non-critical"
        kern = bereken_kern(WY, WP, WS, YYY, PPP, SSS)
        response = f"{self.name} responds in a {emotion} way to {trigger}. Status: {status}. Intention: {intent_status}. Kern: {kern}."
        self.log.append((trigger, self.balance, response))
        return response