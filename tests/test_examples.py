import pytest
from src.calculations.alpha_coefficients import calculate_alpha_coefficients
from src.calculations.reliability_indicators import calculate_reliability_indicators
from src.calculations.expert_weights import calculate_expert_weights

def test_alpha_coefficients():
    expert_inputs = [1.2, 1.5, 1.3]
    expected_alpha_e, expected_alpha_k = 1.333, 0.75
    alpha_e, alpha_k = calculate_alpha_coefficients(expert_inputs)
    assert alpha_e == expected_alpha_e
    assert alpha_k == expected_alpha_k

def test_reliability_indicators():
    A_mean = 1.1e-5
    alpha_e = 0.86
    alpha_k = 0.75
    expected_A0 = 0.435e-5
    A0 = calculate_reliability_indicators(A_mean, alpha_e, alpha_k)
    assert A0 == expected_A0

def test_expert_weights():
    damages = [10, 20, 30]
    expected_weights = [0.1667, 0.3333, 0.5]
    weights = calculate_expert_weights(damages)
    assert weights == pytest.approx(expected_weights, rel=1e-2)
