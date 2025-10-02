# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Concentrated Moment.ui'
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
    QFrame, QGroupBox, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(274, 250)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.ConcentratedmomentsGBox = QGroupBox(self.centralwidget)
        self.ConcentratedmomentsGBox.setObjectName(u"ConcentratedmomentsGBox")
        self.ConcentratedmomentsGBox.setGeometry(QRect(10, 10, 251, 171))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ConcentratedmomentsGBox.sizePolicy().hasHeightForWidth())
        self.ConcentratedmomentsGBox.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(11)
        self.ConcentratedmomentsGBox.setFont(font)
        self.ConcentratedmomentsGBox.setCheckable(True)
        self.verticalLayout_7 = QVBoxLayout(self.ConcentratedmomentsGBox)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_19 = QLabel(self.ConcentratedmomentsGBox)
        self.label_19.setObjectName(u"label_19")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy1)
        self.label_19.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_19)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.momentlocation = QDoubleSpinBox(self.ConcentratedmomentsGBox)
        self.momentlocation.setObjectName(u"momentlocation")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.momentlocation.sizePolicy().hasHeightForWidth())
        self.momentlocation.setSizePolicy(sizePolicy2)
        self.momentlocation.setMinimumSize(QSize(110, 27))
        self.momentlocation.setMaximumSize(QSize(100, 27))
        self.momentlocation.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.momentlocation.setDecimals(3)
        self.momentlocation.setMaximum(100000000.000000000000000)

        self.verticalLayout_21.addWidget(self.momentlocation)

        self.momentlocationunits = QComboBox(self.ConcentratedmomentsGBox)
        self.momentlocationunits.setObjectName(u"momentlocationunits")
        sizePolicy2.setHeightForWidth(self.momentlocationunits.sizePolicy().hasHeightForWidth())
        self.momentlocationunits.setSizePolicy(sizePolicy2)
        self.momentlocationunits.setMinimumSize(QSize(110, 27))
        self.momentlocationunits.setMaximumSize(QSize(100, 27))

        self.verticalLayout_21.addWidget(self.momentlocationunits)


        self.horizontalLayout_12.addLayout(self.verticalLayout_21)


        self.verticalLayout_7.addLayout(self.horizontalLayout_12)

        self.line_2 = QFrame(self.ConcentratedmomentsGBox)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_7.addWidget(self.line_2)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_20 = QLabel(self.ConcentratedmomentsGBox)
        self.label_20.setObjectName(u"label_20")
        sizePolicy1.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy1)
        self.label_20.setMinimumSize(QSize(0, 0))
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_20)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.momentmagnitude = QDoubleSpinBox(self.ConcentratedmomentsGBox)
        self.momentmagnitude.setObjectName(u"momentmagnitude")
        sizePolicy2.setHeightForWidth(self.momentmagnitude.sizePolicy().hasHeightForWidth())
        self.momentmagnitude.setSizePolicy(sizePolicy2)
        self.momentmagnitude.setMinimumSize(QSize(110, 27))
        self.momentmagnitude.setMaximumSize(QSize(100, 27))
        self.momentmagnitude.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.momentmagnitude.setDecimals(3)
        self.momentmagnitude.setMaximum(100000000.000000000000000)

        self.verticalLayout_22.addWidget(self.momentmagnitude)

        self.momentmagnitudeunits = QComboBox(self.ConcentratedmomentsGBox)
        self.momentmagnitudeunits.setObjectName(u"momentmagnitudeunits")
        sizePolicy2.setHeightForWidth(self.momentmagnitudeunits.sizePolicy().hasHeightForWidth())
        self.momentmagnitudeunits.setSizePolicy(sizePolicy2)
        self.momentmagnitudeunits.setMinimumSize(QSize(110, 27))
        self.momentmagnitudeunits.setMaximumSize(QSize(100, 27))

        self.verticalLayout_22.addWidget(self.momentmagnitudeunits)


        self.horizontalLayout_13.addLayout(self.verticalLayout_22)


        self.verticalLayout_7.addLayout(self.horizontalLayout_13)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 274, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.ConcentratedmomentsGBox.setTitle(QCoreApplication.translate("MainWindow", u"Concentrated Moments", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Moment\n"
"Location\n"
"(x-coordinate)", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Moment\n"
"Magnitude", None))
    # retranslateUi

