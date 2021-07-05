from PyQt5 import QtWidgets, QtCore, QtGui


class Header(QtWidgets.QHeaderView):
    filterChanged = QtCore.pyqtSignal(int, str)
    fieldsVisible = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields = []
        self.sectionCountChanged.connect(self.generateFields)
        self.sectionResized.connect(self.updateFields)
        self.parent().horizontalScrollBar().valueChanged.connect(self.updateFields)
        self.parent().verticalScrollBar().valueChanged.connect(self.updateFields)

    def setFieldsVisible(self, visible):
        if visible == self.fieldsVisible:
            return
        self.fieldsVisible = visible
        self.generateFields()

    def generateFields(self):
        while self.fields:
            self.fields.pop().deleteLater()
        if self.fieldsVisible:
            for s in range(self.count()):
                edit = QtWidgets.QLineEdit(self)
                edit.show()
                self.fields.append(edit)
                edit.textChanged.connect(lambda text, s=s: self.filterChanged.emit(s, text))
            self.updateFields()
        self.updateGeometries()

    def updateFields(self):
        offset = self.offset()
        y = QtWidgets.QHeaderView.sizeHint(self).height()
        for section, field in enumerate(self.fields):
            field.move(self.sectionPosition(section) - offset, y)
            field.resize(self.sectionSize(section), field.sizeHint().height())

    def updateGeometries(self):
        if self.fields:
            self.setViewportMargins(0, 0, 0, self.fields[0].sizeHint().height())
        else:
            self.setViewportMargins(0, 0, 0, 0)
        super().updateGeometries()
        # ensure that the parent view updates correctly
        self.parent().updateGeometries()
        self.updateFields()

    def sizeHint(self):
        hint = super().sizeHint()
        if self.fields:
            hint.setHeight(hint.height() + self.fields[0].sizeHint().height())
        return hint


class SearchTable(QtWidgets.QTableView):
    def __init__(self):
        super().__init__()
        model = QtGui.QStandardItemModel()
        for row in range(8):
            model.appendRow([QtGui.QStandardItem('Item {} {}'.format(row, i)) for i in range(8)])
        self.setModel(model)
        self.setHorizontalHeader(Header(QtCore.Qt.Horizontal, self))