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

# Voorbeeld trainingsdata voor emotiedetectie
training_data = [
    ("Ik ben zo blij en gelukkig vandaag.", "vreugde"),
    ("Ik voel me verdrietig en somber.", "verdriet"),
    ("Ik ben bang en nerveus.", "angst"),
    ("Ik ben verrast en ongelofelijk verbaasd.", "verrassing"),
    ("Ik voel walging en afschuw.", "walging"),
    ("Ik ben boos en kwaad.", "woede"),
    ("Ik voel liefde en genegenheid.", "liefde")
]

# Train een eenvoudig emotiedetectiemodel
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform([text for text, _ in training_data])
y_train = [label for _, label in training_data]

model = MultinomialNB()
model.fit(X_train, y_train)

def detect_emotion(text):
    """
    Detects the emotion of the given text.
    
    Args:
        text (str): The input text to analyze.
    
    Returns:
        str: The predicted emotion label.
    """
    try:
        cleaned_text = re.sub(r'[.,!?]', '', text).lower()
        X_test = vectorizer.transform([cleaned_text])
        predicted_emotion = model.predict(X_test)[0]
        return predicted_emotion
    except Exception as e:
        print(f"Error detecting emotion: {e}")
        return None

# Basic Framework for Yin-Yang & Rest/balance and Emotional Response in AI
# This is a simple version of the full module but does almost the same as the final version.
# The Yin-Yang module is to look at the input to see if it's positive or negative and then adjust the balance accordingly.
# The YinYangModule is to adjust the balance based on the context and severity of the input.
class YinYangModule:
    def __init__(self, name):
        """
        Initializes the YinYangModule with a name and default balance.
        
        Args:
            name (str): The name of the module.
        """
        self.name = name
        self.balance = 0  # Yin-Yang balance value, range: -45 (Yin) to +45 (Yang)
        self.log = []  # To keep track of balance adjustments and responses

    def adjust_balance(self, context):
        """
        Adjusts Yin-Yang balance based on input context.
        
        Args:
            context (str): The context indicating positive or negative input.
        """
        if context in ["positief/goed", "positive", "happy"]:
            self.balance -= 1  # Move towards Yin
        elif context in ["negatief/slecht", "negative", "sad"]:
            self.balance += 1  # Move towards Yang
        # Keep balance within bounds
        self.balance = max(-45, min(45, self.balance))

    def adjust_balance_dynamic(self, context, severity):
        """
        Dynamically adjusts Yin-Yang balance based on context severity.
        
        Args:
            context (str): The context indicating positive or negative input.
            severity (int): The severity of the context.
        """
        if context in ["positief/goed", "positive", "happy"]:
            self.balance -= severity  # Move towards Yin
        elif context in ["negatief/slecht", "negative", "sad"]:
            self.balance += severity  # Move towards Yang
        # Keep balance within bounds
        self.balance = max(-45, min(45, self.balance))

    def respond(self, trigger):
        """
        Generates response based on current balance and trigger input.
        
        Args:
            trigger (str): The trigger input to respond to.
        
        Returns:
            str: The generated response.
        """
        response = f"{self.name} responds in a calm (Yin) way to {trigger}." if self.balance < 0 else f"{self.name} responds in an active (Yang) way to {trigger}."
        self.log.append((trigger, self.balance, response))
        return response

# Example usage
text = "Ik ben zo blij en gelukkig vandaag."
dominant_emotion = detect_emotion(text)
print(f"Dominante emotie: {dominant_emotion}")

# Create an instance of YinYangModule
yy_module = YinYangModule("YY Module")
yy_module.adjust_balance(dominant_emotion)
response = yy_module.respond("vraag over AI filosofie")
print(response)