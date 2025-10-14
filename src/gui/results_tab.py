from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

class ResultsTab(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.results_label = QLabel("Wyniki obliczeń pojawią się tutaj po naciśnięciu 'Oblicz'")
        self.results_label.setWordWrap(True)
        self.results_label.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        layout.addWidget(self.results_label)

        layout.addStretch()

    def display_results(self, results_text):
        self.results_label.setText(results_text)

    def clear_results(self):
        self.results_label.setText("Wyniki obliczeń pojawią się tutaj po naciśnięciu 'Oblicz'")
