# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Linear Distributed Load.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDoubleSpinBox,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(268, 327)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lineardistributedloadsGBox = QGroupBox(self.centralwidget)
        self.lineardistributedloadsGBox.setObjectName(u"lineardistributedloadsGBox")
        self.lineardistributedloadsGBox.setGeometry(QRect(10, 10, 251, 255))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineardistributedloadsGBox.sizePolicy().hasHeightForWidth())
        self.lineardistributedloadsGBox.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(11)
        self.lineardistributedloadsGBox.setFont(font)
        self.lineardistributedloadsGBox.setCheckable(True)
        self.verticalLayout_10 = QVBoxLayout(self.lineardistributedloadsGBox)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_15 = QLabel(self.lineardistributedloadsGBox)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(110, 0))
        self.label_15.setMaximumSize(QSize(10, 16777215))
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_15, 0, 0, 1, 1)

        self.label_16 = QLabel(self.lineardistributedloadsGBox)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(110, 0))
        self.label_16.setMaximumSize(QSize(10, 16777215))
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_16, 0, 1, 1, 1)

        self.lineardistribloadstart = QDoubleSpinBox(self.lineardistributedloadsGBox)
        self.lineardistribloadstart.setObjectName(u"lineardistribloadstart")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineardistribloadstart.sizePolicy().hasHeightForWidth())
        self.lineardistribloadstart.setSizePolicy(sizePolicy1)
        self.lineardistribloadstart.setMinimumSize(QSize(110, 27))
        self.lineardistribloadstart.setMaximumSize(QSize(100, 27))
        self.lineardistribloadstart.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.lineardistribloadstart.setDecimals(3)
        self.lineardistribloadstart.setMaximum(100000000.000000000000000)

        self.gridLayout.addWidget(self.lineardistribloadstart, 1, 0, 1, 1)

        self.lineardistribloadend = QDoubleSpinBox(self.lineardistributedloadsGBox)
        self.lineardistribloadend.setObjectName(u"lineardistribloadend")
        sizePolicy1.setHeightForWidth(self.lineardistribloadend.sizePolicy().hasHeightForWidth())
        self.lineardistribloadend.setSizePolicy(sizePolicy1)
        self.lineardistribloadend.setMinimumSize(QSize(110, 27))
        self.lineardistribloadend.setMaximumSize(QSize(100, 27))
        self.lineardistribloadend.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.lineardistribloadend.setDecimals(3)
        self.lineardistribloadend.setMaximum(100000000.000000000000000)

        self.gridLayout.addWidget(self.lineardistribloadend, 1, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(107, 38, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 0, 1, 1)

        self.lineardistribloadunits = QComboBox(self.lineardistributedloadsGBox)
        self.lineardistribloadunits.setObjectName(u"lineardistribloadunits")
        sizePolicy1.setHeightForWidth(self.lineardistribloadunits.sizePolicy().hasHeightForWidth())
        self.lineardistribloadunits.setSizePolicy(sizePolicy1)
        self.lineardistribloadunits.setMinimumSize(QSize(110, 27))
        self.lineardistribloadunits.setMaximumSize(QSize(100, 27))

        self.gridLayout.addWidget(self.lineardistribloadunits, 2, 1, 1, 1)


        self.verticalLayout_10.addLayout(self.gridLayout)

        self.line_3 = QFrame(self.lineardistributedloadsGBox)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setLineWidth(2)
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_10.addWidget(self.line_3)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_14 = QLabel(self.lineardistributedloadsGBox)
        self.label_14.setObjectName(u"label_14")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy2)
        self.label_14.setMinimumSize(QSize(0, 0))
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_14)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_17 = QLabel(self.lineardistributedloadsGBox)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_20.addWidget(self.label_17)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.lineardistribloadmagnitudestart = QDoubleSpinBox(self.lineardistributedloadsGBox)
        self.lineardistribloadmagnitudestart.setObjectName(u"lineardistribloadmagnitudestart")
        sizePolicy1.setHeightForWidth(self.lineardistribloadmagnitudestart.sizePolicy().hasHeightForWidth())
        self.lineardistribloadmagnitudestart.setSizePolicy(sizePolicy1)
        self.lineardistribloadmagnitudestart.setMinimumSize(QSize(70, 27))
        self.lineardistribloadmagnitudestart.setMaximumSize(QSize(70, 27))
        self.lineardistribloadmagnitudestart.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.lineardistribloadmagnitudestart.setDecimals(3)
        self.lineardistribloadmagnitudestart.setMaximum(100000000.000000000000000)

        self.verticalLayout_15.addWidget(self.lineardistribloadmagnitudestart)

        self.lineardistribloadmagnitudunits = QComboBox(self.lineardistributedloadsGBox)
        self.lineardistribloadmagnitudunits.setObjectName(u"lineardistribloadmagnitudunits")
        sizePolicy1.setHeightForWidth(self.lineardistribloadmagnitudunits.sizePolicy().hasHeightForWidth())
        self.lineardistribloadmagnitudunits.setSizePolicy(sizePolicy1)
        self.lineardistribloadmagnitudunits.setMinimumSize(QSize(70, 27))
        self.lineardistribloadmagnitudunits.setMaximumSize(QSize(70, 27))

        self.verticalLayout_15.addWidget(self.lineardistribloadmagnitudunits)


        self.verticalLayout_20.addLayout(self.verticalLayout_15)


        self.horizontalLayout_10.addLayout(self.verticalLayout_20)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_18 = QLabel(self.lineardistributedloadsGBox)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_18)

        self.lineardistribloadmagnitudeend = QDoubleSpinBox(self.lineardistributedloadsGBox)
        self.lineardistribloadmagnitudeend.setObjectName(u"lineardistribloadmagnitudeend")
        sizePolicy1.setHeightForWidth(self.lineardistribloadmagnitudeend.sizePolicy().hasHeightForWidth())
        self.lineardistribloadmagnitudeend.setSizePolicy(sizePolicy1)
        self.lineardistribloadmagnitudeend.setMinimumSize(QSize(70, 27))
        self.lineardistribloadmagnitudeend.setMaximumSize(QSize(70, 27))
        self.lineardistribloadmagnitudeend.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.lineardistribloadmagnitudeend.setDecimals(3)
        self.lineardistribloadmagnitudeend.setMaximum(100000000.000000000000000)

        self.verticalLayout_19.addWidget(self.lineardistribloadmagnitudeend)

        self.verticalSpacer_3 = QSpacerItem(20, 31, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_19.addItem(self.verticalSpacer_3)


        self.horizontalLayout_10.addLayout(self.verticalLayout_19)


        self.verticalLayout_10.addLayout(self.horizontalLayout_10)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 268, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lineardistributedloadsGBox.setTitle(QCoreApplication.translate("MainWindow", u"Linear Distributed Loads", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Start of Load\n"
"(x-coordinate)", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"End of Load\n"
"(x-coordinate)", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Load\n"
"Magnitude", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"End", None))
    # retranslateUi

