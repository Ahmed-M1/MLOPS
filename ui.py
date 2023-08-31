from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget


class BMIUI(QWidget):
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
        self.interpretation_label = QLabel()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.weight_label)
        self.layout.addWidget(self.weight_input)
        self.layout.addWidget(self.height_label)
        self.layout.addWidget(self.height_input)
        self.layout.addWidget(self.calculate_button)
        self.layout.addWidget(self.result_label)
        self.layout.addWidget(self.interpretation_label)

        self.setLayout(self.layout)


class BMIUIExtended(BMIUI):
    def __init__(self):
        super().__init__()
        self.category_label = QLabel()

        self.layout.addWidget(self.category_label)


def get_weight_height(widget):
    weight = float(widget.weight_input.text())
    height = float(widget.height_input.text())
    return weight, height


def display_result(widget, bmi, interpretation, category):
    widget.result_label.setText(f"Your BMI is: {round(bmi, 2)}")
    widget.interpretation_label.setText("Interpretation: " + interpretation)
    widget.category_label.setText("Category: " + category)