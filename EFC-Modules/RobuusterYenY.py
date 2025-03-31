# Basic Framework for Yin-Yang & Rest/balance and Emotional Response in AI

class Rest_BalanceModule:
    def __init__(self, name):
        self.name = name
        self.balance = 0  # Yin-Yang balance value, range: -45 (Yin) to +45 (Yang)
        self.log = []  # To keep track of balance adjustments and responses

    def adjust_balance(self, context):
        """ Adjusts Yin-Yang balance based on input context """
        if context in ["Good/Light", "positive", "happy"]:
            self.balance -= 1  # Move towards Yin
        elif context in ["Bad/Dark", "negative", "sad"]:
            self.balance += 1  # Move towards Yang
        # Keep balance within bounds
        self.balance = max(-45, min(45, self.balance))

    def adjust_balance_dynamic(self, context, severity):
        """ Dynamically adjusts Yin-Yang balance based on context severity """
        if context in ["Good/Light", "positive", "happy"]:
            self.balance -= severity  # Move towards Yin
        elif context in ["Bad/Dark", "negative", "sad"]:
            self.balance += severity  # Move towards Yang
        # Keep balance within bounds
        self.balance = max(-45, min(45, self.balance))

    def respond(self, trigger):
        """ Generate response based on current balance and trigger input """
        response = f"{self.name} responds in a calm (Yin) way to {trigger}." if self.balance < 0 else f"{self.name} responds in an active (Yang) way to {trigger}."
        self.log.append((trigger, self.balance, response))
        return response

# Example usage
mystique = Rest_BalanceModule("Myst.")
Neori = Rest_BalanceModule("Neori")

# Adjusting balance based on context
mystique.adjust_balance("positive")
Neori.adjust_balance_dynamic("negative", 2)

# Sample responses based on triggers
print(mystique.respond("question about AI philosophy"))
print(Neori.respond("urgent request"))
