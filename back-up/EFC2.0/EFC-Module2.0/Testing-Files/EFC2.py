# Core calculation
def calculate_core(WY, WP, WS, YYY, PPP, SSS):
    core = (WY * YYY + WP * PPP + WS * SSS) / (WY + WP + WS)
    return core

# YinYangModule
class YinYangModule:
    def __init__(self, decay_constant=10):
        self.balance = 0
        self.decay_constant = decay_constant

    def adjust_balance(self, context):
        if context in ["Good", "Light"]:
            delta = -1
        elif context in ["Bad", "Dark"]:
            delta = +1
        else:
            delta = -self.balance / self.decay_constant

        self.balance = max(-45, min(45, self.balance + delta))

    def get_balance(self):
        return self.balance

# PESEBNModule
class PESEBNModule:
    def __init__(self, alpha, beta):
        self.alpha = alpha
        self.beta = beta

    def behoefte_voldoening(self, behoeften):
        return sum(behoeften)

    def bereken_P(self, primaire_behoeften, secundaire_behoeften):
        P = self.alpha * self.behoefte_voldoening(primaire_behoeften) + self.beta * self.behoefte_voldoening(secundaire_behoeften)
        return P

# SEGRSModule
class SEGRSModule:
    def __init__(self, scaling_factor):
        self.scaling_factor = scaling_factor

    def evaluate_response(self, stimulus_intensity, evaluation):
        response = stimulus_intensity * evaluation * self.scaling_factor
        return response

# Example usage
WY = 0.3
WP = 0.4
WS = 0.3
YYY = 50
PPP = 70
SSS = 60
gamma = 0.5
delta = 0.5

# Calculate core
core_value = calculate_core(WY, WP, WS, YYY, PPP, SSS)
print(f"The calculated core value is: {core_value}")

# YinYangModule
yin_yang_module = YinYangModule(decay_constant=10)
yin_yang_module.adjust_balance("Good")
Y = yin_yang_module.get_balance()
print(f"YinYangModule balance: {Y}")

# PESEBNModule
alpha = 0.6
beta = 0.4
primaire_behoeften = [0.8, 0.9, 0.7]
secundaire_behoeften = [0.6, 0.5, 0.4]
pesebn_module = PESEBNModule(alpha, beta)
P = pesebn_module.bereken_P(primaire_behoeften, secundaire_behoeften)
print(f"PESEBNModule P value: {P}")

# SEGRSModule
scaling_factor = 1.5
stimulus_intensity = 10
evaluation = 0.8
segrs_module = SEGRSModule(scaling_factor)
S = segrs_module.evaluate_response(stimulus_intensity, evaluation)
print(f"SEGRSModule response: {S}")

# Calculate overall state
state = gamma * core_value + delta * (Y + P + S)
print(f"Overall system state: {state}")