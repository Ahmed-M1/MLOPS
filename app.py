import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout




if __name__ == "__main__":
    app = QApplication(sys.argv)
    bmi_calculator = BMICalculator()
    bmi_calculator.show()
    sys.exit(app.exec_())