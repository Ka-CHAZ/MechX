import sys
import math
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton,
    QListWidget, QListWidgetItem, QLabel, QHBoxLayout
)
from PySide6.QtCore import Qt


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TI-84 Style Scientific Calculator")
        self.setFixedSize(500, 650)
        self.setStyleSheet("font-size: 18px;")
        self.mode = "RAD"  # RAD or DEG
        self.memory = 0
        self.current_expression = ""

        self.create_ui()

    def create_ui(self):
        main_layout = QVBoxLayout(self)

        # Mode display and toggle
        mode_layout = QHBoxLayout()
        self.mode_label = QLabel("Mode: RAD")
        toggle_btn = QPushButton("Toggle DEG/RAD")
        toggle_btn.clicked.connect(self.toggle_mode)
        mode_layout.addWidget(self.mode_label)
        mode_layout.addWidget(toggle_btn)
        main_layout.addLayout(mode_layout)

        # History display (scrollable)
        self.history = QListWidget()
        self.history.setSelectionMode(QListWidget.SingleSelection)
        self.history.itemClicked.connect(self.on_history_click)
        main_layout.addWidget(self.history, stretch=2)

        # Button grid
        grid = QGridLayout()
        buttons = [
            ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3), ("C", 0, 4),
            ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3), ("^", 1, 4),
            ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3), ("sqrt", 2, 4),
            ("0", 3, 0), (".", 3, 1), ("=", 3, 2), ("+", 3, 3), ("log", 3, 4),
            ("sin", 4, 0), ("cos", 4, 1), ("tan", 4, 2), ("(", 4, 3), (")", 4, 4),
        ]

        for text, row, col in buttons:
            btn = QPushButton(text)
            btn.clicked.connect(lambda _, t=text: self.on_button_click(t))
            grid.addWidget(btn, row, col)

        main_layout.addLayout(grid)

        # Live expression display (above history)
        self.live_display = QLabel("")
        self.live_display.setAlignment(Qt.AlignRight)
        self.live_display.setStyleSheet("font: 20px 'Courier New'; padding: 10px;")
        main_layout.addWidget(self.live_display)
                
    def toggle_mode(self):
        self.mode = "DEG" if self.mode == "RAD" else "RAD"
        self.mode_label.setText(f"Mode: {self.mode}")

    def on_button_click(self, text):
        if text == "C":
            self.current_expression = ""
            self.live_display.setText("")
        elif text == "=":
            try:
                expr = self.current_expression
                result = self.evaluate_expression(expr)
                self.history.addItem(f"> {expr}")
                self.history.addItem(f"= {result}")
                self.current_expression = ""
                self.live_display.setText("")
            except Exception:
                self.history.addItem(f"> {self.current_expression}")
                self.history.addItem("= Error")
                self.current_expression = ""
                self.live_display.setText("")
        else:
            self.current_expression += text
            self.live_display.setText(self.current_expression)

    def on_history_click(self, item: QListWidgetItem):
        text = item.text()
        if text.startswith("=") or text.startswith(">"):
            value = text[2:].strip()
            self.current_expression += value
            self.live_display.setText(self.current_expression)

    def evaluate_expression(self, expr):
        expr = expr.replace("^", "**")
        expr = expr.replace("sqrt", "math.sqrt")
        expr = expr.replace("log", "math.log10")
        expr = expr.replace("sin", f"math.sin")
        expr = expr.replace("cos", f"math.cos")
        expr = expr.replace("tan", f"math.tan")

        if self.mode == "DEG":
            expr = self.wrap_trig_with_degrees(expr)

        return eval(expr, {"math": math})

    def wrap_trig_with_degrees(self, expr):
        # Wrap arguments of trig functions with math.radians()
        import re
        def wrap(match):
            func = match.group(1)
            arg = match.group(2)
            return f"math.{func}(math.radians({arg}))"
        return re.sub(r"math\.(sin|cos|tan)\(([^)]+)\)", wrap, expr)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Calculator()
    win.show()
    sys.exit(app.exec())