from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGroupBox, QFormLayout, QSpinBox, QLineEdit, QLabel, QComboBox, QPushButton
from PyQt5.QtCore import pyqtSignal

class ConfigurationTab(QWidget):
    form_generated = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        self._create_mode_group(layout)
        self._create_experts_group(layout)
        self._create_system_group(layout)
        self._create_prognostic_group(layout)
        self._create_generate_button(layout)

        layout.addStretch()

    def _create_mode_group(self, layout):
        mode_group = QGroupBox("Wybierz tryb obliczeń")
        mode_layout = QVBoxLayout()
        mode_group.setLayout(mode_layout)

        self.mode_combo = QComboBox()
        self.mode_combo.addItems([
            "Obliczanie A0 (średni strumień uszkodzeń)",
            "Obliczanie E(T0) (oczekiwany czas pracy)",
            "Obliczanie λdi (intensywność uszkodzeń nowych elementów)"
        ])
        mode_layout.addWidget(QLabel("Tryb:"))
        mode_layout.addWidget(self.mode_combo)

        layout.addWidget(mode_group)

    def _create_experts_group(self, layout):
        experts_group = QGroupBox("Liczba ekspertów")
        experts_layout = QFormLayout()
        experts_group.setLayout(experts_layout)

        self.mech_experts_spin = QSpinBox()
        self.mech_experts_spin.setRange(1, 20)
        self.mech_experts_spin.setValue(3)
        experts_layout.addRow("Mechanicy (J_mech):", self.mech_experts_spin)

        self.elec_experts_spin = QSpinBox()
        self.elec_experts_spin.setRange(1, 20)
        self.elec_experts_spin.setValue(5)
        experts_layout.addRow("Elektronicy (J_elec):", self.elec_experts_spin)

        layout.addWidget(experts_group)

    def _create_system_group(self, layout):
        system_group = QGroupBox("Parametry systemu")
        system_layout = QFormLayout()
        system_group.setLayout(system_layout)

        self.modules_spin = QSpinBox()
        self.modules_spin.setRange(1, 100)
        self.modules_spin.setValue(15)
        system_layout.addRow("Liczba modułów (N):", self.modules_spin)

        self.groups_spin = QSpinBox()
        self.groups_spin.setRange(1, 10)
        self.groups_spin.setValue(4)
        system_layout.addRow("Liczba grup elementów:", self.groups_spin)

        layout.addWidget(system_group)

    def _create_prognostic_group(self, layout):
        prog_group = QGroupBox("Dane prognostyczne (z podobnego urządzenia)")
        prog_layout = QFormLayout()
        prog_group.setLayout(prog_layout)

        self.a_mean_input = QLineEdit()
        self.a_mean_input.setPlaceholderText("np. 1.1e-5")
        prog_layout.addRow("Ā (średni strumień):", self.a_mean_input)

        self.a_upper_input = QLineEdit()
        self.a_upper_input.setPlaceholderText("np. 1.5e-5")
        prog_layout.addRow("Ag (górny kres):", self.a_upper_input)

        self.t_expected_input = QLineEdit()
        self.t_expected_input.setPlaceholderText("np. 900")
        prog_layout.addRow("t (oczekiwany czas [h]):", self.t_expected_input)

        self.lambda_p_input = QLineEdit()
        self.lambda_p_input.setPlaceholderText("np. 352.8e-8")
        prog_layout.addRow("λp (intensywność podobnego):", self.lambda_p_input)

        layout.addWidget(prog_group)

    def _create_generate_button(self, layout):
        generate_btn = QPushButton("Generuj formularze dla ekspertów")
        generate_btn.clicked.connect(self.on_generate_clicked)
        generate_btn.setStyleSheet("background-color: #4CAF50; color: white; padding: 10px; font-size: 14px;")
        layout.addWidget(generate_btn)

    def on_generate_clicked(self):
        self.form_generated.emit()

    def get_configuration(self):
        return {
            'mode': self.mode_combo.currentIndex(),
            'j_mech': self.mech_experts_spin.value(),
            'j_elec': self.elec_experts_spin.value(),
            'n_modules': self.modules_spin.value(),
            'n_groups': self.groups_spin.value(),
            'a_mean': self.a_mean_input.text(),
            'a_upper': self.a_upper_input.text(),
            't_expected': self.t_expected_input.text(),
            'lambda_p': self.lambda_p_input.text()
        }
