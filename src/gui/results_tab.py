from PyQt5.QtWidgets import QWidget, QVBoxLayout, QMessageBox

from gui.widgets import ExportButtonPanel, ResultsTextWidget
from gui.export import TxtExporter, CsvExporter, JsonExporter
from gui.export.export_manager import ExportManager
from gui.print import PrintManager


class ResultsTab(QWidget):
    """Tab for displaying and exporting calculation results"""

    def __init__(self):
        super().__init__()
        self.results_data = None
        self._init_components()
        self._init_ui()

    def _init_components(self):
        """Initialize component classes"""
        self.text_widget = ResultsTextWidget()
        self.button_panel = ExportButtonPanel()
        self.export_manager = ExportManager(self)
        self.print_manager = PrintManager(self)

        self.txt_exporter = TxtExporter()
        self.csv_exporter = CsvExporter()
        self.json_exporter = JsonExporter()

    def _init_ui(self):
        """Initialize UI layout"""
        layout = QVBoxLayout()
        self.setLayout(layout)

        layout.addWidget(self.text_widget.get_widget())
        layout.addLayout(self._create_button_layout())

    def _create_button_layout(self):
        """Create button panel layout"""
        self.button_panel.create_buttons(
            self.export_to_txt,
            self.export_to_csv,
            self.export_to_json,
            self.print_results
        )
        return self.button_panel.create_layout()

    def display_results(self, results_text, results_data=None):
        """Display calculation results"""
        self.text_widget.set_text(results_text)

        if results_data:
            self.results_data = results_data
            self.button_panel.enable_all()

    def clear_results(self):
        """Clear displayed results"""
        self.text_widget.set_text("Wyniki obliczeń pojawią się tutaj po naciśnięciu 'Oblicz'")
        self.results_data = None
        self.button_panel.disable_all()

    def export_to_txt(self):
        """Export results to TXT file"""
        if not self._validate_data():
            return

        content = self.txt_exporter.export(
            self.text_widget.get_text(),
            self.results_data
        )
        self.export_manager.export_to_txt(content)

    def export_to_csv(self):
        """Export results to CSV file"""
        if not self._validate_data():
            return

        self.export_manager.export_to_csv(
            self.csv_exporter.export,
            self.results_data
        )

    def export_to_json(self):
        """Export results to JSON file"""
        if not self._validate_data():
            return

        data = self.json_exporter.export(self.results_data)
        self.export_manager.export_to_json(data)

    def print_results(self):
        """Print results using system print dialog"""
        self.print_manager.print_text(self.text_widget.get_widget())

    def _validate_data(self):
        """Validate that results data exists"""
        if not self.results_data:
            QMessageBox.warning(
                self,
                "Brak danych",
                "Brak danych strukturalnych do eksportu."
            )
            return False
        return True
