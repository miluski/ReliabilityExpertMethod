def calculate_A0(A_mean, alpha_e, alpha_k):
    return A_mean * alpha_e * alpha_k

def calculate_E_T0(E_T, K_m, K_e):
    return E_T * K_m * K_e

def calculate_lambda_di(lambda_p, alpha_i):
    return lambda_p * alpha_i

def compute_reliability_indicators(A_mean, E_T, lambda_p, alpha_e, alpha_k, K_m, K_e, alpha_i):
    A0 = calculate_A0(A_mean, alpha_e, alpha_k)
    E_T0 = calculate_E_T0(E_T, K_m, K_e)
    lambda_di = calculate_lambda_di(lambda_p, alpha_i)

    return A0, E_T0, lambda_di
