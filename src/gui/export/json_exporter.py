from datetime import datetime


class JsonExporter:
    """Handles exporting results to JSON format"""

    def export(self, results_data):
        """Export results to JSON structure"""
        return {
            'timestamp': datetime.now().isoformat(),
            'input_data': self._extract_input_data(results_data),
            'calculation_results': self._extract_calculation_results(results_data)
        }

    def _extract_input_data(self, results_data):
        """Extract input data section"""
        return {
            'config': results_data.get('config', {}),
            'kmj_values': results_data.get('kmj_values', []),
            'expert_data': results_data.get('expert_data', [])
        }

    def _extract_calculation_results(self, results_data):
        """Extract calculation results section"""
        return {
            'km': results_data.get('km'),
            'alpha_k': results_data.get('alpha_k'),
            'alpha_e': results_data.get('alpha_e'),
            'alpha_ej_list': results_data.get('alpha_ej_list', []),
            'ke': results_data.get('ke'),
            'ke_j_list': results_data.get('ke_j_list', []),
            'mode': results_data.get('mode'),
            'mode_specific': results_data.get('mode_specific', {})
        }
