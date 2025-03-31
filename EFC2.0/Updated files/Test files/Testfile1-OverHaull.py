import sys
sys.path.append('z:/Project-Root/EFC2.0/Updated files/sentiment-analysis-project')
from sentiment_analysis_EFCAdded import (calculate_core, YinYangModule, PESEBNModule,
    SEGRSModule,
    )
def test_different_oss():
    """
    Test different operational scenarios for sentiment analysis modules.

    This function tests various scenarios by calculating core values, adjusting balance,
    and evaluating responses using different modules. It prints the results for each scenario.
    """
    WY = 0.3
    WP = 0.4
    WS = 0.3
    gamma = 0.5
    delta = 0.5

    # Different scenarios
    scenarios = [
        {"YYY": 50, "PPP": 70, "SSS": 60, "context": "Good", "primary_needs": [0.8, 0.9, 0.7], "secondary_needs": [0.6, 0.5, 0.4], "stimulus_intensity": 10, "evaluation": 0.8},
        {"YYY": 30, "PPP": 50, "SSS": 40, "context": "Bad", "primary_needs": [0.5, 0.6, 0.4], "secondary_needs": [0.3, 0.2, 0.1], "stimulus_intensity": 5, "evaluation": 0.5},
        {"YYY": 70, "PPP": 90, "SSS": 80, "context": "Light", "primary_needs": [0.9, 1.0, 0.8], "secondary_needs": [0.7, 0.6, 0.5], "stimulus_intensity": 15, "evaluation": 1.0},
        {"YYY": 20, "PPP": 40, "SSS": 30, "context": "Dark", "primary_needs": [0.4, 0.5, 0.3], "secondary_needs": [0.2, 0.1, 0.0], "stimulus_intensity": 3, "evaluation": 0.3},
    ]

    for scenario in scenarios:
        core_value = calculate_core(WY, WP, WS, scenario["YYY"], scenario["PPP"], scenario["SSS"])
        yin_yang_module = YinYangModule(decay_constant=10)
        yin_yang_module.adjust_balance(scenario["context"])
        Y = yin_yang_module.get_balance()

        pesebn_module = PESEBNModule(alpha=0.6, beta=0.4)
        P = pesebn_module.bereken_P(scenario["primary_needs"], scenario["secondary_needs"])

        segrs_module = SEGRSModule(scaling_factor=1.5)
        S = segrs_module.evaluate_response(scenario["stimulus_intensity"], scenario["evaluation"])

        state = gamma * core_value + delta * (Y + P + S)
        print(f"Scenario: {scenario}")
        print(f"Core Value: {core_value}, Y: {Y}, P: {P}, S: {S}, Overall State: {state}\n")

if __name__ == "__main__":
    test_different_oss()