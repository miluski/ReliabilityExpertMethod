from datetime import datetime
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import csv
import json


class ExportManager:
    """Manages file export operations with file dialogs"""

    def __init__(self, parent_widget):
        self.parent = parent_widget

    def export_to_txt(self, content):
        """Export content to TXT file"""
        filename = self._get_save_filename(
            "Zapisz wyniki do TXT",
            "txt",
            "Text Files (*.txt)"
        )

        if filename:
            self._write_text_file(filename, content)

    def export_to_csv(self, writer_callback, results_data):
        """Export data to CSV file using callback"""
        filename = self._get_save_filename(
            "Zapisz wyniki do CSV",
            "csv",
            "CSV Files (*.csv)"
        )

        if filename:
            self._write_csv_file(filename, writer_callback, results_data)

    def export_to_json(self, data):
        """Export data to JSON file"""
        filename = self._get_save_filename(
            "Zapisz wyniki do JSON",
            "json",
            "JSON Files (*.json)"
        )

        if filename:
            self._write_json_file(filename, data)

    def _get_save_filename(self, title, extension, file_filter):
        """Get filename from save dialog"""
        default_name = f"reliability_results_{self._get_timestamp()}.{extension}"
        filename, _ = QFileDialog.getSaveFileName(
            self.parent,
            title,
            default_name,
            file_filter
        )
        return filename

    def _get_timestamp(self):
        """Get formatted timestamp"""
        return datetime.now().strftime('%Y%m%d_%H%M%S')

    def _write_text_file(self, filename, content):
        """Write content to text file"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            self._show_success("TXT")
        except Exception as e:
            self._show_error(e)

    def _write_csv_file(self, filename, writer_callback, results_data):
        """Write data to CSV file using callback"""
        try:
            with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
                writer = csv.writer(f, delimiter=';')
                writer_callback(results_data, writer)
            self._show_success("CSV")
        except Exception as e:
            self._show_error(e)

    def _write_json_file(self, filename, data):
        """Write data to JSON file"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            self._show_success("JSON")
        except Exception as e:
            self._show_error(e)

    def _show_success(self, file_type):
        """Show success message"""
        QMessageBox.information(
            self.parent,
            "Sukces",
            f"Wyniki zostały wyeksportowane do pliku {file_type}."
        )

    def _show_error(self, error):
        """Show error message"""
        QMessageBox.critical(
            self.parent,
            "Błąd",
            f"Nie udało się zapisać pliku: {str(error)}"
        )
