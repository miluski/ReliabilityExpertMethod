import pytest
from src.calculations.alpha_coefficients import calculate_alpha_k, calculate_alpha_e
from src.calculations.reliability_indicators import calculate_A0, calculate_E_T0, calculate_lambda_di
from src.calculations.expert_weights import calculate_Ke, calculate_module_weights

def test_example_alpha_k():
    """Test obliczania współczynnika konstrukcyjnego αk"""
    kmj_values = [1.2, 1.5, 1.3]
    expected_Km = 1.333
    expected_alpha_k = 0.75

    Km, alpha_k = calculate_alpha_k(kmj_values)

    assert abs(Km - expected_Km) < 0.01
    assert abs(alpha_k - expected_alpha_k) < 0.01

def test_example_alpha_e():
    """Test obliczania współczynnika elementowego αe"""
    expert_data = [
        [(0.5, 10), (0.3, 3), (0.15, 4), (0.05, 2)]
    ]
    expected_alpha_e = 0.2125

    alpha_ej_list, alpha_e = calculate_alpha_e(expert_data)

    assert abs(alpha_e - expected_alpha_e) < 0.001

def test_example_A0():
    """Test obliczania średniego strumienia uszkodzeń A0"""
    A_mean = 1.1e-5
    alpha_e = 0.46
    alpha_k = 0.83
    expected_A0 = 4.207e-6

    A0 = calculate_A0(A_mean, alpha_e, alpha_k)

    assert abs(A0 - expected_A0) < 1e-7

def test_example_E_T0():
    """Test obliczania oczekiwanego czasu poprawnej pracy E(T0)"""
    E_T = 900
    Km = 1.2
    Ke = 3.673
    expected_E_T0 = 3967.56

    E_T0 = calculate_E_T0(E_T, Km, Ke)

    assert abs(E_T0 - expected_E_T0) < 1.0

def test_example_module_weights():
    """Test obliczania wag modułów"""
    expert_damage_counts = [
        [10, 20, 30],
        [12, 18, 30],
        [11, 19, 30],
    ]
    num_modules = 3

    weights = calculate_module_weights(expert_damage_counts, num_modules)

    assert abs(sum(weights) - num_modules) < 0.001
    assert all(w > 0 for w in weights)
