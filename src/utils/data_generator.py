import random


class DataGenerator:
    """Generates random data for reliability calculations"""

    def __init__(self):
        self.random = random.Random()

    def set_seed(self, seed=None):
        """Set random seed for reproducible results"""
        self.random.seed(seed)

    def generate_kmj_values(self, count):
        """Generate random Kmj values"""
        return [self._generate_kmj() for _ in range(count)]

    def _generate_kmj(self):
        """Generate single Kmj value (0.5 - 1.5)"""
        return round(self.random.uniform(0.5, 1.5), 4)

    def generate_expert_data(self, num_experts, num_groups):
        """Generate random expert data"""
        return [
            self._generate_expert_groups(num_groups)
            for _ in range(num_experts)
        ]

    def _generate_expert_groups(self, num_groups):
        """Generate groups for a single expert"""
        return [
            self._generate_group_values()
            for _ in range(num_groups)
        ]

    def _generate_group_values(self):
        """Generate (ng_n, kg) values for a group"""
        ng_n = round(self.random.uniform(0.8, 1.5), 4)
        kg = round(self.random.uniform(0.7, 1.2), 4)
        return (ng_n, kg)

    def generate_a_mean(self):
        """Generate random average failure stream (scientific notation)"""
        exponent = self.random.randint(-6, -3)
        mantissa = self.random.uniform(1.0, 9.9)
        return f"{mantissa:.2f}e{exponent}"

    def generate_t_expected(self):
        """Generate random expected operation time (hours)"""
        return round(self.random.uniform(500, 10000), 2)

    def generate_lambda_p(self):
        """Generate random failure intensity (scientific notation)"""
        exponent = self.random.randint(-7, -4)
        mantissa = self.random.uniform(1.0, 9.9)
        return f"{mantissa:.2f}e{exponent}"

    def generate_config_value(self, mode):
        """Generate appropriate value based on calculation mode"""
        mode_generators = {
            0: self.generate_a_mean,
            1: self.generate_t_expected,
            2: self.generate_lambda_p
        }
        generator = mode_generators.get(mode)
        return generator() if generator else None
