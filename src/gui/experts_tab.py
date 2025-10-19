from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QScrollArea, QPushButton,
                             QGroupBox, QFormLayout, QDoubleSpinBox, QLabel,
                             QTableWidget, QTableWidgetItem, QHBoxLayout)
from PyQt5.QtCore import pyqtSignal

from utils.data_generator import DataGenerator


class ExpertsTab(QWidget):
    calculation_requested = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.kmj_inputs = []
        self.expert_tables = []
        self.data_generator = DataGenerator()
        self.current_config = None
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll_content = QWidget()
        self.experts_layout = QVBoxLayout()
        scroll_content.setLayout(self.experts_layout)
        scroll.setWidget(scroll_content)

        layout.addWidget(scroll)

        buttons_layout = QHBoxLayout()

        random_btn = QPushButton("🎲 Generuj losowe dane")
        random_btn.clicked.connect(self.on_generate_random_data)
        random_btn.setStyleSheet("background-color: #FF9800; color: white; padding: 10px; font-size: 14px;")
        buttons_layout.addWidget(random_btn)

        calc_btn = QPushButton("Oblicz wskaźniki niezawodności")
        calc_btn.clicked.connect(self.on_calculate_clicked)
        calc_btn.setStyleSheet("background-color: #2196F3; color: white; padding: 10px; font-size: 14px;")
        buttons_layout.addWidget(calc_btn)

        layout.addLayout(buttons_layout)

    def on_calculate_clicked(self):
        self.calculation_requested.emit()

    def on_generate_random_data(self):
        """Generate random data for all fields"""
        if not self.kmj_inputs and not self.expert_tables:
            return

        self._fill_random_kmj()
        self._fill_random_expert_data()

    def _fill_random_kmj(self):
        """Fill Kmj fields with random data"""
        kmj_values = self.data_generator.generate_kmj_values(len(self.kmj_inputs))
        for spin, value in zip(self.kmj_inputs, kmj_values):
            spin.setValue(value)

    def _fill_random_expert_data(self):
        """Fill expert tables with random data"""
        for table in self.expert_tables:
            num_groups = table.rowCount()
            groups_data = self.data_generator._generate_expert_groups(num_groups)

            for row, (ng_n, kg) in enumerate(groups_data):
                table.item(row, 0).setText(str(ng_n))
                table.item(row, 1).setText(str(kg))

    def generate_forms(self, j_mech, j_elec, n_groups):
        while self.experts_layout.count():
            child = self.experts_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        self.kmj_inputs = []
        self.expert_tables = []

        self._create_mechanics_form(j_mech)
        self._create_electronics_form(j_elec, n_groups)

    def _create_mechanics_form(self, j_mech):
        mech_group = QGroupBox(f"Mechanicy - Współczynniki Kmj (od 1 do 2)")
        mech_layout = QFormLayout()
        mech_group.setLayout(mech_layout)

        for i in range(j_mech):
            spin = QDoubleSpinBox()
            spin.setRange(1.0, 2.0)
            spin.setValue(1.0)
            spin.setSingleStep(0.1)
            spin.setDecimals(2)
            mech_layout.addRow(f"Km{i+1}:", spin)
            self.kmj_inputs.append(spin)

        self.experts_layout.addWidget(mech_group)

    def _create_electronics_form(self, j_elec, n_groups):
        elec_group = QGroupBox(f"Elektronicy - Dane dla grup elementów")
        elec_layout = QVBoxLayout()
        elec_group.setLayout(elec_layout)

        for i in range(j_elec):
            expert_label = QLabel(f"Ekspert elektroniczny {i+1}:")
            expert_label.setStyleSheet("font-weight: bold;")
            elec_layout.addWidget(expert_label)

            table = QTableWidget(n_groups, 2)
            table.setHorizontalHeaderLabels(["Ng/N (udział grupy)", "Kg (współczynnik 1-10)"])

            table.setColumnWidth(0, 200)
            table.setColumnWidth(1, 200)

            for row in range(n_groups):
                table.setItem(row, 0, QTableWidgetItem("0.0"))
                table.setItem(row, 1, QTableWidgetItem("1"))

            elec_layout.addWidget(table)
            self.expert_tables.append(table)

        self.experts_layout.addWidget(elec_group)

    def get_expert_data(self):
        kmj_values = [spin.value() for spin in self.kmj_inputs]

        expert_data = []
        for table in self.expert_tables:
            n_groups = table.rowCount()
            groups_data = []
            for row in range(n_groups):
                ng_n = float(table.item(row, 0).text())
                kg = float(table.item(row, 1).text())
                groups_data.append((ng_n, kg))
            expert_data.append(groups_data)

        return kmj_values, expert_data
