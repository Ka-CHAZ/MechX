import sys
from PySide6 import QtCore, QtGui, QtWidgets, QtUiTools
from PySide6.QtCore import QCoreApplication, QDate, QDateTime, QLocale, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt
from PySide6.QtGui import QAction, QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QGradient, QIcon, QImage, QKeySequence, QLinearGradient, QPainter, QPalette, QPixmap, QRadialGradient, QTransform, QPen
from PySide6.QtWidgets import QAbstractSpinBox, QTreeWidget, QTreeWidgetItem, QMdiSubWindow, QMdiArea, QApplication, QComboBox, QDoubleSpinBox, QPushButton, QDialog, QLineEdit, QMenu, QScrollArea, QGridLayout, QVBoxLayout, QHBoxLayout, QFrame, QGroupBox, QHBoxLayout, QLabel, QMainWindow, QMenu, QMenuBar, QSizePolicy, QMessageBox, QStatusBar, QTabWidget, QVBoxLayout, QWidget, QGraphicsView, QGraphicsScene, QGraphicsRectItem, QDoubleSpinBox, QSpacerItem, QSplitter
import math 

from Modules.UnitConverter.UnitConverter_ui import Ui_UnitConverter

class Unit_Converter(QMainWindow, Ui_UnitConverter, QPushButton, QAction):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_UnitConverter()
        self.setupUi(self)
        
        self.setWindowTitle('Unit Converter')
        
        self.unitstyle.clear()
        
        self.unitstyle.addItems(["","Standard Converters", "Fluids", "Electricity"])
        
        self.unitstyle.currentTextChanged.connect(self.update_unit_plane)
        self.unitstyle.currentTextChanged.connect(self.update_unit_sub_cat)
        self.unitstyle.currentTextChanged.connect(self.update_units_from)
        self.unitstyle.currentTextChanged.connect(self.update_units_to)
        self.NUMunit_input.valueChanged.connect(self.unit_convert)
    
    def lock_subwindow_size(sub_window: QMdiSubWindow, widget: QWidget):
        widget.adjustSize()
        size = widget.size()
        sub_window.setMinimumSize(size)
        sub_window.setMaximumSize(size)
        
    def update_unit_plane(self):
        
        style = self.unitstyle.currentText()
        
        self.unitplane.clear()
        
        if style == "Standard Converters":
            self.unitplane.addItems(["Linear Units", "Angular Units"])
        if style == "Fluids":
            self.unitplane.addItems([""])
        if style == "Electricity":
            self.unitplane.addItems([""])

        self.unitplane.currentTextChanged.connect(self.update_unit_sub_cat)
        self.unitplane.currentTextChanged.connect(self.update_units_from)
        self.unitplane.currentTextChanged.connect(self.update_units_to)
        
    def update_unit_sub_cat(self):
        
        style = self.unitstyle.currentText()
        plane = self.unitplane.currentText()
        
        self.unitsubcat.clear()
        
        if style == "Standard Converters" and plane == "Linear Units":
            self.unitsubcat.addItems(["Length and Distance", "Area", "Volume", "Velocity and Speed", "Acceleration", "Force", "Torque", "Moment of Inertia", "Mass and Weight", "Density", "Time", "Temperature", "Energy", "Pressure", "Power"])
        if style == "Standard Converters" and plane == "Angular Units":
            self.unitsubcat.addItems(["Plane Angle", "Angular Velocity", "Angular Acceleration"])
        if style == "Fluids" and plane == "":
            self.unitsubcat.addItems(["Volume", "Volume - Dry", "Specific Volume", "Flow", "Viscosity (Dynamic)", "Viscosity (Kinematic)", "Surface Tension"])
        if style == "Electricity" and plane == "":
            self.unitsubcat.addItems(["Electrical Charge", "Electric Potential (Voltage)", "Current", "Resistance", "Capacitance", "Inductance", "Conductance"])
        
        self.unitsubcat.currentTextChanged.connect(self.update_units_from)
        self.unitsubcat.currentTextChanged.connect(self.update_units_to)
    
    def update_units_from(self):
        
        style = self.unitstyle.currentText()
        plane = self.unitplane.currentText()
        subcat = self.unitsubcat.currentText()
        
        self.units_from.clear()
        #units from standard linear converter units
        if style == "Standard Converters" and plane == "Linear Units" and subcat == "Length and Distance":
            self.units_from.addItems(["Meter [m]", "Kilometer [km]", "Centimeter [cm]", "Millimeter [mm]", "Micrometer [μm, μ]", "Nanometer [nm]", "Mile [mi, mi (int.)]", "Yard [yd]", "Foot [ft]", "Inch [in]", "Light Year [ly]", "Gigameter [Gm]", "Megameter [Mm]", "Micron [μ]", "Megaparsec [Mpc]", "Kiloparsec [kpc]", "Parsec [pc]", "Astronomical Unit [AU, UA]", "League [lea]", "Nautical League (UK)", "Nautical League (int)", "League (statute) [st.league]", "Nautical Mile (UK) [NM (UK)]", "Nautical Mile (international)", "Mile (statute) [mi, mi(US)]", "Mile (US survey) [mi]", "Mile (Roman)", "Kiloyard [kyd]", "Furlong [fur]", "Furlong (US survey) [fur]", "Chain [ch]", "Chain (US survey) [ch]", "Rope", "Rod [rd]", "Rod (US survey) [rd]", "Perch", "Pole", "Fathom [fath]", "Fathom (US survey) [fath]", "Ell", "Foot (US survey) [ft]", "Link [li]", "Link (US survey) [li]", "Cubit (UK)", "Hand", "Span (cloth)", "Finger (cloth)", "Nail (cloth)", "Inch (US survey) [in]", "Barleycorn", "mil [mil, thou]", "Microinch", "Angstrom [A]", "a.u. of length [a.u., b]", "X-unit [X]", "Fermi [F, f]", "Arpent", "Pica", "Point", "Twip", "Aln", "Famn", "Caliber [cl]", "Centiinch [cin]", "Ken", "Long Reed", "Reed", "Plank Length", "Electron Radius (classical)", "Bohr Radius [b, a.u.]", "Earth's Equitorial Radius", "Earth's Polar Radius", "Earth's Distance From the Sun", "Sun's Radius"])
        if style == "Standard Converters" and plane == "Linear Units" and subcat == "Area":
            self.units_from.addItems(["Square Meter [m\u00b2]", "Square Kilometer [km\u00b2]", "Square Centimeter [cm\u00b2]", "Square Millimeter [mm\u00b2]", "Square Micrometer [μm\u00b2]", "Hectare [ha]", "Acre [ac]", "Square Mile [mi\u00b2]", "Square Yard [yd\u00b2]", "Square Foot [ft\u00b2]", "Square Inch [in\u00b2]", "Are [a]", "Barn [b]", "Square Mile (US survey)", "Square Foot (US survey)", "Circular Inch", "Township", "Section", "Acre (US survey) [ac]", "Rood", "Square Chain [ch\u00b2]", "Square Rod", "Square Rod (US Survey)", "Square Perch", "Square Pole", "Square Mil [mil\u00b2]", "Circular Mil", "Homestead", "Electron Cross Section"])
        if style == "Standard Converters" and plane == "Linear Units" and subcat == "Volume":
            self.units_from.addItems(["Cubic Meter [m\u00b3]", "Cubic Kilometer [km\u00b3]", "Cubic Centimeter [cm\u00b3]", "Cubic Millimeter [mm\u00b3]", "Liter [L, l]", "Milliliter [mL]", "Gallon (US) [gal (US)]", "Quart (US) [qt (US)]", "Pint (US) [pt (US)]", "Cup (US)", "Tablespoon (US)", "Teaspoon (US)", "Cubic Mile [mi\u00b3]", "Cubic Yard [yd\u00b3]", "Cubic Foot [ft\u00b3]", "Cubic Inch [in\u00b3]", "Gigaliter [GL]", "Megaliter [ML]", "Kiloliter [kL]", "CC [cc, cm\u00b3]", "Drop", "Barrel (oil) [bbl (oil)]", "Barrel (US) [bbl (US)]", "Barrel (UK) [bbl (UK)]", "Gallon (UK) [gal (UK)]", "Quart (UK) [qt (UK)]", "Pint (UK) [pt (UK)]", "Cup (metric)", "Cup (UK)", "Fluid Ounce (US) [fl oz (US)]", "Fluid Ounce (UK) [fl oz (UK)]", "Tablespoon (metric)", "Tablespoon (UK)", "Dessertspoon (US)", "Dessertspoon (UK)", "Teaspoon (metric)", "Teaspoon (UK)", "Gil (US) [gi]", "Gil (UK) [gi (UK)]", "Minim (US)", "Minim (UK)", "Ton Register [ton reg]", "ccf", "Hundred-cubic foot", "Acre-foot [ac*ft]", "Acre-foot (US survey)", "Acre-inch [ac*in]", "Dekastere", "Stere [st]", "Decistere", "Cord [cd]", "Tun", "Hogshead", "Board foot", "Dram [dr]", "Earth's Volume"])
        if style == "Standard Converters" and plane == "Linear Units" and subcat == "Velocity and Speed":
            self.units_from.addItems(["Meter/Hour [m/hr]", "Meter/Minute [m/min]", "Meter/Second [m/sec]", "Kilometer/Hour [km/hr, KPH]", "Kilometer/Minute [km/min]", "Kilometer/Second [km/sec]", "Centimeter/Hour [cm/hr]", "Centimeter/Minute [cm/min]", "Centimeter/Second [cm/sec]", "Millimeter/Hour [mm/hr]", "Millimeter/Minute [mm/min]", "Millimeter/Second [mm/sec]", "Mile/Hour [mi/hr, MPH]", "Mile/Minute [mi/min]", "Mile/Second [mi/sec]", "Yard/Hour [yd/hr]", "Yard/Minute [yd/min]", "Yard/Second [yd/sec]", "Foot/Hour [ft/hr]", "Foot/Minute [ft/min, FPM]", "Foot/Second [ft/sec, FPS]", "Knot [kt, kn]", "Knot (UK) [kt (UK)]", "Velocity of light in vacuum", "Orbital Velocity Around the Earth (Cosmic Velocity - First)", "Earth Escape Velocity (Cosmic Velocity - Second)", "Solar System Escape Velocity (Cosmic Velocity - Third)", "Earth's Straight-line Orbital Velocity (around the sun)", "Velocity of Sound in Pure Water", "Velocity of Sound in Sea Water (@ 20°C, 10 meter deep)", "Speed of Sound in Air (@ 20°C, 1 atm) [Mach]", "Speed of Sound in Air (SI standard) [Mach]"])
        if style == "Standard Converters" and plane == "Linear Units" and subcat == "Acceleration":
            self.units_from.addItems(["Meter/Hour Squared [m/hr\u00b2]", "Meter/Minute Squared [m/min\u00b2]", "Meter/Second Squared [m/sec\u00b2]", "Kilometer/Hour Squared [km/hr\u00b2]", "Kilometer/Minute Squared [km/min\u00b2]", "Kilometer/Second Squared [km/sec\u00b2]", "Centimeter/Hour Squared [cm/hr\u00b2]", "Centimeter/Minute Squared [cm/min\u00b2]", "Centimeter/Second Squared [cm/sec\u00b2]", "Millimeter/Hour Squared [mm/hr\u00b2]", "Millimeter/Minute Squared [mm/min\u00b2]", "Millimeter/Second Squared [mm/sec\u00b2]", "Mile/Hour Squared [mi/hr\u00b2]", "Mile/Minute Squared [mi/min\u00b2]", "Mile/Second Squared [mi/sec\u00b2]", "Yard/Hour Squared [yd/hr\u00b2]", "Yard/Minute Squared [yd/min\u00b2]", "Yard/Second Squared [yd/sec\u00b2]",  "Foot/Hour Squared [ft/hr\u00b2]", "Foot/Minute Squared [ft/min\u00b2]", "Foot/Second Squared [ft/sec\u00b2]", "Galileo [Gal]", "Earth's Centripetal Acceleration", "Acceleration From Earth's Gravity [g]"])    
        if style == "Standard Converters" and plane == "Linear Units" and subcat == "Force":
            self.units_from.addItems(["Newton [N, J/m, kg*m/sec\u00b2]", "Kilonewton [kN]", "Gram-force [gf]", "Kilogram-force [kgf]", "Ton-force (metric) [tf]", "Giganewton [GN]", "Meganewton [MN]", "Centinewton [cN, J/cm]", "Millinewton [mN]", "Micronewton [µN]", "Dyne [dyn]", "Ton-force (short)", "Ton-force (long) [tonf (UK)]", "Kip-force [kipf]", "Pound-force [lbf]", "Ounce-force [ozf]", "Poundal [pdl]", "Pond [p]", "Kilopond [kp]"])
        if style == "Standard Converters" and plane == "Linear Units" and subcat == "Torque":
            self.units_from.addItems(["Newton Meter [N*m]", "Newton Centimeter [N*cm]", "Newton Millimeter [N*mm]", "Kilonewton Meter [kN*m]", "Dyne Meter [dyn*m]", "Dyne Centimeter [dyn*cm]", "Dyne Millimeter [dyn*mm]", "Kilogram-force Meter [kgf*m]", "Kilogram-force Centimeter [kgf*cm]", "Kilogram-force Millimeter [kgf*mm]", "Gram-force Meter [gf*m]", "Gram-force Centimeter [gf*cm]", "Gram-force Millimeter [gf*mm]", "Ounce-force Foot [ozf*ft]", "Ounce-force Inch [ozf*in]", "Pound-force Foot [lbf*ft]", "Pound-force Inch [lbf*in]", "Ton-force (short) Meter", "Ton-force (long) Meter", "Ton-force (metric) Meter", "Poundal foot [pdl*ft]", "Poundal Inch [pdl*in]"])            
        if style == "Standard Converters" and plane == "Linear Units" and subcat == "Moment of Inertia":
            self.units_from.addItems(["Kilogram Square Meter [kg*m\u00b2]", "Kilogram Square Centimeter [kg*cm\u00b2]", "Kilogram Square Millimeter [kg*mm\u00b2]", "Gram Square Centimeter [g*cm\u00b2]", "Gram Square Millimeter [g*mm\u00b2]", "Kilogram-force Meter Second Squared [kgf*m*sec\u00b2]", "Kilogram-force Centimeter Second Squared [kgf*cm*sec\u00b2]", "Ounce Square Inch [oz*in\u00b2]", "Ounce-force Inch Second Squared [ozf*in*sec\u00b2]", "Pound Square Foot [lb*ft\u00b2]", "Pound-force Foot Square Second [lbf*ft*s\u00b2]", "Pound-force Inch Second Squared [lbf*in*sec\u00b2]", "Slug Square Foot [slug*ft\u00b2]"])
        if style == "Standard Converters" and plane == "Linear Units" and subcat == "Mass and Weight":
            self.units_from.addItems(["Kilogram [kg]", "Gram [g]", "Milligram [mg]", "Ton (metric) [t]", "Pound [lb]", "Ounce [oz]", "Carat [car, ct]", "Ton (short) [ton (US)]", "Ton (long) [ton (UK)]", "Atomic Mass Unit [u]", "Gigagram [Gg]", "Megagram [Mg]", "Centigram [cg]", "Microgram [µg]", "Dalton", "Kilogram-force Square Second/Meter [kgf*sec\u00b2/m]", "Kilopound [kip]", "Slug", "Pound-force Square Second/Foot [lbf*sec\u00b2/ft]", "Pound (troy or apothecary)", "Poundal [pdl]", "Ton (assay) (US) [AT (US)]", "Ton (assay) (UK) [AT (UK)]", "Kiloton (metric) [kt]", "Quintal (metric) [cwt]", "Hundredweight (US)", "Hundredweight (UK)", "Quarter (US) [qr (US)]", "Quarter (UK) [qr (UK)]", "Stone (US)", "Stone (UK)", "Tonne [t]", "Pennyweight [pwt]", "Scruple (apothecary) [s.ap]", "Grain [gr]", "Gamma", "Plank Mass", "Electron Mass (rest)", "Earth's Mass", "Sun's Mass"])            
        if style == "Standard Converters" and plane == "Linear Units" and subcat == "Density":
            self.units_from.addItems(["Kilogram/Cubic Meter [kg/m\u00b3]", "Gram/Cubic Centimeter [g/cm\u00b3]", "Kilogram/Cubic Centimeter [kg/cm\u00b3]", "Gram/Cubic Meter [g/m\u00b3]", "Gram/Cubic Millimeter [g/mm\u00b3]", "Milligram/Cubic Meter [mg/m\u00b3]", "Milligram/Cubic Centimeter [mg/cm\u00b3]", "Milligram/Cubic Millimeter [mg/mm\u00b3]", "Megagram/Liter [Mg/L]", "Kilogram/Liter [kg/L]", "Gram/Liter [g/L]", "Centigram/Liter [cg/L]", "Milligram/Liter [mg/L]", "Microgram/Liter [µg/L]", "Pound/Cubic Inch [lb/in\u00b3]", "Pound/Cubic Foot [lb/ft\u00b3]", "Pound/Cubic Yard [lb/yd\u00b3]", "Pound/Gallon (US)", "Pound/Gallon (UK)", "Ounce/Cubic Inch [oz/in\u00b3]", "Ounce/Cubic Foot [oz/ft\u00b3]", "Ounce/Gallon (US)", "Ounce/Gallon (UK)", "Grain/Gallon (US)", "Grain/Gallon (UK)", "Grain/Cubic Foot [gr/ft\u00b3]", "Ton (short)/Cubic Yard", "Ton (long)/Cubic Yard", "Slug/Cubic Foot [slug/ft\u00b3]", "PSI/1000 Feet", "Earth's Density (mean)"])
        if style == "Standard Converters" and plane == "Linear Units" and subcat == "Time":
            self.units_from.addItems(["Second [sec]", "Millisecond [ms]", "Minute [min]", "Hour [hr]", "Day [d]", "Week", "Month", "Year [y]", "Decade", "Century", "Millenium", "Microsecond [µs]", "Nanosecond [ns]", "Shake", "Month (synodic)", "Year (Julian)", "Year (leap)", "Year (tropical)", "Year (sidereal)", "Day (sidereal)", "Hour (sidereal)", "Minute (sidereal)", "Second (sidereal)", "Fortnight", "Septennial", "Octennial", "Novennial", "Plank Time"])
        if style == "Standard Converters" and plane == "Linear Units" and subcat == "Temperature":
            self.units_from.addItems(["Kelvin [K]", "Celsius [°C]", "Fahrenheit [°F]", "Rankine [°R]", "Reaumur [°r]"])   
        if style == "Standard Converters" and plane == "Linear Units" and subcat == "Energy":
            self.units_from.addItems(["Joule [J]", "Kilojoule [kJ]", "Kilowatt-hour [kW*hr]", "Watt-hour [W*hr]", "Calorie (nutritional)", "Horsepower (metric) Hour", "Btu (IT) [Btu (IT), Btu]", "Btu (th) [Btu (th)]", "Gigajoule [GJ]", "Megajoule [MJ]", "Megaelectron-volt [MeV]", "Kiloelectron-volt [KeV]", "Electron-volt [eV]", "Erg", "Gigawatt-hour [GW*hr]", "Megawatt-hour [MW*hr]", "Kilowatt-second [kW*sec]", "Watt-second [W*s]", "Newton Meter [N*m]", "Horsepower Hour [hp*hr]", "Kilocalorie (IT) [kcal (IT)]", "Kilocalorie (th) [kcal (th)]", "Calorie (IT) [cal (IT), cal]", "Calorie (th) [cal (th)]", "Mega Btu (IT) [MBtu (IT)]", "Ton-hour (refrigeration)", "Fuel Oil Equivalent @kiloliter", "Fuel Oil Equivalent @barrel (US)", "Gigaton [Gton]", "Megaton [Mton]", "Kiloton [kton]", "Ton (explosives)", "Dyne Centimeter [dyn*cm]", "Gram-force Meter [gf*m]", "Gram-force Centimeter [gf*cm]", "Kilogram-force Centimeter", "Kilogram-force Meter", "Kilopond Meter [kp*m]", "Pound-force Foot [lbf*ft]", "Pound-force Inch [lbf*in]", "Ounce-force Inch [ozf*in]", "Foot-pound [ft*lbf]", "Inch-pound [in*lbf]", "Inch-ounce [in*ozf]", "Poundal Foot [pdl*ft]", "Therm", "Therm (EC)", "Therm (US)", "Hartree Energy", "Rydberg Constant"])
        if style == "Standard Converters" and plane == "Linear Units" and subcat == "Power":
            self.units_from.addItems(["Watt [W]", "Gigawatt [GW]", "Megawatt [MW]", "Kilowatt [kW]", "Milliwatt [mW]", "Microwatt [µW]", "Nanowatt [nW]", "Horsepower [hp]", "Horsepower (550 ft*lbf/s)", "Horsepower (metric)", "Horsepower (boiler)", "Horsepower (Electric)", "Horsepower (water)", "Pferdestarke (ps)", "Btu (IT)/Hour [Btu/hr]", "Btu (IT)/Minute [Btu/min]", "Btu (IT)/Second [Btu/sec]", "Btu (th)/Hour [Btu (th)/hr]", "Btu (th)/Minute [Btu (th)/min]", "Btu (th)/Second [Btu (th)/sec]", "MBtu (IT)/Hour [MBtu/hr]", "MBH", "Ton (refrigeration)", "Kilocalorie (IT)/Hour [kcal/hr]", "Kilocalorie (IT)/Minute [kcal/min]", "Kilocalorie (IT)/Second [kcal/sec]", "Kilocalorie (th)/Hour [kcal (th)/hr]", "Kilocalorie (th)/Minute [kcal (th)/min]", "Kilocalorie (th)/Second [kcal (th)/sec]", "Calorie (IT)/Hour [cal/hr]", "Calorie (IT)/Minute [cal/min]", "Calorie (IT)/Second [cal/sec]", "Calorie (th)/Hour [cal (th)/hr]", "Calorie (th)/Minute [cal (th)/min]", "Calorie (th)/Second [cal (th)/sec]", "Foot Pound-force/Hour", "Foot Pound-force/Minute", "Foot Pound-force/Second", "Pound-foot/Hour [lbf*ft/hr]", "Pound-foot/Minute [lbf*ft/min]", "Pound-foot/Second [lbf*ft/sec]", "Erg/Second [erg/s]", "Kilovolt Ampere [kV*A]", "Volt Ampere [V*A]", "Newton Meter/Second [N*m/s]", "Joule/Second [J/s]", "Gigajoule/Second [GJ/s]", "Megajoule/Second [MJ/s]", "Kilojoule/Second [kJ/s]", "Millijoule/Second [mJ/s]", "Microjoule/Second [µJ/s]", "Nanojoule/Second [nJ/s]", "Joule/Hour [J/hr]", "Joule/Minute [J/min]", "Kilojoule/Hour [kJ/hr]", "Kilojoule/Minute [kJ/min]"])
        if style == "Standard Converters" and plane == "Linear Units" and subcat == "Pressure":
            self.units_from.addItems(["Pascal [Pa]", "Kilopascal [kPa]", "Bar", "Pound/Square Inch [PSI]", "Kip/Square Inch [KSI]", "Standard Atmosphere [atm]", "Gigapascal [GPa]", "Megapascal [MPa]", "Millipascal [mPa]", "Micropascal [µPa]", "Nanopascal [nPa]", "Newton/Square Meter [N/m\u00b2]", "Newton/Square Centimeter [N/cm\u00b2]", "Newton/Square Millimeter [N/mm\u00b2]", "Kilonewton/Square Meter [kN/m\u00b2]", "Millibar [mb, mbar]", "Microbar [µb, µbar]", "Dyne/Square Centimeter [dyn/cm\u00b2]", "Kilogram-force/Square Meter [kgf/m\u00b2]", "Kilogram-force/Square Centimeter [kfg/cm\u00b2]", "Kilogram-force/Square Millimeter [kgf/mm\u00b2]", "Gram-force/Square Centimeter [gf/cm\u00b2]", "Ton-force (short)/Square Foot", "Ton-force (short)/Square Inch", "Ton-force (long)/Square Foot", "Ton-Force (long)/Square Inch", "Pound-force/Square Foot [lbf/ft\u00b2]", "Poundal/Square Foot", "Torr [Torr]", "Millitorr [mTorr]", "Centimeter Mercury (0°C) [cmHg]", "Millimeter Mercury (0°C) [mmHg]", "Inch Mercury (32°F) [inHg]", "Inch Mercury (60°F) [inHg]", "Centimeter Water (4°C)", "Millimeter Water (4°C)", "Inch Water (4°C) [inAq]", "Foot Water (4°C) [ftAq]", "Inch Water (60°F) [inAq]", "Foot Water (60°F) [ftAq]", "Atmosphere Technical [at]"])
        #units from standard angular units
        if style == "Standard Converters" and plane == "Angular Units" and subcat == "Plane Angle":
            self.units_from.addItems(["Degree [°]", "Radian [rad]", "Grad [^g]", "Minute [']", "Second ['']", "gon", "sign", "mil","Revolution [r]", "Circle", "Turn", "Quadrant", "Right Angle", "Sextant"])
        if style == "Standard Converters" and plane == "Angular Units" and subcat == "Angular Velocity":
            self.units_from.addItems(["Radian/Second [rad/sec]", "Radian/Day [rad/d]", "Radian/Hour [rad/hr]", "Radian/Minute [rad/min]", "Degree/Day [°/d]", "Degree/Hour [°/hr]", "Degree/Minute [°/min]", "Degree/Second [°/sec]", "Revolution/Day [r/d]", "Revolution/Hour [r/hr]", "Revolution/Minute [r/min, RPM]", "Revolution/Second [r/sec]"])
        if style == "Standard Converters" and plane == "Angular Units" and subcat == "Angular Acceleration":
            self.units_from.addItems(["Radian/Square Second [rad/s\u00b2]", "Radian/Square Minute", "Revolution/Square Second [r/s\u00b2]", "Revolution/Minute/Second", "Revolution/Square Minute"])
        #units from Fluids units
        if style == "Fluids" and plane == "" and subcat == "Volume":
            self.units_from.addItems(["Cubic Meter [m\u00b3]", "Cubic Kilometer [km\u00b3]", "Cubic Centimeter [cm\u00b3]", "Cubic Millimeter [mm\u00b3]", "Liter [L, l]", "Milliliter [mL]", "Gallon (US) [gal (US)]", "Quart (US) [qt (US)]", "Pint (US) [pt (US)]", "Cup (US)", "Tablespoon (US)", "Teaspoon (US)", "Cubic Mile [mi\u00b3]", "Cubic Yard [yd\u00b3]", "Cubic Foot [ft\u00b3]", "Cubic Inch [in\u00b3]", "Cubic Decimeter [dm\u00b3]", "Gigaliter [GL]", "Megaliter [ML]", "Kiloliter [kL]", "Hectoliter [hL]", "Dekaliter [daL]", "CC [cc, cm\u00b3]", "Drop", "Barrel (oil) [bbl (oil)]", "Barrel (US) [bbl (US)]", "Barrel (UK) [bbl (UK)]", "Gallon (UK) [gal (UK)]", "Quart (UK), [qt (UK)]", "Pint (UK) [pt (UK)]", "Cup (metric)", "Cup (UK)", "Fluid Ounce (US) [fl oz (US)]", "Fluid Ounce (UK) [fl oz (UK)]", "Tablespoon (metric)", "Tablespoon (UK)", "Gil (US) [gi]", "Gil (UK) [gi (UK)]", "Minim (US)", "Minim (UK)", "Ton Register [ton reg]", "ccf", "Hundred-cubic foot", "Acre-foot [ac*ft]", "Acre-foot (US survey)", "Acre-inch [ac*in]", "Dekastere", "Cord [cd]", "Tun", "Hogshead", "Board foot", "Dram [dr]", "Earth's Volume"])
        if style == "Fluids" and plane == "" and subcat == "Volume - Dry":
            self.units_from.addItems(["Liter [L, l]", "Barrel dry (US) [bbl dry (US)]", "Pint dry (US) [pt dry (US)]", "Quart dry (US) [qt dry (US)]", "Peck (US) [pk (US)]", "Peck (UK) [pk (UK)]", "Bushel (US) [bu (US)]", "Bushel (UK) [bu (UK)]"])
        if style == "Fluids" and plane == "" and subcat == "Specific Volume":
            self.units_from.addItems(["Cubic Meter/Kilogram", "Cubic Centimeter/Gram", "Liter/Kilogram [L/kg]", "Liter/Gram [L/g]", "Cubic Foot/Kilogram [ft\u00b3/kg]", "Cubic Foot/Pound [ft\u00b3/lb]", "Gallon (US)/Pound", "Gallon (UK)/Pound"])
        if style == "Fluids" and plane == "" and subcat == "Flow":
            self.units_from.addItems(["Cubic Meter/Second [m\u00b3/sec]", "Cubic Meter/Day [m\u00b3/d]", "Cubic Meter/Hour [m\u00b3/hr]", "Cubic Meter/Minute", "Cubic Centimeter/Day", "Cubic Centimeter/Hour", "Cubic Centimeter/Minute", "Cubic Centimeter/Second", "Liter/Day [L/d]", "Liter/Hour [L/hr]", "Liter/Minute [L/min]", "Liter/Second [L/sec]", "Milliliter/Day [mL/d]", "Milliliter/Hour [mL/hr]", "Milliliter/Minute [mL/min]", "Milliliter/Second [mL/sec]", "Gallon (US)/Day [gal (US)/d]", "Gallon (US)/Hour [gal (US)/hr]", "Gallon (US)/Minute [gal (US)/min]", "Gallon (US)/Second [gal (US)/sec]", "Gallon (UK)/Day [gal (UK)/d]", "Gallon (UK)/Hour [gal (UK)/hr]", "Gallon (UK)/Minute [gal (UK)/min]", "Gallon (UK)/Second [gal (UK)/sec]", "Kilobarrel (US)/Day", "Barrel (US)/Day [bbl (US)/d]", "Barrel (US)/Hour [bbl (US)/hr]", "Barrel (US)/Minute", "Barrel (US)/Second", "Acre-foot/Year [ac*ft/y]", "Acre-foot/Day [cs*ft/d]", "Acre-foot/Hour [ac*ft/hr]", "Hundred-cubic Foot/Day", "Hundred-cubic Foot/Hour", "Hundred-cubic Foot/Minute", "Ounce/Hour [oz/hr]", "Ounce/Minute [oz/min]", "Ounce/Seccond [oz/sec]", "Ounce (UK)/Hour [oz (UK)/hr]", "Ounce (UK)/Minute", "Ounce (UK)/Second", "Cubic Yard/Hour [yd\u00b3/hr]", "Cubic Yard/Minute [yd\u00b3/min]", "Cubic Yard/Second [yd\u00b3/sec]", "Cubic Foot/Hour [ft\u00b3/hr]", "Cubic Foot/Minute [ft\u00b3/min]", "Cubic Foot/Second [ft\u00b3/sec]", "Cubic Inch/Hour [in\u00b3/hr]", "Cubic Inch/Minute [in\u00b3/min]", "Cubic Inch/Second [in\u00b3/sec]"])
        if style == "Fluids" and plane == "" and subcat == "Viscosity (Dynamic)":
            self.units_from.addItems(["Pascal Second [pa*s]", "Kilogram-force Second/Square Meter", "Newton Second/Square Meter", "Millinewton Second/Square Meter", "Dyne Second/Square Meter", "Poise [P]", "Gigapoise [GP]", "Megapoise [MP]", "Kilopoise [kP]", "Centipoise [cP]", "Millipoise [mP]", "Micropoise [µP]", "Pound-Force Second/Square Inch", "Pound-Force Second/Square Foot", "Poundal Second/Square Foot", "Gram/Centimeter/Second", "Slug/Foot/Second", "Pound/Foot/Second", "Pound/Foot/Hour [lb/(ft*hr)]"])
        if style == "Fluids" and plane == "" and subcat == "Viscosity (Kinematic)":
            self.units_from.addItems(["Square Meter/Second", "Square Meter/Hour [m\u00b2/hr]", "Square Centimeter/Second", "Square Millimeter/Second", "Square Foot/Second [ft\u00b2/sec]", "Square Foot/Hour [ft\u00b2/hr]", "Square Inch/Second [in\u00b2/sec]", "Stokes [St]", "Gigastokes [GSt]", "Megastokes [MSt]", "Kilostokes [kSt]", "Centistokes [cSt]", "Millistokes [mSt]", "Microstokes [µSt]"])
        if style == "Fluids" and plane == "" and subcat == "Surface Tension":
            self.units_from.addItems(["Newton/Meter [N/m]", "Millinewton/Meter [mN/m]", "Gram-force/Centimeter", "Dyne/Centimeter [dyn/cm]", "Erg/Square Centimeter", "Erg/Square Millimeter", "Poundal/Inch [pd/in]", "Pound-force/Inch [lbf/in]"])
        #units from electricity units 
        if style == "Electricity" and plane == "" and subcat == "Electrical Charge":
            self.units_from.addItems(["Coulomb [C]", "Meagcoulomb [MC]", "Kilocoulomb [kC]", "Millicoulomb [mC]", "Microcoulmob [µC]", "Abcoulomb [abC]", "EMU of Charge", "Statcoulomb [stC]", "ESU of Charge", "Franklin [Fr]", "Ampere-hour [A*hr]", "Ampere-minute [A*min]", "Ampere-second [A*sec]", "Faraday (based on carbon 12)", "Elementary Charge [e]"])
        if style == "Electricity" and plane == "" and subcat == "Electric Potential (Voltage)":
            self.units_from.addItems(["Volt [V]", "Watt/Ampere [W/A]", "Kilovolt [kV]", "Millivolt [mV]", "Abvolt [abV]", "EMU of Electric Potential", "Statvolt [stV]", "ESU of Electric Potential"])
        if style == "Electricity" and plane == "" and subcat == "Current":
            self.units_from.addItems(["Ampere [A]", "Kiloampere [kA]", "Milliampere [mA]", "Biot [Bi]", "Abampere [abA]", "EMU of Current", "Statampere [stA]", "ESU of Current", "CGS e.m. Unit", "CGS e.s. Unit"])
        if style == "Electricity" and plane == "" and subcat == "Resistance":
            self.units_from.addItems(["Ohm [Ω]", "Megaohm [MΩ]", "Kiloohm [kΩ]", "Milliohm [mΩ]", "Microohm [μΩ]", "Volt/Ampere [V/A]", "Reciprocal Siemens [1/S]", "Abohm", "EMU of Resistance", "Statohm", "ESU of Resistance", "Quantized Hall Resistance"])
        if style == "Electricity" and plane == "" and subcat == "Capacitance":
            self.units_from.addItems(["Farad [F]", "Gigafarad [GF]", "Megafarad [MF]", "Kilofarad [kF]", "Centifarad [cF]", "Millifarad [mF]", "Microfarad [μF]", "Nanofarad [nF]", "Picofarad [pF]", "Coulomb/Volt [C/V]", "Abfarad [abF]", "EMU of Capacitance", "Statfarad [stF]", "ESU of Capacitance"])
        if style == "Electricity" and plane == "" and subcat == "Inductance":
            self.units_from.addItems(["Henry [H]", "Gigahenry [GH]", "Megahenry [MH]", "Kilohenry [kH]", "Centihenry [cH]", "Millihenry [mH]", "Microhenry [µH]", "Nanohenry [nH]", "Picohenry [pH]", "Weber/Ampere [Wb/A]", "Abhenry [abH]", "EMU of Inductance", "Stathenry [stH]", "ESU of Inductance"])
        if style == "Electricity" and plane == "" and subcat == "Conductance":
            self.units_from.addItems(["Siemens [S]", "Megasiemens [MS]", "Kilosiemens [kS]", "Millisiemens [mS]", "Microsiemens [µS]", "Ampere/Volt [A/V]", "Mho", "Gemmho", "Micromho", "Abmho", "Statmho", "Quantized Hall Conductance"])
        
        self.units_from.currentTextChanged.connect(self.unit_convert)
        
    def update_units_to(self):
        
        style = self.unitstyle.currentText()
        plane = self.unitplane.currentText()
        subcat = self.unitsubcat.currentText()
        
        self.units_to.clear()
        #units to standard linear converter units
        if style == "Standard Converters" and plane == "Linear Units" and subcat == "Length and Distance":
            self.units_to.addItems(["Meter [m]", "Kilometer [km]", "Centimeter [cm]", "Millimeter [mm]", "Micrometer [μm, μ]", "Nanometer [nm]", "Mile [mi, mi (int.)]", "Yard [yd]", "Foot [ft]", "Inch [in]", "Light Year [ly]", "Gigameter [Gm]", "Megameter [Mm]", "Micron [μ]", "Megaparsec [Mpc]", "Kiloparsec [kpc]", "Parsec [pc]", "Astronomical Unit [AU, UA]", "League [lea]", "Nautical League (UK)", "Nautical League (int)", "League (statute) [st.league]", "Nautical Mile (UK) [NM (UK)]", "Nautical Mile (international)", "Mile (statute) [mi, mi(US)]", "Mile (US survey) [mi]", "Mile (Roman)", "Kiloyard [kyd]", "Furlong [fur]", "Furlong (US survey) [fur]", "Chain [ch]", "Chain (US survey) [ch]", "Rope", "Rod [rd]", "Rod (US survey) [rd]", "Perch", "Pole", "Fathom [fath]", "Fathom (US survey) [fath]", "Ell", "Foot (US survey) [ft]", "Link [li]", "Link (US survey) [li]", "Cubit (UK)", "Hand", "Span (cloth)", "Finger (cloth)", "Nail (cloth)", "Inch (US survey) [in]", "Barleycorn", "mil [mil, thou]", "Microinch", "Angstrom [A]", "a.u. of length [a.u., b]", "X-unit [X]", "Fermi [F, f]", "Arpent", "Pica", "Point", "Twip", "Aln", "Famn", "Caliber [cl]", "Centiinch [cin]", "Ken", "Long Reed", "Reed", "Plank Length", "Electron Radius (classical)", "Bohr Radius [b, a.u.]", "Earth's Equitorial Radius", "Earth's Polar Radius", "Earth's Distance From the Sun", "Sun's Radius"])
        if style == "Standard Converters" and plane == "Linear Units" and subcat == "Area":
            self.units_to.addItems(["Square Meter [m\u00b2]", "Square Kilometer [km\u00b2]", "Square Centimeter [cm\u00b2]", "Square Millimeter [mm\u00b2]", "Square Micrometer [μm\u00b2]", "Hectare [ha]", "Acre [ac]", "Square Mile [mi\u00b2]", "Square Yard [yd\u00b2]", "Square Foot [ft\u00b2]", "Square Inch [in\u00b2]", "Are [a]", "Barn [b]", "Square Mile (US survey)", "Square Foot (US survey)", "Circular Inch", "Township", "Section", "Acre (US survey) [ac]", "Rood", "Square Chain [ch\u00b2]", "Square Rod", "Square Rod (US Survey)", "Square Perch", "Square Pole", "Square Mil [mil\u00b2]", "Circular Mil", "Homestead", "Electron Cross Section"])
        if style == "Standard Converters" and plane == "Linear Units" and subcat == "Volume":
            self.units_to.addItems(["Cubic Meter [m\u00b3]", "Cubic Kilometer [km\u00b3]", "Cubic Centimeter [cm\u00b3]", "Cubic Millimeter [mm\u00b3]", "Liter [L, l]", "Milliliter [mL]", "Gallon (US) [gal (US)]", "Quart (US) [qt (US)]", "Pint (US) [pt (US)]", "Cup (US)", "Tablespoon (US)", "Teaspoon (US)", "Cubic Mile [mi\u00b3]", "Cubic Yard [yd\u00b3]", "Cubic Foot [ft\u00b3]", "Cubic Inch [in\u00b3]", "Gigaliter [GL]", "Megaliter [ML]", "Kiloliter [kL]", "CC [cc, cm\u00b3]", "Drop", "Barrel (oil) [bbl (oil)]", "Barrel (US) [bbl (US)]", "Barrel (UK) [bbl (UK)]", "Gallon (UK) [gal (UK)]", "Quart (UK) [qt (UK)]", "Pint (UK) [pt (UK)]", "Cup (metric)", "Cup (UK)", "Fluid Ounce (US) [fl oz (US)]", "Fluid Ounce (UK) [fl oz (UK)]", "Tablespoon (metric)", "Tablespoon (UK)", "Dessertspoon (US)", "Dessertspoon (UK)", "Teaspoon (metric)", "Teaspoon (UK)", "Gil (US) [gi]", "Gil (UK) [gi (UK)]", "Minim (US)", "Minim (UK)", "Ton Register [ton reg]", "ccf", "Hundred-cubic foot", "Acre-foot [ac*ft]", "Acre-foot (US survey)", "Acre-inch [ac*in]", "Dekastere", "Stere [st]", "Decistere", "Cord [cd]", "Tun", "Hogshead", "Board foot", "Dram [dr]", "Earth's Volume"])
        if style == "Standard Converters" and plane == "Linear Units" and subcat == "Velocity and Speed":
            self.units_to.addItems(["Meter/Hour [m/hr]", "Meter/Minute [m/min]", "Meter/Second [m/sec]", "Kilometer/Hour [km/hr, KPH]", "Kilometer/Minute [km/min]", "Kilometer/Second [km/sec]", "Centimeter/Hour [cm/hr]", "Centimeter/Minute [cm/min]", "Centimeter/Second [cm/sec]", "Millimeter/Hour [mm/hr]", "Millimeter/Minute [mm/min]", "Millimeter/Second [mm/sec]", "Mile/Hour [mi/hr, MPH]", "Mile/Minute [mi/min]", "Mile/Second [mi/sec]", "Yard/Hour [yd/hr]", "Yard/Minute [yd/min]", "Yard/Second [yd/sec]", "Foot/Hour [ft/hr]", "Foot/Minute [ft/min, FPM]", "Foot/Second [ft/sec, FPS]", "Knot [kt, kn]", "Knot (UK) [kt (UK)]", "Velocity of light in vacuum", "Orbital Velocity Around the Earth (Cosmic Velocity - First)", "Earth Escape Velocity (Cosmic Velocity - Second)", "Solar System Escape Velocity (Cosmic Velocity - Third)", "Earth's Straight-line Orbital Velocity (around the sun)", "Velocity of Sound in Pure Water", "Velocity of Sound in Sea Water (@ 20°C, 10 meter deep)", "Speed of Sound in Air (@ 20°C, 1 atm) [Mach]", "Speed of Sound in Air (SI standard) [Mach]"])
        if style == "Standard Converters" and plane == "Linear Units" and subcat == "Acceleration":
            self.units_to.addItems(["Meter/Hour Squared [m/hr\u00b2]", "Meter/Minute Squared [m/min\u00b2]", "Meter/Second Squared [m/sec\u00b2]", "Kilometer/Hour Squared [km/hr\u00b2]", "Kilometer/Minute Squared [km/min\u00b2]", "Kilometer/Second Squared [km/sec\u00b2]", "Centimeter/Hour Squared [cm/hr\u00b2]", "Centimeter/Minute Squared [cm/min\u00b2]", "Centimeter/Second Squared [cm/sec\u00b2]", "Millimeter/Hour Squared [mm/hr\u00b2]", "Millimeter/Minute Squared [mm/min\u00b2]", "Millimeter/Second Squared [mm/sec\u00b2]", "Mile/Hour Squared [mi/hr\u00b2]", "Mile/Minute Squared [mi/min\u00b2]", "Mile/Second Squared [mi/sec\u00b2]", "Yard/Hour Squared [yd/hr\u00b2]", "Yard/Minute Squared [yd/min\u00b2]", "Yard/Second Squared [yd/sec\u00b2]",  "Foot/Hour Squared [ft/hr\u00b2]", "Foot/Minute Squared [ft/min\u00b2]", "Foot/Second Squared [ft/sec\u00b2]", "Galileo [Gal]", "Earth's Centripetal Acceleration", "Acceleration From Earth's Gravity [g]"])    
        if style == "Standard Converters" and plane == "Linear Units" and subcat == "Force":
            self.units_to.addItems(["Newton [N, J/m, kg*m/sec\u00b2]", "Kilonewton [kN]", "Gram-force [gf]", "Kilogram-force [kgf]", "Ton-force (metric) [tf]", "Giganewton [GN]", "Meganewton [MN]", "Centinewton [cN, J/cm]", "Millinewton [mN]", "Micronewton [µN]", "Dyne [dyn]", "Ton-force (short)", "Ton-force (long) [tonf (UK)]", "Kip-force [kipf]", "Pound-force [lbf]", "Ounce-force [ozf]", "Poundal [pdl]", "Pond [p]", "Kilopond [kp]"])
        if style == "Standard Converters" and plane == "Linear Units" and subcat == "Torque":
            self.units_to.addItems(["Newton Meter [N*m]", "Newton Centimeter [N*cm]", "Newton Millimeter [N*mm]", "Kilonewton Meter [kN*m]", "Dyne Meter [dyn*m]", "Dyne Centimeter [dyn*cm]", "Dyne Millimeter [dyn*mm]", "Kilogram-force Meter [kgf*m]", "Kilogram-force Centimeter [kgf*cm]", "Kilogram-force Millimeter [kgf*mm]", "Gram-force Meter [gf*m]", "Gram-force Centimeter [gf*cm]", "Gram-force Millimeter [gf*mm]", "Ounce-force Foot [ozf*ft]", "Ounce-force Inch [ozf*in]", "Pound-force Foot [lbf*ft]", "Pound-force Inch [lbf*in]", "Ton-force (short) Meter", "Ton-force (long) Meter", "Ton-force (metric) Meter", "Poundal foot [pdl*ft]", "Poundal Inch [pdl*in]"])            
        if style == "Standard Converters" and plane == "Linear Units" and subcat == "Moment of Inertia":
            self.units_to.addItems(["Kilogram Square Meter [kg*m\u00b2]", "Kilogram Square Centimeter [kg*cm\u00b2]", "Kilogram Square Millimeter [kg*mm\u00b2]", "Gram Square Centimeter [g*cm\u00b2]", "Gram Square Millimeter [g*mm\u00b2]", "Kilogram-force Meter Second Squared [kgf*m*sec\u00b2]", "Kilogram-force Centimeter Second Squared [kgf*cm*sec\u00b2]", "Ounce Square Inch [oz*in\u00b2]", "Ounce-force Inch Second Squared [ozf*in*sec\u00b2]", "Pound Square Foot [lb*ft\u00b2]", "Pound-force Foot Square Second [lbf*ft*s\u00b2]", "Pound-force Inch Second Squared [lbf*in*sec\u00b2]", "Slug Square Foot [slug*ft\u00b2]"])
        if style == "Standard Converters" and plane == "Linear Units" and subcat == "Mass and Weight":
            self.units_to.addItems(["Kilogram [kg]", "Gram [g]", "Milligram [mg]", "Ton (metric) [t]", "Pound [lb]", "Ounce [oz]", "Carat [car, ct]", "Ton (short) [ton (US)]", "Ton (long) [ton (UK)]", "Atomic Mass Unit [u]", "Gigagram [Gg]", "Megagram [Mg]", "Centigram [cg]", "Microgram [µg]", "Dalton", "Kilogram-force Square Second/Meter [kgf*sec\u00b2/m]", "Kilopound [kip]", "Slug", "Pound-force Square Second/Foot [lbf*sec\u00b2/ft]", "Pound (troy or apothecary)", "Poundal [pdl]", "Ton (assay) (US) [AT (US)]", "Ton (assay) (UK) [AT (UK)]", "Kiloton (metric) [kt]", "Quintal (metric) [cwt]", "Hundredweight (US)", "Hundredweight (UK)", "Quarter (US) [qr (US)]", "Quarter (UK) [qr (UK)]", "Stone (US)", "Stone (UK)", "Tonne [t]", "Pennyweight [pwt]", "Scruple (apothecary) [s.ap]", "Grain [gr]", "Gamma", "Plank Mass", "Electron Mass (rest)", "Earth's Mass", "Sun's Mass"])            
        if style == "Standard Converters" and plane == "Linear Units" and subcat == "Density":
            self.units_to.addItems(["Kilogram/Cubic Meter [kg/m\u00b3]", "Gram/Cubic Centimeter [g/cm\u00b3]", "Kilogram/Cubic Centimeter [kg/cm\u00b3]", "Gram/Cubic Meter [g/m\u00b3]", "Gram/Cubic Millimeter [g/mm\u00b3]", "Milligram/Cubic Meter [mg/m\u00b3]", "Milligram/Cubic Centimeter [mg/cm\u00b3]", "Milligram/Cubic Millimeter [mg/mm\u00b3]", "Megagram/Liter [Mg/L]", "Kilogram/Liter [kg/L]", "Gram/Liter [g/L]", "Centigram/Liter [cg/L]", "Milligram/Liter [mg/L]", "Microgram/Liter [µg/L]", "Pound/Cubic Inch [lb/in\u00b3]", "Pound/Cubic Foot [lb/ft\u00b3]", "Pound/Cubic Yard [lb/yd\u00b3]", "Pound/Gallon (US)", "Pound/Gallon (UK)", "Ounce/Cubic Inch [oz/in\u00b3]", "Ounce/Cubic Foot [oz/ft\u00b3]", "Ounce/Gallon (US)", "Ounce/Gallon (UK)", "Grain/Gallon (US)", "Grain/Gallon (UK)", "Grain/Cubic Foot [gr/ft\u00b3]", "Ton (short)/Cubic Yard", "Ton (long)/Cubic Yard", "Slug/Cubic Foot [slug/ft\u00b3]", "PSI/1000 Feet", "Earth's Density (mean)"])
        if style == "Standard Converters" and plane == "Linear Units" and subcat == "Time":
            self.units_to.addItems(["Second [sec]", "Millisecond [ms]", "Minute [min]", "Hour [hr]", "Day [d]", "Week", "Month", "Year [y]", "Decade", "Century", "Millenium", "Microsecond [µs]", "Nanosecond [ns]", "Shake", "Month (synodic)", "Year (Julian)", "Year (leap)", "Year (tropical)", "Year (sidereal)", "Day (sidereal)", "Hour (sidereal)", "Minute (sidereal)", "Second (sidereal)", "Fortnight", "Septennial", "Octennial", "Novennial", "Plank Time"])
        if style == "Standard Converters" and plane == "Linear Units" and subcat == "Temperature":
            self.units_to.addItems(["Kelvin [K]", "Celsius [°C]", "Fahrenheit [°F]", "Rankine [°R]", "Reaumur [°r]"])   
        if style == "Standard Converters" and plane == "Linear Units" and subcat == "Energy":
            self.units_to.addItems(["Joule [J]", "Kilojoule [kJ]", "Kilowatt-hour [kW*hr]", "Watt-hour [W*hr]", "Calorie (nutritional)", "Horsepower (metric) Hour", "Btu (IT) [Btu (IT), Btu]", "Btu (th) [Btu (th)]", "Gigajoule [GJ]", "Megajoule [MJ]", "Megaelectron-volt [MeV]", "Kiloelectron-volt [KeV]", "Electron-volt [eV]", "Erg", "Gigawatt-hour [GW*hr]", "Megawatt-hour [MW*hr]", "Kilowatt-second [kW*sec]", "Watt-second [W*s]", "Newton Meter [N*m]", "Horsepower Hour [hp*hr]", "Kilocalorie (IT) [kcal (IT)]", "Kilocalorie (th) [kcal (th)]", "Calorie (IT) [cal (IT), cal]", "Calorie (th) [cal (th)]", "Mega Btu (IT) [MBtu (IT)]", "Ton-hour (refrigeration)", "Fuel Oil Equivalent @kiloliter", "Fuel Oil Equivalent @barrel (US)", "Gigaton [Gton]", "Megaton [Mton]", "Kiloton [kton]", "Ton (explosives)", "Dyne Centimeter [dyn*cm]", "Gram-force Meter [gf*m]", "Gram-force Centimeter [gf*cm]", "Kilogram-force Centimeter", "Kilogram-force Meter", "Kilopond Meter [kp*m]", "Pound-force Foot [lbf*ft]", "Pound-force Inch [lbf*in]", "Ounce-force Inch [ozf*in]", "Foot-pound [ft*lbf]", "Inch-pound [in*lbf]", "Inch-ounce [in*ozf]", "Poundal Foot [pdl*ft]", "Therm", "Therm (EC)", "Therm (US)", "Hartree Energy", "Rydberg Constant"])
        if style == "Standard Converters" and plane == "Linear Units" and subcat == "Power":
            self.units_to.addItems(["Watt [W]", "Gigawatt [GW]", "Megawatt [MW]", "Kilowatt [kW]", "Milliwatt [mW]", "Microwatt [µW]", "Nanowatt [nW]", "Horsepower [hp]", "Horsepower (550 ft*lbf/s)", "Horsepower (metric)", "Horsepower (boiler)", "Horsepower (Electric)", "Horsepower (water)", "Pferdestarke (ps)", "Btu (IT)/Hour [Btu/hr]", "Btu (IT)/Minute [Btu/min]", "Btu (IT)/Second [Btu/sec]", "Btu (th)/Hour [Btu (th)/hr]", "Btu (th)/Minute [Btu (th)/min]", "Btu (th)/Second [Btu (th)/sec]", "MBtu (IT)/Hour [MBtu/hr]", "MBH", "Ton (refrigeration)", "Kilocalorie (IT)/Hour [kcal/hr]", "Kilocalorie (IT)/Minute [kcal/min]", "Kilocalorie (IT)/Second [kcal/sec]", "Kilocalorie (th)/Hour [kcal (th)/hr]", "Kilocalorie (th)/Minute [kcal (th)/min]", "Kilocalorie (th)/Second [kcal (th)/sec]", "Calorie (IT)/Hour [cal/hr]", "Calorie (IT)/Minute [cal/min]", "Calorie (IT)/Second [cal/sec]", "Calorie (th)/Hour [cal (th)/hr]", "Calorie (th)/Minute [cal (th)/min]", "Calorie (th)/Second [cal (th)/sec]", "Foot Pound-force/Hour", "Foot Pound-force/Minute", "Foot Pound-force/Second", "Pound-foot/Hour [lbf*ft/hr]", "Pound-foot/Minute [lbf*ft/min]", "Pound-foot/Second [lbf*ft/sec]", "Erg/Second [erg/s]", "Kilovolt Ampere [kV*A]", "Volt Ampere [V*A]", "Newton Meter/Second [N*m/s]", "Joule/Second [J/s]", "Gigajoule/Second [GJ/s]", "Megajoule/Second [MJ/s]", "Kilojoule/Second [kJ/s]", "Millijoule/Second [mJ/s]", "Microjoule/Second [µJ/s]", "Nanojoule/Second [nJ/s]", "Joule/Hour [J/hr]", "Joule/Minute [J/min]", "Kilojoule/Hour [kJ/hr]", "Kilojoule/Minute [kJ/min]"])
        if style == "Standard Converters" and plane == "Linear Units" and subcat == "Pressure":
            self.units_to.addItems(["Pascal [Pa]", "Kilopascal [kPa]", "Bar", "Pound/Square Inch [PSI]", "Kip/Square Inch [KSI]", "Standard Atmosphere [atm]", "Gigapascal [GPa]", "Megapascal [MPa]", "Millipascal [mPa]", "Micropascal [µPa]", "Nanopascal [nPa]", "Newton/Square Meter [N/m\u00b2]", "Newton/Square Centimeter [N/cm\u00b2]", "Newton/Square Millimeter [N/mm\u00b2]", "Kilonewton/Square Meter [kN/m\u00b2]", "Millibar [mb, mbar]", "Microbar [µb, µbar]", "Dyne/Square Centimeter [dyn/cm\u00b2]", "Kilogram-force/Square Meter [kgf/m\u00b2]", "Kilogram-force/Square Centimeter [kfg/cm\u00b2]", "Kilogram-force/Square Millimeter [kgf/mm\u00b2]", "Gram-force/Square Centimeter [gf/cm\u00b2]", "Ton-force (short)/Square Foot", "Ton-force (short)/Square Inch", "Ton-force (long)/Square Foot", "Ton-Force (long)/Square Inch", "Pound-force/Square Foot [lbf/ft\u00b2]", "Poundal/Square Foot", "Torr [Torr]", "Millitorr [mTorr]", "Centimeter Mercury (0°C) [cmHg]", "Millimeter Mercury (0°C) [mmHg]", "Inch Mercury (32°F) [inHg]", "Inch Mercury (60°F) [inHg]", "Centimeter Water (4°C)", "Millimeter Water (4°C)", "Inch Water (4°C) [inAq]", "Foot Water (4°C) [ftAq]", "Inch Water (60°F) [inAq]", "Foot Water (60°F) [ftAq]", "Atmosphere Technical [at]"])
        #units to standard angular units
        if style == "Standard Converters" and plane == "Angular Units" and subcat == "Plane Angle":
            self.units_to.addItems(["Degree [°]", "Radian [rad]", "Grad [^g]", "Minute [']", "Second ['']", "gon", "sign", "mil","Revolution [r]", "Circle", "Turn", "Quadrant", "Right Angle", "Sextant"])
        if style == "Standard Converters" and plane == "Angular Units" and subcat == "Angular Velocity":
            self.units_to.addItems(["Radian/Second [rad/sec]", "Radian/Day [rad/d]", "Radian/Hour [rad/hr]", "Radian/Minute [rad/min]", "Degree/Day [°/d]", "Degree/Hour [°/hr]", "Degree/Minute [°/min]", "Degree/Second [°/sec]", "Revolution/Day [r/d]", "Revolution/Hour [r/hr]", "Revolution/Minute [r/min, RPM]", "Revolution/Second [r/sec]"])
        if style == "Standard Converters" and plane == "Angular Units" and subcat == "Angular Acceleration":
            self.units_to.addItems(["Radian/Square Second [rad/s\u00b2]", "Radian/Square Minute", "Revolution/Square Second [r/s\u00b2]", "Revolution/Minute/Second", "Revolution/Square Minute"])
        #units to Fluids units
        if style == "Fluids" and plane == "" and subcat == "Volume":
            self.units_to.addItems(["Cubic Meter [m\u00b3]", "Cubic Kilometer [km\u00b3]", "Cubic Centimeter [cm\u00b3]", "Cubic Millimeter [mm\u00b3]", "Liter [L, l]", "Milliliter [mL]", "Gallon (US) [gal (US)]", "Quart (US) [qt (US)]", "Pint (US) [pt (US)]", "Cup (US)", "Tablespoon (US)", "Teaspoon (US)", "Cubic Mile [mi\u00b3]", "Cubic Yard [yd\u00b3]", "Cubic Foot [ft\u00b3]", "Cubic Inch [in\u00b3]", "Cubic Decimeter [dm\u00b3]", "Gigaliter [GL]", "Megaliter [ML]", "Kiloliter [kL]", "Hectoliter [hL]", "Dekaliter [daL]", "CC [cc, cm\u00b3]", "Drop", "Barrel (oil) [bbl (oil)]", "Barrel (US) [bbl (US)]", "Barrel (UK) [bbl (UK)]", "Gallon (UK) [gal (UK)]", "Quart (UK), [qt (UK)]", "Pint (UK) [pt (UK)]", "Cup (metric)", "Cup (UK)", "Fluid Ounce (US) [fl oz (US)]", "Fluid Ounce (UK) [fl oz (UK)]", "Tablespoon (metric)", "Tablespoon (UK)", "Gil (US) [gi]", "Gil (UK) [gi (UK)]", "Minim (US)", "Minim (UK)", "Ton Register [ton reg]", "ccf", "Hundred-cubic foot", "Acre-foot [ac*ft]", "Acre-foot (US survey)", "Acre-inch [ac*in]", "Dekastere", "Cord [cd]", "Tun", "Hogshead", "Board foot", "Dram [dr]", "Earth's Volume"])
        if style == "Fluids" and plane == "" and subcat == "Volume - Dry":
            self.units_to.addItems(["Liter [L, l]", "Barrel dry (US) [bbl dry (US)]", "Pint dry (US) [pt dry (US)]", "Quart dry (US) [qt dry (US)]", "Peck (US) [pk (US)]", "Peck (UK) [pk (UK)]", "Bushel (US) [bu (US)]", "Bushel (UK) [bu (UK)]"])
        if style == "Fluids" and plane == "" and subcat == "Specific Volume":
            self.units_to.addItems(["Cubic Meter/Kilogram", "Cubic Centimeter/Gram", "Liter/Kilogram [L/kg]", "Liter/Gram [L/g]", "Cubic Foot/Kilogram [ft\u00b3/kg]", "Cubic Foot/Pound [ft\u00b3/lb]", "Gallon (US)/Pound", "Gallon (UK)/Pound"])
        if style == "Fluids" and plane == "" and subcat == "Flow":
            self.units_to.addItems(["Cubic Meter/Second [m\u00b3/sec]", "Cubic Meter/Day [m\u00b3/d]", "Cubic Meter/Hour [m\u00b3/hr]", "Cubic Meter/Minute", "Cubic Centimeter/Day", "Cubic Centimeter/Hour", "Cubic Centimeter/Minute", "Cubic Centimeter/Second", "Liter/Day [L/d]", "Liter/Hour [L/hr]", "Liter/Minute [L/min]", "Liter/Second [L/sec]", "Milliliter/Day [mL/d]", "Milliliter/Hour [mL/hr]", "Milliliter/Minute [mL/min]", "Milliliter/Second [mL/sec]", "Gallon (US)/Day [gal (US)/d]", "Gallon (US)/Hour [gal (US)/hr]", "Gallon (US)/Minute [gal (US)/min]", "Gallon (US)/Second [gal (US)/sec]", "Gallon (UK)/Day [gal (UK)/d]", "Gallon (UK)/Hour [gal (UK)/hr]", "Gallon (UK)/Minute [gal (UK)/min]", "Gallon (UK)/Second [gal (UK)/sec]", "Kilobarrel (US)/Day", "Barrel (US)/Day [bbl (US)/d]", "Barrel (US)/Hour [bbl (US)/hr]", "Barrel (US)/Minute", "Barrel (US)/Second", "Acre-foot/Year [ac*ft/y]", "Acre-foot/Day [cs*ft/d]", "Acre-foot/Hour [ac*ft/hr]", "Hundred-cubic Foot/Day", "Hundred-cubic Foot/Hour", "Hundred-cubic Foot/Minute", "Ounce/Hour [oz/hr]", "Ounce/Minute [oz/min]", "Ounce/Seccond [oz/sec]", "Ounce (UK)/Hour [oz (UK)/hr]", "Ounce (UK)/Minute", "Ounce (UK)/Second", "Cubic Yard/Hour [yd\u00b3/hr]", "Cubic Yard/Minute [yd\u00b3/min]", "Cubic Yard/Second [yd\u00b3/sec]", "Cubic Foot/Hour [ft\u00b3/hr]", "Cubic Foot/Minute [ft\u00b3/min]", "Cubic Foot/Second [ft\u00b3/sec]", "Cubic Inch/Hour [in\u00b3/hr]", "Cubic Inch/Minute [in\u00b3/min]", "Cubic Inch/Second [in\u00b3/sec]"])
        if style == "Fluids" and plane == "" and subcat == "Viscosity (Dynamic)":
            self.units_to.addItems(["Pascal Second [pa*s]", "Kilogram-force Second/Square Meter", "Newton Second/Square Meter", "Millinewton Second/Square Meter", "Dyne Second/Square Meter", "Poise [P]", "Gigapoise [GP]", "Megapoise [MP]", "Kilopoise [kP]", "Centipoise [cP]", "Millipoise [mP]", "Micropoise [µP]", "Pound-Force Second/Square Inch", "Pound-Force Second/Square Foot", "Poundal Second/Square Foot", "Gram/Centimeter/Second", "Slug/Foot/Second", "Pound/Foot/Second", "Pound/Foot/Hour [lb/(ft*hr)]"])
        if style == "Fluids" and plane == "" and subcat == "Viscosity (Kinematic)":
            self.units_to.addItems(["Square Meter/Second", "Square Meter/Hour [m\u00b2/hr]", "Square Centimeter/Second", "Square Millimeter/Second", "Square Foot/Second [ft\u00b2/sec]", "Square Foot/Hour [ft\u00b2/hr]", "Square Inch/Second [in\u00b2/sec]", "Stokes [St]", "Gigastokes [GSt]", "Megastokes [MSt]", "Kilostokes [kSt]", "Centistokes [cSt]", "Millistokes [mSt]", "Microstokes [µSt]"])
        if style == "Fluids" and plane == "" and subcat == "Surface Tension":
            self.units_to.addItems(["Newton/Meter [N/m]", "Millinewton/Meter [mN/m]", "Gram-force/Centimeter", "Dyne/Centimeter [dyn/cm]", "Erg/Square Centimeter", "Erg/Square Millimeter", "Poundal/Inch [pd/in]", "Pound-force/Inch [lbf/in]"])
        #units to electricity units 
        if style == "Electricity" and plane == "" and subcat == "Electrical Charge":
            self.units_to.addItems(["Coulomb [C]", "Meagcoulomb [MC]", "Kilocoulomb [kC]", "Millicoulomb [mC]", "Microcoulmob [µC]", "Abcoulomb [abC]", "EMU of Charge", "Statcoulomb [stC]", "ESU of Charge", "Franklin [Fr]", "Ampere-hour [A*hr]", "Ampere-minute [A*min]", "Ampere-second [A*sec]", "Faraday (based on carbon 12)", "Elementary Charge [e]"])
        if style == "Electricity" and plane == "" and subcat == "Electric Potential (Voltage)":
            self.units_to.addItems(["Volt [V]", "Watt/Ampere [W/A]", "Kilovolt [kV]", "Millivolt [mV]", "Abvolt [abV]", "EMU of Electric Potential", "Statvolt [stV]", "ESU of Electric Potential"])
        if style == "Electricity" and plane == "" and subcat == "Current":
            self.units_to.addItems(["Ampere [A]", "Kiloampere [kA]", "Milliampere [mA]", "Biot [Bi]", "Abampere [abA]", "EMU of Current", "Statampere [stA]", "ESU of Current", "CGS e.m. Unit", "CGS e.s. Unit"])
        if style == "Electricity" and plane == "" and subcat == "Resistance":
            self.units_to.addItems(["Ohm [Ω]", "Megaohm [MΩ]", "Kiloohm [kΩ]", "Milliohm [mΩ]", "Microohm [μΩ]", "Volt/Ampere [V/A]", "Reciprocal Siemens [1/S]", "Abohm", "EMU of Resistance", "Statohm", "ESU of Resistance", "Quantized Hall Resistance"])
        if style == "Electricity" and plane == "" and subcat == "Capacitance":
            self.units_to.addItems(["Farad [F]", "Gigafarad [GF]", "Megafarad [MF]", "Kilofarad [kF]", "Centifarad [cF]", "Millifarad [mF]", "Microfarad [μF]", "Nanofarad [nF]", "Picofarad [pF]", "Coulomb/Volt [C/V]", "Abfarad [abF]", "EMU of Capacitance", "Statfarad [stF]", "ESU of Capacitance"])
        if style == "Electricity" and plane == "" and subcat == "Inductance":
            self.units_to.addItems(["Henry [H]", "Gigahenry [GH]", "Megahenry [MH]", "Kilohenry [kH]", "Centihenry [cH]", "Millihenry [mH]", "Microhenry [µH]", "Nanohenry [nH]", "Picohenry [pH]", "Weber/Ampere [Wb/A]", "Abhenry [abH]", "EMU of Inductance", "Stathenry [stH]", "ESU of Inductance"])
        if style == "Electricity" and plane == "" and subcat == "Conductance":
            self.units_to.addItems(["Siemens [S]", "Megasiemens [MS]", "Kilosiemens [kS]", "Millisiemens [mS]", "Microsiemens [µS]", "Ampere/Volt [A/V]", "Mho", "Gemmho", "Micromho", "Abmho", "Statmho", "Quantized Hall Conductance"])
        
        self.units_to.currentTextChanged.connect(self.unit_convert)
        
    def unit_convert(self):
        units_from = self.units_from.currentText()
        units_to = self.units_to.currentText()
        NUMinput = self.NUMunit_input.value()
        NUMout = 0
        inter = 0
        NUMunit_output = 0
        pi = math.pi
    #converting from input to standard unit (meters for length, Newtons for force, etc.)
    # inter - short for intermediate. calculation is stored as an intermediate number then converted to the units specified
        #standard linear length units in
        if units_from == "Meter [m]":
            inter = NUMinput * 1
        if units_from == "Kilometer [km]":
            inter = NUMinput * 1000
        if units_from == "Centimeter [cm]":
            inter = NUMinput * 0.01
        if units_from == "Millimeter [mm]":
            inter = NUMinput * 0.001
        if units_from == "Micrometer [μm, μ]" or units_from == "Micron [μ]":
            inter = NUMinput * 1*10**-6
        if units_from == "Nanometer [nm]":
            inter = NUMinput * 1*10**-9
        if units_from == "Mile [mi, mi (int.)]":
            inter = NUMinput * 1609.344
        if units_from == "Yard [yd]":
            inter = NUMinput * 0.9144
        if units_from == "Foot [ft]":
            inter = NUMinput * 0.3048
        if units_from == "Inch [in]":
            inter = NUMinput * 0.0254
        if units_from == "Light Year [ly]":
            inter = NUMinput * 9.46073047258*10**15
        if units_from == "Gigameter [Gm]":
            inter = NUMinput * 1000000000
        if units_from == "Megameter [Mm]":
            inter = NUMinput * 1000000
        if units_from == "Megaparsec [Mpc]":
            inter = NUMinput * 3.085677581288*10**22
        if units_from == "Kiloparsec [kpc]":
            inter = NUMinput * 3.08567758128*10**19
        if units_from == "Parsec [pc]":
            inter = NUMinput * 3.08567758128*10**16
        if units_from == "Astronomical Unit [AU, UA]":
            inter = NUMinput * 149597870691
        if units_from == "League [lea]":
            inter = NUMinput * 4828.032
        if units_from == "Nautical League (UK)":
            inter = NUMinput * 5559.552
        if units_from == "Nautical League (int)":
            inter = NUMinput * 5556
        if units_from == "League (statute) [st.league]":
            inter = NUMinput * 4828.0416560833
        if units_from == "Nautical Mile (UK) [NM (UK)]":
            inter = NUMinput * 1853.184
        if units_from == "Nautical Mile (international)":
            inter = NUMinput * 1852
        if units_from == "Mile (statute) [mi, mi(US)]" or units_from == "Mile (US survey) [mi]":
            inter = NUMinput * 1609.3472186944
        if units_from == "Mile (Roman)":
            inter = NUMinput * 1479.804
        if units_from == "Kiloyard [kyd]":
            inter = NUMinput * 914.4
        if units_from == "Furlong [fur]":
            inter = NUMinput * 201.168
        if units_from == "Furlong (US survey) [fur]":
            inter = NUMinput * 201.1684023368
        if units_from == "Chain [ch]":
            inter = NUMinput * 20.1168
        if units_from == "Chain (US survey) [ch]":
            inter = NUMinput * 20.1168402337
        if units_from == "Rope":
            inter = NUMinput * 6.096
        if units_from == "Rod [rd]" or units_from == "Perch" or units_from == "Pole":
            inter = NUMinput * 5.0292
        if units_from == "Rod (US survey) [rd]":
            inter = NUMinput * 5.0292100584
        if units_from == "Fathom [fath]":
            inter = NUMinput * 1.8288
        if units_from == "Fathom (US survey) [fath]":
            inter = NUMinput * 1.8288036576
        if units_from == "Ell":
            inter = NUMinput * 1.143
        if units_from == "Foot (US survey) [ft]":
            inter = NUMinput * 0.3048006096
        if units_from == "Link [li]":
            inter = NUMinput * 0.201168
        if units_from == "Link (US survey) [li]":
            inter = NUMinput * 0.2011684023
        if units_from == "Cubit (UK)":
            inter = NUMinput * 0.4572
        if units_from == "Hand":
            inter = NUMinput * 0.1016
        if units_from == "Span (cloth)":
            inter = NUMinput * 0.2286
        if units_from == "Finger (cloth)":
            inter = NUMinput * 0.1143
        if units_from == "Nail (cloth)":
            inter = NUMinput * 0.05715
        if units_from == "Inch (US survey) [in]":
            inter = NUMinput * 0.0254000508
        if units_from == "Barleycorn":
            inter = NUMinput * 0.0084666667
        if units_from == "mil [mil, thou]":
            inter = NUMinput * 2.54*10**-5
        if units_from == "Microinch":
            inter = NUMinput * 2.54*10**-8
        if units_from == "Angstrom [A]":
            inter = NUMinput * 1*10**-10
        if units_from == "a.u. of length [a.u., b]":
            inter = NUMinput * 5.2917724900001*10**-11
        if units_from == "X-unit [X]":
            inter = NUMinput * 1.00208*10**13
        if units_from == "Fermi [F, f]":
            inter = NUMinput * 1*10**-15
        if units_from == "Arpent":
            inter = NUMinput * 58.5216
        if units_from == "Pica":
            inter = NUMinput * 0.0042333333
        if units_from == "Point":
            inter = NUMinput * 0.0003527778
        if units_from == "Twip":
            inter = NUMinput * 1.76389*10**-5
        if units_from == "Aln":
            inter = NUMinput * 0.5937777778
        if units_from == "Famn":
            inter = NUMinput * 1.7813333333
        if units_from == "Caliber [cl]" or units_from == "Cenitinch [cin]":
            inter = NUMinput * 0.000254
        if units_from == "Ken":
            inter = NUMinput * 2.11836
        if units_from == "Long Reed":
            inter = NUMinput * 3.2004
        if units_from == "Reed":
            inter = NUMinput * 2.7432
        if units_from == "Plank Length":
            inter = NUMinput * 1.61605*10**-35
        if units_from == "Electron Radius (classical)":
            inter = NUMinput * 2.81794092*10**-15
        if units_from == "Bohr Radius [b, a.u.]":
            inter = NUMinput * 5.291772490000*10**-11
        if units_from == "Earth's Equitorial Radius":
            inter = NUMinput * 6378160
        if units_from == "Earth's Polar Radius":
            inter = NUMinput * 6356776.9999999
        if units_from == "Earth's Distance From the Sun":
            inter = NUMinput * 149600000000
        if units_from == "Sun's Radius":
            inter = NUMinput * 696000000

        #Standard area units in
        if units_from == "Square Meter [m\u00b2]":
            inter = NUMinput * 1
        if units_from == "Square Kilometer [km\u00b2]":
            inter = NUMinput * 1000000
        if units_from == "Square Centimeter [cm\u00b2]":
            inter = NUMinput * 0.0001
        if units_from == "Square Millimeter [mm\u00b2]":
            inter = NUMinput * 1*10**-6
        if units_from == "Square Micrometer [μm\u00b2]":
            inter = NUMinput * 1*10**-12
        if units_from == "Hectare [ha]":
            inter = NUMinput * 10000
        if units_from == "Acre [ac]":
            inter = NUMinput * 4046.8564224
        if units_from == "Square Mile [mi\u00b2]" or units_from == "Section":
            inter = NUMinput * 2589988.110336
        if units_from == "Square Yard [yd\u00b2]":
            inter = NUMinput * 0.83612736
        if units_from == "Square Foot [ft\u00b2]":
            inter = NUMinput * 0.09290304
        if units_from == "Square Inch [in\u00b2]":
            inter = NUMinput * 0.00064516
        if units_from == "Are [a]":
            inter = NUMinput * 100
        if units_from == "Barn [b]":
            inter = NUMinput * 1*10**-28
        if units_from == "Square Mile (US survey)":
            inter = NUMinput * 2589998.4703195
        if units_from == "Square Foot (US survey)":
            inter = NUMinput * 0.0929034116
        if units_from == "Circular Inch":
            inter = NUMinput * 0.0005067075
        if units_from == "Township":
            inter = NUMinput * 93239571.972096
        if units_from == "Acre (US survey) [ac]":
            inter = NUMinput * 4046.8726098743
        if units_from == "Rood":
            inter = NUMinput * 1011.7141056
        if units_from == "Square Chain [ch\u00b2]":
            inter = NUMinput * 404.68564224
        if units_from == "Square Rod" or units_from == "Square Perch" or units_from == "Square Pole":
            inter = NUMinput * 25.29285264
        if units_from == "Square Rod (US survey)":
            inter = NUMinput * 25.2929538117
        if units_from == "Square Mil [mil\u00b2]":
            inter = NUMinput * 6.4516*10**-10
        if units_from == "Circular Mil":
            inter = NUMinput * 5.067074790975*10**-10
        if units_from == "Homestead":
            inter = NUMinput * 647497.027584
        if units_from == "Electron Cross Section":
            inter = NUMinput * 6.6524615999999*10**-29
            
        #standard volume units in
        if units_from == "Cubic Meter [m\u00b3]" or units_from == "Kiloliter [kL]" or units_from == "Stere [st]":
            inter = NUMinput * 1
        if units_from == "Cubic Kilometer [km\u00b3]":
            inter = NUMinput * 1000000000
        if units_from == "Cubic Centimeter [cm\u00b3]" or units_from == "Milliliter [mL]" or units_from == "CC [cc, cm\u00b3]":
            inter = NUMinput * 1*10**-6
        if units_from == "Cubic Millimeter [mm\u00b3]":
            inter = NUMinput * 1*10**-9
        if units_from == "Liter [L, l]":
            inter = NUMinput * 0.001
        if units_from == "Gallon (US) [gal (US)]":
            inter = NUMinput * 0.0037854118
        if units_from == "Quart (US) [qt (US)]":
            inter = NUMinput * 0.0009463529
        if units_from == "Pint (US) [pt (US)]":
            inter = NUMinput * 0.0004731765
        if units_from == "Cup (US)":
            inter = NUMinput * 0.0002365882
        if units_from == "Tablespoon (US)":
            inter = NUMinput * 1.47868*10**-5
        if units_from == "Teaspoon (US)":
            inter = NUMinput * 4.92892159375*10**-6
        if units_from == "Cubic Mile [mi\u00b3]":
            inter = NUMinput * 4168181825.4406
        if units_from == "Cubic Yard [yd\u00b3]":
            inter = NUMinput * 0.764554858
        if units_from == "Cubic Foot [ft\u00b3]":
            inter = NUMinput * 0.0283168466
        if units_from == "Cubic Inch [in\u00b3]":
            inter = NUMinput * 1.63871*10**-5
        if units_from == "Gigaliter [GL]":
            inter = NUMinput * 1000000
        if units_from == "Megaliter [ML]":
            inter = NUMinput * 1000
        if units_from == "Drop":
            inter = NUMinput * 5*10**-8
        if units_from == "Barrel (oil) [bbl (oil)]":
            inter = NUMinput * 0.1589872949
        if units_from == "Barrel (US) [bbl (US)]":
            inter = NUMinput * 0.1192404712
        if units_from == "Barrel (UK) [bbl (UK)]":
            inter = NUMinput * 0.16365924
        if units_from == "Gallon (UK) [gal (UK)]":
            inter = NUMinput * 0.00454609
        if units_from == "Quart (UK) [qt (UK)]":
            inter = NUMinput * 0.0011365225
        if units_from == "Pint (UK) [pt (UK)]":
            inter = NUMinput * 0.0005682613
        if units_from == "Cup (metric)":
            inter = NUMinput * 0.00025
        if units_from == "Cup (UK)":
            inter = NUMinput * 0.0002841306
        if units_from == "Fluid Ounce (US) [fl oz (US)]":
            inter = NUMinput * 2.95735*10**-5
        if units_from == "Fluid Ounce (UK) [fl oz (UK)]":
            inter = NUMinput * 2.84131*10**-5
        if units_from == "Tablespoon (metric)":
            inter = NUMinput * 1.5*10**-5
        if units_from == "Tablespoon (UK)":
            inter = NUMinput * 1.77582*10**-5
        if units_from == "Dessertspoon (US)":
            inter = NUMinput * 9.8578431875*10**-6
        if units_from == "Dessertspoon (UK)":
            inter = NUMinput * 1.18388*10**-5
        if units_from == "Teaspoon (metric)":
            inter = NUMinput * 5*10**-6
        if units_from == "Teaspoon (UK)":
            inter = NUMinput * 5.9193880208333*10**-6
        if units_from == "Gil (US) [gi]":
            inter = NUMinput * 0.0001182941
        if units_from == "Gil (UK) [gi (UK)]":
            inter = NUMinput * 0.0001420653
        if units_from == "Minim (US)":
            inter = NUMinput * 6.1611519921875*10**-8
        if units_from == "Minim (UK)":
            inter = NUMinput * 5.9193880208333*10**-8
        if units_from == "Ton Register [ton reg]":
            inter = NUMinput * 2.8316846592
        if units_from == "ccf":
            inter = NUMinput * 2.8316846592
        if units_from == "Hundred-cubic foot":
            inter = NUMinput * 2.8316846592
        if units_from == "Acre-foot [ac*ft]":
            inter = NUMinput * 1233.4818375475
        if units_from == "Acre-foot (US survey)":
            inter = NUMinput * 1233.4892384682
        if units_from == "Acre-inch [ac*in]":
            inter = NUMinput * 102.790153129
        if units_from == "Dekastere":
            inter = NUMinput * 10
        if units_from == "Cord [cd]":
            inter = NUMinput * 3.6245563638
        if units_from == "Decistere":
            inter = NUMinput * 0.1
        if units_from == "Tun":
            inter = NUMinput * 0.9539237696
        if units_from == "Hogshead":
            inter = NUMinput * 0.2384809424
        if units_from == "Board foot":
            inter = NUMinput * 0.0023597372
        if units_from == "Dram [dr]":
            inter = NUMinput * 3.6966911953125*10**-6
        if units_from == "Earth's Volume":
            inter = NUMinput * 1.083*10**21
        
        #Standard Velocity and Speed units in
        if units_from == "Meter/Hour [m/hr]":
            inter = NUMinput * 0.0002777778
        if units_from == "Meter/Minute [m/min]":
            inter = NUMinput * 0.0166666667
        if units_from == "Meter/Second [m/sec]":
            inter = NUMinput * 1
        if units_from == "Kilometer/Hour [km/hr, KPH]":
            inter = NUMinput * 0.2777777778
        if units_from == "Kilometer/Minute [km/min]":
            inter = NUMinput * 16.6666666667
        if units_from == "Kilometer/Second [km/sec]":
            inter = NUMinput * 1000
        if units_from == "Mile/Hour [mi/hr, MPH]":
            inter = NUMinput * 0.44704
        if units_from == "Mile/Minute [mi/min]":
            inter = NUMinput * 26.8224
        if units_from == "Mile/Second [mi/sec]":
            inter = NUMinput * 1609.344
        if units_from == "Centimeter/Hour [cm/hr]":
            inter = NUMinput * 2.7777777777778*10**-6
        if units_from == "Centimeter/Minute [cm/min]":
            inter = NUMinput * 0.0001666667
        if units_from == "Centimeter/Second [cm/sec]":
            inter = NUMinput * 0.01
        if units_from == "Millimeter/Hour [mm/hr]":
            inter = NUMinput * 2.7777777777778*10**-7
        if units_from == "Millimeter/Minute [mm/min]":
            inter = NUMinput * 1.66667*10**-5
        if units_from == "Millimeter/Second [mm/sec]":
            inter = NUMinput * 0.001
        if units_from == "Yard/Hour [yd/hr]":
            inter = NUMinput * 0.000254
        if units_from == "Yard/Minute [yd/min]":
            inter = NUMinput * 0.01524
        if units_from == "Yard/Second [yd/sec]":
            inter = NUMinput * 0.9144
        if units_from == "Foot/Hour [ft/hr]":
            inter = NUMinput * 8.46667*10**-5
        if units_from == "Foot/Minute [ft/min, FPM]":
            inter = NUMinput * 0.00508
        if units_from == "Foot/Second [ft/sec, FPS]":
            inter = NUMinput * 0.3048
        if units_from == "Knot [kt, kn]":
            inter = NUMinput * 0.5144444444
        if units_from == "Knot (UK) [kt (UK)]":
            inter = NUMinput * 0.5147733333
        if units_from == "Velocity of Light in Vacuum":
            inter = NUMinput * 299792458
        if units_from == "Orbital Velocity Around the Earth (Cosmic Velocity - First)":
            inter = NUMinput * 7899.9999999999
        if units_from == "Earth Escape Velocity (Cosmic Velocity - Second)":
            inter = NUMinput * 11200
        if units_from == "Solar System Escape Velocity (Cosmic Velocity - Third)":
            inter = NUMinput * 16670
        if units_from == "Earth's Straight-line Orbital Velocity (around the sun)":
            inter = NUMinput * 29765
        if units_from == "Velocity of Sound in Pure Water":
            inter = NUMinput * 1482.6999999998
        if units_from == "Velocity of Sound in Sea Water (@ 20°C, 10 meter deep)":
            inter = NUMinput * 1521.6
        if units_from == "Speed of Sound in Air (@ 20°C, 1 atm) [Mach]":
            inter = NUMinput * 343.6
        if units_from == "Speed of Sound in Air (SI standard) [Mach]":
            inter = NUMinput * 295.0464000003
        
        #Standard Acceleration Units in
        if units_from == "Meter/Hour Squared [m/hr\u00b2]":
            inter = NUMinput * 7.716049383*10**-8
        if units_from == "Meter/Minute Squared [m/min\u00b2]":
            inter = NUMinput * 0.000277777778
        if units_from == "Meter/Second Squared [m/sec\u00b2]":
            inter = NUMinput * 1
        if units_from == "Kilometer/Hour Squared [km/hr\u00b2]":
            inter = NUMinput * 0.00007716049
        if units_from == "Kilometer/Minute Squared [km/min\u00b2]":
            inter = NUMinput * 0.277777778
        if units_from == "Kilometer/Second Squared [km/sec\u00b2]":
            inter = NUMinput * 1000
        if units_from == "Centimeter/Hour Squared [cm/hr\u00b2]":
            inter = NUMinput * 7.71604938*10**-10
        if units_from == "Centimeter/Minute Squared [cm/min\u00b2]":
            inter = NUMinput * 2.77777778*10**-6
        if units_from == "Centimeter/Second Squared [cm/sec\u00b2]":
            inter = NUMinput * 0.01
        if units_from == "Millimeter/Hour Squared [mm/hr\u00b2]":
            inter = NUMinput * 7.71604938*10**-11
        if units_from == "Millimeter/Minute Squared [mm/min\u00b2]":
            inter = NUMinput * 2.77777778*10**-7
        if units_from == "Millimeter/Second Squared [mm/sec\u00b2]":
            inter = NUMinput * 0.001
        if units_from == "Mile/Hour Squared [mi/hr\u00b2]":
            inter = NUMinput * 0.00012417777777778
        if units_from == "Mile/Minute Squared [mi/min\u00b2]":
            inter = NUMinput * 0.44704
        if units_from == "Mile/Second Squared [mi/sec\u00b2]":
            inter = NUMinput * 1609.344
        if units_from == "Yard/Hour Squared [yd/hr\u00b2]":
            inter = NUMinput * 7.05555556*10**-8
        if units_from == "Yard/Minute Squared [yd/min\u00b2]":
            inter = NUMinput * 0.000254
        if units_from == "Yard/Second Squared [yd/sec\u00b2]":
            inter = NUMinput * 0.9144
        if units_from == "Foot/Hour Squared [ft/hr\u00b2]":
            inter = NUMinput * 2.35185185*10**-8
        if units_from == "Foot/Minute Squared [ft/min\u00b2]":
            inter = NUMinput * 8.46666667*10**-5
        if units_from == "Foot/Second Squared [ft/sec\u00b2]":
            inter = NUMinput * 0.3048
        if units_from == "Galileo [Gal]":
            inter = NUMinput * 0.01
        if units_from == "Earth's Centripetal Acceleration":
            inter = NUMinput * 5.95*10**-3
        if units_from == "Acceleration From Earth's Gravity [g]":
            inter = NUMinput * 9.807
        
        #Standard Force Units in
        if units_from == "Newton [N, J/m, kg*m/sec\u00b2]":
            inter = NUMinput * 1
        if units_from == "Kilonewton [kN]":
            inter = NUMinput * 1000
        if units_from == "Gram-force [gf]":
            inter = NUMinput * 0.00980665
        if units_from == "Kilogram-force [kgf]":
            inter = NUMinput * 9.80665
        if units_from == "Ton-force (metric) [tf]":
            inter = NUMinput * 9806.65
        if units_from == "Giganewton [GN]":
            inter = NUMinput * 1000000000
        if units_from == "Meganewton [MN]":
            inter = NUMinput * 1000000
        if units_from == "Centinewton [cN, J/cm]":
            inter = NUMinput * 0.01
        if units_from == "Millinewton [mN]":
            inter = NUMinput * 0.001
        if units_from == "Micronewton [µN]":
            inter = NUMinput * 1*10**-6
        if units_from == "Dyne [dyn]":
            inter = NUMinput * 1*10**-5
        if units_from == "Ton-force (short)":
            inter = NUMinput * 8896.443230521
        if units_from == "Ton-force (long) [tonf (UK)]":
            inter = NUMinput * 9964.0164181707
        if units_from == "Kip-force [kipf]":
            inter = NUMinput * 4448.2216152548
        if units_from == "Pound-force [lbf]":
            inter = NUMinput * 4.4482216153
        if units_from == "Ounce-force [ozf]":
            inter = NUMinput * 0.278013851
        if units_from == "Poundal [pdl]":
            inter = NUMinput * 0.1382549544
        if units_from == "Pond [p]":
            inter = NUMinput * 0.00980665
        if units_from == "Kilopond":
            inter = NUMinput * 9.80665
        
        #Standard Torque Units in
        if units_from == "Newton Meter [N*m]":
            inter = NUMinput * 1
        if units_from == "Newton Centimeter [N*cm]":
            inter = NUMinput * 0.01
        if units_from == "Newton Millimeter [N*mm]":
            inter = NUMinput * 0.001
        if units_from == "Kilonewton Meter [kN*m]":
            inter = NUMinput * 1000
        if units_from == "Dyne Meter [dyn*m]":
            inter = NUMinput * 1*10**-5
        if units_from == "Dyne Centimeter [dyn*cm]":
            inter = NUMinput * 1*10**-7
        if units_from == "Dyne Millimeter [dyn*mm]":
            inter = NUMinput * 1*10**-8
        if units_from == "Kilogram-force Meter [kgf*m]":
            inter = NUMinput * 9.80665
        if units_from == "Kilogram-force Centimeter [kgf*cm]":
            inter = NUMinput * 0.0980665
        if units_from == "Kilogram-force Millimeter [kgf*mm]" or units_from == "Gram-force Meter [gf*m]":
            inter = NUMinput * 0.00980665
        if units_from == "Gram-force Centimeter [gf*cm]":
            inter = NUMinput * 9.80665*10**-5
        if units_from == "Gram-force Millimeter [gf*mm]":
            inter = NUMinput * 9.80665*10**-6
        if units_from == "Ounce-force Foot [ozf*ft]":
            inter = NUMinput * 0.084738624
        if units_from == "Ounce-force Inch [ozf*in]":
            inter = NUMinput * 0.007061552
        if units_from == "Pound-force Foot [lbf*ft]":
            inter = NUMinput * 1.355818
        if units_from == "Pound-force Inch [lbf*in]":
            inter = NUMinput *  0.1129848333
        if units_from == "Ton-force (short) Meter":
            inter = NUMinput * 8896.4400000035
        if units_from == "Ton-force (long) Meter":
            inter = NUMinput * 9964.0200000047
        if units_from == "Ton-force (metric) Meter":
            inter = NUMinput * 9806.6499999993
        if units_from == "Poundal foot [pdl*ft]":
            inter = NUMinput * 0.0421401
        if units_from == "Poundal Inch [pdl*in]":
            inter = NUMinput * 0.003511675
        
        #Standard Moment of Inertia Units in 
        if units_from == "Kilogram Square Meter [kg*m\u00b2]":
            inter = NUMinput * 1
        if units_from == "Kilogram Square Centimeter [kg*cm\u00b2]":
            inter = NUMinput * 0.0001
        if units_from == "Kilogram Square Millimeter [kg*mm\u00b2]":
            inter = NUMinput * 1*10**-6
        if units_from == "Gram Square Centimeter [g*cm\u00b2]":
            inter = NUMinput * 1*10**-7
        if units_from == "Gram Square Millimeter [g*mm\u00b2]":
            inter = NUMinput * 1*10**-9
        if units_from == "Kilogram-force Meter Second Squared [kgf*m*sec\u00b2]":
            inter = NUMinput * 9.8066499998
        if units_from == "Kilogram-force Centimeter Second Squared [kgf*cm*sec\u00b2]":
            inter = NUMinput * 0.0980665
        if units_from == "Ounce Square Inch [oz*in\u00b2]":
            inter = NUMinput * 1.829*10**-5
        if units_from == "Ounce-force Inch Second Squared [ozf*in*sec\u00b2]":
            inter = NUMinput * 0.0070615519
        if units_from == "Pound Square Foot [lb*ft\u00b2]":
            inter = NUMinput * 0.0421401101
        if units_from == "Pound-force Foot Square Second [lbf*ft*s\u00b2]":
            inter = NUMinput * 1.3558179619
        if units_from == "Pound-force Inch Second Squared [lbf*in*sec\u00b2]":
            inter = NUMinput * 0.1129848302
        if units_from == "Slug Square Foot [slug*ft\u00b2]":
            inter = NUMinput * 1.3558179619
        
        #Standard Mass Units in
        if units_from == "Kilogram [kg]":
            inter = NUMinput * 1
        if units_from == "Gram [g]":
            inter = NUMinput * 0.001
        if units_from == "Milligram [mg]":
            inter = NUMinput * 1*10**-6
        if units_from == "Ton (metric) [t]" or units_from == "Megagram [Mm]" or units_from == "Tonne [t]":
            inter = NUMinput * 1000
        if units_from == "Pound [lb]":
            inter = NUMinput * 0.45359237
        if units_from == "Ounce [oz]":
            inter = NUMinput * 0.0283495231
        if units_from == "Carat [car, ct]":
            inter = NUMinput * 0.0002
        if units_from == "Ton (short) [ton (US)]":
            inter = NUMinput * 907.18474
        if units_from == "Ton (long) [ton (UK)]":
            inter = NUMinput * 1016.0469088
        if units_from == "Atomic Mass Unit [u]":
            inter = NUMinput * 1.6605402*10**-27
        if units_from == "Gigagram [Gg]":
            inter = NUMinput * 1000000
        if units_from == "Megagram [Mg]":
            inter = NUMinput * 1000
        if units_from == "Centigram [cg]":
            inter = NUMinput * 1*10**-5
        if units_from == "Microgram [µg]":
            inter = NUMinput * 1*10**-9
        if units_from == "Dalton":
            inter = NUMinput * 1.6605300000013*10**-27
        if units_from == "Kilogram-force Square Second/Meter [kgf*sec\u00b2/m]":
            inter = NUMinput * 9.80665
        if units_from == "Kilopound [kip]":
            inter = NUMinput * 453.59237
        if units_from == "Slug" or units_from == "Pound-force Square Second/Foot [lbf*sec\u00b2/ft]":
            inter = NUMinput * 14.5939029372
        if units_from == "Pound (troy or apothecary)":
            inter = NUMinput * 0.3732417216
        if units_from == "Poundal [pdl]":
            inter = NUMinput * 0.0140867196
        if units_from == "Ton (assay) (US) [AT (US)]":
            inter = NUMinput * 0.02916667
        if units_from == "Ton (assay) (UK) [AT (UK)]":
            inter = NUMinput * 0.0326666667
        if units_from == "Kiloton (metric) [kt]":
            inter = NUMinput * 1000000
        if units_from == "Quintal (metric) [cwt]":
            inter = NUMinput * 100
        if units_from == "Hundredweight (US)":
            inter = NUMinput * 45.359237
        if units_from == "Hundredweight (UK)":
            inter = NUMinput * 50.80234544
        if units_from == "Quarter (US) [qr (US)]":
            inter = NUMinput * 11.33980925
        if units_from == "Quarter (UK) [qr (UK)]":
            inter = NUMinput * 12.70058636
        if units_from == "Stone (US)":
            inter = NUMinput * 5.669904625
        if units_from == "Stone (UK)":
            inter = NUMinput * 6.35029318
        if units_from == "Pennyweight [pwt]":
            inter = NUMinput * 0.0015551738
        if units_from == "Scruple (apothecary) [s.ap]":
            inter = NUMinput * 0.0012959782
        if units_from == "Grain [gr]":
            inter = NUMinput * 6.47989*10**-5
        if units_from == "Gamma":
            inter = NUMinput * 1*10**-9
        if units_from == "Plank Mass":
            inter = NUMinput * 2.17671*10**-8
        if units_from == "Electron Mass (rest)":
            inter = NUMinput * 9.1093897*10**-31
        if units_from == "Earth's Mass":
            inter = NUMinput * 5.9760000000002*10**24
        if units_from == "Sun's Mass":
            inter = NUMinput * 2*10**30
        
        #Standard Density Units in
        if units_from == "Kilogram/Cubic Meter [kg/m\u00b3]" or units_from == "Milligram/Cubic Centimeter [mg/cm\u00b3]" or units_from == "Gram/Liter [g/L]":
            inter = NUMinput * 1
        if units_from == "Gram/Cubic Centimeter [g/cm\u00b3]" or units_from == "Milligram/Cubic Millimeter [mg/mm\u00b3]" or units_from == "Kilogram/Liter [kg/L]":
            inter = NUMinput * 1000
        if units_from == "Kilogram/Cubic Centimeter [kg/cm\u00b3]" or units_from == "Gram/Cubic Millimeter [g/mm\u00b3]":
            inter = NUMinput * 1000000
        if units_from == "Gram/Cubic Meter [g/m\u00b3]":
            inter = NUMinput * 0.001
        if units_from == "Milligram/Cubic Meter [mg/m\u00b3]" or units_from == "Microgram/Liter [µg/L]":
            inter = NUMinput * 1*10**-6
        if units_from == "Megagram/Liter [Mg/L]":
            inter = NUMinput * 1000000
        if units_from == "Centigram/Liter [cg/L]":
            inter = NUMinput * 0.01
        if units_from == "Milligram/Liter [mg/L]":
            inter = NUMinput * 0.001
        if units_from == "Pound/Cubic Inch [lb/in\u00b3]":
            inter = NUMinput * 27679.904710191
        if units_from == "Pound/Cubic Foot [lb/ft\u00b3]":
            inter = NUMinput * 16.018463374
        if units_from == "Pound/Cubic Yard [lb/yd\u00b3]":
            inter = NUMinput * 0.5932764213
        if units_from == "Pound/Gallon (US)":
            inter = NUMinput * 119.8264273167
        if units_from == "Pound/Gallon (UK)":
            inter = NUMinput * 99.7763726631
        if units_from == "Ounce/Cubic Inch [oz/in\u00b3]":
            inter = NUMinput * 1729.9940443869
        if units_from == "Ounce/Cubic Foot [oz/ft\u00b3]":
            inter = NUMinput * 1.0011539609
        if units_from == "Ounce/Gallon (US)":
            inter = NUMinput * 7.4891517073
        if units_from == "Ounce/Gallon (UK)":
            inter = NUMinput * 6.2360232914
        if units_from == "Grain/Gallon (US)":
            inter = NUMinput * 0.017118061
        if units_from == "Grain/Gallon (UK)":
            inter = NUMinput * 0.0142537675 
        if units_from == "Grain/Cubic Foot [gr/ft\u00b3]":
            inter = NUMinput * 0.0022883519
        if units_from == "Ton (short)/Cubic Yard":
            inter = NUMinput * 1186.552842515
        if units_from == "Ton (long)/Cubic Yard":
            inter = NUMinput * 1328.9391836174
        if units_from == "Slug/Cubic Foot [slug/ft\u00b3]":
            inter = NUMinput * 515.3788183932
        if units_from == "PSI/1000 Feet":
            inter = NUMinput * 2.3066587258
        if units_from == "Earth's Density (mean)":
            inter = NUMinput * 5517.9999999999
        
        #Standard Time Units in
        if units_from == "Second [sec]":
            inter = NUMinput * 1
        if units_from == "Millisecond [ms]":
            inter = NUMinput * 0.001
        if units_from == "Minute [min]":
            inter = NUMinput * 60
        if units_from == "Hour [hr]":
            inter = NUMinput * 3600
        if units_from == "Day [d]":
            inter = NUMinput * 86400
        if units_from == "Week":
            inter = NUMinput * 604800
        if units_from == "Month":
            inter = NUMinput * 2628000
        if units_from == "Year [y]" or units_from == "Year (Julian)":
            inter = NUMinput * 31557600
        if units_from == "Decade":
            inter = NUMinput * 315576000
        if units_from == "Century":
            inter = NUMinput * 3155760000
        if units_from == "Millenium":
            inter = NUMinput * 31557600000
        if units_from == "Microsecond [µs]":
            inter = NUMinput * 1*10**-6
        if units_from == "Nanosecond [ns]":
            inter = NUMinput * 1*10**-9
        if units_from == "Shake":
            inter = NUMinput * 1*10**-8
        if units_from == "Month (synodic)":
            inter = NUMinput * 2551443.84
        if units_from == "Year (leap)":
            inter = NUMinput * 31622400
        if units_from == "Year (tropical)":
            inter = NUMinput * 31556930
        if units_from == "Year (sidereal)":
            inter = NUMinput * 31558149.54
        if units_from == "Day (sidreal)":
            inter = NUMinput * 86164.09
        if units_from == "Hour (sidereal)":
            inter = NUMinput * 3590.1704166667
        if units_from == "Minute (sidereal)":
            inter = NUMinput * 59.8361736111
        if units_from == "Second (sidereal)":
            inter = NUMinput * 0.9972695602
        if units_from == "Fortnite":
            inter = NUMinput * 1209600
        if units_from == "Septennial":
            inter = NUMinput * 220752000
        if units_from == "Octenial":
            inter = NUMinput * 252288000
        if units_from == "Novennial":
            inter = NUMinput * 283824000
        if units_from == "Plank Time":
            inter = NUMinput * 5.39056*10**-44
        
        #Standard Temperature units in
        if units_from == "Kelvin [K]":
            inter = NUMinput * 1
        if units_from == "Celsius [°C]":
            inter = NUMinput + 273.15
        if units_from == "Fahrenheit [°F]":
            inter = (NUMinput - 32) * 5/9 + 273.15
        if units_from == "Rankine [°R]":
            inter = NUMinput * 0.5555555556
        if units_from == "Reaumur [°r]":
            inter = (NUMinput * 5/4) + 273.15 
        
        #Standard Energy Units in
        if units_from == "Joule [J]" or units_from == "Watt-second [W*s]" or units_from == "Newton Meter [N*m]":
            inter = NUMinput * 1
        if units_from == "Kilojoule [kJ]" or units_from == "Kilowatt-second [kW*sec]":
            inter = NUMinput * 1000
        if units_from == "Kilowatt-hour [kW*hr]":
            inter = NUMinput * 3600000
        if units_from == "Watt-hour [W*hr]":
            inter = NUMinput * 3600
        if units_from == "Calorie (nutritional)" or units_from == "Kilocalorie (IT) [kcal (IT)]":
            inter = NUMinput * 4186.8
        if units_from == "Horsepower (metric) Hour":
            inter = NUMinput * 2647795.5
        if units_from == "Btu (IT) [Btu (IT), Btu]":
            inter = NUMinput * 1055.05585262
        if units_from == "Btu (th) [Btu (th)]":
            inter = NUMinput * 1054.3499999744
        if units_from == "Gigajoule [GJ]":
            inter = NUMinput * 1000000000
        if units_from == "Megajoule [MJ]":
            inter = NUMinput * 1000000
        if units_from == "Megaelectron-volt [MeV]":
            inter = NUMinput * 1.6021766339999*10**-13
        if units_from == "Kiloelectron-volt [KeV]":
            inter = NUMinput * 1.6021766339999*10**-16
        if units_from == "Electron-volt [eV]":
            inter = NUMinput * 1.6021766339999*10**-19
        if units_from == "Erg":
            inter = NUMinput * 1*10**-7
        if units_from == "Gigawatt-hour [GW*hr]":
            inter = NUMinput * 3600000000000
        if units_from == "Megawatt-hour [MW*hr]":
            inter = NUMinput * 3600000000
        if units_from == "Horsepower Hour [hp*hr]":
            inter = NUMinput * 2684519.5368856
        if units_from == "Kilocalorie (th) [kcal (th)]":
            inter = NUMinput * 4184
        if units_from == "Calorie (IT) [cal (IT), cal]":
            inter = NUMinput * 4.1868
        if units_from == "Calorie (th) [cal (th)]":
            inter = NUMinput * 4.184
        if units_from == "Mega Btu (IT) [MBtu (IT)]":
            inter = NUMinput * 1055055852.62
        if units_from == "Ton-hour (refrigeration)":
            inter = NUMinput * 12660670.23144
        if units_from == "Fuel Oil Equivalent @kiloliter":
            inter = NUMinput * 40197627984.822
        if units_from == "Fuel Oil Equivalent @barrel (US)":
            inter = NUMinput * 6383087908.3509
        if units_from == "Gigaton [Gton]":
            inter = NUMinput * 4.184*10**18
        if units_from == "Megaton [Mton]":
            inter = NUMinput * 4.184*10**15
        if units_from == "Kiloton [kton]":
            inter = NUMinput * 4184000000000
        if units_from == "Ton (explosives)":
            inter = NUMinput * 4184000000
        if units_from == "Dyne Centimeter [dyn*cm]":
            inter = NUMinput * 1*10**-7
        if units_from == "Gram-force Meter [gf*m]":
            inter = NUMinput * 0.00980665
        if units_from == "Gram-force Centimeter [gf*cm]":
            inter = NUMinput * 9.80665*10**-5
        if units_from == "Kilogram-force Centimeter":
            inter = NUMinput * 0.098066499997
        if units_from == "Kilogram-force Meter" or units_from == "Kilopond Meter [kp*m]":
            inter = NUMinput * 9.8066499997
        if units_from == "Pound-force Foot [lbf*ft]":
            inter = NUMinput * 1.3558179483
        if units_from == "Pound-force Inch [lbf*in]":
            inter = NUMinput * 0.112984829
        if units_from == "Ounce-force Inch [ozf*in]":
            inter = NUMinput * 0.0070615518
        if units_from == "Foot-pound [ft*lbf]":
            inter = NUMinput * 1.3558179483
        if units_from == "Inch-pound [in*lbf]":
            inter = NUMinput * 0.112984829
        if units_from == "Inch-ounce [in*ozf]":
            inter = NUMinput * 0.0070615518
        if units_from == "Poundal Foot [pdl*ft]":
            inter = NUMinput * 0.04214011
        if units_from == "Therm" or units_from == "Therm (EC)":
            inter = NUMinput * 105505600
        if units_from == "Therm (US)":
            inter = NUMinput * 105480400
        if units_from == "Hartree Energy":
            inter = NUMinput * 4.3597482*10**-18
        if units_from == "Rydberg Constant":
            inter = NUMinput * 2.1798741*10**-18
        
        #Standard Power Units in
        if units_from == "Watt [W]" or units_from == "Volt Ampere [V*A]" or units_from == "Newton Meter/Second [N*m/s]" or units_from == "Joule/Second [J/s]":
            inter = NUMinput * 1
        if units_from == "Gigawatt [GW]" or units_from == "Gigajoule/Second [GJ/s]":
            inter = NUMinput * 1000000000
        if units_from == "Megawatt [MW]" or units_from == "Megajoule/Second [MJ/s]":
            inter = NUMinput * 1000000
        if units_from == "Kilowatt [kW]" or units_from == "Kilovolt Ampere [kV*A]" or units_from == "Kilojoule/Second [kJ/s]":
            inter = NUMinput * 1000
        if units_from == "Milliwatt [mW]" or units_from == "Millijoule/Second [mJ/s]":
            inter = NUMinput * 0.001
        if units_from == "Microwatt [µW]" or units_from == "Microjoule/Second [µJ/s]":
            inter = NUMinput * 1*10**-6
        if units_from == "Nanowatt [nW]" or units_from == "Nanojoule/Second [nJ/s]":
            inter = NUMinput * 1*10**-9
        if units_from == "Horsepower [hp]":
            inter = NUMinput * 745.6998715823
        if units_from == "Horsepower (550 ft*lbf/s)":
            inter = NUMinput * 745.6998715823
        if units_from == "Horsepower (metric)":
            inter = NUMinput * 735.49875
        if units_from == "Horsepower (boiler)":
            inter = NUMinput * 9809.5000000002
        if units_from == "Horsepower (Electric)":
            inter = NUMinput * 746
        if units_from == "Horsepower (water)":
            inter = NUMinput * 746.043
        if units_from == "Pferdestarke (ps)":
            inter = NUMinput * 735.49875
        if units_from == "Btu (IT)/Hour [Btu/hr]":
            inter = NUMinput * 0.2930710702
        if units_from == "Btu (IT)/Minute [Btu/min]":
            inter = NUMinput * 17.5842642103
        if units_from == "Btu (IT)/Second [Btu/sec]":
            inter = NUMinput * 1055.05585262
        if units_from == "Btu (th)/Hour [Btu (th)/hr]":
            inter = NUMinput * 0.292875
        if units_from == "Btu (th)/Minute [Btu (th)/min]":
            inter = NUMinput * 17.5724999996
        if units_from == "Btu (th)/Second [Btu (th)/sec]":
            inter = NUMinput * 1054.3499999744
        if units_from == "MBtu (IT)/Hour [MBtu/hr]":
            inter = NUMinput * 293071.07017222
        if units_from == "MBH":
            inter = NUMinput * 293.0710701722
        if units_from == "Ton (refrigeration)":
            inter = NUMinput * 3516.8528420667
        if units_from == "Kilocalorie (IT)/Hour [kcal/hr]":
            inter = NUMinput * 1.163
        if units_from == "Kilocalorie (IT)/Minute [kcal/min]":
            inter = NUMinput * 69.78
        if units_from == "Kilocalorie (IT)/Second [kcal/sec]":
            inter = NUMinput * 4186.8
        if units_from == "Kilocalorie (th)/Hour [kcal (th)/hr]":
            inter = NUMinput * 1.1622222222
        if units_from == "Kilocalorie (th)/Minute [kcal (th)/min]":
            inter = NUMinput * 69.7333333333
        if units_from == "Kilocalorie (th)/Second [kcal (th)/sec]":
            inter = NUMinput * 4184
        if units_from == "Calorie (IT)/Hour [cal/hr]":
            inter = NUMinput * 0.001163
        if units_from == "Calorie (IT)/Minute [cal/min]":
            inter = NUMinput * 0.06978
        if units_from == "Calorie (IT)/Second [cal/sec]":
            inter = NUMinput * 4.1868
        if units_from == "Calorie (th)/Hour [cal (th)/hr]":
            inter = NUMinput * 0.0011622222
        if units_from == "Calorie (th)/Minute [cal (th)/min]":
            inter = NUMinput * 0.0697333333
        if units_from == "Calorie (th)/Second [cal (th)/sec]":
            inter = NUMinput * 4.184
        if units_from == "Foot Pound-force/Hour":
            inter = NUMinput * 0.0003766161
        if units_from == "Foot Pound-force/Minute":
            inter = NUMinput * 0.0225969658
        if units_from == "Foot Pound-force/Second":
            inter = NUMinput * 1.3558179483
        if units_from == "Pound-foot/Hour [lbf*ft/hr]":
            inter = NUMinput * 0.0003766161
        if units_from == "Pound-foot/Minute [lbf*ft/min]":
            inter = NUMinput * 0.0225969658
        if units_from == "Pound-foot/Second [lbf*ft/sec]":
            inter = NUMinput * 1.3558179483
        if units_from == "Erg/Second [erg/s]":
            inter = NUMinput * 1*10**-7
        if units_from == "Joule/Hour [J/hr]":
            inter = NUMinput * 0.0002777778
        if units_from == "Joule/Minute [J/min]":
            inter = NUMinput * 0.0166666667
        if units_from == "Kilojoule/Hour [kJ/hr]":
            inter = NUMinput * 0.2777777778
        if units_from == "Kilojoule/Minute [kJ/min]":
            inter = NUMinput * 16.6666666667

        #Standard Pressure Units in
        if units_from == "Pascal [Pa]" or units_from == "Newton/Square Meter [N/m\u00b2]":
            inter = NUMinput * 1
        if units_from == "Kilopascal [kPa]" or units_from == "Kilonewton/Square Meter [kN/m\u00b2]":
            inter = NUMinput * 1000
        if units_from == "Bar":
            inter = NUMinput * 100000
        if units_from == "Pound/Square Inch [PSI]":
            inter = NUMinput * 6894.7572931783
        if units_from == "Kip/Square Inch [KSI]":
            inter = NUMinput * 6894757.2931783
        if units_from == "Standard Atmosphere [atm]":
            inter = NUMinput * 101325
        if units_from == "Gigapascal [GPa]":
            inter = NUMinput * 1000000000
        if units_from == "Megapascal [MPa]" or units_from == "Newton/Square Millimeter [N/mm\u00b2]":
            inter = NUMinput * 1000000
        if units_from == "Millipascal [mPa]":
            inter = NUMinput * 0.001
        if units_from == "Micropascal [µPa]":
            inter = NUMinput * 1*10**-6
        if units_from == "Nanopascal [nPa]":
            inter = NUMinput * 1*10**-9
        if units_from == "Newton/Square Centimeter [N/cm\u00b2]":
            inter = NUMinput * 10000
        if units_from == "Millibar [mb, mbar]":
            inter = NUMinput * 100
        if units_from == "Microbar [µb, µbar]" or units_from == "Dyne/Square Centimeter [dyn/cm\u00b2]":
            inter = NUMinput * 0.1
        if units_from == "Kilogram-force/Square Meter [kgf/m\u00b2]":
            inter = NUMinput * 9.80665
        if units_from == "Kilogram-force/Square Centimeter [kfg/cm\u00b2]":
            inter = NUMinput * 98066.5
        if units_from == "Kilogram-force/Square Millimeter [kgf/mm\u00b2]":
            inter = NUMinput * 9806650
        if units_from == "Gram-force/Square Centimeter [gf/cm\u00b2]":
            inter = NUMinput * 98.0665
        if units_from == "Ton-force (short)/Square Foot":
            inter = NUMinput * 95760.517960678
        if units_from == "Ton-force (short)/Square Inch":
            inter = NUMinput * 13789514.586338
        if units_from == "Ton-force (long)/Square Foot":
            inter = NUMinput * 107251.78011595
        if units_from == "Ton-Force (long)/Square Inch":
            inter = NUMinput * 15444256.336697
        if units_from == "Pound-force/Square Foot [lbf/ft\u00b2]":
            inter = NUMinput * 47.8802589804
        if units_from == "Poundal/Square Foot":
            inter = NUMinput * 1.4881639436
        if units_from == "Torr [Torr]":
            inter = NUMinput * 133.3223684211
        if units_from == "Millitorr [mTorr]":
            inter = NUMinput * 0.13332237
        if units_from == "Centimeter Mercury (0°C) [cmHg]":
            inter = NUMinput * 1333.22
        if units_from == "Millimeter Mercury (0°C) [mmHg]":
            inter = NUMinput * 133.322
        if units_from == "Inch Mercury (32°F) [inHg]":
            inter = NUMinput * 3386.38
        if units_from == "Inch Mercury (60°F) [inHg]":
            inter = NUMinput * 3376.85
        if units_from == "Centimeter Water (4°C)":
            inter = NUMinput * 98.0638
        if units_from == "Millimeter Water (4°C)":
            inter = NUMinput * 9.80638
        if units_from == "Inch Water (4°C) [inAq]":
            inter = NUMinput * 249.082
        if units_from == "Foot Water (4°C) [ftAq]":
            inter = NUMinput * 2988.98
        if units_from == "Inch Water (60°F) [inAq]":
            inter = NUMinput * 248.843
        if units_from == "Foot Water (60°F) [ftAq]":
            inter = NUMinput * 2986.116
        if units_from == "Atmosphere Technical [at]":
            inter = NUMinput * 98066.500000003
        
        #Angular plane angle (angular distance) in
        if units_from == "Degree [°]":
            inter = NUMinput * 1
        if units_from == "Radian [rad]":
            inter = NUMinput * (180 / math.pi)
        if units_from == "Grad [^g]" or units_from == "gon":
            inter = NUMinput * 0.9
        if units_from == "Minute [']":
            inter = NUMinput * (1/60)
        if units_from == "Second ['']":
            inter = NUMinput *  (1/3600)
        if units_from == "sign":
            inter = NUMinput * 30
        if units_from == "mil":
            inter = NUMinput * .05625
        if units_from == "Revolution [r]" or units_from == "Circle" or units_from == "Turn":
            inter = NUMinput * 360
        if units_from == "Quadrant" or units_from == "Right Angle":
            inter = NUMinput * 90
        if units_from == "Sextant":
            inter = NUMinput * 60
        
        #Angular units angular velocity in
        if units_from == "Radian/Second [rad/sec]":
            inter = NUMinput * 1
        if units_from == "Radian/Day [rad/d]":
            inter = NUMinput * 1.15741*10**-5
        if units_from == "Radian/Hour [rad/hr]":
            inter = NUMinput * (1/3600)
        if units_from == "Radian/Minute [rad/min]":
            inter = NUMinput * (1/60)
        if units_from == "Degree/Day [°/d]":
            inter = NUMinput * 2.0200570046231*10**-7
        if units_from == "Degree/Hour [°/hr]":
            inter = NUMinput * 4.8481368110954*10**-6
        if units_from == "Degree/Minute [°/min]":
            inter = NUMinput * 0.0002908882
        if units_from == "Degree/Second [°/sec]":
            inter = NUMinput * 0.0174532925
        if units_from == "Revolution/Day [r/d]":
            inter = NUMinput * 7.27221*10**-5
        if units_from == "Revolution/Hour [r/hr]":
            inter = NUMinput * 0.0017453293
        if units_from == "Revolution/Minute [r/min, RPM]":
            inter = NUMinput * 0.1047197551
        if units_from == "Revolution/Second [r/sec]":
            inter = NUMinput * 6.2831853072
            
        #Angular units angular acceleration in
        if units_from == "Radian/Square Second [rad/s\u00b2]":
            inter = NUMinput * 1
        if units_from == "Radian/Square Minute":
            inter = NUMinput * (1/(60**2))
        if units_from == "Revolution/Square Second [r/s\u00b2]":
            inter = NUMinput * 6.2831853069
        if units_from == "Revolution/Minute/Second":
            inter = NUMinput * 0.1047197551
        if units_from == "Revolution/Square Minute":
            inter = NUMinput * 0.0017453293
        
        #Fluid Volume units in
        if units_from == "Cubic Meter [m\u00b3]" or units_from == "Kiloliter [kL]" or units_from == "Stere [st]":
            inter = NUMinput * 1
        if units_from == "Cubic Kilometer [km\u00b3]":
            inter = NUMinput * 1000000000
        if units_from == "Cubic Centimeter [cm\u00b3]" or units_from == "Milliliter [mL]" or units_from == "CC [cc, cm\u00b3]":
            inter = NUMinput * 1*10**-6
        if units_from == "Cubic Millimeter [mm\u00b3]":
            inter = NUMinput * 1*10**-9
        if units_from == "Liter [L, l]":
            inter = NUMinput * 0.001
        if units_from == "Gallon (US) [gal (US)]":
            inter = NUMinput * 0.0037854118
        if units_from == "Quart (US) [qt (US)]":
            inter = NUMinput * 0.0009463529
        if units_from == "Pint (US) [pt (US)]":
            inter = NUMinput * 0.0004731765
        if units_from == "Cup (US)":
            inter = NUMinput * 0.0002365882
        if units_from == "Tablespoon (US)":
            inter = NUMinput * 1.47868*10**-5
        if units_from == "Teaspoon (US)":
            inter = NUMinput * 4.92892159375*10**-6
        if units_from == "Cubic Mile [mi\u00b3]":
            inter = NUMinput * 4168181825.4406
        if units_from == "Cubic Yard [yd\u00b3]":
            inter = NUMinput * 0.764554858
        if units_from == "Cubic Foot [ft\u00b3]":
            inter = NUMinput * 0.0283168466
        if units_from == "Cubic Inch [in\u00b3]":
            inter = NUMinput * 1.63871*10**-5
        if units_from == "Gigaliter [GL]":
            inter = NUMinput * 1000000
        if units_from == "Megaliter [ML]":
            inter = NUMinput * 1000
        if units_from == "Drop":
            inter = NUMinput * 5*10**-8
        if units_from == "Barrel (oil) [bbl (oil)]":
            inter = NUMinput * 0.1589872949
        if units_from == "Barrel (US) [bbl (US)]":
            inter = NUMinput * 0.1192404712
        if units_from == "Barrel (UK) [bbl (UK)]":
            inter = NUMinput * 0.16365924
        if units_from == "Gallon (UK) [gal (UK)]":
            inter = NUMinput * 0.00454609
        if units_from == "Quart (UK) [qt (UK)]":
            inter = NUMinput * 0.0011365225
        if units_from == "Pint (UK) [pt (UK)]":
            inter = NUMinput * 0.0005682613
        if units_from == "Cup (metric)":
            inter = NUMinput * 0.00025
        if units_from == "Cup (UK)":
            inter = NUMinput * 0.0002841306
        if units_from == "Fluid Ounce (US) [fl oz (US)]":
            inter = NUMinput * 2.95735*10**-5
        if units_from == "Fluid Ounce (UK) [fl oz (UK)]":
            inter = NUMinput * 2.84131*10**-5
        if units_from == "Tablespoon (metric)":
            inter = NUMinput * 1.5*10**-5
        if units_from == "Tablespoon (UK)":
            inter = NUMinput * 1.77582*10**-5
        if units_from == "Dessertspoon (US)":
            inter = NUMinput * 9.8578431875*10**-6
        if units_from == "Dessertspoon (UK)":
            inter = NUMinput * 1.18388*10**-5
        if units_from == "Teaspoon (metric)":
            inter = NUMinput * 5*10**-6
        if units_from == "Teaspoon (UK)":
            inter = NUMinput * 5.9193880208333*10**-6
        if units_from == "Gil (US) [gi]":
            inter = NUMinput * 0.0001182941
        if units_from == "Gil (UK) [gi (UK)]":
            inter = NUMinput * 0.0001420653
        if units_from == "Minim (US)":
            inter = NUMinput * 6.1611519921875*10**-8
        if units_from == "Minim (UK)":
            inter = NUMinput * 5.9193880208333*10**-8
        if units_from == "Ton Register [ton reg]":
            inter = NUMinput * 2.8316846592
        if units_from == "ccf":
            inter = NUMinput * 2.8316846592
        if units_from == "Hundred-cubic foot":
            inter = NUMinput * 2.8316846592
        if units_from == "Acre-foot [ac*ft]":
            inter = NUMinput * 1233.4818375475
        if units_from == "Acre-foot (US survey)":
            inter = NUMinput * 1233.4892384682
        if units_from == "Acre-inch [ac*in]":
            inter = NUMinput * 102.790153129
        if units_from == "Dekastere":
            inter = NUMinput * 10
        if units_from == "Cord [cd]":
            inter = NUMinput * 3.6245563638
        if units_from == "Decistere":
            inter = NUMinput * 0.1
        if units_from == "Tun":
            inter = NUMinput * 0.9539237696
        if units_from == "Hogshead":
            inter = NUMinput * 0.2384809424
        if units_from == "Board foot":
            inter = NUMinput * 0.0023597372
        if units_from == "Dram [dr]":
            inter = NUMinput * 3.6966911953125*10**-6
        if units_from == "Earth's Volume":
            inter = NUMinput * 1.083*10**21
        
        #Fluid Volume Dry units in
        if units_from == "Liter [L, l]":
            inter = NUMinput * 1
        if units_from == "Barrel Dry (US) [bbl dry (US)]":
            inter = NUMinput * 115.6271236039
        if units_from == "Pint dry (US) [pt dry (US)]":
            inter = NUMinput * 0.5506104714
        if units_from == "Quart dry (US) [qt dry (US)]":
            inter = NUMinput * 1.1012209428
        if units_from == "Peck (US) [pk (US)]":
            inter = NUMinput * 8.8097675424
        if units_from == "Peck (UK) [pk (UK)]":
            inter = NUMinput * 9.09218
        if units_from == "Bushel (US) [bu (US)]":
            inter = NUMinput * 35.2390701696
        if units_from == "Bushel (UK) [bu (UK)]":
            inter = NUMinput * 36.36872
        
        #Fluid Specific volume units in
        if units_from == "Cubic Meter/Kilogram" or units_from == "Liter/Gram [L/g]":
            inter = NUMinput * 1
        if units_from == "Cubic Centimeter/Gram" or units_from == "Liter/Kilogram [L/kg]":
            inter = NUMinput * 0.001
        if units_from == "Cubic Foot/Kilogram [ft\u00b3/kg]":
            inter = NUMinput * 0.0283168466
        if units_from == "Cubic Foot/Pound [ft\u00b3/lb]":
            inter = NUMinput * 0.06242796
        if units_from == "Gallon (US)/Pound":
            inter = NUMinput * 0.0083454039
        if units_from == "Gallon (UK)/Pound":
            inter = NUMinput * 0.0100224128
            
        #Fluid Flow units in
        if units_from == "Cubic Meter/Second [m\u00b3/sec]":
            inter = NUMinput * 1
        if units_from == "Cubic Meter/Day [m\u00b3/d]":
            inter = NUMinput * 1.15741*10**-5
        if units_from == "Cubic Meter/Hour [m\u00b3/hr]":
            inter = NUMinput * 0.0002777778
        if units_from == "Cubic Meter/Minute":
            inter = NUMinput * 0.0166666667
        if units_from == "Cubic Centimeter/Day" or units_from == "Milliliter/Day [mL/d]":
            inter = NUMinput * 1.1574074074074*10**-11
        if units_from == "Cubic Centimeter/Hour" or units_from == "Milliliter/Hour [mL/hr]":
            inter = NUMinput * 2.7777777777778*10**-10
        if units_from == "Cubic Centimeter/Minute" or units_from == "Milliliter/Minute [mL/min]":
            inter = NUMinput * 1.6666666666667*10**-8
        if units_from == "Cubic Centimeter/Second" or units_from == "Milliliter/Second [mL/sec]":
            inter = NUMinput * 1.0*10**-6
        if units_from == "Liter/Day [L/d]":
            inter = NUMinput * 1.1574074074074*10**-8
        if units_from == "Liter/Hour [L/hr]":
            inter = NUMinput * 2.7777777777778*10**-7
        if units_from == "Liter/Minute [L/min]":
            inter = NUMinput * 1.66667*10**-5
        if units_from == "Liter/Second [L/sec]":
            inter = NUMinput * 0.001
        if units_from == "Gallon (US)/Day [gal (US)/d]":
            inter = NUMinput * 4.3812636388889*10**-8
        if units_from == "Gallon (US)/Hour [gal (US)/hr]":
            inter = NUMinput * 1.0515032733333*10**-6
        if units_from == "Gallon (US)/Minute [gal (US)/min]":
            inter = NUMinput * 6.30902*10**-5
        if units_from == "Gallon (US)/Second [gal (US)/sec]":
            inter = NUMinput * 0.0037854118
        if units_from == "Gallon (UK)/Day [gal (UK)/d]":
            inter = NUMinput * 5.2616782407407*10**-8
        if units_from == "Gallon (UK)/Hour [gal (UK)/hr]":
            inter = NUMinput * 1.2628027777778*10**-6
        if units_from == "Gallon (UK)/Minute [gal (UK)/min]":
            inter = NUMinput * 7.57682*10**-5
        if units_from == "Gallon (UK)/Second [gal (UK)/sec]":
            inter = NUMinput * 0.00454609
        if units_from == "Kilobarrel (US)/Day":
            inter = NUMinput * 0.0018401307
        if units_from == "Barrel (US)/Day [bbl (US)/d]":
            inter = NUMinput * 1.8401307283333*10**-6
        if units_from == "Barrel (US)/Hour [bbl (US)/hr]":
            inter = NUMinput * 4.41631*10**-5
        if units_from == "Barrel (US)/Minute":
            inter = NUMinput * 0.0026497882
        if units_from == "Barrel (US)/Second":
            inter = NUMinput * 0.1589872949
        if units_from == "Acre-foot/Year [ac*ft/y]":
            inter = NUMinput * 3.91136*10**-5
        if units_from == "Acre-foot/Day [cs*ft/d]":
            inter = NUMinput * 0.0142764673
        if units_from == "Acre-foot/Hour [ac*ft/hr]":
            inter = NUMinput * 0.3426352143
        if units_from == "Hundred-cubic Foot/Day":
            inter = NUMinput * 3.27741*10**-5
        if units_from == "Hundred-cubic Foot/Hour":
            inter = NUMinput * 0.0007865791
        if units_from == "Hundred-cubic Foot/Minute":
            inter = NUMinput * 0.0471947443
        if units_from == "Ounce/Hour [oz/hr]":
            inter = NUMinput * 8.2148693229167*10**-9
        if units_from == "Ounce/Minute [oz/min]":
            inter = NUMinput * 4.92892159375*10**-7
        if units_from == "Ounce/Seccond [oz/sec]":
            inter = NUMinput * 2.95735*10**-5
        if units_from == "Ounce (UK)/Hour [oz (UK)/hr]":
            inter = NUMinput * 7.8925178504774*10**-9
        if units_from == "Ounce (UK)/Minute":
            inter = NUMinput * 4.7355107102865*10**-7
        if units_from == "Ounce (UK)/Second":
            inter = NUMinput * 2.84131*10**-5
        if units_from == "Cubic Yard/Hour [yd\u00b3/hr]":
            inter = NUMinput * 0.0002123763
        if units_from == "Cubic Yard/Minute [yd\u00b3/min]":
            inter = NUMinput * 0.012742581
        if units_from == "Cubic Yard/Second [yd\u00b3/sec]":
            inter = NUMinput * 0.764554858
        if units_from == "Cubic Foot/Hour [ft\u00b3/hr]":
            inter = NUMinput * 7.86579072*10**-6
        if units_from == "Cubic Foot/Minute [ft\u00b3/min]":
            inter = NUMinput * 0.0004719474
        if units_from == "Cubic Foot/Second [ft\u00b3/sec]":
            inter = NUMinput * 0.0283168466
        if units_from == "Cubic Inch/Hour [in\u00b3/hr]":
            inter = NUMinput * 4.5519622224454*10**-9
        if units_from == "Cubic Inch/Minute [in\u00b3/min]":
            inter = NUMinput * 2.7311773333333*10**-7
        if units_from == "Cubic Inch/Second [in\u00b3/sec]":
            inter = NUMinput * 1.63871*10**-5
        
        #Fluid Viscosity (Dynamic) units in
        if units_from == "Pascal Second [pa*s]" or units_from == "Newton Second/Square Meter":
            inter = NUMinput * 1
        if units_from == "Kilogram-force Second/Square Meter":
            inter = NUMinput * 9.80665
        if units_from == "Millinewton Second/Square Meter" or units_from == "Centipoise [cP]":
            inter = NUMinput * 0.001
        if units_from == "Dyne Second/Square Meter" or units_from == "Poise [P]" or units_from == "Gram/Centimeter/Second":
            inter = NUMinput * 0.1
        if units_from == "Gigapoise [GP]":
            inter = NUMinput * 100000000
        if units_from == "Megapoise [MP]":
            inter = NUMinput * 100000
        if units_from == "Kilopoise [kP]":
            inter = NUMinput * 100
        if units_from == "Millipoise [mP]":
            inter = NUMinput * 0.0001
        if units_from == "Micropoise [µP]":
            inter = NUMinput * 1*10**-7
        if units_from == "Pound-Force Second/Square Inch":
            inter = NUMinput * 6894.7572931684
        if units_from == "Pound-Force Second/Square Foot" or units_from == "Slug/Foot/Second":
            inter = NUMinput * 47.8802589802
        if units_from == "Poundal Second/Square Foot" or units_from == "Pound/Foot/Second":
            inter = NUMinput * 1.4881639436
        if units_from == "Pound/Foot/Hour [lb/(ft*hr)]":
            inter = NUMinput * 0.0004133789
        
        #Fluid Viscosity (kinematic) units in
        if units_from == "Square Meter/Second":
            inter = NUMinput * 1
        if units_from == "Square Meter/Hour [m\u00b2/hr]":
            inter = NUMinput * 0.0002777778
        if units_from == "Square Centimeter/Second":
            inter = NUMinput * 0.0001
        if units_from == "Square Millimeter/Second":
            inter = NUMinput * 1*10**-6
        if units_from == "Square Foot/Second [ft\u00b2/sec]":
            inter = NUMinput * 0.09290304
        if units_from == "Square Foot/Hour [ft\u00b2/hr]":
            inter = NUMinput * 2.58064*10**-5
        if units_from == "Square Inch/Second [in\u00b2/sec]":
            inter = NUMinput * 0.00064516
        if units_from == "Stokes [St]":
            inter = NUMinput * 0.0001
        if units_from == "Gigastokes [GSt]":
            inter = NUMinput * 100000
        if units_from == "Megastokes [MSt]":
            inter = NUMinput * 100
        if units_from == "Kilostokes [kSt]":
            inter = NUMinput * 0.1
        if units_from == "Centistokes [cSt]":
            inter = NUMinput * 1*10**-6
        if units_from == "Millistokes [mSt]":
            inter = NUMinput * 1*10**-7
        if units_from == "Microstokes [µSt]":
            inter = NUMinput * 1*10**-10
        
        #Fluid Surface Tension units in
        if units_from == "Newton/Meter [N/m]":
            inter = NUMinput * 1
        if units_from == "Millinewton/Meter [mN/m]":
            inter = NUMinput * 0.001
        if units_from == "Gram-force/Centimeter":
            inter = NUMinput * 0.980665
        if units_from == "Dyne/Centimeter [dyn/cm]" or units_from == "Erg/Square Centimeter":
            inter = NUMinput * 0.001
        if units_from == "Erg/Square Millimeter":
            inter = NUMinput * 0.1
        if units_from == "Poundal/Inch [pd/in]":
            inter = NUMinput * 5.443108491
        if units_from == "Pound-force/Inch [lbf/in]":
            inter = NUMinput * 175.1268369864
        
        #Electricity electrical charge units in
        if units_from == "Coulomb [C]" or units_from == "Ampere-second [A*sec]":
            inter = NUMinput * 1
        if units_from == "Meagcoulomb [MC]":
            inter = NUMinput * 1000000
        if units_from == "Kilocoulomb [kC]":
            inter = NUMinput * 1000
        if units_from == "Millicoulomb [mC]":
            inter = NUMinput * 0.001
        if units_from == "Microcoulmob [µC]":
            inter = NUMinput * 1*10**-6
        if units_from == "EMU of Charge" or units_from == "aAbcoulomb [abC]":
            inter = NUMinput * 10
        if units_from == "Statcoulomb [stC]" or units_from == "ESU of Charge" or units_from == "Franklin [Fr]":
            inter = NUMinput * 3.335640951982*10**-10
        if units_from == "Ampere-hour [A*hr]":
            inter = NUMinput * 3600
        if units_from == "Ampere-minute [A*min]":
            inter = NUMinput * 60
        if units_from == "Faraday (based on carbon 12)":
            inter = NUMinput * 96485.309000004
        if units_from == "Elementary Charge [e]":
            inter = NUMinput * 1.60217733*10**-19
        
        #Electricity electric potential units in
        if units_from == "Volt [V]" or units_from == "Watt/Ampere [W/A]":
            inter = NUMinput * 1
        if units_from == "Kilovolt [kV]":
            inter = NUMinput * 1000
        if units_from == "Millivolt [mV]":
            inter = NUMinput * 0.001
        if units_from == "Abvolt [abV]" or units_from == "EMU of Electric Potential":
            inter = NUMinput * 1*10**-8
        if units_from == "Statvolt [stV]" or units_from == "ESU of Electric Potential":
            inter = NUMinput * 299.7925
        
        #Electricity Current units in
        if units_from == "Ampere [A]":
            inter = NUMinput * 1
        if units_from == "Kiloampere [kA]":
            inter = NUMinput * 1000
        if units_from == "Milliampere [mA]":
            inter = NUMinput * 0.001
        if units_from == "Biot [Bi]" or units_from == "Abampere [abA]" or units_from == "EMU of Current" or units_from == "CGS e.m. Unit":
            inter = NUMinput * 10
        if units_from == "Statampere [stA]" or units_from == "ESU of Current" or units_from == "CGS e.s. Unit":
            inter = NUMinput * 3.335641*10**-10
        
        #Electricity Resistance units in
        if units_from == "Ohm [Ω]" or units_from == "Volt/Ampere [V/A]" or units_from == "Reciprocal Siemens [1/S]":
            inter = NUMinput * 1
        if units_from == "Megaohm [MΩ]":
            inter = NUMinput * 1000000
        if units_from == "Kiloohm [kΩ]":
            inter = NUMinput * 1000
        if units_from == "Milliohm [mΩ]":
            inter = NUMinput * 0.001
        if units_from == "Microohm [μΩ]":
            inter = NUMinput * 1*10**-6
        if units_from == "Abohm" or units_from == "EMU of Resistance":
            inter = NUMinput * 1*10**-9
        if units_from == "Statohm" or units_from == "ESU of Resistance":
            inter = NUMinput * 898755200000
        if units_from == "Quantized Hall Resistance":
            inter = NUMinput * 25812.8056
        
        #Electricity Capacitance units in
        if units_from == "Farad [F]" or units_from == "Coulomb/Volt [C/V]":
            inter = NUMinput * 1
        if units_from == "Gigafarad [GF]":
            inter = NUMinput * 1000000000
        if units_from == "Megafarad [MF]":
            inter = NUMinput * 1000000
        if units_from == "Kilofarad [kF]":
            inter = NUMinput * 1000
        if units_from == "Centifarad [cF]":
            inter = NUMinput * 0.01
        if units_from == "Millifarad [mF]":
            inter = NUMinput * 0.001
        if units_from == "Microfarad [μF]":
            inter = NUMinput * 1*10**-6
        if units_from == "Nanofarad [nF]":
            inter = NUMinput * 1*10**-9
        if units_from == "Picofarad [pF]":
            inter = NUMinput * 1*10**-12
        if units_from == "Abfarad [abF]" or units_from == "EMU of Capacitance":
            inter = NUMinput * 1000000000
        if units_from == "Statfarad [stF]" or units_from == "ESU of Capacitance":
            inter = NUMinput * 1.112650056054*10**-12
        
        #Electricity Inductance units in
        if units_from == "Henry [H]" or units_from == "Weber/Ampere [Wb/A]":
            inter = NUMinput * 1
        if units_from == "Gigahenry [GH]":
            inter = NUMinput * 1000000000
        if units_from == "Megahenry [MH]":
            inter = NUMinput * 1000000
        if units_from == "Kilohenry [kH]":
            inter = NUMinput * 1000
        if units_from == "Centihenry [cH]":
            inter = NUMinput * 0.01
        if units_from == "Millihenry [mH]":
            inter = NUMinput * 0.001
        if units_from == "Microhenry [µH]":
            inter = NUMinput * 1*10**-6
        if units_from == "Nanohenry [nH]":
            inter = NUMinput * 1*10**-9
        if units_from == "Picohenry [pH]":
            inter = NUMinput * 1*10**-12
        if units_from == "Abhenry [abH]" or units_from == "EMU of Inductance":
            inter = NUMinput * 1*10**-9
        if units_from == "Stathenry [stH]" or units_from == "ESU of Inductance":
            inter = NUMinput * 898755200000
        
        #Electricity Conductance units in
        if units_from == "Siemens [S]" or units_from == "Ampere/Volt [A/V]" or units_from == "Mho":
            inter = NUMinput * 1
        if units_from == "Megasiemens [MS]":
            inter = NUMinput * 1000000
        if units_from == "Kilosiemens [kS]":
            inter = NUMinput * 1000
        if units_from == "Millisiemens [mS]":
            inter = NUMinput * 0.001
        if units_from == "Microsiemens [µS]" or units_from == "Gemmho" or units_from == "Micromho":
            inter = NUMinput * 1*10**-6
        if units_from == "Abmho":
            inter = NUMinput * 1000000000
        if units_from == "Statmho":
            inter = NUMinput * 1.1123470522803*10**-12
        if units_from == "Quantized Hall Conductance":
            inter = NUMinput * 3.87405*10**-5
            
    #converting from standard to output unit
        #standard linear length units out
        if units_to == "Meter [m]":
            NUMout = inter / 1
        if units_to == "Kilometer [km]":
            NUMout = inter / 1000
        if units_to == "Centimeter [cm]":
            NUMout = inter / 0.01
        if units_to == "Millimeter [mm]":
            NUMout = inter / 0.001
        if units_to == "Micrometer [μm, μ]" or units_to == "Micron [μ]":
            NUMout = inter / 1*10**6
        if units_to == "Nanometer [nm]":
            NUMout = inter / 1*10**9
        if units_to == "Mile [mi, mi (int.)]":
            NUMout = inter / 1609.344
        if units_to == "Yard [yd]":
            NUMout = inter / 0.9144
        if units_to == "Foot [ft]":
            NUMout = inter / 0.3048
        if units_to == "Inch [in]":
            NUMout = inter / 0.0254
        if units_to == "Light Year [ly]":
            NUMout = inter / 9.46073047258*10**15
        if units_to == "Gigameter [Gm]":
            NUMout = inter / 1000000000
        if units_to == "Megameter [Mm]":
            NUMout = inter / 1000000
        if units_to == "Megaparsec [Mpc]":
            NUMout = inter / 3.085677581288*10**22
        if units_to == "Kiloparsec [kpc]":
            NUMout = inter / 3.08567758128*10**19
        if units_to == "Parsec [pc]":
            NUMout = inter / 3.08567758128*10**16
        if units_to == "Astronomical Unit [AU, UA]":
            NUMout = inter / 149597870691
        if units_to == "League [lea]":
            NUMout = inter / 4828.032
        if units_to == "Nautical League (UK)":
            NUMout = inter / 5559.552
        if units_to == "Nautical League (int)":
            NUMout = inter / 5556
        if units_to == "League (statute) [st.league]":
            NUMout = inter / 4828.0416560833
        if units_to == "Nautical Mile (UK) [NM (UK)]":
            NUMout = inter / 1853.184
        if units_to == "Nautical Mile (international)":
            NUMout = inter / 1852
        if units_to == "Mile (statute) [mi, mi(US)]" or units_to == "Mile (US survey) [mi]":
            NUMout = inter / 1609.3472186944
        if units_to == "Mile (Roman)":
            NUMout = inter / 1479.804
        if units_to == "Kiloyard [kyd]":
            NUMout = inter / 914.4
        if units_to == "Furlong [fur]":
            NUMout = inter / 201.168
        if units_to == "Furlong (US survey) [fur]":
            NUMout = inter / 201.1684023368
        if units_to == "Chain [ch]":
            NUMout = inter / 20.1168
        if units_to == "Chain (US survey) [ch]":
            NUMout = inter / 20.1168402337
        if units_to == "Rope":
            NUMout = inter / 6.096
        if units_to == "Rod [rd]" or units_to == "Perch" or units_to == "Pole":
            NUMout = inter / 5.0292
        if units_to == "Rod (US survey) [rd]":
            NUMout = inter / 5.0292100584
        if units_to == "Fathom [fath]":
            NUMout = inter / 1.8288
        if units_to == "Fathom (US survey) [fath]":
            NUMout = inter / 1.8288036576
        if units_to == "Ell":
            NUMout = inter / 1.143
        if units_to == "Foot (US survey) [ft]":
            NUMout = inter / 0.3048006096
        if units_to == "Link [li]":
            NUMout = inter / 0.201168
        if units_to == "Link (US survey) [li]":
            NUMout = inter / 0.2011684023
        if units_to == "Cubit (UK)":
            NUMout = inter / 0.4572
        if units_to == "Hand":
            NUMout = inter / 0.1016
        if units_to == "Span (cloth)":
            NUMout = inter / 0.2286
        if units_to == "Finger (cloth)":
            NUMout = inter / 0.1143
        if units_to == "Nail (cloth)":
            NUMout = inter / 0.05715
        if units_to == "Inch (US survey) [in]":
            NUMout = inter / 0.0254000508
        if units_to == "Barleycorn":
            NUMout = inter / 0.0084666667
        if units_to == "mil [mil, thou]":
            NUMout = inter / 2.54*10**5
        if units_to == "Microinch":
            NUMout = inter / 2.54*10**8
        if units_to == "Angstrom [A]":
            NUMout = inter / 1*10**10
        if units_to == "a.u. of length [a.u., b]":
            NUMout = inter / 5.2917724900001*10**11
        if units_to == "X-unit [X]":
            NUMout = inter / 1.00208*10**13
        if units_to == "Fermi [F, f]":
            NUMout = inter / 1*10**15
        if units_to == "Arpent":
            NUMout = inter / 58.5216
        if units_to == "Pica":
            NUMout = inter / 0.0042333333
        if units_to == "Point":
            NUMout = inter / 0.0003527778
        if units_to == "Twip":
            NUMout = inter / 1.76389*10**5
        if units_to == "Aln":
            NUMout = inter / 0.5937777778
        if units_to == "Famn":
            NUMout = inter / 1.7813333333
        if units_to == "Caliber [cl]" or units_to == "Cenitinch [cin]":
            NUMout = inter / 0.000254
        if units_to == "Ken":
            NUMout = inter / 2.11836
        if units_to == "Long Reed":
            NUMout = inter / 3.2004
        if units_to == "Reed":
            NUMout = inter / 2.7432
        if units_to == "Plank Length":
            NUMout = inter / 1.61605*10**35
        if units_to == "Electron Radius (classical)":
            NUMout = inter / 2.81794092*10**15
        if units_to == "Bohr Radius [b, a.u.]":
            NUMout = inter / 5.291772490000*10**11
        if units_to == "Earth's Equitorial Radius":
            NUMout = inter / 6378160
        if units_to == "Earth's Polar Radius":
            NUMout = inter / 6356776.9999999
        if units_to == "Earth's Distance From the Sun":
            NUMout = inter / 149600000000
        if units_to == "Sun's Radius":
            NUMout = inter / 696000000
        
        #standard area units out
        if units_to == "Square Meter [m\u00b2]":
            NUMout = inter / 1
        if units_to == "Square Kilometer [km\u00b2]":
            NUMout = inter / 1000000
        if units_to == "Square Centimeter [cm\u00b2]":
            NUMout = inter / 0.0001
        if units_to == "Square Millimeter [mm\u00b2]":
            NUMout = inter / 1*10**6
        if units_to == "Square Micrometer [μm\u00b2]":
            NUMout = inter / 1*10**12
        if units_to == "Hectare [ha]":
            NUMout = inter / 10000
        if units_to == "Acre [ac]":
            NUMout = inter / 4046.8564224
        if units_to == "Square Mile [mi\u00b2]" or units_to == "Section":
            NUMout = inter / 2589988.110336
        if units_to == "Square Yard [yd\u00b2]":
            NUMout = inter / 0.83612736
        if units_to == "Square Foot [ft\u00b2]":
            NUMout = inter / 0.09290304
        if units_to == "Square Inch [in\u00b2]":
            NUMout = inter / 0.00064516
        if units_to == "Are [a]":
            NUMout = inter / 100
        if units_to == "Barn [b]":
            NUMout = inter / 1*10**28
        if units_to == "Square Mile (US survey)":
            NUMout = inter / 2589998.4703195
        if units_to == "Square Foot (US survey)":
            NUMout = inter / 0.0929034116
        if units_to == "Circular Inch":
            NUMout = inter / 0.0005067075
        if units_to == "Township":
            NUMout = inter / 93239571.972096
        if units_to == "Acre (US survey) [ac]":
            NUMout = inter / 4046.8726098743
        if units_to == "Rood":
            NUMout = inter / 1011.7141056
        if units_to == "Square Chain [ch\u00b2]":
            NUMout = inter / 404.68564224
        if units_to == "Square Rod" or units_to == "Square Perch" or units_to == "Square Pole":
            NUMout = inter / 25.29285264
        if units_to == "Square Rod (US survey)":
            NUMout = inter / 25.2929538117
        if units_to == "Square Mil [mil\u00b2]":
            NUMout = inter / 6.4516*10**10
        if units_to == "Circular Mil":
            NUMout = inter / 5.067074790975*10**10
        if units_to == "Homestead":
            NUMout = inter / 647497.027584
        if units_to == "Electron Cross Section":
            NUMout = inter / 6.6524615999999*10**29
        
        #Standard Volume units out
        if units_to == "Cubic Meter [m\u00b3]" or units_to == "Kiloliter [kL]" or units_to == "Stere [st]":
            NUMout = inter / 1
        if units_to == "Cubic Kilometer [km\u00b3]":
            NUMout = inter / 1000000000
        if units_to == "Cubic Centimeter [cm\u00b3]" or units_to == "Milliliter [mL]" or units_to == "CC [cc, cm\u00b3]":
            NUMout = inter / 1*10**6
        if units_to == "Cubic Millimeter [mm\u00b3]":
            NUMout = inter / 1*10**9
        if units_to == "Liter [L, l]":
            NUMout = inter / 0.001
        if units_to == "Gallon (US) [gal (US)]":
            NUMout = inter / 0.0037854118
        if units_to == "Quart (US) [qt (US)]":
            NUMout = inter / 0.0009463529
        if units_to == "Pint (US) [pt (US)]":
            NUMout = inter / 0.0004731765
        if units_to == "Cup (US)":
            NUMout = inter / 0.0002365882
        if units_to == "Tablespoon (US)":
            NUMout = inter / 1.47868*10**5
        if units_to == "Teaspoon (US)":
            NUMout = inter / 4.92892159375*10**6
        if units_to == "Cubic Mile [mi\u00b3]":
            NUMout = inter / 4168181825.4406
        if units_to == "Cubic Yard [yd\u00b3]":
            NUMout = inter / 0.764554858
        if units_to == "Cubic Foot [ft\u00b3]":
            NUMout = inter / 0.0283168466
        if units_to == "Cubic Inch [in\u00b3]":
            NUMout = inter / 1.63871*10**5
        if units_to == "Gigaliter [GL]":
            NUMout = inter / 1000000
        if units_to == "Megaliter [ML]":
            NUMout = inter / 1000
        if units_to == "Drop":
            NUMout = inter / 5*10**8
        if units_to == "Barrel (oil) [bbl (oil)]":
            NUMout = inter / 0.1589872949
        if units_to == "Barrel (US) [bbl (US)]":
            NUMout = inter / 0.1192404712
        if units_to == "Barrel (UK) [bbl (UK)]":
            NUMout = inter / 0.16365924
        if units_to == "Gallon (UK) [gal (UK)]":
            NUMout = inter / 0.00454609
        if units_to == "Quart (UK) [qt (UK)]":
            NUMout = inter / 0.0011365225
        if units_to == "Pint (UK) [pt (UK)]":
            NUMout = inter / 0.0005682613
        if units_to == "Cup (metric)":
            NUMout = inter / 0.00025
        if units_to == "Cup (UK)":
            NUMout = inter / 0.0002841306
        if units_to == "Fluid Ounce (US) [fl oz (US)]":
            NUMout = inter / 2.95735*10**5
        if units_to == "Fluid Ounce (UK) [fl oz (UK)]":
            NUMout = inter / 2.84131*10**5
        if units_to == "Tablespoon (metric)":
            NUMout = inter / 1.5*10**5
        if units_to == "Tablespoon (UK)":
            NUMout = inter / 1.77582*10**5
        if units_to == "Dessertspoon (US)":
            NUMout = inter / 9.8578431875*10**6
        if units_to == "Dessertspoon (UK)":
            NUMout = inter / 1.18388*10**5
        if units_to == "Teaspoon (metric)":
            NUMout = inter / 5*10**6
        if units_to == "Teaspoon (UK)":
            NUMout = inter / 5.9193880208333*10**6
        if units_to == "Gil (US) [gi]":
            NUMout = inter / 0.0001182941
        if units_to == "Gil (UK) [gi (UK)]":
            NUMout = inter / 0.0001420653
        if units_to == "Minim (US)":
            NUMout = inter / 6.1611519921875*10**8
        if units_to == "Minim (UK)":
            NUMout = inter / 5.9193880208333*10**8
        if units_to == "Ton Register [ton reg]":
            NUMout = inter / 2.8316846592
        if units_to == "ccf":
            NUMout = inter / 2.8316846592
        if units_to == "Hundred-cubic foot":
            NUMout = inter / 2.8316846592
        if units_to == "Acre-foot [ac*ft]":
            NUMout = inter / 1233.4818375475
        if units_to == "Acre-foot (US survey)":
            NUMout = inter / 1233.4892384682
        if units_to == "Acre-inch [ac*in]":
            NUMout = inter / 102.790153129
        if units_to == "Dekastere":
            NUMout = inter / 10
        if units_to == "Cord [cd]":
            NUMout = inter / 3.6245563638
        if units_to == "Decistere":
            NUMout = inter / 0.1
        if units_to == "Tun":
            NUMout = inter / 0.9539237696
        if units_to == "Hogshead":
            NUMout = inter / 0.2384809424
        if units_to == "Board foot":
            NUMout = inter / 0.0023597372
        if units_to == "Dram [dr]":
            NUMout = inter / 3.6966911953125*10**6
        if units_to == "Earth's Volume":
            NUMout = inter / 1.083*10**21
        
        #Standard Velocity and Speed units out
        if units_to == "Meter/Hour [m/hr]":
            NUMout = inter / 0.0002777778
        if units_to == "Meter/Minute [m/min]":
            NUMout = inter / 0.0166666667
        if units_to == "Meter/Second [m/sec]":
            NUMout = inter / 1
        if units_to == "Kilometer/Hour [km/hr, KPH]":
            NUMout = inter / 0.2777777778
        if units_to == "Kilometer/Minute [km/min]":
            NUMout = inter / 16.6666666667
        if units_to == "Kilometer/Second [km/sec]":
            NUMout = inter / 1000
        if units_to == "Mile/Hour [mi/hr, MPH]":
            NUMout = inter / 0.44704
        if units_to == "Mile/Minute [mi/min]":
            NUMout = inter / 26.8224
        if units_to == "Mile/Second [mi/sec]":
            NUMout = inter / 1609.344
        if units_to == "Centimeter/Hour [cm/hr]":
            NUMout = inter / 2.7777777777778*10**6
        if units_to == "Centimeter/Minute [cm/min]":
            NUMout = inter / 0.0001666667
        if units_to == "Centimeter/Second [cm/sec]":
            NUMout = inter / 0.01
        if units_to == "Millimeter/Hour [mm/hr]":
            NUMout = inter / 2.7777777777778*10**7
        if units_to == "Millimeter/Minute [mm/min]":
            NUMout = inter / 1.66667*10**5
        if units_to == "Millimeter/Second [mm/sec]":
            NUMout = inter / 0.001
        if units_to == "Yard/Hour [yd/hr]":
            NUMout = inter / 0.000254
        if units_to == "Yard/Minute [yd/min]":
            NUMout = inter / 0.01524
        if units_to == "Yard/Second [yd/sec]":
            NUMout = inter / 0.9144
        if units_to == "Foot/Hour [ft/hr]":
            NUMout = inter / 8.46667*10**5
        if units_to == "Foot/Minute [ft/min, FPM]":
            NUMout = inter / 0.00508
        if units_to == "Foot/Second [ft/sec, FPS]":
            NUMout = inter / 0.3048
        if units_to == "Knot [kt, kn]":
            NUMout = inter / 0.5144444444
        if units_to == "Knot (UK) [kt (UK)]":
            NUMout = inter / 0.5147733333
        if units_to == "Velocity of Light in Vacuum":
            NUMout = inter / 299792458
        if units_to == "Orbital Velocity Around the Earth (Cosmic Velocity - First)":
            NUMout = inter / 7899.9999999999
        if units_to == "Earth Escape Velocity (Cosmic Velocity - Second)":
            NUMout = inter / 11200
        if units_to == "Solar System Escape Velocity (Cosmic Velocity - Third)":
            NUMout = inter / 16670
        if units_to == "Earth's Straight-line Orbital Velocity (around the sun)":
            NUMout = inter / 29765
        if units_to == "Velocity of Sound in Pure Water":
            NUMout = inter / 1482.6999999998
        if units_to == "Velocity of Sound in Sea Water (@ 20°C, 10 meter deep)":
            NUMout = inter / 1521.6
        if units_to == "Speed of Sound in Air (@ 20°C, 1 atm) [Mach]":
            NUMout = inter / 343.6
        if units_to == "Speed of Sound in Air (SI standard) [Mach]":
            NUMout = inter / 295.0464000003

        #Standard Acceleration Units out
        if units_to == "Meter/Hour Squared [m/hr\u00b2]":
            NUMout = inter / 7.716049383*10**8
        if units_to == "Meter/Minute Squared [m/min\u00b2]":
            NUMout = inter / 0.000277777778
        if units_to == "Meter/Second Squared [m/sec\u00b2]":
            NUMout = inter / 1
        if units_to == "Kilometer/Hour Squared [km/hr\u00b2]":
            NUMout = inter / 0.00007716049
        if units_to == "Kilometer/Minute Squared [km/min\u00b2]":
            NUMout = inter / 0.277777778
        if units_to == "Kilometer/Second Squared [km/sec\u00b2]":
            NUMout = inter / 1000
        if units_to == "Centimeter/Hour Squared [cm/hr\u00b2]":
            NUMout = inter / 7.71604938*10**10
        if units_to == "Centimeter/Minute Squared [cm/min\u00b2]":
            NUMout = inter / 2.77777778*10**6
        if units_to == "Centimeter/Second Squared [cm/sec\u00b2]":
            NUMout = inter / 0.01
        if units_to == "Millimeter/Hour Squared [mm/hr\u00b2]":
            NUMout = inter / 7.71604938*10**11
        if units_to == "Millimeter/Minute Squared [mm/min\u00b2]":
            NUMout = inter / 2.77777778*10**7
        if units_to == "Millimeter/Second Squared [mm/sec\u00b2]":
            NUMout = inter / 0.001
        if units_to == "Mile/Hour Squared [mi/hr\u00b2]":
            NUMout = inter / 0.00012417777777778
        if units_to == "Mile/Minute Squared [mi/min\u00b2]":
            NUMout = inter / 0.44704
        if units_to == "Mile/Second Squared [mi/sec\u00b2]":
            NUMout = inter / 1609.344
        if units_to == "Yard/Hour Squared [yd/hr\u00b2]":
            NUMout = inter / 7.05555556*10**8
        if units_to == "Yard/Minute Squared [yd/min\u00b2]":
            NUMout = inter / 0.000254
        if units_to == "Yard/Second Squared [yd/sec\u00b2]":
            NUMout = inter / 0.9144
        if units_to == "Foot/Hour Squared [ft/hr\u00b2]":
            NUMout = inter / 2.35185185*10**8
        if units_to == "Foot/Minute Squared [ft/min\u00b2]":
            NUMout = inter / 8.46666667*10**5
        if units_to == "Foot/Second Squared [ft/sec\u00b2]":
            NUMout = inter / 0.3048
        if units_to == "Galileo [Gal]":
            NUMout = inter / 0.01
        if units_to == "Earth's Centripetal Acceleration":
            NUMout = inter / 5.95*10**3
        if units_to == "Acceleration From Earth's Gravity [g]":
            NUMout = inter / 9.807
        
        #Standard Force Units out
        if units_to == "Newton [N, J/m, kg*m/sec\u00b2]":
            NUMout = inter / 1
        if units_to == "Kilonewton [kN]":
            NUMout = inter / 1000
        if units_to == "Gram-force [gf]":
            NUMout = inter / 0.00980665
        if units_to == "Kilogram-force [kgf]":
            NUMout = inter / 9.80665
        if units_to == "Ton-force (metric) [tf]":
            NUMout = inter / 9806.65
        if units_to == "Giganewton [GN]":
            NUMout = inter / 1000000000
        if units_to == "Meganewton [MN]":
            NUMout = inter / 1000000
        if units_to == "Centinewton [cN, J/cm]":
            NUMout = inter / 0.01
        if units_to == "Millinewton [mN]":
            NUMout = inter / 0.001
        if units_to == "Micronewton [µN]":
            NUMout = inter / 1*10**6
        if units_to == "Dyne [dyn]":
            NUMout = inter / 1*10**5
        if units_to == "Ton-force (short)":
            NUMout = inter / 8896.443230521
        if units_to == "Ton-force (long) [tonf (UK)]":
            NUMout = inter / 9964.0164181707
        if units_to == "Kip-force [kipf]":
            NUMout = inter / 4448.2216152548
        if units_to == "Pound-force [lbf]":
            NUMout = inter / 4.4482216153
        if units_to == "Ounce-force [ozf]":
            NUMout = inter / 0.278013851
        if units_to == "Poundal [pdl]":
            NUMout = inter / 0.1382549544
        if units_to == "Pond [p]":
            NUMout = inter / 0.00980665
        if units_to == "Kilopond":
            NUMout = inter / 9.80665
    
        #Standard Torque Units out
        if units_to == "Newton Meter [N*m]":
            NUMout = inter / 1
        if units_to == "Newton Centimeter [N*cm]":
            NUMout = inter / 0.01
        if units_to == "Newton Millimeter [N*mm]":
            NUMout = inter / 0.001
        if units_to == "Kilonewton Meter [kN*m]":
            NUMout = inter / 1000
        if units_to == "Dyne Meter [dyn*m]":
            NUMout = inter / 1*10**5
        if units_to == "Dyne Centimeter [dyn*cm]":
            NUMout = inter / 1*10**7
        if units_to == "Dyne Millimeter [dyn*mm]":
            NUMout = inter / 1*10**8
        if units_to == "Kilogram-force Meter [kgf*m]":
            NUMout = inter / 9.80665
        if units_to == "Kilogram-force Centimeter [kgf*cm]":
            NUMout = inter / 0.0980665
        if units_to == "Kilogram-force Millimeter [kgf*mm]" or units_to == "Gram-force Meter [gf*m]":
            NUMout = inter / 0.00980665
        if units_to == "Gram-force Centimeter [gf*cm]":
            NUMout = inter / 9.80665*10**5
        if units_to == "Gram-force Millimeter [gf*mm]":
            NUMout = inter / 9.80665*10**6
        if units_to == "Ounce-force Foot [ozf*ft]":
            NUMout = inter / 0.084738624
        if units_to == "Ounce-force Inch [ozf*in]":
            NUMout = inter / 0.007061552
        if units_to == "Pound-force Foot [lbf*ft]":
            NUMout = inter / 1.355818
        if units_to == "Pound-force Inch [lbf*in]":
            NUMout = inter /  0.1129848333
        if units_to == "Ton-force (short) Meter":
            NUMout = inter / 8896.4400000035
        if units_to == "Ton-force (long) Meter":
            NUMout = inter / 9964.0200000047
        if units_to == "Ton-force (metric) Meter":
            NUMout = inter / 9806.6499999993
        if units_to == "Poundal foot [pdl*ft]":
            NUMout = inter / 0.0421401
        if units_to == "Poundal Inch [pdl*in]":
            NUMout = inter / 0.003511675
        
        #Standard Moment of Inertia units
        if units_to == "Kilogram Square Meter [kg*m\u00b2]":
            NUMout = inter / 1
        if units_to == "Kilogram Square Centimeter [kg*cm\u00b2]":
            NUMout = inter / 0.0001
        if units_to == "Kilogram Square Millimeter [kg*mm\u00b2]":
            NUMout = inter / 1*10**6
        if units_to == "Gram Square Centimeter [g*cm\u00b2]":
            NUMout = inter / 1*10**7
        if units_to == "Gram Square Millimeter [g*mm\u00b2]":
            NUMout = inter / 1*10**9
        if units_to == "Kilogram-force Meter Second Squared [kgf*m*sec\u00b2]":
            NUMout = inter / 9.8066499998
        if units_to == "Kilogram-force Centimeter Second Squared [kgf*cm*sec\u00b2]":
            NUMout = inter / 0.0980665
        if units_to == "Ounce Square Inch [oz*in\u00b2]":
            NUMout = inter / 1.829*10**5
        if units_to == "Ounce-force Inch/Second Squared [ozf*in*sec\u00b2]":
            NUMout = inter / 0.0070615519
        if units_to == "Pound Square Foot [lb*ft\u00b2]":
            NUMout = inter / 0.0421401101
        if units_from == "Pound-force Foot Square Second [lbf*ft*s\u00b2]":
            inter = NUMinput / 1.3558179619
        if units_to == "Pound-force Inch Second Squared [lbf*in*sec\u00b2]":
            NUMout = inter / 0.1129848302
        if units_to == "Slug Square Foot [slug*ft\u00b2]":
            NUMout = inter / 1.3558179619
        
        #Standard Mass Units out
        if units_to == "Kilogram [kg]":
            NUMout = inter / 1
        if units_to == "Gram [g]":
            NUMout = inter / 0.001
        if units_to == "Milligram [mg]":
            NUMout = inter / 1*10**6
        if units_to == "Ton (metric) [t]" or units_to == "Megagram [Mm]" or units_to == "Tonne [t]":
            NUMout = inter / 1000
        if units_to == "Pound [lb]":
            NUMout = inter / 0.45359237
        if units_to == "Ounce [oz]":
            NUMout = inter / 0.0283495231
        if units_to == "Carat [car, ct]":
            NUMout = inter / 0.0002
        if units_to == "Ton (short) [ton (US)]":
            NUMout = inter / 907.18474
        if units_to == "Ton (long) [ton (UK)]":
            NUMout = inter / 1016.0469088
        if units_to == "Atomic Mass Unit [u]":
            NUMout = inter / 1.6605402*10**27
        if units_to == "Gigagram [Gg]":
            NUMout = inter / 1000000
        if units_to == "Megagram [Mg]":
            NUMoutout = inter / 1000
        if units_to == "Centigram [cg]":
            NUMout = inter / 1*10**5
        if units_to == "Microgram [µg]":
            NUMout = inter / 1*10**9
        if units_to == "Dalton":
            NUMout = inter / 1.6605300000013*10**27
        if units_to == "Kilogram-force Square Second/Meter":
            NUMout = inter / 9.80665
        if units_to == "Kilopound [kip]":
            NUMout = inter / 453.59237
        if units_to == "Slug" or units_to == "Pound-force Square Second/Foot":
            NUMout = inter / 14.5939029372
        if units_to == "Pound (troy or apothecary)":
            NUMout = inter / 0.3732417216
        if units_to == "Poundal [pdl]":
            NUMout = inter / 0.0140867196
        if units_to == "Ton (assay) (US) [AT (US)]":
            NUMout = inter / 0.02916667
        if units_to == "Ton (assay) (UK) [AT (UK)]":
            NUMout = inter / 0.0326666667
        if units_to == "Kiloton (metric) [kt]":
            NUMout = inter / 1000000
        if units_to == "Quintal (metric) [cwt]":
            NUMout = inter / 100
        if units_to == "Hundredweight (US)":
            NUMout = inter / 45.359237
        if units_to == "Hundredweight (UK)":
            NUMout = inter / 50.80234544
        if units_to == "Quarter (US) [qr (US)]":
            NUMout = inter / 11.33980925
        if units_to == "Quarter (UK) [qr (UK)]":
            NUMout = inter / 12.70058636
        if units_to == "Stone (US)":
            NUMout = inter / 5.669904625
        if units_to == "Stone (UK)":
            NUMout = inter / 6.35029318
        if units_to == "Pennyweight [pwt]":
            NUMout = inter / 0.0015551738
        if units_to == "Scruple (apothecary) [s.ap]":
            NUMout = inter / 0.0012959782
        if units_to == "Grain [gr]":
            NUMout = inter / 6.47989*10**5
        if units_to == "Gamma":
            NUMout = inter / 1*10**9
        if units_to == "Plank Mass":
            NUMout = inter / 2.17671*10**8
        if units_to == "Electron Mass (rest)":
            NUMout = inter / 9.1093897*10**31
        if units_to == "Earth's Mass":
            NUMout = inter / 5.9760000000002*10**24
        if units_to == "Sun's Mass":
            NUMout = inter / 2*10**30
    
        #Standard Density Units out
        if units_to == "Kilogram/Cubic Meter [kg/m\u00b3]" or units_to == "Milligram/Cubic Centimeter [mg/cm\u00b3]" or units_to == "Gram/Liter [g/L]":
            NUMout = inter / 1
        if units_to == "Gram/Cubic Centimeter [g/cm\u00b3]" or units_to == "Milligram/Cubic Millimeter [mg/mm\u00b3]" or units_to == "Kilogram/Liter [kg/L]":
            NUMout = inter / 1000
        if units_to == "Kilogram/Cubic Centimeter [kg/cm\u00b3]" or units_to == "Gram/Cubic Millimeter [g/mm\u00b3]":
            NUMout = inter / 1000000
        if units_to == "Gram/Cubic Meter [g/m\u00b3]":
            NUMout = inter / 0.001
        if units_to == "Milligram/Cubic Meter [mg/m\u00b3]" or units_to == "Microgram/Liter [µg/L]":
            NUMout = inter / 1*10**6
        if units_to == "Megagram/Liter [Mg/L]":
            NUMout = inter / 1000000
        if units_to == "Centigram/Liter [cg/L]":
            NUMout = inter / 0.01
        if units_to == "Milligram/Liter [mg/L]":
            NUMout = inter / 0.001
        if units_to == "Pound/Cubic Inch [lb/in\u00b3]":
            NUMout = inter / 27679.904710191
        if units_to == "Pound/Cubic Foot [lb/ft\u00b3]":
            NUMout = inter / 16.018463374
        if units_to == "Pound/Cubic Yard [lb/yd\u00b3]":
            NUMout = inter / 0.5932764213
        if units_to == "Pound/Gallon (US)":
            NUMout = inter / 119.8264273167
        if units_to == "Pound/Gallon (UK)":
            NUMout = inter / 99.7763726631
        if units_to == "Ounce/Cubic Inch [oz/in\u00b3]":
            NUMout = inter / 1729.9940443869
        if units_to == "Ounce/Cubic Foot [oz/ft\u00b3]":
            NUMout = inter / 1.0011539609
        if units_to == "Ounce/Gallon (US)":
            NUMout = inter / 7.4891517073
        if units_to == "Ounce/Gallon (UK)":
            NUMout = inter / 6.2360232914
        if units_to == "Grain/Gallon (US)":
            NUMout = inter / 0.017118061
        if units_to == "Grain/Gallon (UK)":
            NUMout = inter / 0.0142537675 
        if units_to == "Grain/Cubic Foot [gr/ft\u00b3]":
            NUMout = inter / 0.0022883519
        if units_to == "Ton (short)/Cubic Yard":
            NUMout = inter / 1186.552842515
        if units_to == "Ton (long)/Cubic Yard":
            NUMout = inter / 1328.9391836174
        if units_to == "Slug/Cubic Foot [slug/ft\u00b3]":
            NUMout = inter / 515.3788183932
        if units_to == "PSI/1000 Feet":
            NUMout = inter / 2.3066587258
        if units_to == "Earth's Density (mean)":
            NUMout = inter / 5517.9999999999  
        
        #Standard Time Units out
        if units_to == "Second [sec]":
            NUMout = inter / 1
        if units_to == "Millisecond [ms]":
            NUMout = inter / 0.001
        if units_to == "Mintute [mout]":
            NUMout = inter / 60
        if units_to == "Hour [hr]":
            NUMout = inter / 3600
        if units_to == "Day [d]":
            NUMout = inter / 86400
        if units_to == "Week":
            NUMout = inter / 604800
        if units_to == "Month":
            NUMout = inter / 2628000
        if units_to == "Year [y]" or units_to == "Year (Julian)":
            NUMout = inter / 31557600
        if units_to == "Decade":
            NUMout = inter / 315576000
        if units_to == "Century":
            NUMout = inter / 3155760000
        if units_to == "Millenium":
            NUMout = inter / 31557600000
        if units_to == "Microsecond [µs]":
            NUMout = inter / 1*10**6
        if units_to == "Nanosecond [ns]":
            NUMout = inter / 1*10**9
        if units_to == "Shake":
            NUMout = inter / 1*10**8
        if units_to == "Month (synodic)":
            NUMout = inter / 2551443.84
        if units_to == "Year (leap)":
            NUMout = inter / 31622400
        if units_to == "Year (tropical)":
            NUMout = inter / 31556930
        if units_to == "Year (sidereal)":
            NUMout = inter / 31558149.54
        if units_to == "Day (sidreal)":
            NUMout = inter / 86164.09
        if units_to == "Hour (sidereal)":
            NUMout = inter / 3590.1704166667
        if units_to == "Minute (sidereal)":
            NUMout = inter / 59.8361736111
        if units_to == "Second (sidereal)":
            NUMout = inter / 0.9972695602
        if units_to == "Fortnite":
            NUMout = inter / 1209600
        if units_to == "Septennial":
            NUMout = inter / 220752000
        if units_to == "Octenial":
            NUMout = inter / 252288000
        if units_to == "Novennial":
            NUMout = inter / 283824000
        if units_to == "Plank Time":
            NUMout = inter / 5.39056*10**44
        
        #Standard Temperature units out
        if units_to == "Kelvin [K]":
            NUMout = inter / 1
        if units_to == "Celsius [°C]":
            NUMout = inter - 273.15
        if units_to == "Fahrenheit [°F]":
            NUMout = (((inter - 273.15) * 1.8) + 32)
        if units_to == "Rankine [°R]":
            NUMout = inter / 0.5555555556
        if units_to == "Reaumur [°r]":
            NUMout = (inter -273.15) * 4/5
        
        #Standard Energy Units out
        if units_to == "Joule [J]" or units_to == "Watt-second [W*s]" or units_to == "Newton Meter [N*m]":
            NUMout = inter / 1
        if units_to == "Kilojoule [kJ]" or units_to == "Kilowatt-second [kW*sec]":
            NUMout = inter / 1000
        if units_to == "Kilowatt-hour [kW*hr]":
            NUMout = inter / 3600000
        if units_to == "Watt-hour [W*hr]":
            NUMout = inter / 3600
        if units_to == "Calorie (nutritional)" or units_to == "Kilocalorie (IT) [kcal (IT)]":
            NUMout = inter / 4186.8
        if units_to == "Horsepower (metric) Hour":
            NUMout = inter / 2647795.5
        if units_to == "Btu (IT) [Btu (IT), Btu]":
            NUMout = inter / 1055.05585262
        if units_to == "Btu (th) [Btu (th)]":
            NUMout = inter / 1054.3499999744
        if units_to == "Gigajoule [GJ]":
            NUMout = inter / 1000000000
        if units_to == "Megajoule [MJ]":
            NUMout = inter / 1000000
        if units_to == "Megaelectron-volt [MeV]":
            NUMout = inter / 1.6021766339999*10**13
        if units_to == "Kiloelectron-volt [KeV]":
            NUMout = inter / 1.6021766339999*10**16
        if units_to == "Electron-volt [eV]":
            NUMout = inter / 1.6021766339999*10**19
        if units_to == "Erg":
            NUMout = inter / 1*10**7
        if units_to == "Gigawatt-hour [GW*hr]":
            NUMout = inter / 3600000000000
        if units_to == "Megawatt-hour [MW*hr]":
            NUMout = inter / 3600000000
        if units_to == "Horsepower Hour [hp*hr]":
            NUMout = inter / 2684519.5368856
        if units_to == "Kilocalorie (th) [kcal (th)]":
            NUMout = inter / 4184
        if units_to == "Calorie (IT) [cal (IT), cal]":
            NUMout = inter / 4.1868
        if units_to == "Calorie (th) [cal (th)]":
            NUMout = inter / 4.184
        if units_to == "Mega Btu (IT) [MBtu (IT)]":
            NUMout = inter / 1055055852.62
        if units_to == "Ton-hour (refrigeration)":
            NUMout = inter / 12660670.23144
        if units_to == "Fuel Oil Equivalent @kiloliter":
            NUMout = inter / 40197627984.822
        if units_to == "Fuel Oil Equivalent @barrel (US)":
            NUMout = inter / 6383087908.3509
        if units_to == "Gigaton [Gton]":
            NUMout = inter / 4.184*10**18
        if units_to == "Megaton [Mton]":
            NUMout = inter / 4.184*10**15
        if units_to == "Kiloton [kton]":
            NUMout = inter / 4184000000000
        if units_to == "Ton (explosives)":
            NUMout = inter / 4184000000
        if units_to == "Dyne Centimeter [dyn*cm]":
            NUMout = inter / 1*10**7
        if units_to == "Gram-force Meter [gf*m]":
            NUMout = inter / 0.00980665
        if units_to == "Gram-force Centimeter [gf*cm]":
            NUMout = inter / 9.80665*10**5
        if units_to == "Kilogram-force Centimeter":
            NUMout = inter / 0.098066499997
        if units_to == "Kilogram-force Meter" or units_to == "Kilopond Meter [kp*m]":
            NUMout = inter / 9.8066499997
        if units_to == "Pound-force Foot [lbf*ft]":
            NUMout = inter / 1.3558179483
        if units_to == "Pound-force Inch [lbf*out]":
            NUMout = inter / 0.112984829
        if units_to == "Ounce-force Inch [ozf*out]":
            NUMout = inter / 0.0070615518
        if units_to == "Foot-pound [ft*lbf]":
            NUMout = inter / 1.3558179483
        if units_to == "Inch-pound [out*lbf]":
            NUMout = inter / 0.112984829
        if units_to == "Inch-ounce [out*ozf]":
            NUMout = inter / 0.0070615518
        if units_to == "Poundal Foot [pdl*ft]":
            NUMout = inter / 0.04214011
        if units_to == "Therm" or units_to == "Therm (EC)":
            NUMout = inter / 105505600
        if units_to == "Therm (US)":
            NUMout = inter / 105480400
        if units_to == "Hartree Energy":
            NUMout = inter / 4.3597482*10**18
        if units_to == "Rydberg Constant":
            NUMout = inter / 2.1798741*10**18
    
        #Standard Power Units out
        if units_to == "Watt [W]" or units_to == "Volt Ampere [V*A]" or units_to == "Newton Meter/Second [N*m/s]" or units_to == "Joule/Second [J/s]":
            NUMout = inter / 1
        if units_to == "Gigawatt [GW]" or units_to == "Gigajoule/Second [GJ/s]":
            NUMout = inter / 1000000000
        if units_to == "Megawatt [MW]" or units_to == "Megajoule/Second [MJ/s]":
            NUMout = inter / 1000000
        if units_to == "Kilowatt [kW]" or units_to == "Kilovolt Ampere [kV*A]" or units_to == "Kilojoule/Second [kJ/s]":
            NUMout = inter / 1000
        if units_to == "Milliwatt [mW]" or units_to == "Millijoule/Second [mJ/s]":
            NUMout = inter / 0.001
        if units_to == "Microwatt [µW]" or units_to == "Microjoule/Second [µJ/s]":
            NUMout = inter / 1*10**6
        if units_to == "Nanowatt [nW]" or units_to == "Nanojoule/Second [nJ/s]":
            NUMout = inter / 1*10**9
        if units_to == "Horsepower [hp]":
            NUMout = inter / 745.6998715823
        if units_to == "Horsepower (550 ft*lbf/s)":
            NUMout = inter / 745.6998715823
        if units_to == "Horsepower (metric)":
            NUMout = inter / 735.49875
        if units_to == "Horsepower (boiler)":
            NUMout = inter / 9809.5000000002
        if units_to == "Horsepower (Electric)":
            NUMout = inter / 746
        if units_to == "Horsepower (water)":
            NUMout = inter / 746.043
        if units_to == "Pferdestarke (ps)":
            NUMout = inter / 735.49875
        if units_to == "Btu (IT)/Hour [Btu/hr]":
            NUMout = inter / 0.2930710702
        if units_to == "Btu (IT)/Minute [Btu/min]":
            NUMout = inter / 17.5842642103
        if units_to == "Btu (IT)/Second [Btu/sec]":
            NUMout = inter / 1055.05585262
        if units_to == "Btu (th)/Hour [Btu (th)/hr]":
            NUMout = inter / 0.292875
        if units_to == "Btu (th)/Minute [Btu (th)/min]":
            NUMout = inter / 17.5724999996
        if units_to == "Btu (th)/Second [Btu (th)/sec]":
            NUMout = inter / 1054.3499999744
        if units_to == "MBtu (IT)/Hour [MBtu/hr]":
            NUMout = inter / 293071.07017222
        if units_to == "MBH":
            NUMout = inter / 293.0710701722
        if units_to == "Ton (refrigeration)":
            NUMout = inter / 3516.8528420667
        if units_to == "Kilocalorie (IT)/Hour [kcal/hr]":
            NUMout = inter / 1.163
        if units_to == "Kilocalorie (IT)/Minute [kcal/min]":
            NUMout = inter / 69.78
        if units_to == "Kilocalorie (IT)/Second [kcal/sec]":
            NUMout = inter / 4186.8
        if units_to == "Kilocalorie (th)/Hour [kcal (th)/hr]":
            NUMout = inter / 1.1622222222
        if units_to == "Kilocalorie (th)/Minute [kcal (th)/min]":
            NUMout = inter / 69.7333333333
        if units_to == "Kilocalorie (th)/Second [kcal (th)/sec]":
            NUMout = inter / 4184
        if units_to == "Calorie (IT)/Hour [cal/hr]":
            NUMout = inter / 0.001163
        if units_to == "Calorie (IT)/Minute [cal/min]":
            NUMout = inter / 0.06978
        if units_to == "Calorie (IT)/Second [cal/sec]":
            NUMout = inter / 4.1868
        if units_to == "Calorie (th)/Hour [cal (th)/hr]":
            NUMout = inter / 0.0011622222
        if units_to == "Calorie (th)/Minute [cal (th)/min]":
            NUMout = inter / 0.0697333333
        if units_to == "Calorie (th)/Second [cal (th)/sec]":
            NUMout = inter / 4.184
        if units_to == "Foot Pound-force/Hour":
            NUMout = inter / 0.0003766161
        if units_to == "Foot Pound-force/Minute":
            NUMout = inter / 0.0225969658
        if units_to == "Foot Pound-force/Second":
            NUMout = inter / 1.3558179483
        if units_to == "Pound-foot/Hour [lbf*ft/hr]":
            NUMout = inter / 0.0003766161
        if units_to == "Pound-foot/Minute [lbf*ft/min]":
            NUMout = inter / 0.0225969658
        if units_to == "Pound-foot/Second [lbf*ft/sec]":
            NUMout = inter / 1.3558179483
        if units_to == "Erg/Second [erg/s]":
            NUMout = inter / 1*10**7
        if units_to == "Joule/Hour [J/hr]":
            NUMout = inter / 0.0002777778
        if units_to == "Joule/Minute [J/min]":
            NUMout = inter / 0.0166666667
        if units_to == "Kilojoule/Hour [kJ/hr]":
            NUMout = inter / 0.2777777778
        if units_to == "Kilojoule/Minute [kJ/min]":
            NUMout = inter / 16.6666666667 
        
        #Standard Pressure Units out
        if units_to == "Pascal [Pa]" or units_to == "Newton/Square Meter [N/m\u00b2]":
            NUMout = inter / 1
        if units_to == "Kilopascal [kPa]" or units_to == "Kilonewton/Square Meter [kN/m\u00b2]":
            NUMout = inter / 1000
        if units_to == "Bar":
            NUMout = inter / 100000
        if units_to == "Pound/Square Inch [PSI]":
            NUMout = inter / 6894.7572931783
        if units_to == "Kip/Square Inch [KSI]":
            NUMout = inter / 6894757.2931783
        if units_to == "Standard Atmosphere [atm]":
            NUMout = inter / 101325
        if units_to == "Gigapascal [GPa]":
            NUMout = inter / 1000000000
        if units_to == "Megapascal [MPa]" or units_to == "Newton/Square Millimeter [N/mm\u00b2]":
            NUMout = inter / 1000000
        if units_to == "Millipascal [mPa]":
            NUMout = inter / 0.001
        if units_to == "Micropascal [µPa]":
            NUMout = inter / 1*10**6
        if units_to == "Nanopascal [nPa]":
            NUMout = inter / 1*10**9
        if units_to == "Newton/Square Centimeter [N/cm\u00b2]":
            NUMout = inter / 10000
        if units_to == "Millibar [mb, mbar]":
            NUMout = inter / 100
        if units_to == "Microbar [µb, µbar]" or units_to == "Dyne/Square Centimeter [dyn/cm\u00b2]":
            NUMout = inter / 0.1
        if units_to == "Kilogram-force/Square Meter [kgf/m\u00b2]":
            NUMout = inter / 9.80665
        if units_to == "Kilogram-force/Square Centimeter [kfg/cm\u00b2]":
            NUMout = inter / 98066.5
        if units_to == "Kilogram-force/Square Millimeter [kgf/mm\u00b2]":
            NUMout = inter / 9806650
        if units_to == "Gram-force/Square Centimeter [gf/cm\u00b2]":
            NUMout = inter / 98.0665
        if units_to == "Ton-force (short)/Square Foot":
            NUMout = inter / 95760.517960678
        if units_to == "Ton-force (short)/Square Inch":
            NUMout = inter / 13789514.586338
        if units_to == "Ton-force (long)/Square Foot":
            NUMout = inter / 107251.78011595
        if units_to == "Ton-Force (long)/Square Inch":
            NUMout = inter / 15444256.336697
        if units_to == "Pound-force/Square Foot [lbf/ft\u00b2]":
            NUMout = inter / 47.8802589804
        if units_to == "Poundal/Square Foot":
            NUMout = inter / 1.4881639436
        if units_to == "Torr [Torr]":
            NUMout = inter / 133.3223684211
        if units_to == "Millitorr [mTorr]":
            NUMout = inter / 0.13332237
        if units_to == "Centimeter Mercury (0°C) [cmHg]":
            NUMout = inter / 1333.22
        if units_to == "Millimeter Mercury (0°C) [mmHg]":
            NUMout = inter / 133.322
        if units_to == "Inch Mercury (32°F) [inHg]":
            NUMout = inter / 3386.38
        if units_to == "Inch Mercury (60°F) [inHg]":
            NUMout = inter / 3376.85
        if units_to == "Centimeter Water (4°C)":
            NUMout = inter / 98.0638
        if units_to == "Millimeter Water (4°C)":
            NUMout = inter / 9.80638
        if units_to == "Inch Water (4°C) [inAq]":
            NUMout = inter / 249.082
        if units_to == "Foot Water (4°C) [ftAq]":
            NUMout = inter / 2988.98
        if units_to == "Inch Water (60°F) [inAq]":
            NUMout = inter / 248.843
        if units_to == "Foot Water (60°F) [ftAq]":
            NUMout = inter / 2986.116
        if units_to == "Atmosphere Technical [at]":
            NUMout = inter / 98066.500000003 
        
        #Angular plane angle (angular distance) out
        if units_to == "Degree [°]":
            NUMout = inter / 1
        if units_to == "Radian [rad]":
            NUMout = (inter * math.pi) / 180
        if units_to == "Grad [^g]" or units_to == "gon":
            NUMout = inter / 0.9
        if units_to == "Minute [']":
            NUMout = inter / (1/60)
        if units_to == "Second ['']":
            NUMout = inter /  (1/3600)
        if units_to == "sign":
            NUMout = inter / 30
        if units_to == "mil":
            NUMout = inter / .05625
        if units_to == "Revolution [r]" or units_to == "Circle" or units_to == "Turn":
            NUMout = inter / 360
        if units_to == "Quadrant" or units_to == "Right Angle":
            NUMout = inter / 90
        if units_to == "Sextant":
            NUMout = inter / 60
        
        #Angular units angular velocity out
        if units_to == "Radian/Second [rad/sec]":
            NUMout = inter / 1
        if units_to == "Radian/Day [rad/d]":
            NUMout = inter / 1.15741*10**5
        if units_to == "Radian/Hour [rad/hr]":
            NUMout = inter / (1/3600)
        if units_to == "Radian/Minute [rad/min]":
            NUMout = inter / (1/60)
        if units_to == "Degree/Day [°/d]":
            NUMout = inter / 2.0200570046231*10**7
        if units_to == "Degree/Hour [°/hr]":
            NUMout = inter / 4.8481368110954*10**6
        if units_to == "Degree/Minute [°/min]":
            NUMout = inter / 0.0002908882
        if units_to == "Degree/Second [°/sec]":
            NUMout = inter / 0.0174532925
        if units_to == "Revolution/Day [r/d]":
            NUMout = inter / 7.27221*10**5
        if units_to == "Revolution/Hour [r/hr]":
            NUMout = inter / 0.0017453293
        if units_to == "Revolution/Minute [r/min, RPM]":
            NUMout = inter / 0.1047197551
        if units_to == "Revolution/Second [r/sec]":
            NUMout = inter / 6.2831853072
            
        #Angular units angular acceleration out
        if units_to == "Radian/Square Second [rad/s\u00b2]":
            NUMout = inter / 1
        if units_to == "Radian/Square Minute":
            NUMout = inter / (1/(60**2))
        if units_to == "Revolution/Square Second [r/s\u00b2]":
            NUMout = inter / 6.2831853069
        if units_to == "Revolution/Minute/Second":
            NUMout = inter / 0.1047197551
        if units_to == "Revolution/Square Minute":
            NUMout = inter / 0.0017453293
        
        #Fluid Volume units out
        if units_to == "Cubic Meter [m\u00b3]" or units_to == "Kiloliter [kL]" or units_to == "Stere [st]":
            NUMout = inter / 1
        if units_to == "Cubic Kilometer [km\u00b3]":
            NUMout = inter / 1000000000
        if units_to == "Cubic Centimeter [cm\u00b3]" or units_to == "Milliliter [mL]" or units_to == "CC [cc, cm\u00b3]":
            NUMout = inter / 1*10**6
        if units_to == "Cubic Millimeter [mm\u00b3]":
            NUMout = inter / 1*10**9
        if units_to == "Liter [L, l]":
            NUMout = inter / 0.001
        if units_to == "Gallon (US) [gal (US)]":
            NUMout = inter / 0.0037854118
        if units_to == "Quart (US) [qt (US)]":
            NUMout = inter / 0.0009463529
        if units_to == "Pint (US) [pt (US)]":
            NUMout = inter / 0.0004731765
        if units_to == "Cup (US)":
            NUMout = inter / 0.0002365882
        if units_to == "Tablespoon (US)":
            NUMout = inter / 1.47868*10**5
        if units_to == "Teaspoon (US)":
            NUMout = inter / 4.92892159375*10**6
        if units_to == "Cubic Mile [mi\u00b3]":
            NUMout = inter / 4168181825.4406
        if units_to == "Cubic Yard [yd\u00b3]":
            NUMout = inter / 0.764554858
        if units_to == "Cubic Foot [ft\u00b3]":
            NUMout = inter / 0.0283168466
        if units_to == "Cubic Inch [in\u00b3]":
            NUMout = inter / 1.63871*10**5
        if units_to == "Gigaliter [GL]":
            NUMout = inter / 1000000
        if units_to == "Megaliter [ML]":
            NUMout = inter / 1000
        if units_to == "Drop":
            NUMout = inter / 5*10**8
        if units_to == "Barrel (oil) [bbl (oil)]":
            NUMout = inter / 0.1589872949
        if units_to == "Barrel (US) [bbl (US)]":
            NUMout = inter / 0.1192404712
        if units_to == "Barrel (UK) [bbl (UK)]":
            NUMout = inter / 0.16365924
        if units_to == "Gallon (UK) [gal (UK)]":
            NUMout = inter / 0.00454609
        if units_to == "Quart (UK) [qt (UK)]":
            NUMout = inter / 0.0011365225
        if units_to == "Pint (UK) [pt (UK)]":
            NUMout = inter / 0.0005682613
        if units_to == "Cup (metric)":
            NUMout = inter / 0.00025
        if units_to == "Cup (UK)":
            NUMout = inter / 0.0002841306
        if units_to == "Fluid Ounce (US) [fl oz (US)]":
            NUMout = inter / 2.95735*10**5
        if units_to == "Fluid Ounce (UK) [fl oz (UK)]":
            NUMout = inter / 2.84131*10**5
        if units_to == "Tablespoon (metric)":
            NUMout = inter / 1.5*10**5
        if units_to == "Tablespoon (UK)":
            NUMout = inter / 1.77582*10**5
        if units_to == "Dessertspoon (US)":
            NUMout = inter / 9.8578431875*10**6
        if units_to == "Dessertspoon (UK)":
            NUMout = inter / 1.18388*10**5
        if units_to == "Teaspoon (metric)":
            NUMout = inter / 5*10**6
        if units_to == "Teaspoon (UK)":
            NUMout = inter / 5.9193880208333*10**6
        if units_to == "Gil (US) [gi]":
            NUMout = inter / 0.0001182941
        if units_to == "Gil (UK) [gi (UK)]":
            NUMout = inter / 0.0001420653
        if units_to == "Minim (US)":
            NUMout = inter / 6.1611519921875*10**8
        if units_to == "Minim (UK)":
            NUMout = inter / 5.9193880208333*10**8
        if units_to == "Ton Register [ton reg]":
            NUMout = inter / 2.8316846592
        if units_to == "ccf":
            NUMout = inter / 2.8316846592
        if units_to == "Hundred-cubic foot":
            NUMout = inter / 2.8316846592
        if units_to == "Acre-foot [ac*ft]":
            NUMout = inter / 1233.4818375475
        if units_to == "Acre-foot (US survey)":
            NUMout = inter / 1233.4892384682
        if units_to == "Acre-inch [ac*in]":
            NUMout = inter / 102.790153129
        if units_to == "Dekastere":
            NUMout = inter / 10
        if units_to == "Cord [cd]":
            NUMout = inter / 3.6245563638
        if units_to == "Decistere":
            NUMout = inter / 0.1
        if units_to == "Tun":
            NUMout = inter / 0.9539237696
        if units_to == "Hogshead":
            NUMout = inter / 0.2384809424
        if units_to == "Board foot":
            NUMout = inter / 0.0023597372
        if units_to == "Dram [dr]":
            NUMout = inter / 3.6966911953125*10**6
        if units_to == "Earth's Volume":
            NUMout = inter / 1.083*10**21
        
        #Fluid Volume Dry units out
        if units_to == "Liter [L, l]":
            NUMout = inter / 1
        if units_to == "Barrel Dry (US) [bbl dry (US)]":
            NUMout = inter / 115.6271236039
        if units_to == "Pint dry (US) [pt dry (US)]":
            NUMout = inter / 0.5506104714
        if units_to == "Quart dry (US) [qt dry (US)]":
            NUMout = inter / 1.1012209428
        if units_to == "Peck (US) [pk (US)]":
            NUMout = inter / 8.8097675424
        if units_to == "Peck (UK) [pk (UK)]":
            NUMout = inter / 9.09218
        if units_to == "Bushel (US) [bu (US)]":
            NUMout = inter / 35.2390701696
        if units_to == "Bushel (UK) [bu (UK)]":
            NUMout = inter / 36.36872
        
        #Fluid Specific volume units out
        if units_to == "Cubic Meter/Kilogram" or units_to == "Liter/Gram [L/g]":
            NUMout = inter / 1
        if units_to == "Cubic Centimeter/Gram" or units_to == "Liter/Kilogram [L/kg]":
            NUMout = inter / 0.001
        if units_to == "Cubic Foot/Kilogram [ft\u00b3/kg]":
            NUMout = inter / 0.0283168466
        if units_to == "Cubic Foot/Pound [ft\u00b3/lb]":
            NUMout = inter / 0.06242796
        if units_to == "Gallon (US)/Pound":
            NUMout = inter / 0.0083454039
        if units_to == "Gallon (UK)/Pound":
            NUMout = inter / 0.0100224128
            
        #Fluid Flow units out
        if units_to == "Cubic Meter/Second [m\u00b3/sec]":
            NUMout = inter / 1
        if units_to == "Cubic Meter/Day [m\u00b3/d]":
            NUMout = inter / 1.15741*10**5
        if units_to == "Cubic Meter/Hour [m\u00b3/hr]":
            NUMout = inter / 0.0002777778
        if units_to == "Cubic Meter/Minute":
            NUMout = inter / 0.0166666667
        if units_to == "Cubic Centimeter/Day" or units_to == "Milliliter/Day [mL/d]":
            NUMout = inter / 1.1574074074074*10**11
        if units_to == "Cubic Centimeter/Hour" or units_to == "Milliliter/Hour [mL/hr]":
            NUMout = inter / 2.7777777777778*10**10
        if units_to == "Cubic Centimeter/Minute" or units_to == "Milliliter/Minute [mL/min]":
            NUMout = inter / 1.6666666666667*10**8
        if units_to == "Cubic Centimeter/Second" or units_to == "Milliliter/Second [mL/sec]":
            NUMout = inter / 1.0*10**6
        if units_to == "Liter/Day [L/d]":
            NUMout = inter / 1.1574074074074*10**8
        if units_to == "Liter/Hour [L/hr]":
            NUMout = inter / 2.7777777777778*10**7
        if units_to == "Liter/Minute [L/min]":
            NUMout = inter / 1.66667*10**5
        if units_to == "Liter/Second [L/sec]":
            NUMout = inter / 0.001
        if units_to == "Gallon (US)/Day [gal (US)/d]":
            NUMout = inter / 4.3812636388889*10**8
        if units_to == "Gallon (US)/Hour [gal (US)/hr]":
            NUMout = inter / 1.0515032733333*10**6
        if units_to == "Gallon (US)/Minute [gal (US)/min]":
            NUMout = inter / 6.30902*10**5
        if units_to == "Gallon (US)/Second [gal (US)/sec]":
            NUMout = inter / 0.0037854118
        if units_to == "Gallon (UK)/Day [gal (UK)/d]":
            NUMout = inter / 5.2616782407407*10**8
        if units_to == "Gallon (UK)/Hour [gal (UK)/hr]":
            NUMout = inter / 1.2628027777778*10**6
        if units_to == "Gallon (UK)/Minute [gal (UK)/min]":
            NUMout = inter / 7.57682*10**5
        if units_to == "Gallon (UK)/Second [gal (UK)/sec]":
            NUMout = inter / 0.00454609
        if units_to == "Kilobarrel (US)/Day":
            NUMout = inter / 0.0018401307
        if units_to == "Barrel (US)/Day [bbl (US)/d]":
            NUMout = inter / 1.8401307283333*10**6
        if units_to == "Barrel (US)/Hour [bbl (US)/hr]":
            NUMout = inter / 4.41631*10**5
        if units_to == "Barrel (US)/Minute":
            NUMout = inter / 0.0026497882
        if units_to == "Barrel (US)/Second":
            NUMout = inter / 0.1589872949
        if units_to == "Acre-foot/Year [ac*ft/y]":
            NUMout = inter / 3.91136*10**5
        if units_to == "Acre-foot/Day [cs*ft/d]":
            NUMout = inter / 0.0142764673
        if units_to == "Acre-foot/Hour [ac*ft/hr]":
            NUMout = inter / 0.3426352143
        if units_to == "Hundred-cubic Foot/Day":
            NUMout = inter / 3.27741*10**5
        if units_to == "Hundred-cubic Foot/Hour":
            NUMout = inter / 0.0007865791
        if units_to == "Hundred-cubic Foot/Minute":
            NUMout = inter / 0.0471947443
        if units_to == "Ounce/Hour [oz/hr]":
            NUMout = inter / 8.2148693229167*10**9
        if units_to == "Ounce/Minute [oz/min]":
            NUMout = inter / 4.92892159375*10**7
        if units_to == "Ounce/Seccond [oz/sec]":
            NUMout = inter / 2.95735*10**5
        if units_to == "Ounce (UK)/Hour [oz (UK)/hr]":
            NUMout = inter / 7.8925178504774*10**9
        if units_to == "Ounce (UK)/Minute":
            NUMout = inter / 4.7355107102865*10**7
        if units_to == "Ounce (UK)/Second":
            NUMout = inter / 2.84131*10**5
        if units_to == "Cubic Yard/Hour [yd\u00b3/hr]":
            NUMout = inter / 0.0002123763
        if units_to == "Cubic Yard/Minute [yd\u00b3/min]":
            NUMout = inter / 0.012742581
        if units_to == "Cubic Yard/Second [yd\u00b3/sec]":
            NUMout = inter / 0.764554858
        if units_to == "Cubic Foot/Hour [ft\u00b3/hr]":
            NUMout = inter / 7.86579072*10**6
        if units_to == "Cubic Foot/Minute [ft\u00b3/min]":
            NUMout = inter / 0.0004719474
        if units_to == "Cubic Foot/Second [ft\u00b3/sec]":
            NUMout = inter / 0.0283168466
        if units_to == "Cubic Inch/Hour [in\u00b3/hr]":
            NUMout = inter / 4.5519622224454*10**9
        if units_to == "Cubic Inch/Minute [in\u00b3/min]":
            NUMout = inter / 2.7311773333333*10**7
        if units_to == "Cubic Inch/Second [in\u00b3/sec]":
            NUMout = inter / 1.63871*10**5
        
        #Fluid Viscosity (Dynamic) units out
        if units_to == "Pascal Second [pa*s]" or units_to == "Newton Second/Square Meter":
            NUMout = inter / 1
        if units_to == "Kilogram-force Second/Square Meter":
            NUMout = inter / 9.80665
        if units_to == "Millinewton Second/Square Meter" or units_to == "Centipoise [cP]":
            NUMout = inter / 0.001
        if units_to == "Dyne Second/Square Meter" or units_to == "Poise [P]" or units_to == "Gram/Centimeter/Second":
            NUMout = inter / 0.1
        if units_to == "Gigapoise [GP]":
            NUMout = inter / 100000000
        if units_to == "Megapoise [MP]":
            NUMout = inter / 100000
        if units_to == "Kilopoise [kP]":
            NUMout = inter / 100
        if units_to == "Millipoise [mP]":
            NUMout = inter / 0.0001
        if units_to == "Micropoise [µP]":
            NUMout = inter / 1*10**7
        if units_to == "Pound-Force Second/Square Inch":
            NUMout = inter / 6894.7572931684
        if units_to == "Pound-Force Second/Square Foot" or units_to == "Slug/Foot/Second":
            NUMout = inter / 47.8802589802
        if units_to == "Poundal Second/Square Foot" or units_to == "Pound/Foot/Second":
            NUMout = inter / 1.4881639436
        if units_to == "Pound/Foot/Hour [lb/(ft*hr)]":
            NUMout = inter / 0.0004133789
        
        #Fluid Viscosity (kinematic) units out
        if units_to == "Square Meter/Second":
            NUMout = inter / 1
        if units_to == "Square Meter/Hour [m\u00b2/hr]":
            NUMout = inter / 0.0002777778
        if units_to == "Square Centimeter/Second":
            NUMout = inter / 0.0001
        if units_to == "Square Millimeter/Second":
            NUMout = inter / 1*10**6
        if units_to == "Square Foot/Second [ft\u00b2/sec]":
            NUMout = inter / 0.09290304
        if units_to == "Square Foot/Hour [ft\u00b2/hr]":
            NUMout = inter / 2.58064*10**5
        if units_to == "Square Inch/Second [in\u00b2/sec]":
            NUMout = inter / 0.00064516
        if units_to == "Stokes [St]":
            NUMout = inter / 0.0001
        if units_to == "Gigastokes [GSt]":
            NUMout = inter / 100000
        if units_to == "Megastokes [MSt]":
            NUMout = inter / 100
        if units_to == "Kilostokes [kSt]":
            NUMout = inter / 0.1
        if units_to == "Centistokes [cSt]":
            NUMout = inter / 1*10**6
        if units_to == "Millistokes [mSt]":
            NUMout = inter / 1*10**7
        if units_to == "Microstokes [µSt]":
            NUMout = inter / 1*10**10
        
        #Fluid Surface Tension units out
        if units_to == "Newton/Meter [N/m]":
            NUMout = inter / 1
        if units_to == "Millinewton/Meter [mN/m]":
            NUMout = inter / 0.001
        if units_to == "Gram-force/Centimeter":
            NUMout = inter / 0.980665
        if units_to == "Dyne/Centimeter [dyn/cm]" or units_to == "Erg/Square Centimeter":
            NUMout = inter / 0.001
        if units_to == "Erg/Square Millimeter":
            NUMout = inter / 0.1
        if units_to == "Poundal/Inch [pd/in]":
            NUMout = inter / 5.443108491
        if units_to == "Pound-force/Inch [lbf/in]":
            NUMout = inter / 175.1268369864
        
        #Electricity electrical charge units out
        if units_to == "Coulomb [C]" or units_to == "Ampere-second [A*sec]":
            NUMout = inter / 1
        if units_to == "Meagcoulomb [MC]":
            NUMout = inter / 1000000
        if units_to == "Kilocoulomb [kC]":
            NUMout = inter / 1000
        if units_to == "Millicoulomb [mC]":
            NUMout = inter / 0.001
        if units_to == "Microcoulmob [µC]":
            NUMout = inter / 1*10**6
        if units_to == "EMU of Charge" or units_to == "aAbcoulomb [abC]":
            NUMout = inter / 10
        if units_to == "Statcoulomb [stC]" or units_to == "ESU of Charge" or units_to == "Franklin [Fr]":
            NUMout = inter / 3.335640951982*10**10
        if units_to == "Ampere-hour [A*hr]":
            NUMout = inter / 3600
        if units_to == "Ampere-minute [A*min]":
            NUMout = inter / 60
        if units_to == "Faraday (based on carbon 12)":
            NUMout = inter / 96485.309000004
        if units_to == "Elementary Charge [e]":
            NUMout = inter / 1.60217733*10**19
        
        #Electricity electric potential units out
        if units_to == "Volt [V]" or units_to == "Watt/Ampere [W/A]":
            NUMout = inter / 1
        if units_to == "Kilovolt [kV]":
            NUMout = inter / 1000
        if units_to == "Millivolt [mV]":
            NUMout = inter / 0.001
        if units_to == "Abvolt [abV]" or units_to == "EMU of Electric Potential":
            NUMout = inter / 1*10**8
        if units_to == "Statvolt [stV]" or units_to == "ESU of Electric Potential":
            NUMout = inter / 299.7925
        
        #Electricity Current units out
        if units_to == "Ampere [A]":
            NUMout = inter / 1
        if units_to == "Kiloampere [kA]":
            NUMout = inter / 1000
        if units_to == "Milliampere [mA]":
            NUMout = inter / 0.001
        if units_to == "Biot [Bi]" or units_to == "Abampere [abA]" or units_to == "EMU of Current" or units_to == "CGS e.m. Unit":
            NUMout = inter / 10
        if units_to == "Statampere [stA]" or units_to == "ESU of Current" or units_to == "CGS e.s. Unit":
            NUMout = inter / 3.335641*10**10
        
        #Electricity Resistance units out
        if units_to == "Ohm [Ω]" or units_to == "Volt/Ampere [V/A]" or units_to == "Reciprocal Siemens [1/S]":
            NUMout = inter / 1
        if units_to == "Megaohm [MΩ]":
            NUMout = inter / 1000000
        if units_to == "Kiloohm [kΩ]":
            NUMout = inter / 1000
        if units_to == "Milliohm [mΩ]":
            NUMout = inter / 0.001
        if units_to == "Microohm [μΩ]":
            NUMout = inter / 1*10**6
        if units_to == "Abohm" or units_to == "EMU of Resistance":
            NUMout = inter / 1*10**9
        if units_to == "Statohm" or units_to == "ESU of Resistance":
            NUMout = inter / 898755200000
        if units_to == "Quantized Hall Resistance":
            NUMout = inter / 25812.8056
        
        #Electricity Capacitance units out
        if units_to == "Farad [F]" or units_to == "Coulomb/Volt [C/V]":
            NUMout = inter / 1
        if units_to == "Gigafarad [GF]":
            NUMout = inter / 1000000000
        if units_to == "Megafarad [MF]":
            NUMout = inter / 1000000
        if units_to == "Kilofarad [kF]":
            NUMout = inter / 1000
        if units_to == "Centifarad [cF]":
            NUMout = inter / 0.01
        if units_to == "Millifarad [mF]":
            NUMout = inter / 0.001
        if units_to == "Microfarad [μF]":
            NUMout = inter / 1*10**6
        if units_to == "Nanofarad [nF]":
            NUMout = inter / 1*10**9
        if units_to == "Picofarad [pF]":
            NUMout = inter / 1*10**12
        if units_to == "Abfarad [abF]" or units_to == "EMU of Capacitance":
            NUMout = inter / 1000000000
        if units_to == "Statfarad [stF]" or units_to == "ESU of Capacitance":
            NUMout = inter / 1.112650056054*10**12
        
        #Electricity Inductance units out
        if units_to == "Henry [H]" or units_to == "Weber/Ampere [Wb/A]":
            NUMout = inter / 1
        if units_to == "Gigahenry [GH]":
            NUMout = inter / 1000000000
        if units_to == "Megahenry [MH]":
            NUMout = inter / 1000000
        if units_to == "Kilohenry [kH]":
            NUMout = inter / 1000
        if units_to == "Centihenry [cH]":
            NUMout = inter / 0.01
        if units_to == "Millihenry [mH]":
            NUMout = inter / 0.001
        if units_to == "Microhenry [µH]":
            NUMout = inter / 1*10**6
        if units_to == "Nanohenry [nH]":
            NUMout = inter / 1*10**9
        if units_to == "Picohenry [pH]":
            NUMout = inter / 1*10**12
        if units_to == "Abhenry [abH]" or units_to == "EMU of Inductance":
            NUMout = inter / 1*10**9
        if units_to == "Stathenry [stH]" or units_to == "ESU of Inductance":
            NUMout = inter / 898755200000
        
        #Electricity Conductance units out
        if units_to == "Siemens [S]" or units_to == "Ampere/Volt [A/V]" or units_to == "Mho":
            NUMout = inter / 1
        if units_to == "Megasiemens [MS]":
            NUMout = inter / 1000000
        if units_to == "Kilosiemens [kS]":
            NUMout = inter / 1000
        if units_to == "Millisiemens [mS]":
            NUMout = inter / 0.001
        if units_to == "Microsiemens [µS]" or units_to == "Gemmho" or units_to == "Micromho":
            NUMout = inter / 1*10**6
        if units_to == "Abmho":
            NUMout = inter / 1000000000
        if units_to == "Statmho":
            NUMout = inter / 1.1123470522803*10**12
        if units_to == "Quantized Hall Conductance":
            NUMout = inter / 3.87405*10**5
    
        self.NUMunit_output.setValue(float(NUMout))
