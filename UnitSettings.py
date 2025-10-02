# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UnitSettings.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_UnitSettings(object):
    def setupUi(self, UnitSettings):
        if not UnitSettings.objectName():
            UnitSettings.setObjectName(u"UnitSettings")
        UnitSettings.resize(174, 86)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(UnitSettings.sizePolicy().hasHeightForWidth())
        UnitSettings.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(UnitSettings)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(UnitSettings)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.label)

        self.comboBox = QComboBox(UnitSettings)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy1.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.comboBox)

        self.buttonBox = QDialogButtonBox(UnitSettings)
        self.buttonBox.setObjectName(u"buttonBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy2)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(UnitSettings)
        self.buttonBox.accepted.connect(UnitSettings.accept)
        self.buttonBox.rejected.connect(UnitSettings.reject)

        QMetaObject.connectSlotsByName(UnitSettings)
    # setupUi

    def retranslateUi(self, UnitSettings):
        UnitSettings.setWindowTitle(QCoreApplication.translate("UnitSettings", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("UnitSettings", u"Set Decimal Precision", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("UnitSettings", u"0 (0 Place)", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("UnitSettings", u"0.0 (1 Place)", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("UnitSettings", u"0.00 (2 Place)", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("UnitSettings", u"0.000 (3 Place)", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("UnitSettings", u"0.0000 (4 Place)", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("UnitSettings", u"0.00000 (5 Place)", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("UnitSettings", u"0.000000 (6 Place)", None))

    # retranslateUi

