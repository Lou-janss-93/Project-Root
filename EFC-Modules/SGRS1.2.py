class RestBalanceModule:
    def __init__(self, name):
        self.name = name
        self.balance = 0  # Initialize balance
        self.positive_emotions = ["blij", "optimistisch", "tevreden"]
        self.log = []


    def adjust_balance(self, change):
        if change == "positive":
            self.balance += 1
        elif change == "negative":
            self.balance -= 1

    def adjust_balance_dynamic(self, change, amount):
        if change == "positive":
            self.balance += amount
        elif change == "negative":
            self.balance -= amount

class EmotionModule(RestBalanceModule):
    def __init__(self, name):
        super().__init__(name)
        self.log = []
        self.positive_emotions = ["blij", "optimistisch", "tevreden"]
        self.negative_emotions = ["verdrietig", "bezorgd", "gefrustreerd"]

    def get_emotion(self):
        if self.balance < 0:
            return self.positive_emotions[abs(self.balance) % len(self.positive_emotions)]
        else:
            return self.negative_emotions[self.balance % len(self.negative_emotions)]

    def respond(self, trigger):
        """ Generate response based on current balance and trigger input """
        emotion = self.get_emotion()
        response = f"{self.name} responds in a {emotion} way to {trigger}."
        self.log.append((trigger, self.balance, response))
        return response
class Rest_NeedModule(EmotionModule):
    def __init__(self, name):
        super().__init__(name)
        self.rest_level = 50  # Arbitrary initial rest level

    def adjust_rest(self, context):
        if context in ["rest", "peace"]:
            self.rest_level += 5  # Increase rest
        elif context in ["stress", "urgency"]:
            self.rest_level -= 5  # Decrease rest
        self.rest_level = max(0, min(100, self.rest_level))

    def get_status(self):
        status = "relaxed" if self.rest_level > 50 else "stressed"
        return f"{self.name} is currently {status}."

    def respond(self, trigger):
        """ Generate response based on current balance, rest level, and trigger input """
        emotion = self.get_emotion()
        status = self.get_status()
        response = f"{self.name} responds in a {emotion} way to {trigger}. Status: {status}."
        self.log.append((trigger, self.balance, response))
        return response
class Intent_Module(Rest_NeedModule):
    def __init__(self, name):
        super().__init__(name)
        self.intentions = {"critical": False}

    def set_intention(self, intention, value):
        self.intentions[intention] = value

    def respond(self, trigger):
        """ Generate response based on current balance, rest level, intention, and trigger input """
        emotion = self.get_emotion()
        status = self.get_status()
        intent_status = "critical" if self.intentions.get("critical") else "non-critical"
        response = f"{self.name} responds in a {emotion} way to {trigger}. Status: {status}. Intention: {intent_status}."
        self.log.append((trigger, self.balance, response))
        return response
mystique = Intent_Module("Myst.")
Neori = Intent_Module("Neori")

mystique.adjust_balance("positive")
Neori.adjust_balance_dynamic("negative", 2)
mystique.adjust_rest("rest")
Neori.adjust_rest("stress")

mystique.set_intention("critical", False)
print(Neori.respond("vraag over AI filosofie & ethiek"))

print(mystique.respond("vraag over AI filosofie"))
print(Neori.respond("dringend verzoek"))
print(Neori.respond("vraag over AI filosofie & ethiek"))
print(Neori.respond("vraag over AI filosofie & ethiek"))