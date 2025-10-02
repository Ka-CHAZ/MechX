from PySide6.QtWidgets import (
    QApplication, QMainWindow, QFileDialog, QLabel,
    QVBoxLayout, QWidget, QPushButton, QScrollArea
)
from PySide6.QtCore import Qt
import sys
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Setup UI elements manually or load from UI file
        self.setWindowTitle("File Browser with Scroll Area")

        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout
        layout = QVBoxLayout(central_widget)

        # Browse Button
        self.browse_button = QPushButton("Browse Files")
        layout.addWidget(self.browse_button)

        # Scroll Area setup
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        layout.addWidget(self.scroll_area)

        # Scroll Area content
        self.scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_content)
        self.scroll_area.setWidget(self.scroll_content)

        # Connect browse button
        self.browse_button.clicked.connect(self.open_file_dialog)

    def open_file_dialog(self):
        files, _ = QFileDialog.getOpenFileNames(self, "Select Files")
        if files:
            # Clear previous contents
            for i in reversed(range(self.scroll_layout.count())):
                widget = self.scroll_layout.itemAt(i).widget()
                if widget:
                    widget.setParent(None)

            # Add selected file names as labels
            for file_path in files:
                file_name = os.path.basename(file_path)
                label = QLabel(file_name)
                label.setAlignment(Qt.AlignLeft)
                self.scroll_layout.addWidget(label)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(400, 300)
    window.show()
    sys.exit(app.exec())
    