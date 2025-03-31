import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Vereenvoudigd emotielexicon
emotions = {
    "vreugde": ["blij", "gelukkig", "vrolijk"],
    "vertrouwen": ["vertrouwen", "zeker", "zelfverzekerd"],
    "angst": ["bang", "nerveus", "gespannen"],
    "verrassing": ["verrast", "ongelofelijk", "verbazing"],
    "verdriet": ["verdrietig", "somber", "huilen"],
    "walging": ["walging", "afschuw", "weerzin"],
    "woede": ["boos", "kwaad", "razend"],
    "liefde": ["liefde", "houden van", "genegenheid"]
}

# Example training data for emotion detection
training_data = [
    ("Ik ben zo blij en gelukkig vandaag.", "vreugde"),
    ("Ik voel me verdrietig en somber.", "verdriet"),
    ("Ik ben bang en nerveus.", "angst"),
    # Add more training examples
]

# Train a simple emotion detection model
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform([text for text, label in training_data])
y_train = [label for text, label in training_data]

model = MultinomialNB()
model.fit(X_train, y_train)

def detect_emotion(text):
    cleaned_text = re.sub(r'[.,!?]', '', text).lower()
    X_test = vectorizer.transform([cleaned_text])
    predicted_emotion = model.predict(X_test)[0]
    return predicted_emotion

class Rest_BalanceModule:
    def __init__(self, name):
        self.name = name
        self.balance = 0  # Yin-Yang balance value, range: -45 (Yin) to +45 (Yang)
        self.log = []  # To keep track of balance adjustments and responses

    def adjust_balance(self, context):
        """ Adjusts Yin-Yang balance based on input context """
        if context in ["positief/goed", "positive", "happy"]:
            self.balance -= 1  # Move towards Yin
        elif context in ["negatief/slecht", "negative", "sad"]:
            self.balance += 1  # Move towards Yang
        # Keep balance within bounds
        self.balance = max(-45, min(45, self.balance))

    def adjust_balance_dynamic(self, context, severity):
        """ Dynamically adjusts Yin-Yang balance based on context severity """
        if context in ["positief/goed", "positive", "happy"]:
            self.balance -= severity  # Move towards Yin
        elif context in ["negatief/slecht", "negative", "sad"]:
            self.balance += severity  # Move towards Yang
        # Keep balance within bounds
        self.balance = max(-45, min(45, self.balance))

    def respond(self, trigger):
        """ Generate response based on current balance and trigger input """
        response = f"{self.name} responds in a calm (Yin) way to {trigger}." if self.balance < 0 else f"{self.name} responds in an active (Yang) way to {trigger}."
        self.log.append((trigger, self.balance, response))
        return response

class EmotionModule(Rest_BalanceModule):
    def __init__(self, name):
        super().__init__(name)
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

# Example usage
mystique = Intent_Module("Myst.")
Neori = Intent_Module("Neori")

mystique.adjust_balance("positief/goed")
Neori.adjust_balance_dynamic("negatief/slecht", 2)
mystique.adjust_rest("rest")
Neori.adjust_rest("stress")

mystique.set_intention("critical", False)
print(Neori.respond("vraag over AI filosofie en ethiek"))

print(mystique.respond("vraag over AI filosofie"))
print(Neori.respond("dringend verzoek"))
print(mystique.respond("vraag over AI filosofie & ethiek"))
print(Neori.respond("vraag over AI filosofie & ethiek"))