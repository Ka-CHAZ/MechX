# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MechanicsEngine_Mainscreen.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QDockWidget,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QMainWindow, QMdiArea, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTabWidget, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MEMainWindow(object):
    def setupUi(self, MEMainWindow):
        if not MEMainWindow.objectName():
            MEMainWindow.setObjectName(u"MEMainWindow")
        MEMainWindow.resize(1596, 1130)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MEMainWindow.sizePolicy().hasHeightForWidth())
        MEMainWindow.setSizePolicy(sizePolicy)
        MEMainWindow.setMinimumSize(QSize(270, 610))
        MEMainWindow.setMaximumSize(QSize(16777215, 16777215))
        MEMainWindow.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        MEMainWindow.setTabShape(QTabWidget.TabShape.Rounded)
        MEMainWindow.setDockNestingEnabled(False)
        MEMainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.actionUnit_Converter = QAction(MEMainWindow)
        self.actionUnit_Converter.setObjectName(u"actionUnit_Converter")
        self.actionMoments_of_Inertia = QAction(MEMainWindow)
        self.actionMoments_of_Inertia.setObjectName(u"actionMoments_of_Inertia")
        self.actionVectors = QAction(MEMainWindow)
        self.actionVectors.setObjectName(u"actionVectors")
        self.actionFriction_and_Force = QAction(MEMainWindow)
        self.actionFriction_and_Force.setObjectName(u"actionFriction_and_Force")
        self.actionFasteners = QAction(MEMainWindow)
        self.actionFasteners.setObjectName(u"actionFasteners")
        self.actionMaterial_Properties = QAction(MEMainWindow)
        self.actionMaterial_Properties.setObjectName(u"actionMaterial_Properties")
        self.actionCM_and_CG = QAction(MEMainWindow)
        self.actionCM_and_CG.setObjectName(u"actionCM_and_CG")
        self.actionTrusses = QAction(MEMainWindow)
        self.actionTrusses.setObjectName(u"actionTrusses")
        self.actionBeamsMoments_of_Inertia = QAction(MEMainWindow)
        self.actionBeamsMoments_of_Inertia.setObjectName(u"actionBeamsMoments_of_Inertia")
        self.actionShear_and_Moment = QAction(MEMainWindow)
        self.actionShear_and_Moment.setObjectName(u"actionShear_and_Moment")
        self.actionIndeterminate_Axial_Structures = QAction(MEMainWindow)
        self.actionIndeterminate_Axial_Structures.setObjectName(u"actionIndeterminate_Axial_Structures")
        self.actionFlexure = QAction(MEMainWindow)
        self.actionFlexure.setObjectName(u"actionFlexure")
        self.actionBeam_Deformation = QAction(MEMainWindow)
        self.actionBeam_Deformation.setObjectName(u"actionBeam_Deformation")
        self.actionAxial_Beam_Deformation = QAction(MEMainWindow)
        self.actionAxial_Beam_Deformation.setObjectName(u"actionAxial_Beam_Deformation")
        self.actionTorsional_Beam_Deformation = QAction(MEMainWindow)
        self.actionTorsional_Beam_Deformation.setObjectName(u"actionTorsional_Beam_Deformation")
        self.actionSupported_Beams = QAction(MEMainWindow)
        self.actionSupported_Beams.setObjectName(u"actionSupported_Beams")
        self.actionMohr_s_Circle = QAction(MEMainWindow)
        self.actionMohr_s_Circle.setObjectName(u"actionMohr_s_Circle")
        self.actionC_Clamp = QAction(MEMainWindow)
        self.actionC_Clamp.setObjectName(u"actionC_Clamp")
        self.actionCompression_Link = QAction(MEMainWindow)
        self.actionCompression_Link.setObjectName(u"actionCompression_Link")
        self.actionTension_Link = QAction(MEMainWindow)
        self.actionTension_Link.setObjectName(u"actionTension_Link")
        self.actionPost = QAction(MEMainWindow)
        self.actionPost.setObjectName(u"actionPost")
        self.actionPost_and_Beam = QAction(MEMainWindow)
        self.actionPost_and_Beam.setObjectName(u"actionPost_and_Beam")
        self.actionKinematic_Diagraming = QAction(MEMainWindow)
        self.actionKinematic_Diagraming.setObjectName(u"actionKinematic_Diagraming")
        self.actionVector_Analysis = QAction(MEMainWindow)
        self.actionVector_Analysis.setObjectName(u"actionVector_Analysis")
        self.actionGDT_Checker = QAction(MEMainWindow)
        self.actionGDT_Checker.setObjectName(u"actionGDT_Checker")
        self.actionVirtual_Condition_Calculator = QAction(MEMainWindow)
        self.actionVirtual_Condition_Calculator.setObjectName(u"actionVirtual_Condition_Calculator")
        self.actionLimits_and_Fits = QAction(MEMainWindow)
        self.actionLimits_and_Fits.setObjectName(u"actionLimits_and_Fits")
        self.actionGDTFasteners = QAction(MEMainWindow)
        self.actionGDTFasteners.setObjectName(u"actionGDTFasteners")
        self.actionPaper_Gauging = QAction(MEMainWindow)
        self.actionPaper_Gauging.setObjectName(u"actionPaper_Gauging")
        self.actionTolerance_Finder = QAction(MEMainWindow)
        self.actionTolerance_Finder.setObjectName(u"actionTolerance_Finder")
        self.actionDiameter_Deviation = QAction(MEMainWindow)
        self.actionDiameter_Deviation.setObjectName(u"actionDiameter_Deviation")
        self.actionTorsion = QAction(MEMainWindow)
        self.actionTorsion.setObjectName(u"actionTorsion")
        self.actionPressure = QAction(MEMainWindow)
        self.actionPressure.setObjectName(u"actionPressure")
        self.actionAddMohr_s_Circle = QAction(MEMainWindow)
        self.actionAddMohr_s_Circle.setObjectName(u"actionAddMohr_s_Circle")
        self.actionModule_List = QAction(MEMainWindow)
        self.actionModule_List.setObjectName(u"actionModule_List")
        self.actionQuit = QAction(MEMainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionNotepad = QAction(MEMainWindow)
        self.actionNotepad.setObjectName(u"actionNotepad")
        self.actionCalculator = QAction(MEMainWindow)
        self.actionCalculator.setObjectName(u"actionCalculator")
        self.actionScreenshot = QAction(MEMainWindow)
        self.actionScreenshot.setObjectName(u"actionScreenshot")
        self.actionPerfer_SI_units = QAction(MEMainWindow)
        self.actionPerfer_SI_units.setObjectName(u"actionPerfer_SI_units")
        self.actionPerfer_Metric_Units = QAction(MEMainWindow)
        self.actionPerfer_Metric_Units.setObjectName(u"actionPerfer_Metric_Units")
        self.actionMaterials_list = QAction(MEMainWindow)
        self.actionMaterials_list.setObjectName(u"actionMaterials_list")
        self.actionCross_Sectional_Beams_and_Shapes_Lists = QAction(MEMainWindow)
        self.actionCross_Sectional_Beams_and_Shapes_Lists.setObjectName(u"actionCross_Sectional_Beams_and_Shapes_Lists")
        self.actionAbout = QAction(MEMainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionUnit_Converter_help = QAction(MEMainWindow)
        self.actionUnit_Converter_help.setObjectName(u"actionUnit_Converter_help")
        self.actionMoments_of_Inertia_help = QAction(MEMainWindow)
        self.actionMoments_of_Inertia_help.setObjectName(u"actionMoments_of_Inertia_help")
        self.actionVectors_help = QAction(MEMainWindow)
        self.actionVectors_help.setObjectName(u"actionVectors_help")
        self.actionFriction_and_Force_help = QAction(MEMainWindow)
        self.actionFriction_and_Force_help.setObjectName(u"actionFriction_and_Force_help")
        self.actionFasteners_help = QAction(MEMainWindow)
        self.actionFasteners_help.setObjectName(u"actionFasteners_help")
        self.actionMaterial_Properties_help = QAction(MEMainWindow)
        self.actionMaterial_Properties_help.setObjectName(u"actionMaterial_Properties_help")
        self.actionCM_and_CG_help = QAction(MEMainWindow)
        self.actionCM_and_CG_help.setObjectName(u"actionCM_and_CG_help")
        self.actionTrusses_help = QAction(MEMainWindow)
        self.actionTrusses_help.setObjectName(u"actionTrusses_help")
        self.actionBeamsMoments_of_Inertia_help = QAction(MEMainWindow)
        self.actionBeamsMoments_of_Inertia_help.setObjectName(u"actionBeamsMoments_of_Inertia_help")
        self.actionShear_and_Moment_help = QAction(MEMainWindow)
        self.actionShear_and_Moment_help.setObjectName(u"actionShear_and_Moment_help")
        self.actionIndeterminate_Axial_Structures_help = QAction(MEMainWindow)
        self.actionIndeterminate_Axial_Structures_help.setObjectName(u"actionIndeterminate_Axial_Structures_help")
        self.actionFlexure_help = QAction(MEMainWindow)
        self.actionFlexure_help.setObjectName(u"actionFlexure_help")
        self.actionBeam_Deformation_help = QAction(MEMainWindow)
        self.actionBeam_Deformation_help.setObjectName(u"actionBeam_Deformation_help")
        self.actionAxial_Beam_Deformation_help = QAction(MEMainWindow)
        self.actionAxial_Beam_Deformation_help.setObjectName(u"actionAxial_Beam_Deformation_help")
        self.actionTorsional_Beam_Deformation_help = QAction(MEMainWindow)
        self.actionTorsional_Beam_Deformation_help.setObjectName(u"actionTorsional_Beam_Deformation_help")
        self.actionSupported_Beams_help = QAction(MEMainWindow)
        self.actionSupported_Beams_help.setObjectName(u"actionSupported_Beams_help")
        self.actionMohr_s_Circle_help = QAction(MEMainWindow)
        self.actionMohr_s_Circle_help.setObjectName(u"actionMohr_s_Circle_help")
        self.actionC_Clamp_help = QAction(MEMainWindow)
        self.actionC_Clamp_help.setObjectName(u"actionC_Clamp_help")
        self.actionCompression_Link_help = QAction(MEMainWindow)
        self.actionCompression_Link_help.setObjectName(u"actionCompression_Link_help")
        self.actionTension_Link_help = QAction(MEMainWindow)
        self.actionTension_Link_help.setObjectName(u"actionTension_Link_help")
        self.actionPost_help = QAction(MEMainWindow)
        self.actionPost_help.setObjectName(u"actionPost_help")
        self.actionPost_and_Beam_help = QAction(MEMainWindow)
        self.actionPost_and_Beam_help.setObjectName(u"actionPost_and_Beam_help")
        self.actionSolid_shaft_and_Pipe_help = QAction(MEMainWindow)
        self.actionSolid_shaft_and_Pipe_help.setObjectName(u"actionSolid_shaft_and_Pipe_help")
        self.actionKinematic_Diagraming_help = QAction(MEMainWindow)
        self.actionKinematic_Diagraming_help.setObjectName(u"actionKinematic_Diagraming_help")
        self.actionVector_and_Motion_Analysis_help = QAction(MEMainWindow)
        self.actionVector_and_Motion_Analysis_help.setObjectName(u"actionVector_and_Motion_Analysis_help")
        self.actionGDT_Checker_help = QAction(MEMainWindow)
        self.actionGDT_Checker_help.setObjectName(u"actionGDT_Checker_help")
        self.actionVirtual_Condition_Calculator_help = QAction(MEMainWindow)
        self.actionVirtual_Condition_Calculator_help.setObjectName(u"actionVirtual_Condition_Calculator_help")
        self.actionLimits_and_Fits_help = QAction(MEMainWindow)
        self.actionLimits_and_Fits_help.setObjectName(u"actionLimits_and_Fits_help")
        self.actionGDTFasteners_help = QAction(MEMainWindow)
        self.actionGDTFasteners_help.setObjectName(u"actionGDTFasteners_help")
        self.actionPaper_Gauging_help = QAction(MEMainWindow)
        self.actionPaper_Gauging_help.setObjectName(u"actionPaper_Gauging_help")
        self.actionTolerance_Finder_help = QAction(MEMainWindow)
        self.actionTolerance_Finder_help.setObjectName(u"actionTolerance_Finder_help")
        self.actionDiameter_Deviation_help = QAction(MEMainWindow)
        self.actionDiameter_Deviation_help.setObjectName(u"actionDiameter_Deviation_help")
        self.actionTorsion_help = QAction(MEMainWindow)
        self.actionTorsion_help.setObjectName(u"actionTorsion_help")
        self.actionPressure_help = QAction(MEMainWindow)
        self.actionPressure_help.setObjectName(u"actionPressure_help")
        self.actionTheme = QAction(MEMainWindow)
        self.actionTheme.setObjectName(u"actionTheme")
        self.actionSaftey_Factors = QAction(MEMainWindow)
        self.actionSaftey_Factors.setObjectName(u"actionSaftey_Factors")
        self.actionSolid_Shaft_and_Pipe = QAction(MEMainWindow)
        self.actionSolid_Shaft_and_Pipe.setObjectName(u"actionSolid_Shaft_and_Pipe")
        self.actionMohr_s_Circle_2 = QAction(MEMainWindow)
        self.actionMohr_s_Circle_2.setObjectName(u"actionMohr_s_Circle_2")
        self.actionFit_Classes = QAction(MEMainWindow)
        self.actionFit_Classes.setObjectName(u"actionFit_Classes")
        self.actionCredits = QAction(MEMainWindow)
        self.actionCredits.setObjectName(u"actionCredits")
        self.actionUnit_Converter_2 = QAction(MEMainWindow)
        self.actionUnit_Converter_2.setObjectName(u"actionUnit_Converter_2")
        self.actionColumn_Buckling = QAction(MEMainWindow)
        self.actionColumn_Buckling.setObjectName(u"actionColumn_Buckling")
        self.actionDeterminate_Beams = QAction(MEMainWindow)
        self.actionDeterminate_Beams.setObjectName(u"actionDeterminate_Beams")
        self.actionSimple_Torsion = QAction(MEMainWindow)
        self.actionSimple_Torsion.setObjectName(u"actionSimple_Torsion")
        self.actionMohr_s_Circle_3 = QAction(MEMainWindow)
        self.actionMohr_s_Circle_3.setObjectName(u"actionMohr_s_Circle_3")
        self.actionFlexure_2 = QAction(MEMainWindow)
        self.actionFlexure_2.setObjectName(u"actionFlexure_2")
        self.actionPressure_Vessels = QAction(MEMainWindow)
        self.actionPressure_Vessels.setObjectName(u"actionPressure_Vessels")
        self.actionKinematic_Digramming = QAction(MEMainWindow)
        self.actionKinematic_Digramming.setObjectName(u"actionKinematic_Digramming")
        self.actionIndeterminate_Coaxial_Shafts = QAction(MEMainWindow)
        self.actionIndeterminate_Coaxial_Shafts.setObjectName(u"actionIndeterminate_Coaxial_Shafts")
        self.actionGear_Trains = QAction(MEMainWindow)
        self.actionGear_Trains.setObjectName(u"actionGear_Trains")
        self.actionAdvanced_Gear_Calculator = QAction(MEMainWindow)
        self.actionAdvanced_Gear_Calculator.setObjectName(u"actionAdvanced_Gear_Calculator")
        self.actionShaft_Design = QAction(MEMainWindow)
        self.actionShaft_Design.setObjectName(u"actionShaft_Design")
        self.actionGear_Driven_Shafts = QAction(MEMainWindow)
        self.actionGear_Driven_Shafts.setObjectName(u"actionGear_Driven_Shafts")
        self.actionChain_Drives = QAction(MEMainWindow)
        self.actionChain_Drives.setObjectName(u"actionChain_Drives")
        self.actionBelt_Drived = QAction(MEMainWindow)
        self.actionBelt_Drived.setObjectName(u"actionBelt_Drived")
        self.actionBearing_Calculator = QAction(MEMainWindow)
        self.actionBearing_Calculator.setObjectName(u"actionBearing_Calculator")
        self.actionKey_Calculator = QAction(MEMainWindow)
        self.actionKey_Calculator.setObjectName(u"actionKey_Calculator")
        self.actionQuit_all = QAction(MEMainWindow)
        self.actionQuit_all.setObjectName(u"actionQuit_all")
        self.actionCascade = QAction(MEMainWindow)
        self.actionCascade.setObjectName(u"actionCascade")
        self.actionTile = QAction(MEMainWindow)
        self.actionTile.setObjectName(u"actionTile")
        self.actionClose_All = QAction(MEMainWindow)
        self.actionClose_All.setObjectName(u"actionClose_All")
        self.actionCascade_2 = QAction(MEMainWindow)
        self.actionCascade_2.setObjectName(u"actionCascade_2")
        self.actionTile_2 = QAction(MEMainWindow)
        self.actionTile_2.setObjectName(u"actionTile_2")
        self.actionClose_All_2 = QAction(MEMainWindow)
        self.actionClose_All_2.setObjectName(u"actionClose_All_2")
        self.actionModule_Help = QAction(MEMainWindow)
        self.actionModule_Help.setObjectName(u"actionModule_Help")
        self.actionGD_T = QAction(MEMainWindow)
        self.actionGD_T.setObjectName(u"actionGD_T")
        self.centralwidget = QWidget(MEMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Unitconverter = QPushButton(self.centralwidget)
        self.Unitconverter.setObjectName(u"Unitconverter")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Unitconverter.sizePolicy().hasHeightForWidth())
        self.Unitconverter.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.Unitconverter)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line_2)

        self.Tables = QPushButton(self.centralwidget)
        self.Tables.setObjectName(u"Tables")
        sizePolicy1.setHeightForWidth(self.Tables.sizePolicy().hasHeightForWidth())
        self.Tables.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.Tables)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.Screenshot = QPushButton(self.centralwidget)
        self.Screenshot.setObjectName(u"Screenshot")
        sizePolicy1.setHeightForWidth(self.Screenshot.sizePolicy().hasHeightForWidth())
        self.Screenshot.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.Screenshot)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.mdiArea = QMdiArea(self.centralwidget)
        self.mdiArea.setObjectName(u"mdiArea")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mdiArea.sizePolicy().hasHeightForWidth())
        self.mdiArea.setSizePolicy(sizePolicy2)
        self.mdiArea.setFrameShape(QFrame.Shape.WinPanel)
        self.mdiArea.setFrameShadow(QFrame.Shadow.Sunken)
        self.mdiArea.setLineWidth(2)
        self.mdiArea.setMidLineWidth(0)
        self.mdiArea.setViewMode(QMdiArea.ViewMode.SubWindowView)
        self.mdiArea.setTabsClosable(True)
        self.mdiArea.setTabsMovable(True)

        self.gridLayout.addWidget(self.mdiArea, 1, 0, 1, 1)

        MEMainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MEMainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MEMainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MEMainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1596, 33))
        self.menu_File = QMenu(self.menubar)
        self.menu_File.setObjectName(u"menu_File")
        self.menu_Settings = QMenu(self.menu_File)
        self.menu_Settings.setObjectName(u"menu_Settings")
        self.menu_Utilites = QMenu(self.menubar)
        self.menu_Utilites.setObjectName(u"menu_Utilites")
        self.menuTables = QMenu(self.menu_Utilites)
        self.menuTables.setObjectName(u"menuTables")
        self.menu_Help = QMenu(self.menubar)
        self.menu_Help.setObjectName(u"menu_Help")
        self.menuWindow_2 = QMenu(self.menubar)
        self.menuWindow_2.setObjectName(u"menuWindow_2")
        MEMainWindow.setMenuBar(self.menubar)
        self.Modulelistdock = QDockWidget(MEMainWindow)
        self.Modulelistdock.setObjectName(u"Modulelistdock")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.Modulelistdock.sizePolicy().hasHeightForWidth())
        self.Modulelistdock.setSizePolicy(sizePolicy3)
        self.Modulelistdock.setMinimumSize(QSize(97, 97))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(10)
        self.Modulelistdock.setFont(font)
        self.Modulelistdock.setAutoFillBackground(False)
        self.Modulelistdock.setFloating(False)
        self.Modulelistdock.setFeatures(QDockWidget.DockWidgetFeature.DockWidgetFloatable|QDockWidget.DockWidgetFeature.DockWidgetMovable)
        self.Modulelistdock.setAllowedAreas(Qt.DockWidgetArea.LeftDockWidgetArea|Qt.DockWidgetArea.RightDockWidgetArea)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Modulelist = QTreeWidget(self.dockWidgetContents)
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setForeground(0, brush);
        self.Modulelist.setHeaderItem(__qtreewidgetitem)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.NoBrush)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.SolidPattern)
        brush3 = QBrush(QColor(255, 255, 255, 255))
        brush3.setStyle(Qt.NoBrush)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.NoBrush)
        brush5 = QBrush(QColor(0, 0, 0, 255))
        brush5.setStyle(Qt.NoBrush)
        brush6 = QBrush(QColor(0, 0, 0, 255))
        brush6.setStyle(Qt.NoBrush)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.NoBrush)
        brush8 = QBrush(QColor(0, 0, 0, 255))
        brush8.setStyle(Qt.NoBrush)
        brush9 = QBrush(QColor(0, 0, 0, 255))
        brush9.setStyle(Qt.NoBrush)
        brush10 = QBrush(QColor(99, 99, 99, 255))
        brush10.setStyle(Qt.SolidPattern)
        brush11 = QBrush(QColor(154, 154, 154, 255))
        brush11.setStyle(Qt.SolidPattern)
        __qtreewidgetitem1 = QTreeWidgetItem(self.Modulelist)
        __qtreewidgetitem1.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qtreewidgetitem1.setBackground(0, brush1);
        __qtreewidgetitem1.setForeground(0, brush);
        __qtreewidgetitem2 = QTreeWidgetItem(self.Modulelist)
        __qtreewidgetitem2.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qtreewidgetitem2.setBackground(0, brush);
        __qtreewidgetitem2.setForeground(0, brush2);
        __qtreewidgetitem3 = QTreeWidgetItem(__qtreewidgetitem2)
        __qtreewidgetitem3.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qtreewidgetitem3.setBackground(0, brush4);
        __qtreewidgetitem3.setForeground(0, brush3);
        __qtreewidgetitem4 = QTreeWidgetItem(__qtreewidgetitem2)
        __qtreewidgetitem4.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qtreewidgetitem4.setBackground(0, brush5);
        __qtreewidgetitem5 = QTreeWidgetItem(__qtreewidgetitem2)
        __qtreewidgetitem5.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qtreewidgetitem5.setBackground(0, brush6);
        __qtreewidgetitem6 = QTreeWidgetItem(__qtreewidgetitem2)
        __qtreewidgetitem6.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qtreewidgetitem6.setBackground(0, brush7);
        __qtreewidgetitem7 = QTreeWidgetItem(__qtreewidgetitem2)
        __qtreewidgetitem7.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qtreewidgetitem7.setBackground(0, brush8);
        __qtreewidgetitem8 = QTreeWidgetItem(__qtreewidgetitem2)
        __qtreewidgetitem8.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qtreewidgetitem8.setBackground(0, brush9);
        __qtreewidgetitem9 = QTreeWidgetItem(self.Modulelist)
        __qtreewidgetitem9.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qtreewidgetitem9.setBackground(0, brush);
        __qtreewidgetitem9.setForeground(0, brush2);
        __qtreewidgetitem10 = QTreeWidgetItem(__qtreewidgetitem9)
        __qtreewidgetitem10.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qtreewidgetitem10.setBackground(0, brush10);
        __qtreewidgetitem10.setForeground(0, brush2);
        __qtreewidgetitem11 = QTreeWidgetItem(__qtreewidgetitem10)
        __qtreewidgetitem11.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qtreewidgetitem12 = QTreeWidgetItem(__qtreewidgetitem10)
        __qtreewidgetitem12.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qtreewidgetitem13 = QTreeWidgetItem(__qtreewidgetitem10)
        __qtreewidgetitem13.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qtreewidgetitem14 = QTreeWidgetItem(__qtreewidgetitem10)
        __qtreewidgetitem14.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qtreewidgetitem15 = QTreeWidgetItem(__qtreewidgetitem10)
        __qtreewidgetitem15.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qtreewidgetitem16 = QTreeWidgetItem(__qtreewidgetitem10)
        __qtreewidgetitem16.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qtreewidgetitem17 = QTreeWidgetItem(__qtreewidgetitem10)
        __qtreewidgetitem17.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qtreewidgetitem18 = QTreeWidgetItem(__qtreewidgetitem10)
        __qtreewidgetitem18.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qtreewidgetitem18.setBackground(0, brush11);
        __qtreewidgetitem18.setForeground(0, brush2);
        __qtreewidgetitem19 = QTreeWidgetItem(__qtreewidgetitem18)
        __qtreewidgetitem19.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qtreewidgetitem20 = QTreeWidgetItem(__qtreewidgetitem18)
        __qtreewidgetitem20.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qtreewidgetitem21 = QTreeWidgetItem(__qtreewidgetitem18)
        __qtreewidgetitem21.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qtreewidgetitem22 = QTreeWidgetItem(self.Modulelist)
        __qtreewidgetitem22.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qtreewidgetitem22.setBackground(0, brush);
        __qtreewidgetitem22.setForeground(0, brush2);
        __qtreewidgetitem23 = QTreeWidgetItem(__qtreewidgetitem22)
        __qtreewidgetitem23.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qtreewidgetitem24 = QTreeWidgetItem(__qtreewidgetitem22)
        __qtreewidgetitem24.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qtreewidgetitem25 = QTreeWidgetItem(__qtreewidgetitem22)
        __qtreewidgetitem25.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qtreewidgetitem26 = QTreeWidgetItem(__qtreewidgetitem22)
        __qtreewidgetitem26.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qtreewidgetitem27 = QTreeWidgetItem(__qtreewidgetitem22)
        __qtreewidgetitem27.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qtreewidgetitem28 = QTreeWidgetItem(__qtreewidgetitem22)
        __qtreewidgetitem28.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qtreewidgetitem29 = QTreeWidgetItem(__qtreewidgetitem22)
        __qtreewidgetitem29.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qtreewidgetitem30 = QTreeWidgetItem(__qtreewidgetitem22)
        __qtreewidgetitem30.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qtreewidgetitem31 = QTreeWidgetItem(self.Modulelist)
        __qtreewidgetitem31.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qtreewidgetitem31.setBackground(0, brush);
        __qtreewidgetitem31.setForeground(0, brush2);
        __qtreewidgetitem32 = QTreeWidgetItem(__qtreewidgetitem31)
        __qtreewidgetitem32.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qtreewidgetitem32.setBackground(0, brush10);
        __qtreewidgetitem32.setForeground(0, brush2);
        __qtreewidgetitem33 = QTreeWidgetItem(__qtreewidgetitem32)
        __qtreewidgetitem33.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qtreewidgetitem34 = QTreeWidgetItem(__qtreewidgetitem32)
        __qtreewidgetitem34.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qtreewidgetitem35 = QTreeWidgetItem(__qtreewidgetitem32)
        __qtreewidgetitem35.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qtreewidgetitem35.setBackground(0, brush11);
        __qtreewidgetitem35.setForeground(0, brush2);
        __qtreewidgetitem36 = QTreeWidgetItem(__qtreewidgetitem35)
        __qtreewidgetitem36.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qtreewidgetitem37 = QTreeWidgetItem(__qtreewidgetitem35)
        __qtreewidgetitem37.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qtreewidgetitem38 = QTreeWidgetItem(__qtreewidgetitem35)
        __qtreewidgetitem38.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qtreewidgetitem39 = QTreeWidgetItem(__qtreewidgetitem31)
        __qtreewidgetitem39.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qtreewidgetitem40 = QTreeWidgetItem(__qtreewidgetitem31)
        __qtreewidgetitem40.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qtreewidgetitem41 = QTreeWidgetItem(self.Modulelist)
        __qtreewidgetitem41.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qtreewidgetitem41.setBackground(0, brush);
        __qtreewidgetitem41.setForeground(0, brush2);
        __qtreewidgetitem42 = QTreeWidgetItem(__qtreewidgetitem41)
        __qtreewidgetitem42.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qtreewidgetitem43 = QTreeWidgetItem(__qtreewidgetitem41)
        __qtreewidgetitem43.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qtreewidgetitem44 = QTreeWidgetItem(__qtreewidgetitem41)
        __qtreewidgetitem44.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qtreewidgetitem45 = QTreeWidgetItem(__qtreewidgetitem41)
        __qtreewidgetitem45.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qtreewidgetitem46 = QTreeWidgetItem(__qtreewidgetitem41)
        __qtreewidgetitem46.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qtreewidgetitem47 = QTreeWidgetItem(__qtreewidgetitem41)
        __qtreewidgetitem47.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qtreewidgetitem48 = QTreeWidgetItem(self.Modulelist)
        __qtreewidgetitem48.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.Modulelist.setObjectName(u"Modulelist")
        sizePolicy3.setHeightForWidth(self.Modulelist.sizePolicy().hasHeightForWidth())
        self.Modulelist.setSizePolicy(sizePolicy3)
        font1 = QFont()
        font1.setFamilies([u"Century Gothic"])
        font1.setPointSize(13)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setKerning(True)
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.Modulelist.setFont(font1)
        self.Modulelist.setFocusPolicy(Qt.FocusPolicy.WheelFocus)
        self.Modulelist.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.Modulelist.setEditTriggers(QAbstractItemView.EditTrigger.DoubleClicked|QAbstractItemView.EditTrigger.EditKeyPressed)
        self.Modulelist.setTabKeyNavigation(True)
        self.Modulelist.setAlternatingRowColors(True)
        self.Modulelist.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.Modulelist.setAnimated(True)
        self.Modulelist.setWordWrap(True)
        self.Modulelist.setColumnCount(1)

        self.verticalLayout.addWidget(self.Modulelist)

        self.Modulelistdock.setWidget(self.dockWidgetContents)
        MEMainWindow.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.Modulelistdock)

        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menuWindow_2.menuAction())
        self.menubar.addAction(self.menu_Utilites.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.menu_File.addAction(self.menu_Settings.menuAction())
        self.menu_File.addAction(self.actionQuit)
        self.menu_Settings.addAction(self.actionTheme)
        self.menu_Utilites.addAction(self.actionNotepad)
        self.menu_Utilites.addAction(self.actionUnit_Converter_2)
        self.menu_Utilites.addAction(self.actionScreenshot)
        self.menu_Utilites.addAction(self.menuTables.menuAction())
        self.menuTables.addAction(self.actionMaterials_list)
        self.menuTables.addAction(self.actionCross_Sectional_Beams_and_Shapes_Lists)
        self.menuTables.addAction(self.actionSaftey_Factors)
        self.menuTables.addAction(self.actionFit_Classes)
        self.menuTables.addAction(self.actionGD_T)
        self.menu_Help.addAction(self.actionModule_Help)
        self.menu_Help.addAction(self.actionAbout)
        self.menuWindow_2.addAction(self.actionCascade_2)
        self.menuWindow_2.addAction(self.actionTile_2)
        self.menuWindow_2.addAction(self.actionClose_All_2)

        self.retranslateUi(MEMainWindow)

        QMetaObject.connectSlotsByName(MEMainWindow)
    # setupUi

    def retranslateUi(self, MEMainWindow):
        MEMainWindow.setWindowTitle(QCoreApplication.translate("MEMainWindow", u"MainWindow", None))
        self.actionUnit_Converter.setText(QCoreApplication.translate("MEMainWindow", u"Unit Converter", None))
        self.actionMoments_of_Inertia.setText(QCoreApplication.translate("MEMainWindow", u"Moments of Inertia", None))
        self.actionVectors.setText(QCoreApplication.translate("MEMainWindow", u"Vectors", None))
        self.actionFriction_and_Force.setText(QCoreApplication.translate("MEMainWindow", u"Friction and Force", None))
        self.actionFasteners.setText(QCoreApplication.translate("MEMainWindow", u"Fasteners", None))
        self.actionMaterial_Properties.setText(QCoreApplication.translate("MEMainWindow", u"Material Properties", None))
        self.actionCM_and_CG.setText(QCoreApplication.translate("MEMainWindow", u"CM and CG", None))
        self.actionTrusses.setText(QCoreApplication.translate("MEMainWindow", u"Trusses", None))
        self.actionBeamsMoments_of_Inertia.setText(QCoreApplication.translate("MEMainWindow", u"Moments of Inertia", None))
        self.actionShear_and_Moment.setText(QCoreApplication.translate("MEMainWindow", u"Shear and Moment", None))
        self.actionIndeterminate_Axial_Structures.setText(QCoreApplication.translate("MEMainWindow", u"Indeterminate Axial Structures", None))
        self.actionFlexure.setText(QCoreApplication.translate("MEMainWindow", u"Flexure", None))
        self.actionBeam_Deformation.setText(QCoreApplication.translate("MEMainWindow", u"Beam Deformation", None))
        self.actionAxial_Beam_Deformation.setText(QCoreApplication.translate("MEMainWindow", u"Axial Beam Deformation", None))
        self.actionTorsional_Beam_Deformation.setText(QCoreApplication.translate("MEMainWindow", u"Torsional Beam Deformation", None))
        self.actionSupported_Beams.setText(QCoreApplication.translate("MEMainWindow", u"Supported Beams", None))
        self.actionMohr_s_Circle.setText(QCoreApplication.translate("MEMainWindow", u"Mohr's Circle", None))
        self.actionC_Clamp.setText(QCoreApplication.translate("MEMainWindow", u"C-Clamp", None))
        self.actionCompression_Link.setText(QCoreApplication.translate("MEMainWindow", u"Compression Link", None))
        self.actionTension_Link.setText(QCoreApplication.translate("MEMainWindow", u"Tension Link", None))
        self.actionPost.setText(QCoreApplication.translate("MEMainWindow", u"Post", None))
        self.actionPost_and_Beam.setText(QCoreApplication.translate("MEMainWindow", u"Post and Beam", None))
        self.actionKinematic_Diagraming.setText(QCoreApplication.translate("MEMainWindow", u"Kinematic Diagraming", None))
        self.actionVector_Analysis.setText(QCoreApplication.translate("MEMainWindow", u"Vector Analysis", None))
        self.actionGDT_Checker.setText(QCoreApplication.translate("MEMainWindow", u"GDT Checker", None))
        self.actionVirtual_Condition_Calculator.setText(QCoreApplication.translate("MEMainWindow", u"Virtual Condition Calculator", None))
        self.actionLimits_and_Fits.setText(QCoreApplication.translate("MEMainWindow", u"Limits and Fits", None))
        self.actionGDTFasteners.setText(QCoreApplication.translate("MEMainWindow", u"Fasteners", None))
        self.actionPaper_Gauging.setText(QCoreApplication.translate("MEMainWindow", u"Paper Gauging", None))
        self.actionTolerance_Finder.setText(QCoreApplication.translate("MEMainWindow", u"Tolerance Finder", None))
        self.actionDiameter_Deviation.setText(QCoreApplication.translate("MEMainWindow", u"Diameter Deviation", None))
        self.actionTorsion.setText(QCoreApplication.translate("MEMainWindow", u"Torsion", None))
        self.actionPressure.setText(QCoreApplication.translate("MEMainWindow", u"Pressure", None))
        self.actionAddMohr_s_Circle.setText(QCoreApplication.translate("MEMainWindow", u"Mohr's Circle", None))
        self.actionModule_List.setText(QCoreApplication.translate("MEMainWindow", u"Module List", None))
        self.actionQuit.setText(QCoreApplication.translate("MEMainWindow", u"Quit", None))
        self.actionNotepad.setText(QCoreApplication.translate("MEMainWindow", u"Notepad", None))
        self.actionCalculator.setText(QCoreApplication.translate("MEMainWindow", u"Calculator", None))
        self.actionScreenshot.setText(QCoreApplication.translate("MEMainWindow", u"Screenshot", None))
        self.actionPerfer_SI_units.setText(QCoreApplication.translate("MEMainWindow", u"Edit Saftey Factor", None))
        self.actionPerfer_Metric_Units.setText(QCoreApplication.translate("MEMainWindow", u"Theme", None))
        self.actionMaterials_list.setText(QCoreApplication.translate("MEMainWindow", u"Materials List", None))
        self.actionCross_Sectional_Beams_and_Shapes_Lists.setText(QCoreApplication.translate("MEMainWindow", u"Beams and Shapes Lists", None))
        self.actionAbout.setText(QCoreApplication.translate("MEMainWindow", u"About", None))
        self.actionUnit_Converter_help.setText(QCoreApplication.translate("MEMainWindow", u"Unit Converter", None))
        self.actionMoments_of_Inertia_help.setText(QCoreApplication.translate("MEMainWindow", u"Moments of Inertia", None))
        self.actionVectors_help.setText(QCoreApplication.translate("MEMainWindow", u"Vectors", None))
        self.actionFriction_and_Force_help.setText(QCoreApplication.translate("MEMainWindow", u"Friction and Force", None))
        self.actionFasteners_help.setText(QCoreApplication.translate("MEMainWindow", u"Fasteners", None))
        self.actionMaterial_Properties_help.setText(QCoreApplication.translate("MEMainWindow", u"Material Properties", None))
        self.actionCM_and_CG_help.setText(QCoreApplication.translate("MEMainWindow", u"CM and CG", None))
        self.actionTrusses_help.setText(QCoreApplication.translate("MEMainWindow", u"Trusses", None))
        self.actionBeamsMoments_of_Inertia_help.setText(QCoreApplication.translate("MEMainWindow", u"Moments of Inertia", None))
        self.actionShear_and_Moment_help.setText(QCoreApplication.translate("MEMainWindow", u"Shear and Moment", None))
        self.actionIndeterminate_Axial_Structures_help.setText(QCoreApplication.translate("MEMainWindow", u"Indeterminate Axial Structures", None))
        self.actionFlexure_help.setText(QCoreApplication.translate("MEMainWindow", u"Flexure", None))
        self.actionBeam_Deformation_help.setText(QCoreApplication.translate("MEMainWindow", u"Beam Deformation", None))
        self.actionAxial_Beam_Deformation_help.setText(QCoreApplication.translate("MEMainWindow", u"Axial Beam Deformation", None))
        self.actionTorsional_Beam_Deformation_help.setText(QCoreApplication.translate("MEMainWindow", u"Torsional Beam Deformation", None))
        self.actionSupported_Beams_help.setText(QCoreApplication.translate("MEMainWindow", u"Supported Beams", None))
        self.actionMohr_s_Circle_help.setText(QCoreApplication.translate("MEMainWindow", u"Mohr's Circle", None))
        self.actionC_Clamp_help.setText(QCoreApplication.translate("MEMainWindow", u"C-Clamp", None))
        self.actionCompression_Link_help.setText(QCoreApplication.translate("MEMainWindow", u"Compression Link", None))
        self.actionTension_Link_help.setText(QCoreApplication.translate("MEMainWindow", u"Tension Link", None))
        self.actionPost_help.setText(QCoreApplication.translate("MEMainWindow", u"Post", None))
        self.actionPost_and_Beam_help.setText(QCoreApplication.translate("MEMainWindow", u"Post and Beam", None))
        self.actionSolid_shaft_and_Pipe_help.setText(QCoreApplication.translate("MEMainWindow", u"Solid Shaft and Pipe", None))
        self.actionKinematic_Diagraming_help.setText(QCoreApplication.translate("MEMainWindow", u"Kinematic Diagraming", None))
        self.actionVector_and_Motion_Analysis_help.setText(QCoreApplication.translate("MEMainWindow", u"Vector and Motion Analysis", None))
        self.actionGDT_Checker_help.setText(QCoreApplication.translate("MEMainWindow", u"GDT Checker", None))
        self.actionVirtual_Condition_Calculator_help.setText(QCoreApplication.translate("MEMainWindow", u"Virtual Condition Calculator", None))
        self.actionLimits_and_Fits_help.setText(QCoreApplication.translate("MEMainWindow", u"Limits and Fits", None))
        self.actionGDTFasteners_help.setText(QCoreApplication.translate("MEMainWindow", u"Fasteners", None))
        self.actionPaper_Gauging_help.setText(QCoreApplication.translate("MEMainWindow", u"Paper Gauging", None))
        self.actionTolerance_Finder_help.setText(QCoreApplication.translate("MEMainWindow", u"Tolerance Finder", None))
        self.actionDiameter_Deviation_help.setText(QCoreApplication.translate("MEMainWindow", u"Diameter Deviation", None))
        self.actionTorsion_help.setText(QCoreApplication.translate("MEMainWindow", u"Torsion", None))
        self.actionPressure_help.setText(QCoreApplication.translate("MEMainWindow", u"Pressure", None))
        self.actionTheme.setText(QCoreApplication.translate("MEMainWindow", u"Theme", None))
        self.actionSaftey_Factors.setText(QCoreApplication.translate("MEMainWindow", u"Saftey Factors", None))
        self.actionSolid_Shaft_and_Pipe.setText(QCoreApplication.translate("MEMainWindow", u"Solid Shaft and Pipe", None))
        self.actionMohr_s_Circle_2.setText(QCoreApplication.translate("MEMainWindow", u"Mohr's Circle", None))
        self.actionFit_Classes.setText(QCoreApplication.translate("MEMainWindow", u"Fit Classes", None))
        self.actionCredits.setText(QCoreApplication.translate("MEMainWindow", u"Credits", None))
        self.actionUnit_Converter_2.setText(QCoreApplication.translate("MEMainWindow", u"Unit Converter", None))
        self.actionColumn_Buckling.setText(QCoreApplication.translate("MEMainWindow", u"Column Buckling", None))
        self.actionDeterminate_Beams.setText(QCoreApplication.translate("MEMainWindow", u"Determinate Beams", None))
        self.actionSimple_Torsion.setText(QCoreApplication.translate("MEMainWindow", u"Simple Torsion", None))
        self.actionMohr_s_Circle_3.setText(QCoreApplication.translate("MEMainWindow", u"Mohr's Circle", None))
        self.actionFlexure_2.setText(QCoreApplication.translate("MEMainWindow", u"Flexure", None))
        self.actionPressure_Vessels.setText(QCoreApplication.translate("MEMainWindow", u"Pressure Vessels", None))
        self.actionKinematic_Digramming.setText(QCoreApplication.translate("MEMainWindow", u"Kinematic Digramming", None))
        self.actionIndeterminate_Coaxial_Shafts.setText(QCoreApplication.translate("MEMainWindow", u"Indeterminate Coaxial Shafts", None))
        self.actionGear_Trains.setText(QCoreApplication.translate("MEMainWindow", u"Gear Trains", None))
        self.actionAdvanced_Gear_Calculator.setText(QCoreApplication.translate("MEMainWindow", u"Advanced Gear Calculator", None))
        self.actionShaft_Design.setText(QCoreApplication.translate("MEMainWindow", u"Shaft Design", None))
        self.actionGear_Driven_Shafts.setText(QCoreApplication.translate("MEMainWindow", u"Gear Driven Shafts", None))
        self.actionChain_Drives.setText(QCoreApplication.translate("MEMainWindow", u"Chain Drives", None))
        self.actionBelt_Drived.setText(QCoreApplication.translate("MEMainWindow", u"Belt Drives", None))
        self.actionBearing_Calculator.setText(QCoreApplication.translate("MEMainWindow", u"Bearing Calculator", None))
        self.actionKey_Calculator.setText(QCoreApplication.translate("MEMainWindow", u"Key Calculator", None))
        self.actionQuit_all.setText(QCoreApplication.translate("MEMainWindow", u"Quit All", None))
        self.actionCascade.setText(QCoreApplication.translate("MEMainWindow", u"Cascade", None))
        self.actionTile.setText(QCoreApplication.translate("MEMainWindow", u"Tile", None))
        self.actionClose_All.setText(QCoreApplication.translate("MEMainWindow", u"Close All", None))
        self.actionCascade_2.setText(QCoreApplication.translate("MEMainWindow", u"Cascade", None))
        self.actionTile_2.setText(QCoreApplication.translate("MEMainWindow", u"Tile", None))
        self.actionClose_All_2.setText(QCoreApplication.translate("MEMainWindow", u"Close All", None))
        self.actionModule_Help.setText(QCoreApplication.translate("MEMainWindow", u"Module Help", None))
        self.actionGD_T.setText(QCoreApplication.translate("MEMainWindow", u"GD&T", None))
        self.Unitconverter.setText(QCoreApplication.translate("MEMainWindow", u"Unit Converter", None))
        self.pushButton.setText(QCoreApplication.translate("MEMainWindow", u"Notepad", None))
        self.Tables.setText(QCoreApplication.translate("MEMainWindow", u"Tables", None))
        self.Screenshot.setText(QCoreApplication.translate("MEMainWindow", u"Screen Shot", None))
        self.menu_File.setTitle(QCoreApplication.translate("MEMainWindow", u"&File", None))
        self.menu_Settings.setTitle(QCoreApplication.translate("MEMainWindow", u"Settings", None))
        self.menu_Utilites.setTitle(QCoreApplication.translate("MEMainWindow", u"&Utilites", None))
        self.menuTables.setTitle(QCoreApplication.translate("MEMainWindow", u"Tables", None))
        self.menu_Help.setTitle(QCoreApplication.translate("MEMainWindow", u"&Help", None))
        self.menuWindow_2.setTitle(QCoreApplication.translate("MEMainWindow", u"Window", None))
        self.Modulelistdock.setWindowTitle(QCoreApplication.translate("MEMainWindow", u"Module List", None))
        ___qtreewidgetitem = self.Modulelist.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MEMainWindow", u"Module List", None));

        __sortingEnabled = self.Modulelist.isSortingEnabled()
        self.Modulelist.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.Modulelist.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MEMainWindow", u"Notepad", None));
        ___qtreewidgetitem2 = self.Modulelist.topLevelItem(1)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MEMainWindow", u"General Analysis", None));
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem2.setToolTip(0, QCoreApplication.translate("MEMainWindow", u"General Analysis List", None));
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem3 = ___qtreewidgetitem2.child(0)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MEMainWindow", u"Unit Converter", None));
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem3.setToolTip(0, QCoreApplication.translate("MEMainWindow", u"Unit Converter Module", None));
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem4 = ___qtreewidgetitem2.child(1)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("MEMainWindow", u"Moments of Inertia", None));
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem4.setToolTip(0, QCoreApplication.translate("MEMainWindow", u"Moment of Inertia Module", None));
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem5 = ___qtreewidgetitem2.child(2)
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("MEMainWindow", u"Vectors", None));
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem5.setToolTip(0, QCoreApplication.translate("MEMainWindow", u"Vector Analysis Module", None));
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem6 = ___qtreewidgetitem2.child(3)
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("MEMainWindow", u"Fasteners", None));
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem6.setToolTip(0, QCoreApplication.translate("MEMainWindow", u"Basic Fasteners Module", None));
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem7 = ___qtreewidgetitem2.child(4)
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("MEMainWindow", u"Material Properties", None));
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem7.setToolTip(0, QCoreApplication.translate("MEMainWindow", u"Material Properties Module", None));
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem8 = ___qtreewidgetitem2.child(5)
        ___qtreewidgetitem8.setText(0, QCoreApplication.translate("MEMainWindow", u"Center of Mass and Center of Gravity", None));
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem8.setToolTip(0, QCoreApplication.translate("MEMainWindow", u"Center of Mass and Center of Gravity Module", None));
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem9 = self.Modulelist.topLevelItem(2)
        ___qtreewidgetitem9.setText(0, QCoreApplication.translate("MEMainWindow", u"Beams and Loads", None));
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem9.setToolTip(0, QCoreApplication.translate("MEMainWindow", u"Beams and Loads List", None));
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem10 = ___qtreewidgetitem9.child(0)
        ___qtreewidgetitem10.setText(0, QCoreApplication.translate("MEMainWindow", u"General Beam Analysis", None));
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem10.setToolTip(0, QCoreApplication.translate("MEMainWindow", u"General Beam Analysis List", None));
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem11 = ___qtreewidgetitem10.child(0)
        ___qtreewidgetitem11.setText(0, QCoreApplication.translate("MEMainWindow", u"Trusses", None));
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem11.setToolTip(0, QCoreApplication.translate("MEMainWindow", u"Truss Module", None));
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem12 = ___qtreewidgetitem10.child(1)
        ___qtreewidgetitem12.setText(0, QCoreApplication.translate("MEMainWindow", u"Moments of Inertia", None));
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem12.setToolTip(0, QCoreApplication.translate("MEMainWindow", u"Moment of Inertia Module", None));
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem13 = ___qtreewidgetitem10.child(2)
        ___qtreewidgetitem13.setText(0, QCoreApplication.translate("MEMainWindow", u"Determinate Beams", None));
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem13.setToolTip(0, QCoreApplication.translate("MEMainWindow", u"Determinate Beams Module", None));
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem14 = ___qtreewidgetitem10.child(3)
        ___qtreewidgetitem14.setText(0, QCoreApplication.translate("MEMainWindow", u"Column Buckling", None));
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem14.setToolTip(0, QCoreApplication.translate("MEMainWindow", u"Column Buckling Module", None));
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem15 = ___qtreewidgetitem10.child(4)
        ___qtreewidgetitem15.setText(0, QCoreApplication.translate("MEMainWindow", u"Flexure", None));
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem15.setToolTip(0, QCoreApplication.translate("MEMainWindow", u"Flexure Module", None));
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem16 = ___qtreewidgetitem10.child(5)
        ___qtreewidgetitem16.setText(0, QCoreApplication.translate("MEMainWindow", u"Indeterminate Axial Structures", None));
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem16.setToolTip(0, QCoreApplication.translate("MEMainWindow", u"Indeterminate Axial Structures Module", None));
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem17 = ___qtreewidgetitem10.child(6)
        ___qtreewidgetitem17.setText(0, QCoreApplication.translate("MEMainWindow", u"Mohr's Circle", None));
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem17.setToolTip(0, QCoreApplication.translate("MEMainWindow", u"Mohr's Circle Module", None));
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem18 = ___qtreewidgetitem10.child(7)
        ___qtreewidgetitem18.setText(0, QCoreApplication.translate("MEMainWindow", u"Deformation analysis", None));
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem18.setToolTip(0, QCoreApplication.translate("MEMainWindow", u"Deformation Analysis List", None));
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem19 = ___qtreewidgetitem18.child(0)
        ___qtreewidgetitem19.setText(0, QCoreApplication.translate("MEMainWindow", u"Generic Beam Deformation Analysis", None));
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem19.setToolTip(0, QCoreApplication.translate("MEMainWindow", u"Generic Beam Deformation Module", None));
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem20 = ___qtreewidgetitem18.child(1)
        ___qtreewidgetitem20.setText(0, QCoreApplication.translate("MEMainWindow", u"Axial Beam Deformation", None));
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem20.setToolTip(0, QCoreApplication.translate("MEMainWindow", u"Axial Beam Deformation Module", None));
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem21 = ___qtreewidgetitem18.child(2)
        ___qtreewidgetitem21.setText(0, QCoreApplication.translate("MEMainWindow", u"Torsional Beam Deformation", None));
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem21.setToolTip(0, QCoreApplication.translate("MEMainWindow", u"Torsioanl Beam Deformation Module", None));
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem22 = self.Modulelist.topLevelItem(3)
        ___qtreewidgetitem22.setText(0, QCoreApplication.translate("MEMainWindow", u"Basic Mechanics Analysis", None));
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem22.setToolTip(0, QCoreApplication.translate("MEMainWindow", u"Basic Mechanics Analysis List", None));
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem23 = ___qtreewidgetitem22.child(0)
        ___qtreewidgetitem23.setText(0, QCoreApplication.translate("MEMainWindow", u"Determinate Beams", None));
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem23.setToolTip(0, QCoreApplication.translate("MEMainWindow", u"Determinate Beams Module", None));
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem24 = ___qtreewidgetitem22.child(1)
        ___qtreewidgetitem24.setText(0, QCoreApplication.translate("MEMainWindow", u"Simple Torsion", None));
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem24.setToolTip(0, QCoreApplication.translate("MEMainWindow", u"Simple Torsion Module", None));
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem25 = ___qtreewidgetitem22.child(2)
        ___qtreewidgetitem25.setText(0, QCoreApplication.translate("MEMainWindow", u"Mohr's Circle", None));
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem25.setToolTip(0, QCoreApplication.translate("MEMainWindow", u"Morh's Circle Module", None));
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem26 = ___qtreewidgetitem22.child(3)
        ___qtreewidgetitem26.setText(0, QCoreApplication.translate("MEMainWindow", u"Flexure", None));
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem26.setToolTip(0, QCoreApplication.translate("MEMainWindow", u"Flexure Module", None));
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem27 = ___qtreewidgetitem22.child(4)
        ___qtreewidgetitem27.setText(0, QCoreApplication.translate("MEMainWindow", u"Pressure Vessels", None));
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem27.setToolTip(0, QCoreApplication.translate("MEMainWindow", u"Pressure Vessels Module", None));
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem28 = ___qtreewidgetitem22.child(5)
        ___qtreewidgetitem28.setText(0, QCoreApplication.translate("MEMainWindow", u"Kinematic Diagraming", None));
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem28.setToolTip(0, QCoreApplication.translate("MEMainWindow", u"Kinematic Diagraming Module", None));
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem29 = ___qtreewidgetitem22.child(6)
        ___qtreewidgetitem29.setText(0, QCoreApplication.translate("MEMainWindow", u"Indeterminate Coaxial Shafts", None));
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem29.setToolTip(0, QCoreApplication.translate("MEMainWindow", u"Indeterminate Coaxial Shafts Module", None));
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem30 = ___qtreewidgetitem22.child(7)
        ___qtreewidgetitem30.setText(0, QCoreApplication.translate("MEMainWindow", u"Indeterminate End-to-End Shafts", None));
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem30.setToolTip(0, QCoreApplication.translate("MEMainWindow", u"Indeterminate End-to-End Shafts Module", None));
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem31 = self.Modulelist.topLevelItem(4)
        ___qtreewidgetitem31.setText(0, QCoreApplication.translate("MEMainWindow", u"Machine Design Elements", None));
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem31.setToolTip(0, QCoreApplication.translate("MEMainWindow", u"Machine Design Elements List", None));
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem32 = ___qtreewidgetitem31.child(0)
        ___qtreewidgetitem32.setText(0, QCoreApplication.translate("MEMainWindow", u"Machine Drives", None));
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem32.setToolTip(0, QCoreApplication.translate("MEMainWindow", u"Machine Drives List", None));
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem33 = ___qtreewidgetitem32.child(0)
        ___qtreewidgetitem33.setText(0, QCoreApplication.translate("MEMainWindow", u"Belt Drives", None));
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem33.setToolTip(0, QCoreApplication.translate("MEMainWindow", u"Belt Drives Module", None));
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem34 = ___qtreewidgetitem32.child(1)
        ___qtreewidgetitem34.setText(0, QCoreApplication.translate("MEMainWindow", u"Chain Drives", None));
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem34.setToolTip(0, QCoreApplication.translate("MEMainWindow", u"Chain Drive Module", None));
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem35 = ___qtreewidgetitem32.child(2)
        ___qtreewidgetitem35.setText(0, QCoreApplication.translate("MEMainWindow", u"Gears", None));
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem35.setToolTip(0, QCoreApplication.translate("MEMainWindow", u"Gear List", None));
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem36 = ___qtreewidgetitem35.child(0)
        ___qtreewidgetitem36.setText(0, QCoreApplication.translate("MEMainWindow", u"Gear Driven Shafts", None));
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem36.setToolTip(0, QCoreApplication.translate("MEMainWindow", u"Gear Driven Shafts Module", None));
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem37 = ___qtreewidgetitem35.child(1)
        ___qtreewidgetitem37.setText(0, QCoreApplication.translate("MEMainWindow", u"Gear Trains", None));
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem37.setToolTip(0, QCoreApplication.translate("MEMainWindow", u"Gear Trains Module", None));
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem38 = ___qtreewidgetitem35.child(2)
        ___qtreewidgetitem38.setText(0, QCoreApplication.translate("MEMainWindow", u"Advanced Gear Calculator", None));
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem38.setToolTip(0, QCoreApplication.translate("MEMainWindow", u"Advanced Gear Calculator Module", None));
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem39 = ___qtreewidgetitem31.child(1)
        ___qtreewidgetitem39.setText(0, QCoreApplication.translate("MEMainWindow", u"Bearing Calculator", None));
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem39.setToolTip(0, QCoreApplication.translate("MEMainWindow", u"Bearing Calculator", None));
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem40 = ___qtreewidgetitem31.child(2)
        ___qtreewidgetitem40.setText(0, QCoreApplication.translate("MEMainWindow", u"Key Calculator", None));
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem40.setToolTip(0, QCoreApplication.translate("MEMainWindow", u"Key Calculator Module", None));
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem41 = self.Modulelist.topLevelItem(5)
        ___qtreewidgetitem41.setText(0, QCoreApplication.translate("MEMainWindow", u"Engineering and Drafting", None));
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem41.setToolTip(0, QCoreApplication.translate("MEMainWindow", u"Engineering and Drafting List", None));
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem42 = ___qtreewidgetitem41.child(0)
        ___qtreewidgetitem42.setText(0, QCoreApplication.translate("MEMainWindow", u"GD&T Checker", None));
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem42.setToolTip(0, QCoreApplication.translate("MEMainWindow", u"GD&T Checker Module", None));
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem43 = ___qtreewidgetitem41.child(1)
        ___qtreewidgetitem43.setText(0, QCoreApplication.translate("MEMainWindow", u"Limits and Fits", None));
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem43.setToolTip(0, QCoreApplication.translate("MEMainWindow", u"Limits and Fits Module", None));
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem44 = ___qtreewidgetitem41.child(2)
        ___qtreewidgetitem44.setText(0, QCoreApplication.translate("MEMainWindow", u"Fixed and Floating Fastener Calculator", None));
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem44.setToolTip(0, QCoreApplication.translate("MEMainWindow", u"GD&T Fastener Module", None));
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem45 = ___qtreewidgetitem41.child(3)
        ___qtreewidgetitem45.setText(0, QCoreApplication.translate("MEMainWindow", u"Paper Gauging ", None));
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem45.setToolTip(0, QCoreApplication.translate("MEMainWindow", u"Paper Gauging Module", None));
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem46 = ___qtreewidgetitem41.child(4)
        ___qtreewidgetitem46.setText(0, QCoreApplication.translate("MEMainWindow", u"Tolerance Finder", None));
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem46.setToolTip(0, QCoreApplication.translate("MEMainWindow", u"Tolerance Finder Module", None));
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem47 = ___qtreewidgetitem41.child(5)
        ___qtreewidgetitem47.setText(0, QCoreApplication.translate("MEMainWindow", u"Diameter Deviation", None));
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem47.setToolTip(0, QCoreApplication.translate("MEMainWindow", u"Diameter Deviation Module", None));
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem48 = self.Modulelist.topLevelItem(6)
        ___qtreewidgetitem48.setText(0, QCoreApplication.translate("MEMainWindow", u"Additional Calculators", None));
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem48.setToolTip(0, QCoreApplication.translate("MEMainWindow", u"Additional Calculators List", None));
#endif // QT_CONFIG(tooltip)
        self.Modulelist.setSortingEnabled(__sortingEnabled)

    # retranslateUi

