import csv
import io
import os
import re
from PySide6.QtWidgets import QMainWindow, QMessageBox
from UnitConverter.UnitConverter_ui_new import Ui_UnitConverter


def parse_base_factor(value):
    if value is None:
        return 1.0

    text = str(value).strip()
    if text == '':
        return 1.0

    normalized = text.lower().replace(' ', '')
    if normalized in {'x', '1'}:
        return 1.0

    if '*' in normalized:
        match = re.search(r'x\*([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)', normalized)
        if match:
            return float(match.group(1))

    if '/' in normalized:
        match = re.search(r'x/([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)', normalized)
        if match:
            divisor = float(match.group(1))
            if divisor == 0:
                return 1.0
            return 1.0 / divisor

    try:
        return float(text)
    except ValueError:
        return 1.0


def decode_csv_text(value):
    text = str(value)

    def replace_escape(match):
        return chr(int(match.group(1) or match.group(2) or match.group(3), 16))

    return re.sub(r'\\u([0-9A-Fa-f]{4})|\\U([0-9A-Fa-f]{8})|\\x([0-9A-Fa-f]{2})', replace_escape, text)


def read_csv_rows(filename, expected_headers):
    with open(filename, 'rb') as csvfile:
        data = csvfile.read()

    encodings = ('utf-8-sig', 'utf-16', 'utf-16-le', 'utf-16-be', 'cp1252', 'latin-1')
    expected_headers = {header.lower() for header in expected_headers}
    last_error = None

    for encoding in encodings:
        try:
            text = data.decode(encoding)
            reader = csv.DictReader(io.StringIO(text, newline=''))
            fieldnames = reader.fieldnames or []
            normalized_fieldnames = [
                fieldname.strip().lstrip('\ufeff') if fieldname else fieldname
                for fieldname in fieldnames
            ]
            if not expected_headers.intersection(
                fieldname.lower() for fieldname in normalized_fieldnames if fieldname
            ):
                continue
            reader.fieldnames = normalized_fieldnames
            return list(reader), encoding
        except (UnicodeDecodeError, UnicodeError, csv.Error) as error:
            last_error = error

    raise UnicodeError(f'Could not decode CSV file: {filename}') from last_error


class Unit_Converter(QMainWindow, Ui_UnitConverter):
    def __init__(self):
        super().__init__()
        self.ui = Ui_UnitConverter()
        self.setupUi(self)
        self.setWindowTitle('Unit Converter')

        try:
            self.unitstyle.currentTextChanged.disconnect(self.unitsubcat.setCurrentText)
        except Exception:
            pass

        self.conversion_data = {}
        self.index_map = {}
        self.type_to_category = {}

        csv_path = os.path.join(os.path.dirname(__file__), 'main_index.csv')
        self.load_main_index(csv_path)

        self.unitstyle.clear()
        if self.index_map:
            self.unitstyle.addItems(list(self.index_map.keys()))
            self.unitstyle.setCurrentIndex(0)

        self.unitstyle.currentTextChanged.connect(self.update_unitsubcat)
        self.unitsubcat.currentTextChanged.connect(self.subcategory_selected)

        self.units_from.currentTextChanged.connect(self.unit_convert)
        self.units_to.currentTextChanged.connect(self.unit_convert)
        self.NUMunit_input.valueChanged.connect(self.unit_convert)

        if self.unitstyle.count() > 0:
            self.update_unitsubcat(self.unitstyle.currentText())

    def load_main_index(self, filename):
        if not os.path.isfile(filename):
            QMessageBox.warning(self, 'Index Load', f'main_index.csv not found: {filename}')
            return

        try:
            rows, encoding = read_csv_rows(filename, ('Category', 'Type'))
            for row in rows:
                cat = row.get('Category') or row.get('category') or row.get('CategoryName')
                typ = row.get('Type') or row.get('type') or row.get('TypeName')
                if not cat or not typ:
                    continue
                cat = cat.strip()
                typ = typ.strip()
                self.index_map.setdefault(cat, [])
                if typ not in self.index_map[cat]:
                    self.index_map[cat].append(typ)
            print(f'[UnitConverter] Loaded index {filename} using {encoding}')
        except Exception as e:
            QMessageBox.warning(self, 'Index Load', f'Could not load main_index.csv: {e}')

    def update_unitsubcat(self, category):
        self.unitsubcat.blockSignals(True)
        self.unitsubcat.clear()
        types = self.index_map.get(category, [])
        if types:
            self.unitsubcat.addItems(types)
            if self.unitsubcat.count() > 0:
                self.unitsubcat.setCurrentIndex(0)
        self.unitsubcat.blockSignals(False)
        self.subcategory_selected(self.unitsubcat.currentText())

    def _resolve_unit_csv_path(self, subcat):
        csv_dir = os.path.join(os.path.dirname(__file__), 'units_data')
        candidates = [
            os.path.join(csv_dir, f'{subcat}.csv'),
            os.path.join(csv_dir, f'{subcat.lower()}.csv'),
            os.path.join(csv_dir, f'{subcat.title()}.csv'),
        ]

        for path in candidates:
            if os.path.isfile(path):
                return path

        for file_name in sorted(os.listdir(csv_dir)):
            if file_name.lower() == f'{subcat.lower()}.csv':
                return os.path.join(csv_dir, file_name)

        return os.path.join(csv_dir, f'{subcat}.csv')

    def subcategory_selected(self, subcat):
        if not subcat:
            return

        category = self.unitstyle.currentText()
        if not category:
            return

        csv_path = self._resolve_unit_csv_path(subcat)
        units_map = {}
        if os.path.isfile(csv_path):
            try:
                rows, encoding = read_csv_rows(csv_path, ('UnitName', 'Name', 'unit'))
                loaded_rows = 0
                for row in rows:
                    name = row.get('UnitName') or row.get('Name') or row.get('unit')
                    if not name:
                        continue
                    name = str(name).strip()
                    abbreviation = decode_csv_text(row.get('Abrv') or '').strip()
                    use = decode_csv_text(row.get('Use') or '').strip()
                    if abbreviation:
                        name += f' [{abbreviation}]'
                    if use:
                        name += f' ({use})'
                    factor_raw = row.get('toBase') or row.get('to_base')
                    factor = parse_base_factor(factor_raw)
                    units_map[name] = factor
                    loaded_rows += 1
                print(f'[UnitConverter] Loaded {loaded_rows} units from {csv_path} using {encoding}')
            except Exception as error:
                print(f'[UnitConverter] Failed to load {csv_path}: {error}')
                units_map = {}
        else:
            print(f'[UnitConverter] Missing unit file for {category}/{subcat}: {csv_path}')
            QMessageBox.information(self, 'Units Missing', f'Unit file not found: {csv_path}')

        self.conversion_data.setdefault(category, {})
        self.conversion_data[category][subcat] = units_map

        self.units_from.blockSignals(True)
        self.units_to.blockSignals(True)
        self.units_from.clear()
        self.units_to.clear()
        if units_map:
            units = list(units_map.keys())
            self.units_from.addItems(units)
            self.units_to.addItems(units)
            if len(units) > 0:
                self.units_from.setCurrentIndex(0)
                self.units_to.setCurrentIndex(0)
        self.units_from.blockSignals(False)
        self.units_to.blockSignals(False)

        self.unit_convert()

    def unit_convert(self):
        cat = self.unitstyle.currentText()
        sub = self.unitsubcat.currentText()
        if not cat or not sub:
            return

        u_from = self.units_from.currentText()
        u_to = self.units_to.currentText()
        if not u_from or not u_to:
            return

        try:
            val_in = float(self.NUMunit_input.value())
        except Exception:
            return

        try:
            factors = self.conversion_data.get(cat, {}).get(sub, {})
            if u_from not in factors or u_to not in factors:
                return
            base_value = val_in * factors[u_from]
            result = base_value / factors[u_to]
            self.NUMunit_output.setValue(result)
        except Exception:
            return