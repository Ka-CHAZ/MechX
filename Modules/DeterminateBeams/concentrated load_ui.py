# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'concentrated load.ui'
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
        MainWindow.resize(276, 248)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.ConcentratedloadsGBox = QGroupBox(self.centralwidget)
        self.ConcentratedloadsGBox.setObjectName(u"ConcentratedloadsGBox")
        self.ConcentratedloadsGBox.setGeometry(QRect(10, 10, 251, 171))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ConcentratedloadsGBox.sizePolicy().hasHeightForWidth())
        self.ConcentratedloadsGBox.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(11)
        self.ConcentratedloadsGBox.setFont(font)
        self.ConcentratedloadsGBox.setCheckable(True)
        self.verticalLayout_8 = QVBoxLayout(self.ConcentratedloadsGBox)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.ConcentratedloadsGBox)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.concenloadlocation = QDoubleSpinBox(self.ConcentratedloadsGBox)
        self.concenloadlocation.setObjectName(u"concenloadlocation")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.concenloadlocation.sizePolicy().hasHeightForWidth())
        self.concenloadlocation.setSizePolicy(sizePolicy2)
        self.concenloadlocation.setMinimumSize(QSize(110, 27))
        self.concenloadlocation.setMaximumSize(QSize(100, 27))
        self.concenloadlocation.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.concenloadmagnitude.setDecimals(3)
        self.concenloadlocation.setMaximum(100000000.000000000000000)

        self.verticalLayout_2.addWidget(self.concenloadlocation)

        self.concenloadlocationunits = QComboBox(self.ConcentratedloadsGBox)
        self.concenloadlocationunits.setObjectName(u"concenloadlocationunits")
        sizePolicy2.setHeightForWidth(self.concenloadlocationunits.sizePolicy().hasHeightForWidth())
        self.concenloadlocationunits.setSizePolicy(sizePolicy2)
        self.concenloadlocationunits.setMinimumSize(QSize(110, 27))
        self.concenloadlocationunits.setMaximumSize(QSize(100, 27))
        self.concenloadlocationunits.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.verticalLayout_2.addWidget(self.concenloadlocationunits)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.verticalLayout_8.addLayout(self.horizontalLayout_2)

        self.line_4 = QFrame(self.ConcentratedloadsGBox)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setLineWidth(2)
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_8.addWidget(self.line_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.ConcentratedloadsGBox)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setMinimumSize(QSize(97, 0))
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.concenloadmagnitude = QDoubleSpinBox(self.ConcentratedloadsGBox)
        self.concenloadmagnitude.setObjectName(u"concenloadmagnitude")
        sizePolicy2.setHeightForWidth(self.concenloadmagnitude.sizePolicy().hasHeightForWidth())
        self.concenloadmagnitude.setSizePolicy(sizePolicy2)
        self.concenloadmagnitude.setMinimumSize(QSize(110, 27))
        self.concenloadmagnitude.setMaximumSize(QSize(100, 27))
        self.concenloadmagnitude.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.concenloadmagnitude.setDecimals(3)
        self.concenloadmagnitude.setMaximum(100000000.000000000000000)

        self.verticalLayout_3.addWidget(self.concenloadmagnitude)

        self.concenloadmagnitudeunits = QComboBox(self.ConcentratedloadsGBox)
        self.concenloadmagnitudeunits.setObjectName(u"concenloadmagnitudeunits")
        sizePolicy2.setHeightForWidth(self.concenloadmagnitudeunits.sizePolicy().hasHeightForWidth())
        self.concenloadmagnitudeunits.setSizePolicy(sizePolicy2)
        self.concenloadmagnitudeunits.setMinimumSize(QSize(110, 27))
        self.concenloadmagnitudeunits.setMaximumSize(QSize(100, 27))

        self.verticalLayout_3.addWidget(self.concenloadmagnitudeunits)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)


        self.verticalLayout_8.addLayout(self.horizontalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 276, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.ConcentratedloadsGBox.setTitle(QCoreApplication.translate("MainWindow", u"Concentrated Loads", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Load Location\n"
"(x-coordinate)", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Load\n"
"Magnitude", None))
    # retranslateUi

