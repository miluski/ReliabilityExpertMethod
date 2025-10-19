from PyQt5.QtWidgets import QPushButton, QHBoxLayout


class ExportButtonPanel:
    """Manages export and print buttons"""

    def __init__(self):
        self.export_txt_btn = None
        self.export_csv_btn = None
        self.export_json_btn = None
        self.print_btn = None

    def create_buttons(self, txt_callback, csv_callback, json_callback, print_callback):
        """Create all export buttons"""
        self.export_txt_btn = self._create_button("📄 Eksportuj do TXT", txt_callback)
        self.export_csv_btn = self._create_button("📊 Eksportuj do CSV", csv_callback)
        self.export_json_btn = self._create_button("🗂️ Eksportuj do JSON", json_callback)
        self.print_btn = self._create_button("🖨️ Drukuj", print_callback)

    def _create_button(self, text, callback):
        """Create a single button"""
        button = QPushButton(text)
        button.setEnabled(False)
        button.clicked.connect(callback)
        return button

    def create_layout(self):
        """Create horizontal layout with buttons"""
        layout = QHBoxLayout()
        layout.addWidget(self.export_txt_btn)
        layout.addWidget(self.export_csv_btn)
        layout.addWidget(self.export_json_btn)
        layout.addWidget(self.print_btn)
        layout.addStretch()
        return layout

    def enable_all(self):
        """Enable all buttons"""
        self.export_txt_btn.setEnabled(True)
        self.export_csv_btn.setEnabled(True)
        self.export_json_btn.setEnabled(True)
        self.print_btn.setEnabled(True)

    def disable_all(self):
        """Disable all buttons"""
        self.export_txt_btn.setEnabled(False)
        self.export_csv_btn.setEnabled(False)
        self.export_json_btn.setEnabled(False)
        self.print_btn.setEnabled(False)
