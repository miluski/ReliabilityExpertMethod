from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QMessageBox, QTabWidget
from PyQt5.QtCore import Qt
import sys

from gui.config_tab import ConfigurationTab
from gui.experts_tab import ExpertsTab
from gui.results_tab import ResultsTab
from gui.calculator import ReliabilityCalculator

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Prognozowanie Niezawodności - Metoda Ekspertów")
        self.setGeometry(100, 100, 1200, 800)

        self.calculator = ReliabilityCalculator()

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        main_layout = QVBoxLayout()
        self.central_widget.setLayout(main_layout)

        header_label = QLabel("System Prognozowania Niezawodności - Metoda Ekspertów")
        header_label.setStyleSheet("font-size: 18px; font-weight: bold; padding: 10px;")
        header_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(header_label)

        self.tabs = QTabWidget()
        main_layout.addWidget(self.tabs)

        self.config_tab = ConfigurationTab()
        self.tabs.addTab(self.config_tab, "Konfiguracja")

        self.experts_tab = ExpertsTab()
        self.tabs.addTab(self.experts_tab, "Dane Ekspertów")

        self.results_tab = ResultsTab()
        self.tabs.addTab(self.results_tab, "Wyniki")

        self.config_tab.form_generated.connect(self.on_form_generated)
        self.experts_tab.calculation_requested.connect(self.on_calculate_reliability)

        self.statusBar().showMessage("Gotowy do pracy")

    def on_form_generated(self):
        config = self.config_tab.get_configuration()
        self.experts_tab.generate_forms(
            config['j_mech'],
            config['j_elec'],
            config['n_groups']
        )
        self.statusBar().showMessage("Formularze wygenerowane pomyślnie")

    def on_calculate_reliability(self):
        try:
            config = self.config_tab.get_configuration()
            kmj_values, expert_data = self.experts_tab.get_expert_data()

            results = self.calculator.calculate(config, kmj_values, expert_data)

            self.results_tab.display_results(results)
            self.tabs.setCurrentIndex(2)
            self.statusBar().showMessage("Obliczenia zakończone pomyślnie")

            QMessageBox.information(self, "Sukces", "Obliczenia wykonane pomyślnie!")

        except Exception as e:
            QMessageBox.critical(self, "Błąd", f"Wystąpił błąd podczas obliczeń:\n{str(e)}")
            self.statusBar().showMessage("Błąd obliczeń")

    def run(self):
        self.show()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
