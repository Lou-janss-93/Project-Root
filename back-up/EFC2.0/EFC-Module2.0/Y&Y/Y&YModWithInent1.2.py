class YinYangModule:
    def __init__(self, decay_constant=10):
        self.balance = 0  # Initial balance value
        self.decay_constant = decay_constant  # Decay constant for gradual return to zero

    def adjust_balance(self, context, intent):
        """ Adjusts the balance based on the context and intent """
        if context in ["Good", "Light"]:
            delta = -1
        elif context in ["Bad", "Dark"]:
            delta = +1
        else:
            delta = -self.balance / self.decay_constant  # Gradual return to zero

        # Adjust delta based on intent
        if intent == "strong":
            delta *= 2  # Double the effect for strong intent
        elif intent == "weak":
            delta *= 0.5  # Halve the effect for weak intent

        # Update the balance with the new delta, ensuring it stays within the range [-45, 45]
        self.balance = max(-45, min(45, self.balance + delta))

    def get_balance(self):
        """ Returns the current balance """
        return self.balance

# Voorbeeldgebruik
yin_yang_module = YinYangModule(decay_constant=10)

# Aanpassingen op basis van verschillende contexten en intenties
yin_yang_module.adjust_balance("Good", "strong")
print(f"Balance after 'Good' context with strong intent: {yin_yang_module.get_balance()}")

yin_yang_module.adjust_balance("Bad", "weak")
print(f"Balance after 'Bad' context with weak intent: {yin_yang_module.get_balance()}")

# Geen context, dus de balans keert geleidelijk terug naar nul
yin_yang_module.adjust_balance(None, None)
print(f"Balance after no context: {yin_yang_module.get_balance()}")