# DISC scores initialisatie
scores = {"D": 0, "I": 0, "S": 0, "C": 0}

# Voorbeeldvragen
questions = {
    "D": "Ik neem graag de leiding in projecten.",
    "I": "Ik werk graag in een team en motiveer anderen.",
    "S": "Ik hou van een voorspelbare en stabiele werkomgeving.",
    "C": "Ik volg liever regels en ben analytisch in mijn benadering."
}

# Simulatie van antwoorden (1 - 5 schaal, 5 is het hoogst)
answers = {"D": 4, "I": 5, "S": 3, "C": 2}

# Scores berekenen
for type_, answer in answers.items():
    scores[type_] += answer

# Resultaten en feedback
for type_, score in scores.items():
    if type_ == "D":
        print(f"Dominantie Score: {score} - Sterke voorkeur voor leiderschap en controle.")
    elif type_ == "I":
        print(f"Invloed Score: {score} - Sociaal en enthousiasmerend.")
    elif type_ == "S":
        print(f"Stabiliteit Score: {score} - Geeft voorkeur aan consistentie en stabiliteit.")
    elif type_ == "C":
        print(f"Conformiteit Score: {score} - Nauwkeurig en gericht op regels.")
