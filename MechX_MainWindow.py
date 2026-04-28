import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMdiArea, QMdiSubWindow, QTreeWidget, QWidget
from PySide6.QtCore import Qt, QSize
from PySide6 import QtGui
from PySide6.QtGui import QIcon, QAction

from MechX_Home.MechX_Mainscreen_ui import Ui_MEMainWindow  # Import main UI
from Unitconverter.UnitConverter_Module import Unit_Converter  # Import Unit Converter classes
from Determinatebeams.DeterminateBeams_Module import Determinate_beams  # Import Determinate Beams classes
from MechX_Home.credits_ui import Ui_credits  # Import credits UI

class MdiApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up main UI
        self.ui = Ui_MEMainWindow()
        self.ui.setupUi(self)
        
        self.setWindowTitle('MechX pre-alpha v 0.2.2')
        
        self.setWindowIcon(QtGui.QIcon('gearNB.ico'))

        # Reference widgets
        self.mdi_area: QMdiArea = self.ui.mdiArea
        self.tree_widget = self.ui.Modulelist

        # Map tree item text to corresponding subwindow class
        self.sub_windows = {
            "Unit Converter": Unit_Converter,
            "Determinate Beams": Determinate_beams,
            # Add more here as needed
        }

        self.ui.Modulelist.expandAll()
        
        # Connect signal for tree widget
        self.tree_widget.itemClicked.connect(self.open_subwindow)
        self.ui.Unitconverter.clicked.connect(self.open_unit_converter)
        self.ui.actionUnit_Converter.triggered.connect(self.open_unit_converter)
        self.ui.actionAbout.triggered.connect(self.credits)

    def open_subwindow(self, item, column):
        item_text = item.text(column)
        if item_text not in self.sub_windows:
            return

        SubWindowClass = self.sub_windows[item_text]
        sub_widget = SubWindowClass()

        sub_window = QMdiSubWindow()
        sub_window.setWidget(sub_widget)

        # Lock the subwindow size based on the widget's UI size
        lock_subwindow_size(sub_window, sub_widget)

        # Remove maximize button and resizing
        sub_window.setAttribute(Qt.WA_DeleteOnClose)
        sub_window.setWindowFlags(
            Qt.Window |
            Qt.CustomizeWindowHint |
            Qt.WindowTitleHint |
            Qt.WindowMinimizeButtonHint |  # show minimize button
            Qt.WindowCloseButtonHint       #show close button
        )

        self.mdi_area.addSubWindow(sub_window)
        sub_window.show()
        
    def open_unit_converter(self):
        self.UnitConverter = Unit_Converter()
        self.UnitConverter.show()
        
    def credits(self):
        self.credits_window = credits()
        self.credits_window.show()

class credits(QMainWindow, Ui_credits):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_credits
        self.setupUi(self)
        
        self.setWindowTitle('Mechanics Engine Credits')

#function to lock subwindow size
def lock_subwindow_size(sub_window: QMdiSubWindow, widget: QWidget, extra_width: int = 15, extra_height: int = 25):
    widget.adjustSize()
    size = widget.size()
    
    # Add horizontal padding
    padded_size = size + QSize(extra_width, extra_height)

    sub_window.setMinimumSize(padded_size)
    sub_window.setMaximumSize(padded_size)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MdiApp()
    main_window.showMaximized()
    main_window.show()
    sys.exit(app.exec())