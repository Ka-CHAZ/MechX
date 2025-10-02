import sys
from PySide6 import QtCore, QtGui, QtWidgets, QtUiTools
from PySide6.QtCore import QCoreApplication, QDate, QDateTime, QRectF, QLocale, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QPointF
from PySide6.QtGui import QAction, QBrush, QColor, QPainterPath, QConicalGradient, QCursor, QFont, QFontDatabase, QGradient, QIcon, QImage, QKeySequence, QLinearGradient, QPainter, QPalette, QPixmap, QRadialGradient, QTransform, QPen, QPolygonF
from PySide6.QtWidgets import QAbstractSpinBox, QGraphicsPathItem, QTreeWidget, QTreeWidgetItem, QMdiSubWindow, QMdiArea, QApplication, QComboBox, QDoubleSpinBox, QPushButton, QDialog, QLineEdit, QMenu, QScrollArea, QGridLayout, QVBoxLayout, QHBoxLayout, QFrame, QGroupBox, QHBoxLayout, QLabel, QMainWindow, QMenu, QMenuBar, QSizePolicy, QMessageBox, QStatusBar, QTabWidget, QVBoxLayout, QWidget, QGraphicsView, QGraphicsScene, QGraphicsRectItem, QDoubleSpinBox, QSpacerItem, QSplitter, QGraphicsTextItem, QGraphicsPolygonItem, QGraphicsEllipseItem, QGraphicsLineItem
import math 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg

from Determinatebeams.Shearandmomentdiagramming_ui import Ui_shearandmomentscalculator

class Determinate_beams(QMainWindow, Ui_shearandmomentscalculator, QAction):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_shearandmomentscalculator()
        self.setupUi(self)
        
        self.setWindowTitle('Determinate Beams')
        
        self.Beamsetuplength.hide()
        self.supportlocation.hide()
        self.Uppntload.hide()
        self.Downpntload.hide()
        self.lineardistribloadup.hide()
        self.lineardistribloaddown.hide()
        self.varibledistribloadup.hide()
        self.varibdistribloaddown.hide()
        self.momentccw.hide()
        self.momentcw.hide()
        self.label_7.hide()
        self.elemetsscrollarea.hide()
        self.label_6.hide()
        self.visualizerlengthunits.hide()
        self.label_6.hide()
        self.loadsscroll.hide()
        self.label_8.hide()
        self.reactionsscroll.hide()
        self.visualizerloadunits.hide()
        self.Switchshearconvention.hide()
        self.visualizermomentunits.hide()
        self.Switchmomentconvention.hide()
        self.label_9.hide()
        self.Loadsdiagram.hide()
        self.Sheargraph.hide()
        self.Momentgraph.hide()
        
        self.Uppntload.clicked.connect(self.add_concenuploads)
        self.Downpntload.clicked.connect(self.add_concendownloads)
        self.lineardistribloadup.clicked.connect(self.add_uniformuploads)
        self.lineardistribloaddown.clicked.connect(self.add_uniformdownloads)
        self.varibledistribloadup.clicked.connect(self.add_lineardistribuploads)
        self.varibdistribloaddown.clicked.connect(self.add_lineardistribdownloads)
        self.momentccw.clicked.connect(self.add_momentccw)
        self.momentcw.clicked.connect(self.add_momentcw)
        
        self.entersetup.clicked.connect(self.readloads)
        self.entersetup.clicked.connect(self._create_linear_load)
        self.entersetup.clicked.connect(self._create_point_load)
        self.entersetup.clicked.connect(self._create_uniform_load)
        self.entersetup.clicked.connect(self._update_linear_load)
        self.entersetup.clicked.connect(self._update_point_load)
        self.entersetup.clicked.connect(self._update_uniform_load)
        self.entersetup.clicked.connect(self._update_moment_load)
        self.entersetup.clicked.connect(self.sheargraph)
        self.entersetup.clicked.connect(self.momentgraph)
        
        self.Beamlength.valueChanged.connect(self.update_beam_length)
        self.beamlengthunits.currentIndexChanged.connect(self.update_beam_length)

        self.leftsupportlocation.valueChanged.connect(self.drawfixedsupports)
        self.leftsupportlocation.valueChanged.connect(self.update_fixedsupports)
        self.rightsupportlocation.valueChanged.connect(self.drawrollersupports)
        self.rightsupportlocation.valueChanged.connect(self.update_rollersupports)

        self.scroll_area = self.elemetsscrollarea
        
        self.scroll_widget = self.scrollAreaWidgetContents
        self.scroll_layout = QVBoxLayout(self.scroll_widget)
        self.scroll_widget.setLayout(self.scroll_layout)
        
        self.loads_scene = QGraphicsScene(self)
        self.Loadsdiagram.setScene(self.loads_scene)
        self.loads_scene.setSceneRect(0, 12.5, 590, 25)
        
        self.load_items = {}  # keeps track of arrows drawn for each load

        self.shear_scene = QGraphicsScene(self)
        self.Sheargraph.setScene(self.shear_scene)

        self.moment_scene = QGraphicsScene(self)
        self.Momentgraph.setScene(self.moment_scene)
        
        self.variablesupports.clicked.connect(self.varsupportsbeam)
        self.lftsidesupport.clicked.connect(self.leftsidebeam)
        self.rtsidesupport.clicked.connect(self.rightsidebeam)

        self.scroll_area.setWidget(self.scroll_widget)
        
        self.cupl_group_box_counter = 0
        self.cdl_group_box_counter = 0
        self.uupl_group_box_counter = 0
        self.udl_group_box_counter = 0
        self.ldupl_group_box_counter = 0
        self.lddl_group_box_counter = 0
        self.mccw_group_box_counter = 0
        self.mcw_group_box_counter = 0
        
        pen = QPen()
        pen.setWidth(2)
        pen.setColor(QColor(180, 180, 180))
        
        pinnedtriangle = QPolygonF([
                QPointF(0, 40),
                QPointF(-15, 65),
                QPointF(+15, 65)
            ])
                
        self.pinnedtriangle = QGraphicsPolygonItem(pinnedtriangle)
        self.pinnedtriangle.setPen(pen)
        self.pinnedtriangle_Visible = False

        self.pinnedsupportline = QGraphicsLineItem(-23, 65, 23, 65)
        self.pinnedsupportline.setPen(pen)
        self.pinnedsupportline_Visible = False

        self.sp1 = QGraphicsLineItem(-15, 65, -21, 73)
        self.sp1.setPen(pen)
        self.sp1_Visible = False
        self.sp2 = QGraphicsLineItem(-6, 65, -12, 73)
        self.sp2.setPen(pen)
        self.sp2_Visible = False
        self.sp3 = QGraphicsLineItem(3, 65, -3, 73)
        self.sp3.setPen(pen)
        self.sp3_Visible = False
        self.sp4 = QGraphicsLineItem(12, 65, 6, 73)
        self.sp4.setPen(pen)
        self.sp4_Visible = False
        self.sp5 = QGraphicsLineItem(21, 65, 15, 73)
        self.sp5.setPen(pen)
        self.sp5_Visible = False

        #roller
        self.rollersupport = QGraphicsEllipseItem(-12.5, 40, 25, 25)
        self.rollersupport.setPen(pen)
        self.rollersupport_Visible = False

        self.rollerline = QGraphicsLineItem(-23, 65, 23, 65)
        self.rollerline.setPen(pen)
        self.rollerline_Visible = False

        self.rsp1 = QGraphicsLineItem(-15, 65, -21, 73)
        self.rsp1.setPen(pen)
        self.rsp1_Visible = False
        self.rsp2 = QGraphicsLineItem(-6, 65, -12, 73)
        self.rsp2.setPen(pen)
        self.rsp2_Visible = False
        self.rsp3 = QGraphicsLineItem(3, 65, -3, 73)
        self.rsp3.setPen(pen)
        self.rsp3_Visible = False
        self.rsp4 = QGraphicsLineItem(12, 65, 6, 73)
        self.rsp4.setPen(pen)
        self.rsp4_Visible = False
        self.rsp5 = QGraphicsLineItem(21, 65, 15, 73)
        self.rsp5.setPen(pen)
        self.rsp5_Visible = False
        
    def _create_moment_symbol(self, radius=75, cw=True, color=QColor("red")):
        from PySide6.QtCore import QRectF, Qt
        from PySide6.QtGui import QPainterPath, QPen, QColor
        from PySide6.QtWidgets import QGraphicsPathItem, QGraphicsLineItem
        import math

        rect = QRectF(-radius, -radius, 2*radius, 2*radius)
        path = QPainterPath()

        if cw:
            start_deg, sweep_deg = 90, -270   # CW: start top, sweep right-down-left
        else:
            start_deg, sweep_deg = 90, 270    # CCW: start top, sweep left-down-right

        path.arcMoveTo(rect, start_deg)
        path.arcTo(rect, start_deg, sweep_deg)

        arc = QGraphicsPathItem(path)
        arc.setPen(QPen(color, 2))

        # Compute arrowhead tip location at end of arc
        end_deg = start_deg + sweep_deg
        theta = math.radians(end_deg)
        tip_x = radius * math.cos(theta)
        tip_y = -radius * math.sin(theta)

        # Tangent direction at arc end
        t_x = -math.sin(theta)
        t_y = -math.cos(theta)
        sign = 1.0 if sweep_deg > 0 else -1.0
        dir_x = sign * t_x
        dir_y = sign * t_y
        norm = math.hypot(dir_x, dir_y) or 1.0
        u_x, u_y = dir_x / norm, dir_y / norm

        # Build arrowhead
        size = 8.0
        back_x, back_y = -u_x * size, -u_y * size
        phi = math.radians(25.0)

        cos_phi, sin_phi = math.cos(phi), math.sin(phi)
        v1_x = back_x * cos_phi - back_y * sin_phi
        v1_y = back_x * sin_phi + back_y * cos_phi
        v2_x = back_x * cos_phi + back_y * sin_phi
        v2_y = -back_x * sin_phi + back_y * cos_phi

        hx1, hy1 = tip_x + v1_x, tip_y + v1_y
        hx2, hy2 = tip_x + v2_x, tip_y + v2_y

        head1 = QGraphicsLineItem(tip_x, tip_y, hx1, hy1)
        head2 = QGraphicsLineItem(tip_x, tip_y, hx2, hy2)

        head1.setPen(QPen(color, 2))
        head2.setPen(QPen(color, 2))

        return arc, head1, head2

    def add_concenuploads(self):
        self.cupl_group_box_counter += 1
        
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setPointSize(12)
        
        elementbox = QGroupBox(f"Concentrated Load p{self.cdl_group_box_counter} [UP]")
        elementbox.setObjectName(u"ConcentratedloadsGBox")
        elementbox.setGeometry(QRect(10, 10, 251, 171))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(elementbox.sizePolicy().hasHeightForWidth())
        elementbox.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(11)
        elementbox.setFont(font)
        elementbox.setCheckable(True)
        self.verticalLayout_8 = QVBoxLayout(elementbox)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel("Load Location\n(x-coordinate)")
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
        self.concenloadlocation = QDoubleSpinBox(elementbox)
        self.concenloadlocation.setObjectName(u"concenloadlocation")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.concenloadlocation.sizePolicy().hasHeightForWidth())
        self.concenloadlocation.setSizePolicy(sizePolicy2)
        self.concenloadlocation.setMinimumSize(QSize(110, 27))
        self.concenloadlocation.setMaximumSize(QSize(100, 27))
        self.concenloadlocation.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.concenloadlocation.setDecimals(3)
        self.concenloadlocation.setMaximum(100000000.000000000000000)
        self.verticalLayout_2.addWidget(self.concenloadlocation)

        self.concenloadlocationunits = QComboBox(elementbox)
        self.concenloadlocationunits.setObjectName(u"concenloadlocationunits")
        sizePolicy2.setHeightForWidth(self.concenloadlocationunits.sizePolicy().hasHeightForWidth())
        self.concenloadlocationunits.setSizePolicy(sizePolicy2)
        self.concenloadlocationunits.setMinimumSize(QSize(110, 27))
        self.concenloadlocationunits.setMaximumSize(QSize(100, 27))
        self.concenloadlocationunits.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.verticalLayout_2.addWidget(self.concenloadlocationunits)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_8.addLayout(self.horizontalLayout_2)

        self.line_4 = QFrame(elementbox)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setLineWidth(2)
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)
        self.verticalLayout_8.addWidget(self.line_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel("Load\nMagnitude")
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setMinimumSize(QSize(97, 0))
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.horizontalLayout_3.addWidget(self.label_3)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.concenloadmagnitude = QDoubleSpinBox(elementbox)
        self.concenloadmagnitude.setObjectName(u"concenloadmagnitude")
        sizePolicy2.setHeightForWidth(self.concenloadmagnitude.sizePolicy().hasHeightForWidth())
        self.concenloadmagnitude.setSizePolicy(sizePolicy2)
        self.concenloadmagnitude.setMinimumSize(QSize(110, 27))
        self.concenloadmagnitude.setMaximumSize(QSize(100, 27))
        self.concenloadmagnitude.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.concenloadmagnitude.setDecimals(3)
        self.concenloadmagnitude.setMaximum(100000000.000000000000000)
        self.verticalLayout_3.addWidget(self.concenloadmagnitude)

        self.concenloadmagnitudeunits = QComboBox(elementbox)
        self.concenloadmagnitudeunits.setObjectName(u"concenloadmagnitudeunits")
        sizePolicy2.setHeightForWidth(self.concenloadmagnitudeunits.sizePolicy().hasHeightForWidth())
        self.concenloadmagnitudeunits.setSizePolicy(sizePolicy2)
        self.concenloadmagnitudeunits.setMinimumSize(QSize(110, 27))
        self.concenloadmagnitudeunits.setMaximumSize(QSize(100, 27))
        self.verticalLayout_3.addWidget(self.concenloadmagnitudeunits)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_8.addLayout(self.horizontalLayout_3)
        
        self.concenloadlocationunits.addItems(["", "mm", "m", "in.", "ft"])
        self.concenloadmagnitudeunits.addItems(["", "N", "kN", "lb", "kip"])
        
        self.scroll_layout.addWidget(elementbox)
        
        elementbox.toggled.connect(lambda checked: self.remove_groupbox(elementbox, checked))
        
    def add_concendownloads(self):
        self.cdl_group_box_counter += 1
        
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setPointSize(12)
        
        elementbox = QGroupBox(f"Concentrated Load p{self.cdl_group_box_counter} [DOWN]")
        elementbox.setObjectName(u"ConcentratedloadsGBox")
        elementbox.setGeometry(QRect(10, 10, 251, 171))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(elementbox.sizePolicy().hasHeightForWidth())
        elementbox.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(11)
        elementbox.setFont(font)
        elementbox.setCheckable(True)
        self.verticalLayout_8 = QVBoxLayout(elementbox)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel("Load Location\n(x-coordinate)")
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
        self.concenloadlocation = QDoubleSpinBox(elementbox)
        self.concenloadlocation.setObjectName(u"concenloadlocation")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.concenloadlocation.sizePolicy().hasHeightForWidth())
        self.concenloadlocation.setSizePolicy(sizePolicy2)
        self.concenloadlocation.setMinimumSize(QSize(110, 27))
        self.concenloadlocation.setMaximumSize(QSize(100, 27))
        self.concenloadlocation.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.concenloadlocation.setDecimals(3)
        self.concenloadlocation.setMaximum(100000000.000000000000000)
        self.verticalLayout_2.addWidget(self.concenloadlocation)

        self.concenloadlocationunits = QComboBox(elementbox)
        self.concenloadlocationunits.setObjectName(u"concenloadlocationunits")
        sizePolicy2.setHeightForWidth(self.concenloadlocationunits.sizePolicy().hasHeightForWidth())
        self.concenloadlocationunits.setSizePolicy(sizePolicy2)
        self.concenloadlocationunits.setMinimumSize(QSize(110, 27))
        self.concenloadlocationunits.setMaximumSize(QSize(100, 27))
        self.concenloadlocationunits.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.verticalLayout_2.addWidget(self.concenloadlocationunits)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_8.addLayout(self.horizontalLayout_2)

        self.line_4 = QFrame(elementbox)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setLineWidth(2)
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)
        self.verticalLayout_8.addWidget(self.line_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel("Load\nMagnitude")
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setMinimumSize(QSize(97, 0))
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.horizontalLayout_3.addWidget(self.label_3)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.concenloadmagnitude = QDoubleSpinBox(elementbox)
        self.concenloadmagnitude.setObjectName(u"concenloadmagnitude")
        sizePolicy2.setHeightForWidth(self.concenloadmagnitude.sizePolicy().hasHeightForWidth())
        self.concenloadmagnitude.setSizePolicy(sizePolicy2)
        self.concenloadmagnitude.setMinimumSize(QSize(110, 27))
        self.concenloadmagnitude.setMaximumSize(QSize(100, 27))
        self.concenloadmagnitude.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.concenloadmagnitude.setDecimals(3)
        self.concenloadmagnitude.setMaximum(100000000.000000000000000)
        self.verticalLayout_3.addWidget(self.concenloadmagnitude)

        self.concenloadmagnitudeunits = QComboBox(elementbox)
        self.concenloadmagnitudeunits.setObjectName(u"concenloadmagnitudeunits")
        sizePolicy2.setHeightForWidth(self.concenloadmagnitudeunits.sizePolicy().hasHeightForWidth())
        self.concenloadmagnitudeunits.setSizePolicy(sizePolicy2)
        self.concenloadmagnitudeunits.setMinimumSize(QSize(110, 27))
        self.concenloadmagnitudeunits.setMaximumSize(QSize(100, 27))
        self.verticalLayout_3.addWidget(self.concenloadmagnitudeunits)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_8.addLayout(self.horizontalLayout_3)
        
        self.concenloadlocationunits.addItems(["", "mm", "m", "in.", "ft"])
        self.concenloadmagnitudeunits.addItems(["", "N", "kN", "lb", "kip"])

        self.scroll_layout.addWidget(elementbox)
        elementbox.toggled.connect(lambda checked: self.remove_groupbox(elementbox, checked))
        
    def add_uniformuploads(self):
        self.uupl_group_box_counter += 1
        
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setPointSize(12)
        
        elementbox = QGroupBox(f"Uniform Load W{self.uupl_group_box_counter} [UP]")
        elementbox.setGeometry(QRect(10, 0, 251, 221))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(elementbox.sizePolicy().hasHeightForWidth())
        elementbox.setSizePolicy(sizePolicy)
        elementbox.setMinimumSize(QSize(251, 221))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(11)
        elementbox.setFont(font)
        elementbox.setCheckable(True)
        self.verticalLayout_9 = QVBoxLayout(elementbox)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_11 = QLabel("Start of Load\n(x-coordinate)")
        self.label_11.setObjectName(u"label_11")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy1)
        self.label_11.setMinimumSize(QSize(110, 0))
        self.label_11.setMaximumSize(QSize(110, 16777215))
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout.addWidget(self.label_11, 0, 0, 1, 1)

        self.label_12 = QLabel("End of Load\n(x-coordinate)")
        self.label_12.setObjectName(u"label_12")
        sizePolicy1.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy1)
        self.label_12.setMinimumSize(QSize(0, 43))
        self.label_12.setMaximumSize(QSize(16777215, 43))
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout.addWidget(self.label_12, 0, 1, 1, 2)

        self.uniformloadstart = QDoubleSpinBox(elementbox)
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

        self.uniformloadend = QDoubleSpinBox(elementbox)
        self.uniformloadend.setObjectName(u"uniformloadend")
        sizePolicy2.setHeightForWidth(self.uniformloadend.sizePolicy().hasHeightForWidth())
        self.uniformloadend.setSizePolicy(sizePolicy2)
        self.uniformloadend.setMinimumSize(QSize(110, 27))
        self.uniformloadend.setMaximumSize(QSize(100, 27))
        self.uniformloadend.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.uniformloadend.setDecimals(3)
        self.uniformloadend.setMaximum(100000000.000000000000000)
        self.gridLayout.addWidget(self.uniformloadend, 1, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(110, 28, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(self.verticalSpacer, 2, 0, 1, 2)
        
        self.uniformloadunits = QComboBox(elementbox)
        self.uniformloadunits.setObjectName(u"uniformloadunits")
        sizePolicy2.setHeightForWidth(self.uniformloadunits.sizePolicy().hasHeightForWidth())
        self.uniformloadunits.setSizePolicy(sizePolicy2)
        self.uniformloadunits.setMinimumSize(QSize(110, 27))
        self.uniformloadunits.setMaximumSize(QSize(100, 27))
        self.gridLayout.addWidget(self.uniformloadunits, 2, 2, 1, 1)
        self.verticalLayout_9.addLayout(self.gridLayout)

        self.line = QFrame(elementbox)
        self.line.setObjectName(u"line")
        self.line.setLineWidth(2)
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.verticalLayout_9.addWidget(self.line)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_13 = QLabel("Load\nMagnitude")
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(100, 0))
        self.label_13.setMaximumSize(QSize(112, 16777215))
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.horizontalLayout_9.addWidget(self.label_13)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.uniformloadmagnitude = QDoubleSpinBox(elementbox)
        self.uniformloadmagnitude.setObjectName(u"uniformloadmagnitude")
        sizePolicy2.setHeightForWidth(self.uniformloadmagnitude.sizePolicy().hasHeightForWidth())
        self.uniformloadmagnitude.setSizePolicy(sizePolicy2)
        self.uniformloadmagnitude.setMinimumSize(QSize(110, 27))
        self.uniformloadmagnitude.setMaximumSize(QSize(100, 27))
        self.uniformloadmagnitude.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.uniformloadmagnitude.setDecimals(3)
        self.uniformloadmagnitude.setMaximum(100000000.000000000000000)
        self.verticalLayout_14.addWidget(self.uniformloadmagnitude)

        self.uniformloadmagnitudunits = QComboBox(elementbox)
        self.uniformloadmagnitudunits.setObjectName(u"uniformloadmagnitudunits")
        sizePolicy2.setHeightForWidth(self.uniformloadmagnitudunits.sizePolicy().hasHeightForWidth())
        self.uniformloadmagnitudunits.setSizePolicy(sizePolicy2)
        self.uniformloadmagnitudunits.setMinimumSize(QSize(110, 27))
        self.uniformloadmagnitudunits.setMaximumSize(QSize(100, 27))
        self.verticalLayout_14.addWidget(self.uniformloadmagnitudunits)
        self.horizontalLayout_9.addLayout(self.verticalLayout_14)
        self.verticalLayout_9.addLayout(self.horizontalLayout_9)
        
        self.uniformloadunits.addItems(["", "mm", "m", "in.", "ft"])
        self.uniformloadmagnitudunits.addItems(["", "N", "kN", "lb", "kip"])

        self.scroll_layout.addWidget(elementbox)
        elementbox.toggled.connect(lambda checked: self.remove_groupbox(elementbox, checked))
        
    def add_uniformdownloads(self):
        self.udl_group_box_counter += 1
        
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setPointSize(12)
        
        elementbox = QGroupBox(f"Uniform Load w{self.udl_group_box_counter} [DOWN]")
        elementbox.setGeometry(QRect(10, 0, 251, 221))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(elementbox.sizePolicy().hasHeightForWidth())
        elementbox.setSizePolicy(sizePolicy)
        elementbox.setMinimumSize(QSize(251, 221))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(11)
        elementbox.setFont(font)
        elementbox.setCheckable(True)
        self.verticalLayout_9 = QVBoxLayout(elementbox)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_11 = QLabel("Start of Load\n(x-coordinate)")
        self.label_11.setObjectName(u"label_11")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy1)
        self.label_11.setMinimumSize(QSize(110, 0))
        self.label_11.setMaximumSize(QSize(110, 16777215))
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout.addWidget(self.label_11, 0, 0, 1, 1)

        self.label_12 = QLabel("End of Load\n(x-coordinate)")
        self.label_12.setObjectName(u"label_12")
        sizePolicy1.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy1)
        self.label_12.setMinimumSize(QSize(0, 43))
        self.label_12.setMaximumSize(QSize(16777215, 43))
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout.addWidget(self.label_12, 0, 1, 1, 2)

        self.uniformloadstart = QDoubleSpinBox(elementbox)
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

        self.uniformloadend = QDoubleSpinBox(elementbox)
        self.uniformloadend.setObjectName(u"uniformloadend")
        sizePolicy2.setHeightForWidth(self.uniformloadend.sizePolicy().hasHeightForWidth())
        self.uniformloadend.setSizePolicy(sizePolicy2)
        self.uniformloadend.setMinimumSize(QSize(110, 27))
        self.uniformloadend.setMaximumSize(QSize(100, 27))
        self.uniformloadend.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.uniformloadend.setDecimals(3)
        self.uniformloadend.setMaximum(100000000.000000000000000)
        self.gridLayout.addWidget(self.uniformloadend, 1, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(110, 28, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(self.verticalSpacer, 2, 0, 1, 2)
        
        self.uniformloadunits = QComboBox(elementbox)
        self.uniformloadunits.setObjectName(u"uniformloadunits")
        sizePolicy2.setHeightForWidth(self.uniformloadunits.sizePolicy().hasHeightForWidth())
        self.uniformloadunits.setSizePolicy(sizePolicy2)
        self.uniformloadunits.setMinimumSize(QSize(110, 27))
        self.uniformloadunits.setMaximumSize(QSize(100, 27))
        self.gridLayout.addWidget(self.uniformloadunits, 2, 2, 1, 1)
        self.verticalLayout_9.addLayout(self.gridLayout)

        self.line = QFrame(elementbox)
        self.line.setObjectName(u"line")
        self.line.setLineWidth(2)
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.verticalLayout_9.addWidget(self.line)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_13 = QLabel("Load\nMagnitude")
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(100, 0))
        self.label_13.setMaximumSize(QSize(112, 16777215))
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.horizontalLayout_9.addWidget(self.label_13)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.uniformloadmagnitude = QDoubleSpinBox(elementbox)
        self.uniformloadmagnitude.setObjectName(u"uniformloadmagnitude")
        sizePolicy2.setHeightForWidth(self.uniformloadmagnitude.sizePolicy().hasHeightForWidth())
        self.uniformloadmagnitude.setSizePolicy(sizePolicy2)
        self.uniformloadmagnitude.setMinimumSize(QSize(110, 27))
        self.uniformloadmagnitude.setMaximumSize(QSize(100, 27))
        self.uniformloadmagnitude.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.uniformloadmagnitude.setDecimals(3)
        self.uniformloadmagnitude.setMaximum(100000000.000000000000000)
        self.verticalLayout_14.addWidget(self.uniformloadmagnitude)

        self.uniformloadmagnitudunits = QComboBox(elementbox)
        self.uniformloadmagnitudunits.setObjectName(u"uniformloadmagnitudunits")
        sizePolicy2.setHeightForWidth(self.uniformloadmagnitudunits.sizePolicy().hasHeightForWidth())
        self.uniformloadmagnitudunits.setSizePolicy(sizePolicy2)
        self.uniformloadmagnitudunits.setMinimumSize(QSize(110, 27))
        self.uniformloadmagnitudunits.setMaximumSize(QSize(100, 27))
        self.verticalLayout_14.addWidget(self.uniformloadmagnitudunits)
        self.horizontalLayout_9.addLayout(self.verticalLayout_14)
        self.verticalLayout_9.addLayout(self.horizontalLayout_9)
        
        self.uniformloadunits.addItems(["", "mm", "m", "in.", "ft"])
        self.uniformloadmagnitudunits.addItems(["", "N", "kN", "lb", "kip"])
        
        self.scroll_layout.addWidget(elementbox)
        elementbox.toggled.connect(lambda checked: self.remove_groupbox(elementbox, checked))
        
    def add_lineardistribuploads(self):
        self.ldupl_group_box_counter += 1
        
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setPointSize(12)
        
        elementbox = QGroupBox(f"Linear Distributed Load Q{self.ldupl_group_box_counter} [UP]")
        elementbox.setGeometry(QRect(10, 10, 251, 255))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(elementbox.sizePolicy().hasHeightForWidth())
        elementbox.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(11)
        elementbox.setFont(font)
        elementbox.setCheckable(True)
        self.verticalLayout_10 = QVBoxLayout(elementbox)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_15 = QLabel("Start of Load\n(x-coordinate)")
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(110, 0))
        self.label_15.setMaximumSize(QSize(10, 16777215))
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout.addWidget(self.label_15, 0, 0, 1, 1)

        self.label_16 = QLabel("End of Load\n(x-coordinate)")
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(110, 0))
        self.label_16.setMaximumSize(QSize(10, 16777215))
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout.addWidget(self.label_16, 0, 1, 1, 1)

        self.lineardistribloadstart = QDoubleSpinBox(elementbox)
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

        self.lineardistribloadend = QDoubleSpinBox(elementbox)
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

        self.lineardistribloadunits = QComboBox(elementbox)
        self.lineardistribloadunits.setObjectName(u"lineardistribloadunits")
        sizePolicy1.setHeightForWidth(self.lineardistribloadunits.sizePolicy().hasHeightForWidth())
        self.lineardistribloadunits.setSizePolicy(sizePolicy1)
        self.lineardistribloadunits.setMinimumSize(QSize(110, 27))
        self.lineardistribloadunits.setMaximumSize(QSize(100, 27))
        self.gridLayout.addWidget(self.lineardistribloadunits, 2, 1, 1, 1)
        self.verticalLayout_10.addLayout(self.gridLayout)

        self.line_3 = QFrame(elementbox)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setLineWidth(2)
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.verticalLayout_10.addWidget(self.line_3)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_14 = QLabel("Load\nMagnitude")
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
        self.label_17 = QLabel("Start")
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_20.addWidget(self.label_17)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.lineardistribloadmagnitudestart = QDoubleSpinBox(elementbox)
        self.lineardistribloadmagnitudestart.setObjectName(u"lineardistribloadmagnitudestart")
        sizePolicy1.setHeightForWidth(self.lineardistribloadmagnitudestart.sizePolicy().hasHeightForWidth())
        self.lineardistribloadmagnitudestart.setSizePolicy(sizePolicy1)
        self.lineardistribloadmagnitudestart.setMinimumSize(QSize(70, 27))
        self.lineardistribloadmagnitudestart.setMaximumSize(QSize(70, 27))
        self.lineardistribloadmagnitudestart.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.lineardistribloadmagnitudestart.setDecimals(3)
        self.lineardistribloadmagnitudestart.setMaximum(100000000.000000000000000)
        self.verticalLayout_15.addWidget(self.lineardistribloadmagnitudestart)

        self.lineardistribloadmagnitudunits = QComboBox(elementbox)
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
        self.label_18 = QLabel("End")
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_19.addWidget(self.label_18)

        self.lineardistribloadmagnitudeend = QDoubleSpinBox(elementbox)
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
        
        self.lineardistribloadunits.addItems(["", "mm", "m", "in.", "ft"])
        self.lineardistribloadmagnitudunits.addItems(["", "N", "kN", "lb", "kip"])
        
        self.scroll_layout.addWidget(elementbox)
        elementbox.toggled.connect(lambda checked: self.remove_groupbox(elementbox, checked))
        
    def add_lineardistribdownloads(self):
        self.lddl_group_box_counter += 1
        
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setPointSize(12)
        
        elementbox = QGroupBox(f"Linear Distributed Load q{self.lddl_group_box_counter} [DOWN]")
        elementbox.setGeometry(QRect(10, 10, 251, 255))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(elementbox.sizePolicy().hasHeightForWidth())
        elementbox.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(11)
        elementbox.setFont(font)
        elementbox.setCheckable(True)
        self.verticalLayout_10 = QVBoxLayout(elementbox)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_15 = QLabel("Start of Load\n(x-coordinate)")
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(110, 0))
        self.label_15.setMaximumSize(QSize(10, 16777215))
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout.addWidget(self.label_15, 0, 0, 1, 1)

        self.label_16 = QLabel("End of Load\n(x-coordinate)")
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(110, 0))
        self.label_16.setMaximumSize(QSize(10, 16777215))
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout.addWidget(self.label_16, 0, 1, 1, 1)

        self.lineardistribloadstart = QDoubleSpinBox(elementbox)
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

        self.lineardistribloadend = QDoubleSpinBox(elementbox)
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

        self.lineardistribloadunits = QComboBox(elementbox)
        self.lineardistribloadunits.setObjectName(u"lineardistribloadunits")
        sizePolicy1.setHeightForWidth(self.lineardistribloadunits.sizePolicy().hasHeightForWidth())
        self.lineardistribloadunits.setSizePolicy(sizePolicy1)
        self.lineardistribloadunits.setMinimumSize(QSize(110, 27))
        self.lineardistribloadunits.setMaximumSize(QSize(100, 27))
        self.gridLayout.addWidget(self.lineardistribloadunits, 2, 1, 1, 1)
        self.verticalLayout_10.addLayout(self.gridLayout)

        self.line_3 = QFrame(elementbox)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setLineWidth(2)
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.verticalLayout_10.addWidget(self.line_3)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_14 = QLabel("Load\nMagnitude")
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
        self.label_17 = QLabel("Start")
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_20.addWidget(self.label_17)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.lineardistribloadmagnitudestart = QDoubleSpinBox(elementbox)
        self.lineardistribloadmagnitudestart.setObjectName(u"lineardistribloadmagnitudestart")
        sizePolicy1.setHeightForWidth(self.lineardistribloadmagnitudestart.sizePolicy().hasHeightForWidth())
        self.lineardistribloadmagnitudestart.setSizePolicy(sizePolicy1)
        self.lineardistribloadmagnitudestart.setMinimumSize(QSize(70, 27))
        self.lineardistribloadmagnitudestart.setMaximumSize(QSize(70, 27))
        self.lineardistribloadmagnitudestart.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.lineardistribloadmagnitudestart.setDecimals(3)
        self.lineardistribloadmagnitudestart.setMaximum(100000000.000000000000000)
        self.verticalLayout_15.addWidget(self.lineardistribloadmagnitudestart)

        self.lineardistribloadmagnitudunits = QComboBox(elementbox)
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
        self.label_18 = QLabel("End")
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_19.addWidget(self.label_18)

        self.lineardistribloadmagnitudeend = QDoubleSpinBox(elementbox)
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
        
        self.lineardistribloadunits.addItems(["", "mm", "m", "in.", "ft"])
        self.lineardistribloadmagnitudunits.addItems(["", "N", "kN", "lb", "kip"])
        
        self.scroll_layout.addWidget(elementbox)
        elementbox.toggled.connect(lambda checked: self.remove_groupbox(elementbox, checked))
        
    def add_momentccw(self):
        self.mccw_group_box_counter += 1
        
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setPointSize(12)

        elementbox = QGroupBox(f"Concentrated Moment M{self.mccw_group_box_counter} [CCW]")
        elementbox.setGeometry(QRect(10, 10, 251, 171))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(elementbox.sizePolicy().hasHeightForWidth())
        elementbox.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(11)
        elementbox.setFont(font)
        elementbox.setCheckable(True)
        self.verticalLayout_7 = QVBoxLayout(elementbox)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_19 = QLabel("Moment\nLocation\n(x-coordinate)")
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
        self.momentlocation = QDoubleSpinBox(elementbox)
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

        self.momentlocationunits = QComboBox(elementbox)
        self.momentlocationunits.setObjectName(u"momentlocationunits")
        sizePolicy2.setHeightForWidth(self.momentlocationunits.sizePolicy().hasHeightForWidth())
        self.momentlocationunits.setSizePolicy(sizePolicy2)
        self.momentlocationunits.setMinimumSize(QSize(110, 27))
        self.momentlocationunits.setMaximumSize(QSize(100, 27))
        self.verticalLayout_21.addWidget(self.momentlocationunits)
        self.horizontalLayout_12.addLayout(self.verticalLayout_21)
        self.verticalLayout_7.addLayout(self.horizontalLayout_12)

        self.line_2 = QFrame(elementbox)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.verticalLayout_7.addWidget(self.line_2)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_20 = QLabel("Moment\nMagnitude")
        self.label_20.setObjectName(u"label_20")
        sizePolicy1.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy1)
        self.label_20.setMinimumSize(QSize(0, 0))
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.horizontalLayout_13.addWidget(self.label_20)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.momentmagnitude = QDoubleSpinBox(elementbox)
        self.momentmagnitude.setObjectName(u"momentmagnitude")
        sizePolicy2.setHeightForWidth(self.momentmagnitude.sizePolicy().hasHeightForWidth())
        self.momentmagnitude.setSizePolicy(sizePolicy2)
        self.momentmagnitude.setMinimumSize(QSize(110, 27))
        self.momentmagnitude.setMaximumSize(QSize(100, 27))
        self.momentmagnitude.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.momentmagnitude.setDecimals(3)
        self.momentmagnitude.setMaximum(100000000.000000000000000)
        self.verticalLayout_22.addWidget(self.momentmagnitude)

        self.momentmagnitudeunits = QComboBox(elementbox)
        self.momentmagnitudeunits.setObjectName(u"momentmagnitudeunits")
        sizePolicy2.setHeightForWidth(self.momentmagnitudeunits.sizePolicy().hasHeightForWidth())
        self.momentmagnitudeunits.setSizePolicy(sizePolicy2)
        self.momentmagnitudeunits.setMinimumSize(QSize(110, 27))
        self.momentmagnitudeunits.setMaximumSize(QSize(100, 27))
        self.verticalLayout_22.addWidget(self.momentmagnitudeunits)
        self.horizontalLayout_13.addLayout(self.verticalLayout_22)
        self.verticalLayout_7.addLayout(self.horizontalLayout_13)
        
        self.momentlocationunits.addItems(["", "mm", "m", "in.", "ft"])
        self.momentmagnitudeunits.addItems(["", "N-m", "N-mm", "kN-m", "kN-mm", "lb-in.", "lb-ft", "kip-in.", "kip-ft"])
        
        self.scroll_layout.addWidget(elementbox)
        elementbox.toggled.connect(lambda checked: self.remove_groupbox(elementbox, checked))

    def add_momentcw(self):
        self.mcw_group_box_counter += 1
    
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setPointSize(12)

        elementbox = QGroupBox(f"Concentrated Moment m{self.mcw_group_box_counter} [CW]")
        elementbox.setGeometry(QRect(10, 10, 251, 171))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(elementbox.sizePolicy().hasHeightForWidth())
        elementbox.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(11)
        elementbox.setFont(font)
        elementbox.setCheckable(True)
        self.verticalLayout_7 = QVBoxLayout(elementbox)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_19 = QLabel("Moment\nLocation\n(x-coordinate)")
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
        self.momentlocation = QDoubleSpinBox(elementbox)
        self.momentlocation.setObjectName(u"momentlocation")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.momentlocation.sizePolicy().hasHeightForWidth())
        self.momentlocation.setSizePolicy(sizePolicy2)
        self.momentlocation.setMinimumSize(QSize(110, 27))
        self.momentlocation.setMaximumSize(QSize(100, 27))
        self.momentlocation.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.momentlocation.setMaximum(100000000.000000000000000)
        self.verticalLayout_21.addWidget(self.momentlocation)

        self.momentlocationunits = QComboBox(elementbox)
        self.momentlocationunits.setObjectName(u"momentlocationunits")
        sizePolicy2.setHeightForWidth(self.momentlocationunits.sizePolicy().hasHeightForWidth())
        self.momentlocationunits.setSizePolicy(sizePolicy2)
        self.momentlocationunits.setMinimumSize(QSize(110, 27))
        self.momentlocationunits.setMaximumSize(QSize(100, 27))
        self.verticalLayout_21.addWidget(self.momentlocationunits)
        self.horizontalLayout_12.addLayout(self.verticalLayout_21)
        self.verticalLayout_7.addLayout(self.horizontalLayout_12)

        self.line_2 = QFrame(elementbox)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.verticalLayout_7.addWidget(self.line_2)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_20 = QLabel("Moment\nMagnitude")
        self.label_20.setObjectName(u"label_20")
        sizePolicy1.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy1)
        self.label_20.setMinimumSize(QSize(0, 0))
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.horizontalLayout_13.addWidget(self.label_20)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.momentmagnitude = QDoubleSpinBox(elementbox)
        self.momentmagnitude.setObjectName(u"momentmagnitude")
        sizePolicy2.setHeightForWidth(self.momentmagnitude.sizePolicy().hasHeightForWidth())
        self.momentmagnitude.setSizePolicy(sizePolicy2)
        self.momentmagnitude.setMinimumSize(QSize(110, 27))
        self.momentmagnitude.setMaximumSize(QSize(100, 27))
        self.momentmagnitude.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.momentmagnitude.setMaximum(100000000.000000000000000)
        self.verticalLayout_22.addWidget(self.momentmagnitude)

        self.momentmagnitudeunits = QComboBox(elementbox)
        self.momentmagnitudeunits.setObjectName(u"momentmagnitudeunits")
        sizePolicy2.setHeightForWidth(self.momentmagnitudeunits.sizePolicy().hasHeightForWidth())
        self.momentmagnitudeunits.setSizePolicy(sizePolicy2)
        self.momentmagnitudeunits.setMinimumSize(QSize(110, 27))
        self.momentmagnitudeunits.setMaximumSize(QSize(100, 27))
        self.verticalLayout_22.addWidget(self.momentmagnitudeunits)
        self.horizontalLayout_13.addLayout(self.verticalLayout_22)
        self.verticalLayout_7.addLayout(self.horizontalLayout_13)
        
        self.momentlocationunits.addItems(["", "mm", "m", "in.", "ft"])
        self.momentmagnitudeunits.addItems(["", "N-m", "N-mm", "kN-m", "kN-mm", "lb-in.", "lb-ft", "kip-in.", "kip-ft"])
        
        self.scroll_layout.addWidget(elementbox)
        elementbox.toggled.connect(lambda checked: self.remove_groupbox(elementbox, checked))
    
    def remove_groupbox(self, elementbox, checked):
        #Removes the group box when unchecked.
        if not checked:
            self.scroll_layout.removeWidget(elementbox)
            # remove graphics if present
            if elementbox in self.load_items:
                for it in self.load_items[elementbox].get("items", []):
                    # each entry may contain triplets or a list-of-tuples
                    if isinstance(it, tuple) or isinstance(it, list):
                        for sub in it:
                            try:
                                self.loads_scene.removeItem(sub)
                            except Exception:
                                pass
                    else:
                        try:
                            self.loads_scene.removeItem(it)
                        except Exception:
                            pass
                del self.load_items[elementbox]
            elementbox.deleteLater()
    
    def readloads(self):
        self.ensure_load_graphics()   # make sure graphics exist and signals are connected
        
        for i in range(self.scroll_layout.count()):
            group_box = self.scroll_layout.itemAt(i).widget()
            if isinstance(group_box, QGroupBox):
                print(f"GroupBox Name: {group_box.title()}")
                
                # Read DoubleSpinBox values
                for spin_box in group_box.findChildren(QDoubleSpinBox):
                    print(f"  {spin_box.objectName()} value: {spin_box.value()}")
                
                # Read ComboBox values and items
                for combo_box in group_box.findChildren(QComboBox):
                    print(f"  {combo_box.objectName()} selected: {combo_box.currentText()}")
                
                print()
        
    def varsupportsbeam(self):
        self.current_beamscene = 1
        
        # Clear the scene before drawing
        self.loads_scene.clear()
        self.Beamlength.clear()
        self.beamlengthunits.setCurrentIndex(0)
        self.leftsupportlocation.clear()
        self.rightsupportlocation.clear()

        # Create a rectangle item
        pen = QPen()
        pen.setWidth(1)
        pen.setColor(QColor("black"))
        
        pen2 = QPen()
        pen2.setWidth(3)
        pen2.setColor(QColor("white"))
        
        rect_item = QGraphicsRectItem(0, 0, 590, 40)
        rect_item.setPen(pen)
        rect_item.setBrush(QtGui.QBrush(QtGui.QColor(100, 100, 100)))  # Set color

        # Add the rectangle to the scene
        self.loads_scene.addItem(rect_item)
        
        self.text_item = QGraphicsTextItem()
        self.loads_scene.addItem(self.text_item)

        #Show the elements of the beam setup
        if self.Beamsetuplength.isHidden():
            self.Beamsetuplength.setVisible(not self.Beamsetuplength.isVisible())
        if self.supportlocation.isHidden():
            self.supportlocation.setVisible(not self.supportlocation.isVisible())
        if self.Uppntload.isHidden():
            self.Uppntload.setVisible(not self.Uppntload.isVisible())
        if self.Downpntload.isHidden():
            self.Downpntload.setVisible(not self.Downpntload.isVisible())
        if self.lineardistribloadup.isHidden():
            self.lineardistribloadup.setVisible(not self.lineardistribloadup.isVisible())
        if self.lineardistribloaddown.isHidden():
            self.lineardistribloaddown.setVisible(not self.lineardistribloaddown.isVisible())
        if self.varibledistribloadup.isHidden():
            self.varibledistribloadup.setVisible(not self.varibledistribloadup.isVisible())
        if self.varibdistribloaddown.isHidden():
            self.varibdistribloaddown.setVisible(not self.varibdistribloaddown.isVisible())
        if self.momentccw.isHidden():
            self.momentccw.setVisible(not self.momentccw.isVisible())
        if self.momentcw.isHidden():
            self.momentcw.setVisible(not self.momentcw.isVisible())
        if self.label_7.isHidden():
            self.label_7.setVisible(not self.label_7.isVisible())
        if self.elemetsscrollarea.isHidden():
            self.elemetsscrollarea.setVisible(not self.elemetsscrollarea.isVisible())
        if self.label_6.isHidden():
            self.label_6.setVisible(not self.label_6.isVisible())
        if self.visualizerlengthunits.isHidden():
            self.visualizerlengthunits.setVisible(not self.visualizerlengthunits.isVisible())
        if self.loadsscroll.isHidden():
            self.loadsscroll.setVisible(not self.loadsscroll.isVisible())
        if self.label_8.isHidden():
            self.label_8.setVisible(not self.label_8.isVisible())
        if self.reactionsscroll.isHidden():
            self.reactionsscroll.setVisible(not self.reactionsscroll.isVisible())
        if self.visualizerloadunits.isHidden():
            self.visualizerloadunits.setVisible(not self.visualizerloadunits.isVisible())
        if self.Switchshearconvention.isHidden():
            self.Switchshearconvention.setVisible(not self.Switchshearconvention.isVisible())
        if self.visualizermomentunits.isHidden():
            self.visualizermomentunits.setVisible(not self.visualizermomentunits.isVisible())
        if self.Switchmomentconvention.isHidden():
            self.Switchmomentconvention.setVisible(not self.Switchmomentconvention.isVisible())
        if self.label_9.isHidden():
            self.label_9.setVisible(not self.label_9.isVisible())
        if self.Loadsdiagram.isHidden():
            self.Loadsdiagram.setVisible(not self.Loadsdiagram.isVisible())
        if self.Sheargraph.isHidden():
            self.Sheargraph.setVisible(not self.Sheargraph.isVisible())
        if self.Momentgraph.isHidden():
            self.Momentgraph.setVisible(not self.Momentgraph.isVisible())
    
    def leftsidebeam(self):
        self.current_beamscene = 2
        
        # Clear the scene before drawing
        self.loads_scene.clear()
        self.Beamlength.clear()
        self.beamlengthunits.setCurrentIndex(0)

        # Create a rectangle item
        pen = QPen()
        pen.setWidth(2)
        pen.setColor(QColor("black"))
        
        pen2 = QPen()
        pen2.setWidth(3)
        pen2.setColor(QColor("white"))
        
        rect_item = QGraphicsRectItem(0, 0, 590, 40)
        rect_item.setPen(pen)
        rect_item.setBrush(QtGui.QBrush(QtGui.QColor(100, 100, 100)))  # Set color

        line = self.loads_scene.addLine(-3, -50, -3, 100, pen2)
        s1 = self.loads_scene.addLine(-4, -35, -15, -27, pen2)
        s3 = self.loads_scene.addLine(-4, -5, -15, 3, pen2)
        s5 = self.loads_scene.addLine(-4, 25, -15, 33, pen2)
        s7 = self.loads_scene.addLine(-4, 55, -15, 63, pen2)
        s7 = self.loads_scene.addLine(-4, 85, -15, 93, pen2)

        # Add the rectangle to the scene
        self.loads_scene.addItem(rect_item)

        self.text_item = QGraphicsTextItem()
        self.loads_scene.addItem(self.text_item)

        #Show the elements of the beam setup
        if self.Beamsetuplength.isHidden():
            self.Beamsetuplength.setVisible(not self.Beamsetuplength.isVisible())
        if self.supportlocation.isVisible():
            self.supportlocation.setHidden(not self.supportlocation.isHidden())
        if self.Uppntload.isHidden():
            self.Uppntload.setVisible(not self.Uppntload.isVisible())
        if self.Downpntload.isHidden():
            self.Downpntload.setVisible(not self.Downpntload.isVisible())
        if self.lineardistribloadup.isHidden():
            self.lineardistribloadup.setVisible(not self.lineardistribloadup.isVisible())
        if self.lineardistribloaddown.isHidden():
            self.lineardistribloaddown.setVisible(not self.lineardistribloaddown.isVisible())
        if self.varibledistribloadup.isHidden():
            self.varibledistribloadup.setVisible(not self.varibledistribloadup.isVisible())
        if self.varibdistribloaddown.isHidden():
            self.varibdistribloaddown.setVisible(not self.varibdistribloaddown.isVisible())
        if self.momentccw.isHidden():
            self.momentccw.setVisible(not self.momentccw.isVisible())
        if self.momentcw.isHidden():
            self.momentcw.setVisible(not self.momentcw.isVisible())
        if self.label_7.isHidden():
            self.label_7.setVisible(not self.label_7.isVisible())
        if self.elemetsscrollarea.isHidden():
            self.elemetsscrollarea.setVisible(not self.elemetsscrollarea.isVisible())
        if self.label_6.isHidden():
            self.label_6.setVisible(not self.label_6.isVisible())
        if self.visualizerlengthunits.isHidden():
            self.visualizerlengthunits.setVisible(not self.visualizerlengthunits.isVisible())
        if self.loadsscroll.isHidden():
            self.loadsscroll.setVisible(not self.loadsscroll.isVisible())
        if self.label_8.isHidden():
            self.label_8.setVisible(not self.label_8.isVisible())
        if self.reactionsscroll.isHidden():
            self.reactionsscroll.setVisible(not self.reactionsscroll.isVisible())
        if self.visualizerloadunits.isHidden():
            self.visualizerloadunits.setVisible(not self.visualizerloadunits.isVisible())
        if self.Switchshearconvention.isHidden():
            self.Switchshearconvention.setVisible(not self.Switchshearconvention.isVisible())
        if self.visualizermomentunits.isHidden():
            self.visualizermomentunits.setVisible(not self.visualizermomentunits.isVisible())
        if self.Switchmomentconvention.isHidden():
            self.Switchmomentconvention.setVisible(not self.Switchmomentconvention.isVisible())
        if self.label_9.isHidden():
            self.label_9.setVisible(not self.label_9.isVisible())
        if self.Loadsdiagram.isHidden():
            self.Loadsdiagram.setVisible(not self.Loadsdiagram.isVisible())
        if self.Sheargraph.isHidden():
            self.Sheargraph.setVisible(not self.Sheargraph.isVisible())
        if self.Momentgraph.isHidden():
            self.Momentgraph.setVisible(not self.Momentgraph.isVisible())
        
    def rightsidebeam(self):
        self.current_beamscene = 3
        
        # Clear the scene before drawing
        self.loads_scene.clear()
        self.Beamlength.clear()
        self.beamlengthunits.setCurrentIndex(0)

        # Create a rectangle item
        pen = QPen()
        pen.setWidth(1)
        pen.setColor(QColor("black"))
        
        pen2 = QPen()
        pen2.setWidth(3)
        pen2.setColor(QColor("white"))
        
        rect_item = QGraphicsRectItem(0, 0, 590, 40)
        rect_item.setPen(pen)
        rect_item.setBrush(QtGui.QBrush(QtGui.QColor(100, 100, 100)))  # Set color

        line = self.loads_scene.addLine(593, -50, 593, 100, pen2)
        s1 = self.loads_scene.addLine(594, -35, 605, -27, pen2)
        s3 = self.loads_scene.addLine(594, -5, 605, 3, pen2)
        s5 = self.loads_scene.addLine(594, 25, 605, 33, pen2)
        s7 = self.loads_scene.addLine(594, 55, 605, 63, pen2)
        s7 = self.loads_scene.addLine(594, 85, 605, 93, pen2)

        # Add the rectangle to the scene
        self.loads_scene.addItem(rect_item)

        self.text_item = QGraphicsTextItem()
        self.loads_scene.addItem(self.text_item)

        #Show the elements of the beam setup
        if self.Beamsetuplength.isHidden():
            self.Beamsetuplength.setVisible(not self.Beamsetuplength.isVisible())
        if self.supportlocation.isVisible():
            self.supportlocation.setHidden(not self.supportlocation.isHidden())
        if self.Uppntload.isHidden():
            self.Uppntload.setVisible(not self.Uppntload.isVisible())
        if self.Downpntload.isHidden():
            self.Downpntload.setVisible(not self.Downpntload.isVisible())
        if self.lineardistribloadup.isHidden():
            self.lineardistribloadup.setVisible(not self.lineardistribloadup.isVisible())
        if self.lineardistribloaddown.isHidden():
            self.lineardistribloaddown.setVisible(not self.lineardistribloaddown.isVisible())
        if self.varibledistribloadup.isHidden():
            self.varibledistribloadup.setVisible(not self.varibledistribloadup.isVisible())
        if self.varibdistribloaddown.isHidden():
            self.varibdistribloaddown.setVisible(not self.varibdistribloaddown.isVisible())
        if self.momentccw.isHidden():
            self.momentccw.setVisible(not self.momentccw.isVisible())
        if self.momentcw.isHidden():
            self.momentcw.setVisible(not self.momentcw.isVisible())
        if self.label_7.isHidden():
            self.label_7.setVisible(not self.label_7.isVisible())
        if self.elemetsscrollarea.isHidden():
            self.elemetsscrollarea.setVisible(not self.elemetsscrollarea.isVisible())
        if self.label_6.isHidden():
            self.label_6.setVisible(not self.label_6.isVisible())
        if self.visualizerlengthunits.isHidden():
            self.visualizerlengthunits.setVisible(not self.visualizerlengthunits.isVisible())
        if self.loadsscroll.isHidden():
            self.loadsscroll.setVisible(not self.loadsscroll.isVisible())
        if self.label_8.isHidden():
            self.label_8.setVisible(not self.label_8.isVisible())
        if self.reactionsscroll.isHidden():
            self.reactionsscroll.setVisible(not self.reactionsscroll.isVisible())
        if self.visualizerloadunits.isHidden():
            self.visualizerloadunits.setVisible(not self.visualizerloadunits.isVisible())
        if self.Switchshearconvention.isHidden():
            self.Switchshearconvention.setVisible(not self.Switchshearconvention.isVisible())
        if self.visualizermomentunits.isHidden():
            self.visualizermomentunits.setVisible(not self.visualizermomentunits.isVisible())
        if self.Switchmomentconvention.isHidden():
            self.Switchmomentconvention.setVisible(not self.Switchmomentconvention.isVisible())
        if self.label_9.isHidden():
            self.label_9.setVisible(not self.label_9.isVisible())
        if self.Loadsdiagram.isHidden():
            self.Loadsdiagram.setVisible(not self.Loadsdiagram.isVisible())
        if self.Sheargraph.isHidden():
            self.Sheargraph.setVisible(not self.Sheargraph.isVisible())
        if self.Momentgraph.isHidden():
            self.Momentgraph.setVisible(not self.Momentgraph.isVisible())
    
    def update_beam_length(self):
        # Get the length from the line edit and update the beam length
        beamlength = self.Beamlength.value()
        units = self.beamlengthunits.currentText()
        current_beamscene = self.current_beamscene
        
        pen = QPen()
        pen.setWidth(1)
        pen.setColor(QColor(85, 85, 85))

        if beamlength and units:
            try:
                beamlength = float(beamlength)
                print(f"Beam length set to: {beamlength} {units}")

                line = self.loads_scene.addLine(590, -65, 590, 115, pen)
                line2 = self.loads_scene.addLine(0, -65, 0, 115, pen)

                if current_beamscene == 1 or current_beamscene == 2:
                    length_text = self.text_item.setPlainText(f"{beamlength} {units}")
                    self.text_item.setFont(QFont("Arial", 12))
                    self.text_item.setPos(525, -90)  # Adjust position as needed
                    self.text_item.setDefaultTextColor(QColor(255, 255, 255))  # Set text color to white
                elif current_beamscene == 3:
                    length_text = self.text_item.setPlainText(f"{beamlength} {units}")
                    self.text_item.setFont(QFont("Arial", 12))
                    self.text_item.setPos(-25, -90)  # Adjust position as needed
                    self.text_item.setDefaultTextColor(QColor(255, 255, 255))  # Set text color to white
                
            except ValueError:
                print("Invalid length value")
    
    def drawfixedsupports(self):
        beamlength = self.Beamlength.value()
        pinnedlocation = self.leftsupportlocation.value()
        fixedsupportpixellocation = 590*pinnedlocation
        self.fixedsupportpixellocation = fixedsupportpixellocation
        self.beamlength = beamlength

        print(f"calculated pinned location: {(fixedsupportpixellocation/beamlength)}")
        
        if not self.pinnedtriangle_Visible:
            self.loads_scene.addItem(self.pinnedtriangle)
            self.pinnedtriangle.setPos((fixedsupportpixellocation/beamlength), 0)
            self.pinnedtriangle_Visible = True
        
        if not self.pinnedsupportline_Visible:
            self.loads_scene.addItem(self.pinnedsupportline)
            self.pinnedsupportline.setPos((fixedsupportpixellocation/beamlength), 0)
            self.pinnedsupportline_Visible = True
        
        if not self.sp1_Visible:
            self.loads_scene.addItem(self.sp1)
            self.sp1.setPos((fixedsupportpixellocation/beamlength), 0)
            self.sp1_Visible = True

        if not self.sp2_Visible:
            self.loads_scene.addItem(self.sp2)
            self.sp2.setPos((fixedsupportpixellocation/beamlength), 0)
            self.sp2_Visible = True

        if not self.sp3_Visible:
            self.loads_scene.addItem(self.sp3)
            self.sp3.setPos((fixedsupportpixellocation/beamlength), 0)
            self.sp3_Visible = True

        if not self.sp4_Visible:
            self.loads_scene.addItem(self.sp4)
            self.sp4.setPos((fixedsupportpixellocation/beamlength), 0)
            self.sp4_Visible = True

        if not self.sp5_Visible:
            self.loads_scene.addItem(self.sp5)
            self.sp5.setPos((fixedsupportpixellocation/beamlength), 0)
            self.sp5_Visible = True
    
    def drawrollersupports(self):
        #Roller support
        beamlength = self.Beamlength.value()
        rollerlocation = self.rightsupportlocation.value()
        rollersupportpixellocation = 590*rollerlocation
        self.rollersupportpixellocation = rollersupportpixellocation
        self.beamlength = beamlength

        if not self.rollersupport_Visible:
            self.loads_scene.addItem(self.rollersupport)
            self.rollersupport.setPos((rollersupportpixellocation/beamlength), 0)
            self.rollersupport_Visible = True

        if not self.rollerline_Visible:
            self.loads_scene.addItem(self.rollerline)
            self.rollerline.setPos((rollersupportpixellocation/beamlength), 0)
            self.rollerline_Visible = True
        
        if not self.rsp1_Visible:
            self.loads_scene.addItem(self.rsp1)
            self.rsp1.setPos(((rollersupportpixellocation/beamlength)), 0)
            self.rsp1_Visible = True

        if not self.rsp2_Visible:
            self.loads_scene.addItem(self.rsp2)
            self.rsp2.setPos(((rollersupportpixellocation/beamlength)), 0)
            self.rsp2_Visible = True

        if not self.rsp3_Visible:
            self.loads_scene.addItem(self.rsp3)
            self.rsp3.setPos(((rollersupportpixellocation/beamlength)), 0)
            self.rsp3_Visible = True

        if not self.rsp4_Visible:
            self.loads_scene.addItem(self.rsp4)
            self.rsp4.setPos(((rollersupportpixellocation/beamlength)), 0)
            self.rsp4_Visible = True

        if not self.rsp5_Visible:
            self.loads_scene.addItem(self.rsp5)
            self.rsp5.setPos(((rollersupportpixellocation/beamlength)), 0)
            self.rsp5_Visible = True

    def update_fixedsupports(self):
        if self.pinnedtriangle_Visible:
            self.pinnedtriangle.setPos(self.fixedsupportpixellocation/self.beamlength, 0)
        
        if self.pinnedsupportline_Visible:
            self.pinnedsupportline.setPos(self.fixedsupportpixellocation/self.beamlength, 0)

        if self.sp1_Visible:
            self.sp1.setPos(self.fixedsupportpixellocation/self.beamlength, 0)
        
        if self.sp2_Visible:
            self.sp2.setPos(self.fixedsupportpixellocation/self.beamlength, 0) 
        if self.sp3_Visible:
            self.sp3.setPos(self.fixedsupportpixellocation/self.beamlength, 0)
        if self.sp4_Visible:
            self.sp4.setPos(self.fixedsupportpixellocation/self.beamlength, 0)
        if self.sp5_Visible:
            self.sp5.setPos(self.fixedsupportpixellocation/self.beamlength, 0)
    
    def update_rollersupports(self):
        #Roller support
        if self.rollersupport_Visible:
            self.rollersupport.setPos(self.rollersupportpixellocation/self.beamlength, 0)
        
        if self.rollerline_Visible:
            self.rollerline.setPos(self.rollersupportpixellocation/self.beamlength, 0)
            
        if self.rsp1_Visible:
            self.rsp1.setPos((self.rollersupportpixellocation/self.beamlength), 0)
        if self.rsp2_Visible:
            self.rsp2.setPos((self.rollersupportpixellocation/self.beamlength), 0)
        if self.rsp3_Visible:
            self.rsp3.setPos((self.rollersupportpixellocation/self.beamlength), 0)
        if self.rsp4_Visible:
            self.rsp4.setPos((self.rollersupportpixellocation/self.beamlength), 0)
        if self.rsp5_Visible:
            self.rsp5.setPos((self.rollersupportpixellocation/self.beamlength), 0)

    def _find_spin(self, group_box, name_substr):
        for sb in group_box.findChildren(QDoubleSpinBox):
            nm = sb.objectName() or ""
            if name_substr in nm:
                return sb
        children = group_box.findChildren(QDoubleSpinBox)
        return children[0] if children else None

    def _find_combo(self, group_box, name_substr):
        for c in group_box.findChildren(QComboBox):
            nm = c.objectName() or ""
            if name_substr in nm:
                return c
        children = group_box.findChildren(QComboBox)
        return children[0] if children else None
    
    # conversion factors to meters
    _UNIT_TO_M = {
    "m": 1.0,
    "mm": 0.001,
    "in.": 0.0254,
    "ft": 0.3048,
    }

    DEBUG_UNITS = True  # set False to disable unit debug prints

    def convert_to_beam_units(self, value: float, from_unit: str, to_unit: str = None) -> float:
        """
        Convert 'value' from from_unit → to_unit (beam unit).
        Units supported: m, mm, in., ft
        """
        if to_unit is None:
            to_unit = self.beamlengthunits.currentText()

        if from_unit not in self._UNIT_TO_M or to_unit not in self._UNIT_TO_M:
            if self.DEBUG_UNITS:
                print(f"[LoadsUnitConv] Unknown unit: from={from_unit}, to={to_unit}, value={value}")
            return value

        value_m = value * self._UNIT_TO_M[from_unit]      # → meters
        result = value_m / self._UNIT_TO_M[to_unit]       # → beam units

        if self.DEBUG_UNITS:
            print(f"[LoadsUnitConv] {value} {from_unit} → {result:.4f} {to_unit}")

        return result
    # ---------- ensure graphics exist for each load discovered ----------
    def ensure_load_graphics(self):
        """Create persistent graphics for any newly-added groupboxes."""
        for i in range(self.scroll_layout.count()):
            item = self.scroll_layout.itemAt(i)
            if item is None:
                continue
            group_box = item.widget()
            # Defensive check: skip non-QGroupBox items (spacers etc.)
            if not isinstance(group_box, QGroupBox):
                continue

            if group_box in self.load_items:
                continue

            title = (group_box.title() or "").lower()
            if "concentrated load" in title:
                self._create_point_load(group_box)
            elif "uniform load" in title or "uniform" in title:
                self._create_uniform_load(group_box)
            elif "linear distributed" in title or "lineardistrib" in title:
                self._create_linear_load(group_box)
            elif "concentrated moment" in title or "moment" in title:
                self._create_moment_load(group_box)

    # ---------- create + update for point loads ----------
    def _create_point_load(self, group_box):
        if not isinstance(group_box, QGroupBox):
            return
        title = (group_box.title() or "").lower()
        pen = QPen(QColor("#233AA3"), 2) if "[down]" in title else QPen(QColor("#233AA3"), 2)

        # create trunk + two head lines with trivial geometry; update will set actual lines
        trunk = self.loads_scene.addLine(0, 0, 0, 1, pen)
        head1 = self.loads_scene.addLine(0, 0, 0, 0, pen)
        head2 = self.loads_scene.addLine(0, 0, 0, 0, pen)

        self.load_items[group_box] = {"type": "point", "items": [trunk, head1, head2]}

        # connect the location spinbox safely (capture group_box as default arg)
        loc_sb = self._find_spin(group_box, "concenloadlocation")
        if loc_sb:
            loc_sb.valueChanged.connect(lambda _, gb=group_box: self.update_load(gb))

        # initial placement
        self._update_point_load(group_box)

    def _update_point_load(self, group_box):
        entry = self.load_items.get(group_box)
        if not entry or entry.get("type") != "point":
            return

        loc_sb = self._find_spin(group_box, "concenloadlocation")
        unit_cb = self._find_combo(group_box, "concenloadlocationunits")
        if not loc_sb or not unit_cb:
            return

        loc_val = loc_sb.value()
        loc_unit = unit_cb.currentText()
        beam_unit = self.beamlengthunits.currentText()

        loc_beam = self.convert_to_beam_units(loc_val, loc_unit, beam_unit)

        beamlength = max(1.0, self.Beamlength.value())
        scale = 590.0 / beamlength
        x = loc_beam * scale

        down = "[down]" in (group_box.title() or "").lower()
        L = 50 if down else -50

        trunk, head1, head2 = entry["items"]

        # offset for downward arrows so they don't overlay beam
        y_offset = -50 if down else 0
        trunk.setLine(0, 0, 0, L)
        trunk.setPos(x, y_offset)

        if down:
            head1.setLine(0, L, -5, L - 10)
            head2.setLine(0, L, 5, L - 10)
        else:
            head1.setLine(0, L, -5, L + 10)
            head2.setLine(0, L, 5, L + 10)

        head1.setPos(x, y_offset)
        head2.setPos(x, y_offset)

    # ---------- create + update for uniform loads ----------
    def _create_uniform_load(self, group_box):
        if not isinstance(group_box, QGroupBox):
            return
        title = (group_box.title() or "").lower()
        pen = QPen(QColor("#233AA3"), 1) if "[down]" in title else QPen(QColor("#233AA3"), 1)

        arrows = []
        max_arrows = 20
        for _ in range(max_arrows):
            trunk = self.loads_scene.addLine(0, 0, 0, 30, pen)
            head1 = self.loads_scene.addLine(0, 30, -4, 22, pen)
            head2 = self.loads_scene.addLine(0, 30, 4, 22, pen)
            arrows.append((trunk, head1, head2))

        self.load_items[group_box] = {"type": "uniform", "items": arrows}

        start_sb = self._find_spin(group_box, "uniformloadstart")
        end_sb = self._find_spin(group_box, "uniformloadend")
        if start_sb:
            start_sb.valueChanged.connect(lambda _, gb=group_box: self.update_load(gb))
        if end_sb:
            end_sb.valueChanged.connect(lambda _, gb=group_box: self.update_load(gb))

        self._update_uniform_load(group_box)

    def _update_uniform_load(self, group_box):
        entry = self.load_items.get(group_box)
        if not entry or entry.get("type") != "uniform":
            return

        start_sb = self._find_spin(group_box, "uniformloadstart")
        end_sb = self._find_spin(group_box, "uniformloadend")
        unit_cb = self._find_combo(group_box, "uniformloadunits")
        if not start_sb or not end_sb or not unit_cb:
            return

        beam_unit = self.beamlengthunits.currentText()
        start_beam = self.convert_to_beam_units(start_sb.value(), unit_cb.currentText(), beam_unit)
        end_beam = self.convert_to_beam_units(end_sb.value(), unit_cb.currentText(), beam_unit)

        beamlength = max(1.0, self.Beamlength.value())
        scale = 590.0 / beamlength
        x1 = start_beam * scale
        x2 = end_beam * scale
        if x2 < x1:
            x1, x2 = x2, x1

        # closer spacing
        step_px = 15

        arrows = entry["items"]
        used = 0
        down = "[down]" in (group_box.title() or "").lower()

        for x in range(int(x1), int(x2) + 1, step_px):
            if used >= len(arrows):
                break
            trunk, head1, head2 = arrows[used]
            if down:
                trunk.setLine(0, 0, 0, 30)
                head1.setLine(0, 30, -4, 22)
                head2.setLine(0, 30, 4, 22)
                trunk.setPos(x, -30)  # small upward offset
                head1.setPos(x, -30)
                head2.setPos(x, -30)
            else:
                trunk.setLine(0, 0, 0, -30)
                head1.setLine(0, -30, -4, -22)
                head2.setLine(0, -30, 4, -22)
                trunk.setPos(x, 0)
                head1.setPos(x, 0)
                head2.setPos(x, 0)
            used += 1

        for idx in range(used, len(arrows)):
            trunk, head1, head2 = arrows[idx]
            trunk.setPos(-9999, -9999)
            head1.setPos(-9999, -9999)
            head2.setPos(-9999, -9999)
        
    # ---------- create + update for linear (graded) distributed loads ----------
    def _create_linear_load(self, group_box):
        if not isinstance(group_box, QGroupBox):
            return
        title = (group_box.title() or "").lower()
        pen = QPen(QColor("#233AA3"), 1) if "[down]" in title else QPen(QColor("#233AA3"), 1)

        arrows = []
        max_arrows = 20
        for _ in range(max_arrows):
            trunk = self.loads_scene.addLine(0, 0, 0, 1, pen)
            head1 = self.loads_scene.addLine(0, 1, -3, -7, pen)
            head2 = self.loads_scene.addLine(0, 1, 3, -7, pen)
            arrows.append((trunk, head1, head2))

        self.load_items[group_box] = {"type": "linear", "items": arrows}

        for name in ("lineardistribloadstart", "lineardistribloadend",
                    "lineardistribloadmagnitudestart", "lineardistribloadmagnitudeend"):
            sb = self._find_spin(group_box, name)
            if sb:
                sb.valueChanged.connect(lambda _, gb=group_box: self.update_load(gb))

        self._update_linear_load(group_box)

    def _update_linear_load(self, group_box):
        entry = self.load_items.get(group_box)
        if not entry or entry.get("type") != "linear":
            return

        start_sb = self._find_spin(group_box, "lineardistribloadstart")
        end_sb = self._find_spin(group_box, "lineardistribloadend")
        mag1_sb = self._find_spin(group_box, "lineardistribloadmagnitude")
        mag2_sb = self._find_spin(group_box, "lineardistribloadmagnitudeend")
        length_unit_cb = self._find_combo(group_box, "lineardistribloadstartunit")
        if not (start_sb and end_sb and mag1_sb and mag2_sb and length_unit_cb):
            return

        # convert start/end to beam units
        beam_unit = self.beamlengthunits.currentText()
        start_beam = self.convert_to_beam_units(start_sb.value(), length_unit_cb.currentText(), beam_unit)
        end_beam = self.convert_to_beam_units(end_sb.value(), length_unit_cb.currentText(), beam_unit)

        beamlength = max(1.0, self.Beamlength.value())
        scale = 590.0 / beamlength
        x1 = start_beam * scale
        x2 = end_beam * scale
        if x2 < x1:
            x1, x2 = x2, x1

        m1 = mag1_sb.value()
        m2 = mag2_sb.value()

        steps = 15
        arrows = entry["items"]
        used = 0
        down = "[down]" in (group_box.title() or "").lower()

        max_mag = max(abs(m1), abs(m2), 1.0)

        for j in range(steps + 1):
            if used >= len(arrows):
                break
            t = j / float(steps)
            x = x1 + (x2 - x1) * t
            mag = m1 + (m2 - m1) * t
            mag_norm = abs(mag) / max_mag
            length_px = mag_norm * 30  # scale length

            trunk, head1, head2 = arrows[used]

            if down:
                # --- Downwards arrows: keep heads in-line ---
                head_y = 30
                tail_y = head_y - length_px
                trunk.setLine(0, tail_y, 0, head_y)
                head1.setLine(0, head_y, -3, head_y - 8)
                head2.setLine(0, head_y, 3, head_y - 8)
                y_offset = -30
                trunk.setPos(x, y_offset)
                head1.setPos(x, y_offset)
                head2.setPos(x, y_offset)

            else:
                # --- Upwards arrows: tails in-line at beam, heads slanted ---
                tail_y = 0  # all tails sit on the beam
                head_y = -length_px
                trunk.setLine(0, tail_y, 0, head_y)
                head1.setLine(0, head_y, -3, head_y + 8)
                head2.setLine(0, head_y, 3, head_y + 8)
                y_offset = 0
                trunk.setPos(x, y_offset)
                head1.setPos(x, y_offset)
                head2.setPos(x, y_offset)

            used += 1

        # hide unused
        for idx in range(used, len(arrows)):
            trunk, head1, head2 = arrows[idx]
            trunk.setPos(-9999, -9999)
            head1.setPos(-9999, -9999)
            head2.setPos(-9999, -9999)
            
    def _create_moment_load(self, group_box):
        """
        Create (and register) a moment symbol for the given group_box.
        Direction (CW/CCW) is detected from the groupbox title.
        """
        if not isinstance(group_box, QGroupBox):
            return

        title = (group_box.title() or "").lower()
        # default to CW unless title contains 'ccw'
        cw = "ccw" not in title

        # create symbol (arc + two head lines)
        arc, head1, head2 = self._create_moment_symbol(radius=25, cw=cw)

        # add to scene
        # Use same scene you use elsewhere for loads (Loadsdiagram.scene())
        self.Loadsdiagram.scene().addItem(arc)
        self.Loadsdiagram.scene().addItem(head1)
        self.Loadsdiagram.scene().addItem(head2)

        # store items + direction flag
        self.load_items[group_box] = {
            "type": "moment",
            "items": (arc, head1, head2),
            "cw": cw
        }

        # connect updates (spin and units)
        loc_sb = self._find_spin(group_box, "momentlocation")
        unit_cb = self._find_combo(group_box, "momentlocationunits")  # note plural matches UI
        if loc_sb:
            loc_sb.valueChanged.connect(lambda _, gb=group_box: self.update_load(gb))
        if unit_cb:
            unit_cb.currentIndexChanged.connect(lambda _, gb=group_box: self.update_load(gb))

        # initial update/position
        self._update_moment_load(group_box)
        
    def _update_moment_load(self, group_box):
        """
        Update the moment graphic position for group_box.
        Fallbacks:
        - if groupbox unit combobox isn't found, treat input as beam units
        - if something missing, exit gracefully
        """
        entry = self.load_items.get(group_box)
        if not entry or entry.get("type") != "moment":
            return

        arc, head1, head2 = entry["items"]
        cw = entry.get("cw", True)

        # get location spinbox (required)
        loc_sb = self._find_spin(group_box, "momentlocation")
        if not loc_sb:
            return

        # try to find the unit combobox inside the groupbox (note: UI uses 'momentlocationunits')
        unit_cb = self._find_combo(group_box, "momentlocationunits")  # plural
        # if not found, assume the value is already in beam units
        if unit_cb:
            loc_unit = unit_cb.currentText()
        else:
            loc_unit = self.beamlengthunits.currentText()

        loc_val = loc_sb.value()
        beam_unit = self.beamlengthunits.currentText()

        # Convert to beam units (convert_to_beam_units handles unknown units gracefully)
        loc_beam = self.convert_to_beam_units(loc_val, loc_unit, beam_unit)

        # pixel scale (same approach used elsewhere)
        beamlength = max(1.0, self.Beamlength.value())
        scale = 590.0 / beamlength
        x = loc_beam * scale

        # Move whole symbol together (offset so it doesn't overlap beam)
        y_offset = 20
        arc.setPos(x, y_offset)
        head1.setPos(x, y_offset)
        head2.setPos(x, y_offset)
            
    # ---------- dispatcher to ensure items exist and update a single groupbox ----------
    def update_load(self, group_box):
        # defensive: ignore accidental boolean or other wrong args
        if not isinstance(group_box, QGroupBox):
            return

        # ensure items exist first
        if group_box not in self.load_items:
            self.ensure_load_graphics()

        entry = self.load_items.get(group_box)
        if not entry:
            return

        t = entry.get("type")
        if t == "point":
            self._update_point_load(group_box)
        elif t == "uniform":
            self._update_uniform_load(group_box)
        elif t == "linear":
            self._update_linear_load(group_box)
        elif t == "moment":
            self._update_moment_load(group_box)

    def sheargraph(self):
        import numpy as np
        from matplotlib.backends.backend_agg import FigureCanvasAgg

        beam_length = self.Beamlength.value()  # fallback if not set
        x = np.linspace(0, beam_length, 200)
        y = np.sin(x)  # replace with real shear values

        plt.style.use("dark_background")

        view_size = self.Sheargraph.viewport().size()
        dpi = 100
        fig_w = max(1, (view_size.width() - 5) / dpi)
        fig_h = max(1, (view_size.height() - 5) / dpi)

        fig, ax = plt.subplots(figsize=(fig_w, fig_h), dpi=dpi, facecolor="#202020")
        ax.set_facecolor("#202020")

        # Plot shear force
        ax.plot(x, y, color="deepskyblue", linewidth=2)

        # Axis formatting
        ax.axhline(0, color="gray", linewidth=2.5)  # thickened axis line
        ax.axvline(0, color="gray", linewidth=2.5)  # thickened axis line
        ax.axvline(self.leftsupportlocation.value(), color="#DD7f21", linestyle="--", linewidth=1.5)  # left support
        ax.axvline(self.rightsupportlocation.value(), color="#DD7f21", linestyle="--", linewidth=1.5)  # right support
        ax.set_title("Shear Force Diagram", color="white")
        ax.set_xlabel(f"Beam Length ({self.beamlengthunits.currentText()})", color="white")
        ax.set_ylabel("Shear (V)", color="white")
        ax.set_xlim(0, beam_length)

        ax.tick_params(colors="white")
        ax.grid(True, color="gray", alpha=0.5)

        fig.tight_layout(pad=0.2)

        # Render to QImage
        canvas = FigureCanvasAgg(fig)
        canvas.draw()
        buf = canvas.buffer_rgba()
        width, height = canvas.get_width_height()
        image = QtGui.QImage(buf, width, height, QtGui.QImage.Format_RGBA8888)

        # Update graphics scene
        self.shear_scene.clear()
        pixmap = QtGui.QPixmap.fromImage(image)
        item = self.shear_scene.addPixmap(pixmap)
        self.shear_scene.setSceneRect(item.boundingRect())

        self.Sheargraph.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Sheargraph.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Sheargraph.fitInView(self.shear_scene.sceneRect(), Qt.KeepAspectRatio)

        plt.close(fig)


    def momentgraph(self):
        import numpy as np
        from matplotlib.backends.backend_agg import FigureCanvasAgg

        beam_length = self.Beamlength.value()  # fallback if not set
        x = np.linspace(0, beam_length, 200)
        y = -np.cos(x)  # replace with real moment values

        plt.style.use("dark_background")

        view_size = self.Momentgraph.viewport().size()
        dpi = 100
        fig_w = max(1, (view_size.width() - 5) / dpi)
        fig_h = max(1, (view_size.height() - 5) / dpi)

        fig, ax = plt.subplots(figsize=(fig_w, fig_h), dpi=dpi, facecolor="#202020")
        ax.set_facecolor("#202020")

        # Plot moment diagram
        ax.plot(x, y, color="orangered", linewidth=2)

        # Axis formatting
        ax.axhline(0, color="gray", linewidth=2.5)  # thickened axis line
        ax.axvline(0, color="gray", linewidth=2.5)  # thickened axis line
        ax.axvline(self.leftsupportlocation.value(), color="#DD7f21", linestyle="--", linewidth=1.5)  # left support
        ax.axvline(self.rightsupportlocation.value(), color="#DD7f21", linestyle="--", linewidth=1.5)  # right support
        ax.set_title("Moment Diagram", color="white")
        ax.set_xlabel(f"Beam Length ({self.beamlengthunits.currentText()})", color="white")
        ax.set_ylabel("Moment (M)", color="white")
        ax.set_xlim(0, beam_length)

        ax.tick_params(colors="white")
        ax.grid(True, color="gray", alpha=0.5)

        fig.tight_layout(pad=0.2)

        canvas = FigureCanvasAgg(fig)
        canvas.draw()
        buf = canvas.buffer_rgba()
        width, height = canvas.get_width_height()
        image = QtGui.QImage(buf, width, height, QtGui.QImage.Format_RGBA8888)

        self.moment_scene.clear()
        pixmap = QtGui.QPixmap.fromImage(image)
        item = self.moment_scene.addPixmap(pixmap)
        self.moment_scene.setSceneRect(item.boundingRect())

        self.Momentgraph.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Momentgraph.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Momentgraph.fitInView(self.moment_scene.sceneRect(), Qt.KeepAspectRatio)

        plt.close(fig)