# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Uniform Load.ui'
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
        MainWindow.resize(272, 283)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.uniformloadsGBox = QGroupBox(self.centralwidget)
        self.uniformloadsGBox.setObjectName(u"uniformloadsGBox")
        self.uniformloadsGBox.setGeometry(QRect(10, 0, 251, 221))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uniformloadsGBox.sizePolicy().hasHeightForWidth())
        self.uniformloadsGBox.setSizePolicy(sizePolicy)
        self.uniformloadsGBox.setMinimumSize(QSize(251, 221))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(11)
        self.uniformloadsGBox.setFont(font)
        self.uniformloadsGBox.setCheckable(True)
        self.verticalLayout_9 = QVBoxLayout(self.uniformloadsGBox)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_11 = QLabel(self.uniformloadsGBox)
        self.label_11.setObjectName(u"label_11")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy1)
        self.label_11.setMinimumSize(QSize(0, 0))
        self.label_11.setMaximumSize(QSize(16777215, 16777215))
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_11, 0, 0, 1, 1)

        self.label_12 = QLabel(self.uniformloadsGBox)
        self.label_12.setObjectName(u"label_12")
        sizePolicy1.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy1)
        self.label_12.setMinimumSize(QSize(0, 43))
        self.label_12.setMaximumSize(QSize(16777215, 43))
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_12, 0, 1, 1, 1)

        self.uniformloadstart = QDoubleSpinBox(self.uniformloadsGBox)
        self.uniformloadstart.setObjectName(u"uniformloadstart")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.uniformloadstart.sizePolicy().hasHeightForWidth())
        self.uniformloadstart.setSizePolicy(sizePolicy2)
        self.uniformloadstart.setMinimumSize(QSize(110, 27))
        self.uniformloadstart.setMaximumSize(QSize(100, 27))
        self.uniformloadstart.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.uniformloadstart.setDecimals(3)
        self.uniformloadstart.setMaximum(100000000.000000000000000)

        self.gridLayout.addWidget(self.uniformloadstart, 1, 0, 1, 1)

        self.uniformloadend = QDoubleSpinBox(self.uniformloadsGBox)
        self.uniformloadend.setObjectName(u"uniformloadend")
        sizePolicy2.setHeightForWidth(self.uniformloadend.sizePolicy().hasHeightForWidth())
        self.uniformloadend.setSizePolicy(sizePolicy2)
        self.uniformloadend.setMinimumSize(QSize(110, 27))
        self.uniformloadend.setMaximumSize(QSize(100, 27))
        self.uniformloadend.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.uniformloadend.setDecimals(3)
        self.uniformloadend.setMaximum(100000000.000000000000000)

        self.gridLayout.addWidget(self.uniformloadend, 1, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(110, 28, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.uniformloadunits = QComboBox(self.uniformloadsGBox)
        self.uniformloadunits.setObjectName(u"uniformloadunits")
        sizePolicy2.setHeightForWidth(self.uniformloadunits.sizePolicy().hasHeightForWidth())
        self.uniformloadunits.setSizePolicy(sizePolicy2)
        self.uniformloadunits.setMinimumSize(QSize(110, 27))
        self.uniformloadunits.setMaximumSize(QSize(100, 27))

        self.gridLayout.addWidget(self.uniformloadunits, 2, 1, 1, 1)


        self.verticalLayout_9.addLayout(self.gridLayout)

        self.line = QFrame(self.uniformloadsGBox)
        self.line.setObjectName(u"line")
        self.line.setLineWidth(2)
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_9.addWidget(self.line)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_13 = QLabel(self.uniformloadsGBox)
        self.label_13.setObjectName(u"label_13")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy3)
        self.label_13.setMinimumSize(QSize(100, 0))
        self.label_13.setMaximumSize(QSize(112, 16777215))
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_13)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.uniformloadmagnitude = QDoubleSpinBox(self.uniformloadsGBox)
        self.uniformloadmagnitude.setObjectName(u"uniformloadmagnitude")
        sizePolicy2.setHeightForWidth(self.uniformloadmagnitude.sizePolicy().hasHeightForWidth())
        self.uniformloadmagnitude.setSizePolicy(sizePolicy2)
        self.uniformloadmagnitude.setMinimumSize(QSize(110, 27))
        self.uniformloadmagnitude.setMaximumSize(QSize(100, 27))
        self.uniformloadmagnitude.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.uniformloadmagnitude.setDecimals(3)
        self.uniformloadmagnitude.setMaximum(100000000.000000000000000)

        self.verticalLayout_14.addWidget(self.uniformloadmagnitude)

        self.uniformloadmagnitudunits = QComboBox(self.uniformloadsGBox)
        self.uniformloadmagnitudunits.setObjectName(u"uniformloadmagnitudunits")
        sizePolicy2.setHeightForWidth(self.uniformloadmagnitudunits.sizePolicy().hasHeightForWidth())
        self.uniformloadmagnitudunits.setSizePolicy(sizePolicy2)
        self.uniformloadmagnitudunits.setMinimumSize(QSize(110, 27))
        self.uniformloadmagnitudunits.setMaximumSize(QSize(100, 27))

        self.verticalLayout_14.addWidget(self.uniformloadmagnitudunits)


        self.horizontalLayout_9.addLayout(self.verticalLayout_14)


        self.verticalLayout_9.addLayout(self.horizontalLayout_9)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 272, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.uniformloadsGBox.setTitle(QCoreApplication.translate("MainWindow", u"Uniform Loads", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Start of Load\n"
"(x-coordinate)", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"End of Load\n"
"(x-coordinate)", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Load\n"
"Magnitude", None))
    # retranslateUi

