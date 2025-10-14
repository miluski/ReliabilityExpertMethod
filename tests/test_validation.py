import pytest
from src.utils.data_validation import validate_expert_inputs, validate_module_weights

def test_validate_expert_inputs_valid():
    valid_inputs = {
        'Kmj': [1.2, 1.5, 1.3],
        'Ng/N': [0.6, 0.2, 0.15, 0.05],
        'Kg': [2, 4, 1, 1]
    }
    assert validate_expert_inputs(valid_inputs) == True

def test_validate_expert_inputs_invalid():
    invalid_inputs = {
        'Kmj': [1.2, -1.5, 1.3],
        'Ng/N': [0.6, 0.2, 0.15, 0.05],
        'Kg': [2, 4, 1, 1]
    }
    assert validate_expert_inputs(invalid_inputs) == False

def test_validate_module_weights_valid():
    valid_weights = [10, 20, 30]
    assert validate_module_weights(valid_weights) == True

def test_validate_module_weights_invalid():
    invalid_weights = [10, -20, 30]  
    assert validate_module_weights(invalid_weights) == False

def test_validate_module_weights_empty():
    empty_weights = []
    assert validate_module_weights(empty_weights) == False
