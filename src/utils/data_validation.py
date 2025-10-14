def validate_positive_number(value):
    try:
        number = float(value)
        if number <= 0:
            raise ValueError("Value must be a positive number.")
        return number
    except ValueError as e:
        raise ValueError(f"Invalid input: {e}")

def validate_percentage(value):
    try:
        percentage = float(value)
        if percentage < 0 or percentage > 100:
            raise ValueError("Percentage must be between 0 and 100.")
        return percentage
    except ValueError as e:
        raise ValueError(f"Invalid input: {e}")

def validate_expert_input(expert_data):
    if not isinstance(expert_data, dict):
        raise ValueError("Expert data must be a dictionary.")

    for expert, data in expert_data.items():
        if 'Km' in data:
            validate_positive_number(data['Km'])
        if 'Ng' in data:
            validate_percentage(data['Ng'])
        if 'Kg' in data:
            validate_positive_number(data['Kg'])

def validate_module_weights(weights):
    if not isinstance(weights, list):
        raise ValueError("Weights must be a list.")

    total_weight = sum(weights)
    if total_weight <= 0:
        raise ValueError("Total weight must be greater than zero.")

    return weights
