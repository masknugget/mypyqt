import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QTreeWidgetItem, QProgressBar
from PySide2.QtCore import Qt
from control_part.c_qtree.QTree import Ui_MainWindow


class TrackUserProgress:
    def __init__(self):
        # Different color template for the QProgressBar depending on it's value
        self.red_template = """
        QProgressBar{
            text-align:center;
            border-radius: 5px;
            border: 2px solid #757575;
            height:  10px;
        }
        QProgressBar::chunk{
            background-color: #FF5252;
        }
        """
        self.yellow_template = """
        QProgressBar{
            text-align:center;
            border-radius: 5px;
            border: 2px solid #757575;
            height: 10px;
        }
        QProgressBar::chunk{
            background-color: #FFD740;
        }
        """
        self.green_template = """
        QProgressBar{
            text-align:center;
            border-radius: 5px;
            border: 2px solid #757575;
            height: 10px;
        }
        QProgressBar::chunk{
            background-color: #69F0AE;
        }
        """
        self.blue_template = """
        QProgressBar{
            text-align:center;
            border-radius: 5px;
            border: 2px solid #757575;
            height: 10px;
        }
        QProgressBar::chunk{
            background-color: #448AFF;
        }
        """

    def return_progress_color(self, progress_count):
        """
        :param progress_count: value of the QProgressBar
        :return: Returns specific color template based on the progress_count parameter
        """
        if progress_count < 10:
            return self.red_template
        elif 15 < progress_count <= 35:
            return self.yellow_template
        elif 35 < progress_count <= 65:
            return self.green_template
        else:
            return self.blue_template


class UserData:
    def __init__(self, name, status, tasks):
        self.name = name
        self.status = status
        self.tasks = tasks


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Set the headers
        self.dataTreeWidget.setHeaderLabels(['ID', 'NAME', 'STATUS'])
        # Create dummy users
        user_1 = UserData("Alan", "Online", {"Task_A": 25, "Task_B": 60})
        user_2 = UserData("Max", "Online", {"Task_A": 68})
        user_3 = UserData("Scarlet", "Offline", {"Task_A": 5, "Task_B": 55, "Task_C": 25})
        users_list = [user_1, user_2, user_3]
        # Loop through users to get the value and insert for each row
        self.dataTreeWidget.clear()
        for index, user in enumerate(users_list):
            self.user_data = QTreeWidgetItem()
            progress_bar_tracker = TrackUserProgress()
            self.user_data.setData(0, Qt.DisplayRole, index)
            self.user_data.setData(1, Qt.DisplayRole, user.name)
            self.user_data.setData(2, Qt.DisplayRole, user.status)
            self.dataTreeWidget.addTopLevelItem(self.user_data)
            # Loop through each user's tasks and display it's progress bar.
            for user_task in sorted(list(user.tasks.keys())):
                user_task_child = QTreeWidgetItem()
                user_task_progress = QProgressBar()
                user_task_progress.setStyleSheet((progress_bar_tracker.return_progress_color(user.tasks[user_task])))
                user_task_progress.setValue(user.tasks[user_task])
                user_task_child.setData(0, Qt.DisplayRole, user_task)
                self.user_data.addChild(user_task_child)
                self.dataTreeWidget.setItemWidget(user_task_child, 1, user_task_progress)
        # Variable that handles when to expand and collapse all the columns
        self.click_counter = 2
        self.treeButton.clicked.connect(self.view_hide_clicked)

    def view_hide_clicked(self):
        if self.click_counter % 2 == 0:
            self.dataTreeWidget.expandAll()

        elif self.click_counter % 2 != 0:
            self.dataTreeWidget.collapseAll()

        self.click_counter += 1


if __name__ == '__main__':
    app = QApplication([])
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())