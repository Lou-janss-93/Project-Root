from EFC2 import calculate_core, YinYangModule, PESEBNModule, SEGRSModule

def test_critical_point():
    WY = 0.3
    WP = 0.4
    WS = 0.3
    gamma = 0.5
    delta = 0.5

    # Critical scenario
    critical_scenario = {
        "YYY": 100, "PPP": 100, "SSS": 100, "context": "Bad",
        "primary_needs": [1.0, 1.0, 1.0], "secondary_needs": [1.0, 1.0, 1.0],
        "stimulus_intensity": 20, "evaluation": 1.5
    }

    core_value = calculate_core(WY, WP, WS, critical_scenario["YYY"], critical_scenario["PPP"], critical_scenario["SSS"])
    yin_yang_module = YinYangModule(decay_constant=10)
    yin_yang_module.adjust_balance(critical_scenario["context"])
    Y = yin_yang_module.get_balance()

    pesebn_module = PESEBNModule(alpha=0.6, beta=0.4)
    P = pesebn_module.bereken_P(critical_scenario["primary_needs"], critical_scenario["secondary_needs"])

    segrs_module = SEGRSModule(scaling_factor=1.5)
    S = segrs_module.evaluate_response(critical_scenario["stimulus_intensity"], critical_scenario["evaluation"])

    state = gamma * core_value + delta * (Y + P + S)
    print(f"Critical Scenario: {critical_scenario}")
    print(f"Core Value: {core_value}, Y: {Y}, P: {P}, S: {S}, Overall State: {state}\n")

if __name__ == "__main__":
    test_critical_point()