import csv


class CsvExporter:
    """Handles exporting results to CSV format"""

    def export(self, results_data, writer):
        """Export results to CSV using provided writer"""
        self._write_header(writer)
        self._write_input_data(writer, results_data)
        self._write_results(writer, results_data)

    def _write_header(self, writer):
        """Write CSV header"""
        writer.writerow(['========================================'])
        writer.writerow(['DANE WEJŚCIOWE I WYNIKI OBLICZEŃ'])
        writer.writerow(['========================================'])
        writer.writerow([])

    def _write_input_data(self, writer, results_data):
        """Write input data section"""
        self._write_config(writer, results_data)
        self._write_kmj_values(writer, results_data)
        self._write_expert_data(writer, results_data)

    def _write_config(self, writer, results_data):
        """Write configuration section"""
        config = results_data.get('config', {})
        writer.writerow(['KONFIGURACJA'])
        writer.writerow(['Tryb obliczeń', self._get_mode_name(config.get('mode', 0))])
        writer.writerow(['Liczba ekspertów', config.get('j_elec', 0)])
        writer.writerow(['Liczba grup', config.get('n_groups', 0)])

        self._write_optional_config(writer, config)
        writer.writerow([])

    def _write_optional_config(self, writer, config):
        """Write optional configuration parameters"""
        if config.get('a_mean'):
            writer.writerow(['Średni strumień (Ā)', config.get('a_mean')])
        if config.get('t_expected'):
            writer.writerow(['Oczekiwany czas (E*(T))', f"{float(config.get('t_expected')):.2f} h"])
        if config.get('lambda_p'):
            writer.writerow(['Lambda p (λp)', config.get('lambda_p')])

    def _write_kmj_values(self, writer, results_data):
        """Write Kmj values section"""
        kmj_values = results_data.get('kmj_values', [])
        if not kmj_values:
            return

        writer.writerow(['DANE MECHANICZNE - Kmj'])
        for i, kmj in enumerate(kmj_values, 1):
            writer.writerow([f'Kmj{i}', f'{kmj:.4f}'])
        writer.writerow([])

    def _write_expert_data(self, writer, results_data):
        """Write expert data section"""
        expert_data = results_data.get('expert_data', [])
        if not expert_data:
            return

        writer.writerow(['DANE EKSPERTÓW (Grupy)'])
        for i, expert_groups in enumerate(expert_data, 1):
            self._write_expert_groups(writer, i, expert_groups)
        writer.writerow([])

    def _write_expert_groups(self, writer, expert_num, expert_groups):
        """Write groups for a single expert"""
        writer.writerow([f'Ekspert {expert_num}', '', ''])
        writer.writerow(['  Grupa', 'ng_n', 'kg'])

        if isinstance(expert_groups, list):
            for j, group in enumerate(expert_groups, 1):
                if isinstance(group, (tuple, list)) and len(group) >= 2:
                    ng_n, kg = group[0], group[1]
                    writer.writerow([f'  {j}', f'{ng_n:.4f}', f'{kg:.4f}'])

    def _write_results(self, writer, results_data):
        """Write calculation results section"""
        writer.writerow(['========================================'])
        writer.writerow(['WYNIKI OBLICZEŃ'])
        writer.writerow(['========================================'])
        writer.writerow([])

        self._write_mechanical_coefficients(writer, results_data)
        self._write_electronic_coefficients(writer, results_data)
        self._write_exploitation_coefficients(writer, results_data)
        self._write_mode_specific(writer, results_data)

    def _write_mechanical_coefficients(self, writer, results_data):
        """Write mechanical coefficients"""
        writer.writerow(['WSPÓŁCZYNNIKI MECHANICZNE'])
        writer.writerow(['Km', f"{results_data.get('km', 0):.4f}"])
        writer.writerow(['αk', f"{results_data.get('alpha_k', 0):.4f}"])
        writer.writerow([])

    def _write_electronic_coefficients(self, writer, results_data):
        """Write electronic coefficients"""
        writer.writerow(['WSPÓŁCZYNNIKI ELEKTRONICZNE'])
        writer.writerow(['αe', f"{results_data.get('alpha_e', 0):.4f}"])

        if 'alpha_ej_list' in results_data:
            for i, alpha_ej in enumerate(results_data['alpha_ej_list'], 1):
                writer.writerow([f'αe{i}', f'{alpha_ej:.4f}'])
        writer.writerow([])

    def _write_exploitation_coefficients(self, writer, results_data):
        """Write exploitation coefficients"""
        writer.writerow(['WSPÓŁCZYNNIKI EKSPLOATACYJNE'])
        writer.writerow(['Ke', f"{results_data.get('ke', 0):.4f}"])

        if 'ke_j_list' in results_data:
            for i, ke_j in enumerate(results_data['ke_j_list'], 1):
                writer.writerow([f'Ke{i}', f'{ke_j:.4f}'])
        writer.writerow([])

    def _write_mode_specific(self, writer, results_data):
        """Write mode-specific results"""
        if 'mode_specific' not in results_data or not results_data['mode_specific']:
            return

        writer.writerow(['WYNIKI SPECYFICZNE DLA TRYBU'])
        mode_data = results_data['mode_specific']

        for key, value in mode_data.items():
            formatted_value = self._format_value(value)
            writer.writerow([key, formatted_value])

    def _format_value(self, value):
        """Format value for CSV output"""
        if isinstance(value, (int, float)):
            if abs(value) < 0.001:
                return f'{value:.6e}'
            return f'{value:.4f}'
        return str(value)

    def _get_mode_name(self, mode):
        """Get human-readable mode name"""
        modes = {
            0: "Średni strumień uszkodzeń (A0)",
            1: "Oczekiwany czas pracy (E(T0))",
            2: "Intensywność uszkodzeń (λdi)"
        }
        return modes.get(mode, f"Tryb {mode}")
