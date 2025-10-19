from datetime import datetime


class TxtExporter:
    """Handles exporting results to TXT format"""

    def export(self, results_text, results_data):
        """Export results to TXT file"""
        content = self._build_content(results_text, results_data)
        return content

    def _build_content(self, results_text, results_data):
        """Build complete TXT content"""
        sections = [
            self._build_header(),
            self._build_input_section(results_data),
            self._build_results_section(results_text)
        ]
        return '\n'.join(sections)

    def _build_header(self):
        """Build header section"""
        return "=" * 60 + "\nDANE WEJŚCIOWE\n" + "=" * 60 + "\n"

    def _build_input_section(self, results_data):
        """Build input data section"""
        if not results_data:
            return ""

        sections = [
            self._build_config_section(results_data),
            self._build_kmj_section(results_data),
            self._build_expert_section(results_data)
        ]
        return '\n'.join(filter(None, sections))

    def _build_config_section(self, results_data):
        """Build configuration section"""
        config = results_data.get('config', {})
        lines = ["KONFIGURACJA:"]

        lines.append(f"  Tryb: {self._get_mode_name(config.get('mode', 0))}")
        lines.append(f"  Liczba ekspertów: {config.get('j_elec', 0)}")
        lines.append(f"  Liczba grup: {config.get('n_groups', 0)}")

        lines.extend(self._add_optional_params(config))
        return '\n'.join(lines) + '\n'

    def _add_optional_params(self, config):
        """Add optional configuration parameters"""
        lines = []
        if config.get('a_mean'):
            lines.append(f"  Średni strumień (Ā): {config.get('a_mean')}")
        if config.get('t_expected'):
            lines.append(f"  Oczekiwany czas (E*(T)): {float(config.get('t_expected')):.2f} h")
        if config.get('lambda_p'):
            lines.append(f"  Lambda p (λp): {config.get('lambda_p')}")
        return lines

    def _build_kmj_section(self, results_data):
        """Build Kmj values section"""
        kmj_values = results_data.get('kmj_values', [])
        if not kmj_values:
            return ""

        lines = ["DANE MECHANICZNE (Kmj):"]
        for i, kmj in enumerate(kmj_values, 1):
            lines.append(f"  Kmj{i} = {kmj:.4f}")
        return '\n'.join(lines) + '\n'

    def _build_expert_section(self, results_data):
        """Build expert data section"""
        expert_data = results_data.get('expert_data', [])
        if not expert_data:
            return ""

        lines = ["DANE EKSPERTÓW (Grupy):"]
        for i, expert_groups in enumerate(expert_data, 1):
            lines.extend(self._format_expert_groups(i, expert_groups))
        return '\n'.join(lines) + '\n'

    def _format_expert_groups(self, expert_num, expert_groups):
        """Format groups for a single expert"""
        lines = [f"\n  Ekspert {expert_num}:"]

        if isinstance(expert_groups, list):
            for j, group in enumerate(expert_groups, 1):
                if isinstance(group, (tuple, list)) and len(group) >= 2:
                    ng_n, kg = group[0], group[1]
                    lines.append(f"    Grupa {j}: ng_n = {ng_n:.4f}, kg = {kg:.4f}")
        return lines

    def _build_results_section(self, results_text):
        """Build results section"""
        header = "\n" + "=" * 60 + "\nWYNIKI OBLICZEŃ\n" + "=" * 60 + "\n\n"
        return header + results_text

    def _get_mode_name(self, mode):
        """Get human-readable mode name"""
        modes = {
            0: "Średni strumień uszkodzeń (A0)",
            1: "Oczekiwany czas pracy (E(T0))",
            2: "Intensywność uszkodzeń (λdi)"
        }
        return modes.get(mode, f"Tryb {mode}")
