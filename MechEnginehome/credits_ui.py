# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'credits.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_credits(object):
    def setupUi(self, credits):
        if not credits.objectName():
            credits.setObjectName(u"credits")
        credits.resize(370, 550)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(credits.sizePolicy().hasHeightForWidth())
        credits.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(credits)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 0, 351, 491))
        font = QFont()
        font.setFamilies([u"Consolas"])
        self.widget.setFont(font)
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Consolas"])
        font1.setPointSize(20)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setFamilies([u"Consolas"])
        font2.setPointSize(10)
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.verticalSpacer = QSpacerItem(20, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        font3 = QFont()
        font3.setFamilies([u"Consolas"])
        font3.setPointSize(12)
        self.label_4.setFont(font3)
        self.label_4.setTextFormat(Qt.TextFormat.PlainText)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_4)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font3)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        font4 = QFont()
        font4.setFamilies([u"Consolas"])
        font4.setPointSize(14)
        self.label_7.setFont(font4)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_7)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font3)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_6)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font4)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_5)

        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font3)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_8)

        self.verticalSpacer_5 = QSpacerItem(20, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font3)
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_9)

        credits.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(credits)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 370, 33))
        credits.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(credits)
        self.statusbar.setObjectName(u"statusbar")
        credits.setStatusBar(self.statusbar)

        self.retranslateUi(credits)

        QMetaObject.connectSlotsByName(credits)
    # setupUi

    def retranslateUi(self, credits):
        credits.setWindowTitle(QCoreApplication.translate("credits", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("credits", u"Mechanics Engine", None))
        self.label_3.setText(QCoreApplication.translate("credits", u"Version Alpha 0.0.12", None))
        self.label_4.setText(QCoreApplication.translate("credits", u"A Mathematics and engineering\n"
"software for calculating,\n"
"analyzing, graphing, and displaying,\n"
"static, kinematic, dynamic,\n"
"and material properties of solids,\n"
"structures, and machine elements ", None))
        self.label_2.setText(QCoreApplication.translate("credits", u"Author: James Karczewski", None))
        self.label_7.setText(QCoreApplication.translate("credits", u"Credits", None))
        self.label_6.setText(QCoreApplication.translate("credits", u"Kelly Ryba\n"
"Tom Filipiak\n"
"Ryan Weister", None))
        self.label_5.setText(QCoreApplication.translate("credits", u"Dr. Timothy Philpot", None))
        self.label_8.setText(QCoreApplication.translate("credits", u"For his dedication to MDSolids\n"
"the inspiration for Mechanics Engine", None))
        self.label_9.setText(QCoreApplication.translate("credits", u"For additional information,\n"
"look on the Mechanics Engine website\n"
"or cantact ____________", None))
    # retranslateUi

