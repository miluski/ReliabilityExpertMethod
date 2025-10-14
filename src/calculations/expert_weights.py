def calculate_Ke(expert_data):
    if not expert_data:
        raise ValueError("Dane ekspertów nie mogą być puste")

    J = len(expert_data)
    ke_j_list = []

    for expert_groups in expert_data:
        ke_j = 0.0
        for ng_n, kg_j in expert_groups:
            ke_j += (ng_n * kg_j)
        ke_j_list.append(ke_j)

    ke = sum(ke_j_list) / J

    return ke_j_list, ke


def calculate_module_weights(expert_damage_counts, num_modules):
    if not expert_damage_counts:
        raise ValueError("Dane ankiet nie mogą być puste")

    K = len(expert_damage_counts)
    N = num_modules

    mj_list = []
    for j in range(N):
        mjk_sum = sum(expert_damage_counts[k][j] for k in range(K))
        mj = mjk_sum / K
        mj_list.append(mj)

    m = sum(mj_list)

    if m == 0:
        raise ValueError("Suma uszkodzeń nie może być zero")

    module_weights = [(mj * N) / m for mj in mj_list]

    return module_weights


def normalize_weights(weights):
    if isinstance(weights, dict):
        total = sum(weights.values())
        if total == 0:
            raise ValueError("Suma wag nie może być zero")
        return {key: val / total for key, val in weights.items()}
    else:
        total = sum(weights)
        if total == 0:
            raise ValueError("Suma wag nie może być zero")
        return [w / total for w in weights]
