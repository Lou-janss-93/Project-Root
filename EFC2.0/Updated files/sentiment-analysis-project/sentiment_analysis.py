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
    if "happy" in text:
        return "happy"
    elif "sad" in text:
        return "sad"
    elif "okay" in text:
        return "neutral"
    elif "happy" in text and "sad" in text:
        return "mixed"
    elif "anxious" in text:
        return "anxious"
    else:
        return "unknown"