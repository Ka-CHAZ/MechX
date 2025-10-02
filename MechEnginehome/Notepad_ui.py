# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Notepad.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFontComboBox, QHBoxLayout,
    QMainWindow, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpinBox, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(545, 371)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.fontComboBox = QFontComboBox(self.centralwidget)
        self.fontComboBox.setObjectName(u"fontComboBox")

        self.horizontalLayout.addWidget(self.fontComboBox)

        self.textsize = QSpinBox(self.centralwidget)
        self.textsize.setObjectName(u"textsize")

        self.horizontalLayout.addWidget(self.textsize)

        self.textcolor = QComboBox(self.centralwidget)
        self.textcolor.setObjectName(u"textcolor")

        self.horizontalLayout.addWidget(self.textcolor)

        self.texthighlight = QComboBox(self.centralwidget)
        self.texthighlight.setObjectName(u"texthighlight")

        self.horizontalLayout.addWidget(self.texthighlight)

        self.bulletpoints = QComboBox(self.centralwidget)
        self.bulletpoints.setObjectName(u"bulletpoints")

        self.horizontalLayout.addWidget(self.bulletpoints)

        self.insertsymbols = QPushButton(self.centralwidget)
        self.insertsymbols.setObjectName(u"insertsymbols")

        self.horizontalLayout.addWidget(self.insertsymbols)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.plainTextEdit)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 545, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.insertsymbols.setText(QCoreApplication.translate("MainWindow", u"symbols", None))
    # retranslateUi

