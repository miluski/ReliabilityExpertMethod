import unittest
from src.calculations.alpha_coefficients import calculate_alpha_k, calculate_alpha_e
from src.calculations.reliability_indicators import calculate_A0, calculate_E_T0, calculate_lambda_di

class TestCalculations(unittest.TestCase):

    def test_calculate_alpha_k(self):
        Km_values = [1.3, 1.0, 1.2]
        expected_alpha_k = 1 / (sum(Km_values) / len(Km_values))
        self.assertAlmostEqual(calculate_alpha_k(Km_values), expected_alpha_k)

    def test_calculate_alpha_e(self):
        Ng_N_values = [0.6, 0.2, 0.15, 0.05]
        Kg_values = [2, 4, 1, 1]
        expected_alpha_e = sum((Ng / N) * (1 / Kg) for Ng, Kg in zip(Ng_N_values, Kg_values)) / len(Ng_N_values)
        self.assertAlmostEqual(calculate_alpha_e(Ng_N_values, Kg_values), expected_alpha_e)

    def test_calculate_A0(self):
        A_bar = 1.1e-5
        alpha_e = 0.86
        alpha_k = 0.86
        expected_A0 = A_bar * alpha_e * alpha_k
        self.assertAlmostEqual(calculate_A0(A_bar, alpha_e, alpha_k), expected_A0)

    def test_calculate_E_T0(self):
        E_T = 900
        Km = 1.2
        Ke = 3.673
        expected_E_T0 = E_T * Km * Ke
        self.assertAlmostEqual(calculate_E_T0(E_T, Km, Ke), expected_E_T0)

    def test_calculate_lambda_di(self):
        lambda_p = 1e-5
        alpha_i = 0.17
        expected_lambda_di = lambda_p * alpha_i
        self.assertAlmostEqual(calculate_lambda_di(lambda_p, alpha_i), expected_lambda_di)

if __name__ == '__main__':
    unittest.main()