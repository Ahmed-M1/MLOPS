import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout


class BMICalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BMI Calculator")
        self.setGeometry(300, 300, 300, 200)

        self.weight_label = QLabel("Weight (kg):")
        self.weight_input = QLineEdit()
        self.height_label = QLabel("Height (m):")
        self.height_input = QLineEdit()
        self.calculate_button = QPushButton("Calculate")
        self.result_label = QLabel()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.weight_label)
        self.layout.addWidget(self.weight_input)
        self.layout.addWidget(self.height_label)
        self.layout.addWidget(self.height_input)
        self.layout.addWidget(self.calculate_button)
        self.layout.addWidget(self.result_label)

        self.calculate_button.clicked.connect(self.calculate_bmi)

        self.setLayout(self.layout)


  