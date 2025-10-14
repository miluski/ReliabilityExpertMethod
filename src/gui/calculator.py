from calculations.alpha_coefficients import calculate_alpha_k, calculate_alpha_e
from calculations.expert_weights import calculate_Ke
from calculations.reliability_indicators import calculate_A0, calculate_E_T0

class ReliabilityCalculator:
    def __init__(self):
        pass

    def calculate(self, config, kmj_values, expert_data):
        km, alpha_k = calculate_alpha_k(kmj_values)
        alpha_ej_list, alpha_e = calculate_alpha_e(expert_data)
        ke_j_list, ke = calculate_Ke(expert_data)

        results = self._build_results_text(km, alpha_k, alpha_e, alpha_ej_list, ke, ke_j_list)

        mode = config['mode']
        results += self._calculate_mode_specific(mode, config, km, ke, alpha_e, alpha_k)

        results += "\n" + "=" * 60 + "\n"

        return results

    def _build_results_text(self, km, alpha_k, alpha_e, alpha_ej_list, ke, ke_j_list):
        results = "=" * 60 + "\n"
        results += "WYNIKI OBLICZEŃ\n"
        results += "=" * 60 + "\n\n"

        results += f"1. WSPÓŁCZYNNIKI MECHANICZNE\n"
        results += f"   Km = {km:.4f}\n"
        results += f"   αk = {alpha_k:.4f}\n\n"

        results += f"2. WSPÓŁCZYNNIKI ELEKTRONICZNE\n"
        results += f"   αe = {alpha_e:.4f}\n"
        results += f"   Współczynniki ekspertów:\n"
        for i, alpha_ej in enumerate(alpha_ej_list, 1):
            results += f"      αe{i} = {alpha_ej:.4f}\n"

        results += f"\n3. WSPÓŁCZYNNIKI EKSPLOATACYJNE\n"
        results += f"   Ke = {ke:.4f}\n"
        results += f"   Współczynniki ekspertów:\n"
        for i, ke_j in enumerate(ke_j_list, 1):
            results += f"      Ke{i} = {ke_j:.4f}\n"

        return results

    def _calculate_mode_specific(self, mode, config, km, ke, alpha_e, alpha_k):
        results = ""

        if mode == 0:
            results += self._calculate_a0(config, alpha_e, alpha_k)
        elif mode == 1:
            results += self._calculate_e_t0(config, km, ke)
        elif mode == 2:
            results += self._calculate_lambda_di(config, alpha_e)

        return results

    def _calculate_a0(self, config, alpha_e, alpha_k):
        a_mean_str = config['a_mean']
        if a_mean_str:
            a_mean = float(a_mean_str)
            a0 = calculate_A0(a_mean, alpha_e, alpha_k)
            return (f"\n4. ŚREDNI STRUMIEŃ USZKODZEŃ\n"
                   f"   Ā = {a_mean:.6e}\n"
                   f"   A0 ≤ {a0:.6e}\n")
        else:
            return f"\n4. BRAK DANYCH dla Ā\n"

    def _calculate_e_t0(self, config, km, ke):
        t_str = config['t_expected']
        if t_str:
            t_expected = float(t_str)
            e_t0 = calculate_E_T0(t_expected, km, ke)
            return (f"\n4. OCZEKIWANY CZAS PRACY\n"
                   f"   E*(T) = {t_expected:.2f} h\n"
                   f"   E(T0) ≥ {e_t0:.2f} h\n")
        else:
            return f"\n4. BRAK DANYCH dla t\n"

    def _calculate_lambda_di(self, config, alpha_e):
        lambda_p_str = config['lambda_p']
        if lambda_p_str:
            lambda_p = float(lambda_p_str)
            ki_avg = 1.0 / alpha_e if alpha_e > 0 else 1.0
            alpha_i = 1.0 / ki_avg
            lambda_di = lambda_p * alpha_i
            return (f"\n4. INTENSYWNOŚĆ USZKODZEŃ NOWYCH ELEMENTÓW\n"
                   f"   λp = {lambda_p:.6e}\n"
                   f"   αi = {alpha_i:.4f}\n"
                   f"   λdi = {lambda_di:.6e}\n")
        else:
            return f"\n4. BRAK DANYCH dla λp\n"
