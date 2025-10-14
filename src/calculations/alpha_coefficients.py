def calculate_alpha_k(kmj_values):
    if not kmj_values:
        raise ValueError("Lista Kmj nie może być pusta")

    J = len(kmj_values)
    Km = sum(kmj_values) / J
    alpha_k = 1.0 / Km

    return Km, alpha_k


def calculate_alpha_e(expert_data):
    if not expert_data:
        raise ValueError("Dane ekspertów nie mogą być puste")

    J = len(expert_data)
    alpha_ej_list = []

    for expert_groups in expert_data:
        alpha_ej = 0.0
        for ng_n, kg in expert_groups:
            if kg <= 0:
                raise ValueError(f"Kg musi być większe od 0, otrzymano: {kg}")
            alpha_ej += (ng_n / kg)
        alpha_ej_list.append(alpha_ej)

    alpha_e = sum(alpha_ej_list) / J

    return alpha_ej_list, alpha_e


def calculate_alpha_i(ki):
    if ki <= 0:
        raise ValueError("ki musi być większe od 0")

    return 1.0 / ki
