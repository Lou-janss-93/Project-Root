class PESEBNModule:
    def __init__(self, alpha, beta):
        self.alpha = alpha
        self.beta = beta
        self.name = "PESEBN Module"  # naam toevoegen

    def behoefte_voldoening(self, behoeften):
        """ Bereken de voldoening van behoeften, waarbij elke behoefte een waarde tussen 0 en 1 heeft """
        return sum(behoeften)

    def bereken_P(self, primaire_behoeften, secundaire_behoeften):
        """ Bereken de waarde P op basis van de voldoening van primaire en secundaire behoeften """
        P = self.alpha * self.behoefte_voldoening(primaire_behoeften) + self.beta * self.behoefte_voldoening(secundaire_behoeften)
        return P

    def some_functionality(self):
        """ Voeg hier de specifieke functionaliteit toe """
        print(f"{self.name} is performing some functionality.")
        return self.bereken_P([0.8, 0.9, 0.7], [0.6, 0.5, 0.4])  # Example values

# Voorbeeld gebruik
if __name__ == "__main__":
    alpha = 0.6  # Gewicht voor primaire behoeften
    beta = 0.4   # Gewicht voor secundaire behoeften

    # Voorbeeldwaarden voor behoeften (waarden tussen 0 en 1)
    primaire_behoeften = [0.8, 0.9, 0.7]  # Voorbeeld: voedsel, water, onderdak
    secundaire_behoeften = [0.6, 0.5, 0.4]  # Voorbeeld: sociale interactie, zelfontplooiing

    # Maak een PESEBN-module
    pesebn_module = PESEBNModule(alpha, beta)

    # Bereken de waarde P
    P_waarde = pesebn_module.bereken_P(primaire_behoeften, secundaire_behoeften)
    print(f"De berekende waarde van P is: {P_waarde}")