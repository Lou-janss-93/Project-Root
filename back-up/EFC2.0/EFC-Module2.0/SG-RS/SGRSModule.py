class SEGRSModule:
    def __init__(self, scaling_factor):
        self.scaling_factor = scaling_factor  # Scaling factor k

    def evaluate_response(self, stimulus_intensity, evaluation):
        """ Bereken de respons op basis van stimulusintensiteit en evaluatie """
        response = stimulus_intensity * evaluation * self.scaling_factor
        return response

# Voorbeeldgebruik
scaling_factor = 1.5  # Voorbeeldwaarde voor de schaalfactor

# Maak een SEGRS-module
segrs_module = SEGRSModule(scaling_factor)

# Voorbeeldwaarden voor stimulusintensiteit en evaluatie
stimulus_intensity = 10  # Voorbeeld: intensiteit van de stimulus
evaluation = 0.8  # Voorbeeld: positieve evaluatie

# Bereken de respons
response = segrs_module.evaluate_response(stimulus_intensity, evaluation)
print(f"De berekende respons is: {response}")

# Voorbeeld met negatieve evaluatie
evaluation_negative = -0.5  # Voorbeeld: negatieve evaluatie
response_negative = segrs_module.evaluate_response(stimulus_intensity, evaluation_negative)
print(f"De berekende respons met negatieve evaluatie is: {response_negative}")