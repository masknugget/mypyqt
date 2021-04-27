import sys
from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel, QSqlTableModel
from PyQt5.QtWidgets import QApplication, QMessageBox, QTableView


class Demo(QTableView):
    def __init__(self):
        super(Demo, self).__init__()
        self.db = None
        self.db_connect()
        self.sql_exec()

    def db_connect(self):
        self.db = QSqlDatabase.addDatabase('QMYSQL')
        self.db.setHostName('localhost')
        self.db.setDatabaseName('test_db')
        self.db.setUserName('root')
        self.db.setPassword('password')
        if not self.db.open():
            QMessageBox.critical(self, 'Database Connection', self.db.lastError().text())

    def closeEvent(self, QCloseEvent):
        self.db.close()

    def sql_exec(self):
        model = QSqlQueryModel()                        # 1
        model.setQuery("SELECT id, name, class, score FROM students")
        model.setHeaderData(0, Qt.Horizontal, 'ID')
        model.setHeaderData(1, Qt.Horizontal, 'Name')
        model.setHeaderData(2, Qt.Horizontal, 'Class')
        model.setHeaderData(3, Qt.Horizontal, ' Score')

        self.setModel(model)                            # 2

        for i in range(model.rowCount()):               # 3
            id = model.record(i).value('id')
            name = model.record(i).value(1)
            print(id, name)

        print('---------------------')

        for i in range(model.rowCount()):               # 4
            id = model.data(model.index(i, 0))
            name = model.data(model.index(i, 1))
            print(id, name)


    def sql_exec(self):
        model = QSqlTableModel()                            # 1
        model.setTable('students')
        model.setEditStrategy(QSqlTableModel.OnFieldChange)
        model.setHeaderData(0, Qt.Horizontal, 'ID')
        model.setHeaderData(1, Qt.Horizontal, 'Class')
        model.setHeaderData(2, Qt.Horizontal, 'Name')
        model.setHeaderData(3, Qt.Horizontal, 'Score')
        model.select()

        self.setModel(model)

    def sql_exec(self):
        model = QSqlTableModel()
        model.setTable('students')
        model.setEditStrategy(QSqlTableModel.OnFieldChange)
        model.setHeaderData(0, Qt.Horizontal, 'ID')
        model.setHeaderData(1, Qt.Horizontal, 'Class')
        model.setHeaderData(2, Qt.Horizontal, 'Name')
        model.setHeaderData(3, Qt.Horizontal, 'Score')
        model.select()

        model.insertRow(0)  # 1
        model.setData(model.index(0, 0), 201801010111)
        model.setData(model.index(0, 1), '0101')
        model.setData(model.index(0, 2), 'Who Cares')
        model.setData(model.index(0, 3), 0.5)
        model.submit()

        self.setModel(model)

    def sql_exec(self):
        model = QSqlTableModel()
        model.setTable('students')
        model.setEditStrategy(QSqlTableModel.OnFieldChange)
        model.setHeaderData(0, Qt.Horizontal, 'ID')
        model.setHeaderData(1, Qt.Horizontal, 'Class')
        model.setHeaderData(2, Qt.Horizontal, 'Name')
        model.setHeaderData(3, Qt.Horizontal, 'Score')

        model.insertRow(0)
        model.setData(model.index(0, 0), 2018010111)
        model.setData(model.index(0, 1), '0101')
        model.setData(model.index(0, 2), 'Who Cares')
        model.setData(model.index(0, 3), 0.5)
        model.submit()

        model.setFilter('score < 60')  # 1
        model.select()

        self.setModel(model)

    def sql_exec(self):
        model = QSqlTableModel()
        model.setTable('students')
        model.setEditStrategy(QSqlTableModel.OnFieldChange)
        model.setHeaderData(0, Qt.Horizontal, 'ID')
        model.setHeaderData(1, Qt.Horizontal, 'Class')
        model.setHeaderData(2, Qt.Horizontal, 'Name')
        model.setHeaderData(3, Qt.Horizontal, 'Score')

        model.insertRow(0)
        model.setData(model.index(0, 0), 2018010111)
        model.setData(model.index(0, 1), '0101')
        model.setData(model.index(0, 2), 'Who Cares')
        model.setData(model.index(0, 3), 0.5)
        model.submit()

        model.setFilter('score < 60')
        model.select()

        model.removeRow(0)  # 1
        model.submit()

        self.setModel(model)

    ​

    def sql_exec(self):
        model = QSqlRelationalTableModel()
        model.setTable('students')

        # 1
        model.setRelation(1, QSqlRelation('teachers', 'class', 'name'))

        # 2
        model.setHeaderData(0, Qt.Horizontal, 'ID')
        model.setHeaderData(1, Qt.Horizontal, 'Teacher')
        model.setHeaderData(2, Qt.Horizontal, 'Student')
        model.setHeaderData(3, Qt.Horizontal, 'Score')
        model.select()

        self.setModel(model)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())

