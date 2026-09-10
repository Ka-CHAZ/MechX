# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FixedFloating Fasteners.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_GDTFasteners(object):
    def setupUi(self, GDTFasteners):
        if not GDTFasteners.objectName():
            GDTFasteners.setObjectName(u"GDTFasteners")
        GDTFasteners.resize(176, 410)
        self.centralwidget = QWidget(GDTFasteners)
        self.centralwidget.setObjectName(u"centralwidget")
        self.FixedFloating = QComboBox(self.centralwidget)
        self.FixedFloating.setObjectName(u"FixedFloating")
        self.FixedFloating.setGeometry(QRect(10, 160, 131, 31))
        self.Tolerance = QDoubleSpinBox(self.centralwidget)
        self.Tolerance.setObjectName(u"Tolerance")
        self.Tolerance.setGeometry(QRect(10, 230, 131, 31))
        self.Hole = QDoubleSpinBox(self.centralwidget)
        self.Hole.setObjectName(u"Hole")
        self.Hole.setGeometry(QRect(10, 270, 131, 31))
        self.Fastener = QDoubleSpinBox(self.centralwidget)
        self.Fastener.setObjectName(u"Fastener")
        self.Fastener.setGeometry(QRect(10, 310, 131, 31))
        self.Calculatebutton = QPushButton(self.centralwidget)
        self.Calculatebutton.setObjectName(u"Calculatebutton")
        self.Calculatebutton.setGeometry(QRect(10, 200, 131, 24))
        GDTFasteners.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(GDTFasteners)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 176, 33))
        GDTFasteners.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(GDTFasteners)
        self.statusbar.setObjectName(u"statusbar")
        GDTFasteners.setStatusBar(self.statusbar)

        self.retranslateUi(GDTFasteners)

        QMetaObject.connectSlotsByName(GDTFasteners)
    # setupUi

    def retranslateUi(self, GDTFasteners):
        GDTFasteners.setWindowTitle(QCoreApplication.translate("GDTFasteners", u"MainWindow", None))
        self.Calculatebutton.setText(QCoreApplication.translate("GDTFasteners", u"Enter", None))
    # retranslateUi

