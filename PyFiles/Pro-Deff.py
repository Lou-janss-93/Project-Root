# Import de benodigde bibliotheken
from sklearn.linear_model import LinearRegression
import numpy as np

# Data voor training (voor nu kiezen we simpele data)
# X: Eigenschap (bijvoorbeeld de grootte van een huis in vierkante meters)
# y: Prijs (bijvoorbeeld de prijs van een huis)
X = np.array([[1], [2], [3], [4], [5]])  # Een lijst met groottes
y = np.array([1, 4, 9, 16, 25])         # De bijbehorende prijzen

# Maak en train het model
model = LinearRegression()               # We maken een eenvoudig model
model.fit(X, y)                          # Train het model met de data

# Voorspelling voor een nieuw voorbeeld
nieuwe_data = np.array([[6]])            # Grootte van een huis
voorspelling = model.predict(nieuwe_data)

# Print de voorspelling
print("Voorspelling voor een huis van 6 m²:", voorspelling)
