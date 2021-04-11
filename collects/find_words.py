from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets
import os
import sys


#   Find keywords of a file name including ext name
#   Can also find keyword in a readable text file


class MyDialog(QtWidgets.QDialog):

    def __init__(self):
        super(MyDialog, self).__init__(parent=None)

        self.setWindowTitle("Find Words/Files")
        self.setMinimumSize(300, 100)
        palette = QtGui.QPalette()
        self.setPalette(palette)

        #   Able to maximize window, remove top left icon
        self.setWindowFlags(self.windowFlags() |
                            QtCore.Qt.WindowSystemMenuHint |
                            QtCore.Qt.WindowMinMaxButtonsHint
                            )
        self.create_widgets()
        self.create_layout()
        self.init_UIState()
        self.create_connections()

    def create_widgets(self):
        #   This sets up the csv_path location. To where this py file is executed
        dir, file = os.path.split(__file__)

        #   Instructions button
        self.instructions_button = QtWidgets.QPushButton('Instructions')
        self.instructions_button.setFont(QtGui.QFont('Segoe UI', 10))
        self.instructions_button.setAutoDefault(False)
        self.instructions_button.setFixedSize(100, 25)

        #   Always on top button
        self.always_on_top_button = QtWidgets.QPushButton('Always on Top')
        self.always_on_top_button.setFont(QtGui.QFont('Segoe UI', 10))
        self.always_on_top_button.setAutoDefault(False)
        self.always_on_top_button.setFixedSize(100, 25)

        #   Horizontal line
        self.line = QtWidgets.QFrame()
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setStyleSheet('color: rgb(100,100,100)')

        #   Keyword label
        self.keyword_label = QtWidgets.QLabel('To Find: ')
        self.keyword_label.setFont(QtGui.QFont('Segoe UI', 10))

        #   Keyword line edit
        self.keywords_line_edit = QtWidgets.QLineEdit()
        self.keywords_line_edit.setPlaceholderText('some word/some file name')
        self.keywords_line_edit.setFont(QtGui.QFont('Segoe UI', 10))

        #   Category spacer
        self.category_spacer = QtWidgets.QSpacerItem(100, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)

        #   Category label
        self.category_label = QtWidgets.QLabel('Category:')
        self.category_label.setFont(QtGui.QFont('Segoe UI', 10))

        #   Checkbox button
        self.find_words_checkBox = QtWidgets.QCheckBox('Find Word')
        self.find_words_checkBox.setFont(QtGui.QFont('Segoe UI', 10))

        #   Checkbox button
        self.find_file_checkBox = QtWidgets.QCheckBox('Find File/Ext')
        self.find_file_checkBox.setFont(QtGui.QFont('Segoe UI', 10))

        #   Path label
        self.path_label = QtWidgets.QLabel('Path: ')
        self.path_label.setFont(QtGui.QFont('Segoe UI', 10))

        #   Path line edit
        self.path_line_edit = QtWidgets.QLineEdit()
        self.path_line_edit.setPlaceholderText('C:/Users/')
        self.path_line_edit.setFont(QtGui.QFont('Segoe UI', 10))

        #   Path button
        self.path_button = QtWidgets.QPushButton('Path')
        self.path_button.setFont(QtGui.QFont('Segoe UI', 10))
        self.path_button.setAutoDefault(False)
        self.path_button.setFixedSize(70, 25)

        #   Start button
        self.start_button = QtWidgets.QPushButton('Start')
        self.start_button.setFont(QtGui.QFont('Segoe UI', 10))
        self.start_button.setFixedSize(300, 25)
        self.start_button.setAutoDefault(False)

        #   Text browser
        self.text_browser = QtWidgets.QTextBrowser()
        #   Prevent text disappear when clicking on hyperlink
        self.text_browser.setOpenLinks(False)
        self.text_browser.setFont(QtGui.QFont('Segoe UI', 10))
        self.text_browser.setPlaceholderText('Results will be printed here'
                                             '\nIf no results, this will be blank')
        self.text_browser.setLineWrapMode(QtWidgets.QTextBrowser.NoWrap)

        #   Progress bar
        self.progress_bar = QtWidgets.QProgressBar()
        self.progress_bar.setValue(0)

    def create_layout(self):
        aot_layout = QtWidgets.QHBoxLayout()
        aot_layout.addWidget(self.instructions_button)
        aot_layout.addWidget(self.always_on_top_button)

        explain_layout = QtWidgets.QHBoxLayout()
        explain_layout.setContentsMargins(0, 0, 0, 0)

        line_layout = QtWidgets.QHBoxLayout()
        line_layout.setContentsMargins(0, 5, 0, 0)
        line_layout.addWidget(self.line)

        keyword_layout = QtWidgets.QHBoxLayout()
        keyword_layout.setContentsMargins(0, 5, 0, 0)
        keyword_layout.addWidget(self.keyword_label)
        keyword_layout.addWidget(self.keywords_line_edit)

        category_layout = QtWidgets.QHBoxLayout()
        category_layout.addWidget(self.category_label, alignment=QtCore.Qt.AlignCenter)
        category_layout.addWidget(self.find_words_checkBox, alignment=QtCore.Qt.AlignLeft)
        category_layout.addWidget(self.find_file_checkBox, alignment=QtCore.Qt.AlignCenter)

        path_btn_layout = QtWidgets.QHBoxLayout()
        path_btn_layout.setContentsMargins(0, 5, 0, 0)
        path_btn_layout.addWidget(self.path_label)
        path_btn_layout.addWidget(self.path_line_edit)
        path_btn_layout.addWidget(self.path_button)

        start_btn_layout = QtWidgets.QHBoxLayout()
        start_btn_layout.addWidget(self.start_button, alignment=QtCore.Qt.AlignCenter)
        start_btn_layout.setContentsMargins(0, 10, 0, 0)

        list_layout = QtWidgets.QHBoxLayout()
        list_layout.setContentsMargins(0, 10, 0, 0)
        list_layout.addWidget(self.text_browser)

        progress_layout = QtWidgets.QHBoxLayout()
        progress_layout.addWidget(self.progress_bar)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setAlignment(QtCore.Qt.AlignTop)
        main_layout.addLayout(aot_layout)
        main_layout.addLayout(line_layout)
        main_layout.addLayout(category_layout)
        main_layout.addLayout(keyword_layout)
        main_layout.addLayout(path_btn_layout)
        main_layout.addLayout(start_btn_layout)
        main_layout.addLayout(list_layout)
        main_layout.addLayout(progress_layout)

    #   Init state after creation
    def init_UIState(self):
        self.find_words_checkBox.setChecked(True)

    #   Link
    def create_connections(self):
        self.instructions_button.clicked.connect(self.instructions)
        self.always_on_top_button.clicked.connect(self.aot)
        self.find_file_checkBox.clicked.connect(self.uncheckOther1)
        self.find_words_checkBox.clicked.connect(self.uncheckOther2)
        self.path_button.clicked.connect(self.find_address)
        self.start_button.clicked.connect(self.main)

        #   Omit main function when pressing enter on lineedit
        self.keywords_line_edit.returnPressed.connect(self.main)
        self.path_line_edit.returnPressed.connect(self.main)
        self.text_browser.anchorClicked.connect(self.handle_links)

    def instructions(self):
        self.my_dialog2 = MyDialog2()
        self.my_dialog2.show()

    def closeEvent(self, event):
        #   Make sure no instance are working in background
        sys.exit()
        try:
            #   make sure instruction window is closed, when main window closes
            self.my_dialog2.close()
        except:
            pass

    #   Prevent closing app from pressing Esc key
    def keyPressEvent(self, event):
        if not event.key() == QtCore.Qt.Key_Escape:
            super(MyDialog, self).keyPressEvent(event)

    #   Toggle always on top
    def aot(self):
        on = bool(my_dialog.windowFlags() & QtCore.Qt.WindowStaysOnTopHint)
        my_dialog.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint, not on)

        #   Last remembered window size
        x = str(my_dialog.size()).split("(")[1].split(",")[0]
        y = str(my_dialog.size()).split("(")[1].split(",")[1].replace(")", "")
        my_dialog.resize(int(x), int(y))
        my_dialog.show()

    def uncheckOther1(self):
        if self.find_file_checkBox.isChecked:
            self.find_words_checkBox.setChecked(False)

    def uncheckOther2(self):
        if self.find_words_checkBox.isChecked:
            self.find_file_checkBox.setChecked(False)

    #   Location for folders of items
    def find_address(self):
        file_path = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Folder", "")
        file_path = str(file_path)

        if file_path:
            self.path_line_edit.setText(file_path)

    #   Main code
    def main(self):
        #   Sets progress bar 0 each time start button is pressed
        self.progress_bar.setValue(0)

        new_path = self.path_line_edit.text()

        #   If either keyword box or path box is empty, nothing will happen
        if self.keywords_line_edit.text() == '':
            return
        if new_path == '':
            return

        #   Checkbox button 1
        if self.find_file_checkBox.isChecked():
            procedure = 'Find File/Ext'
        #   Checkbox button 2
        if self.find_words_checkBox.isChecked():
            procedure = 'Find Word'

        if procedure == 'Find File/Ext':
            keyword_list = []
            keywords = self.keywords_line_edit.text()

            #   Creates list from keywords
            # keyword_list = [i.strip() for i in keywords.split(',')]
            keyword_list = [keywords.strip()]

            #   Clears the box list each time start button is pressed
            self.text_browser.clear()

            countdown = 0
            #   Finds all files in root and its dirs
            for root, dirs, files in os.walk(new_path):
                for file in files:
                    fileNameLowered = file.lower()

                    #   Progress bar runs while calculation
                    self.progress_bar.setValue(countdown * 20 / len(files))
                    #   Since windows is weird it mixes \ and /. And to keep it consistent.
                    #   It'll replace the \ in the end
                    edit_path = root.replace('\\', '/')
                    for keys in keyword_list:
                        keyNameLowered = keys.lower()
                        if keyNameLowered in fileNameLowered:
                            #   If  these keywords do match some parts of a filename
                            #   It'll fill the list.
                            self.text_browser.setTextColor(QtGui.QColor(255, 255, 255))
                            self.text_browser.append('')
                            self.text_browser.append('')

                            url = QtCore.QUrl.fromLocalFile(edit_path).toString()
                            folder_location = "<a href=\"{}\"> <font>{}</font> </a>".format(url, edit_path)
                            self.text_browser.append('<em>Full_path_________ </em>' + folder_location)
                            self.text_browser.append('<em>File_name________ </em>' + '<span>{}</span>'.format(file))

                countdown += 1
        else:
            keyword = self.keywords_line_edit.text()

            #   Clears the box list each time start button is pressed
            self.text_browser.clear()

            count = 0
            #   Stores the file and its path
            read_files = {}
            #   Add readable files
            file_ext = ['.txt', '.py', '.pyp', '.md', '.csv', '.cs', 'cpp', '.java', '.js', '.html', '.css', '.doc',
                        '.rtf', '.xlsx', '.c']
            #   Finds all files in root and its dirs
            for root, dirs, files in os.walk(new_path):
                for file in files:
                    file_name, ext = os.path.splitext(file)
                    if ext in file_ext:
                        #   Since dictionaries cant have duplicate key names. I will
                        #   add _tempString_ the end of root and remove it in the next for loop
                        #   down below
                        if root in read_files.keys():
                            read_files[root + '_tempString_' + str(count)] = file
                        else:
                            read_files[root] = file
                        count += 1

            countdown = 0
            #   When it does find readable files
            for path, file in read_files.items():
                if '_tempString_' in path:
                    true_path = path.split('_tempString_')[0]
                else:
                    true_path = path
                with open(true_path + '/' + file, 'r') as f:
                    #   Progress bar runs while calculation
                    self.progress_bar.setValue(countdown * 40 / len(read_files))
                    #   try except is used because unicode error when reading some py files
                    try:
                        for num, line in enumerate(f, 1):
                            lineLowered = line.lower()
                            #   Since windows is weird it mixes \ and /. And to keep it consistent.
                            #   It'll replace the \ in the end
                            edit_path = true_path.replace('\\', '/')
                            keywordLowered = keyword.lower()
                            if keywordLowered in lineLowered:
                                #   Appends the link box edit line if a keyword is found
                                self.text_browser.setTextColor(QtGui.QColor(255, 255, 255))
                                self.text_browser.append('')
                                self.text_browser.append('')

                                url = QtCore.QUrl.fromLocalFile(edit_path).toString()
                                folder_location = "<a href=\"{}\"> <font>{}</font> </a>".format(url, edit_path)
                                self.text_browser.append('<em>Full_path_________ </em>' + folder_location)
                                self.text_browser.append('<em>File_name________ </em>' + '<span>{}</span>'.format(file))
                                self.text_browser.append(
                                    '<em>Line_number_____ </em>' + '<span>{}</span>'.format(str(num)))
                                self.text_browser.append(
                                    '<em>Full_line__________ </em>' + "<span>{}</span>".format(line.lstrip()))
                    except:
                        pass
                countdown += 1
        self.progress_bar.setValue(100)

    #   Able to open folders with spaces in them
    def handle_links(self, url):
        if not url.scheme():
            url = QtCore.QUrl.fromLocalFile(url.toString())
        QtGui.QDesktopServices.openUrl(url)


#   Instruction
class MyDialog2(QtWidgets.QDialog):
    def __init__(self):
        super(MyDialog2, self).__init__(parent=None)

        self.setWindowTitle("Find Files/Words")
        self.setFixedSize(300, 300)
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
        #   Able to maximize window, remove icon
        self.setWindowFlags(self.windowFlags() |
                            QtCore.Qt.WindowSystemMenuHint |
                            QtCore.Qt.WindowMinMaxButtonsHint
                            )

        string_1 = 'INSTRUCTIONS \n\nFind File Ext \nTo look for file or its file type extension. Type the keywords you are looking for. '
        string_2 = 'Click on "Find File/Ext", then press "Start". \n\nFind Word. \nTo search a word, in a "read-able text file". Type the word, click on "Find Word" '
        string_3 = 'and press "Start.'
        my_strings = string_1 + string_2 + string_3
        self.path_explain_label = QtWidgets.QLabel(my_strings)
        self.path_explain_label.setFont(QtGui.QFont('Segoe UI', 10))
        self.path_explain_label.setWordWrap(True)

        explain_layout = QtWidgets.QHBoxLayout(self)
        explain_layout.addWidget(self.path_explain_label)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    #   Dark mode
    app.setStyle(QtWidgets.QStyleFactory.create('fusion'))
    dark_palette = QtGui.QPalette()
    #   Base
    dark_palette.setColor(QtGui.QPalette.Window, QtGui.QColor(68, 68, 68))
    dark_palette.setColor(QtGui.QPalette.WindowText, QtGui.QColor(208, 208, 208))
    #   Text box
    dark_palette.setColor(QtGui.QPalette.Base, QtGui.QColor(43, 43, 43))
    dark_palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(208, 208, 208))
    dark_palette.setColor(QtGui.QPalette.ToolTipBase, QtGui.QColor(208, 208, 208))
    dark_palette.setColor(QtGui.QPalette.ToolTipBase, QtGui.QColor(208, 208, 208))
    dark_palette.setColor(QtGui.QPalette.Text, QtGui.QColor(208, 208, 208))
    #   Button
    dark_palette.setColor(QtGui.QPalette.Button, QtGui.QColor(70, 70, 70))
    dark_palette.setColor(QtGui.QPalette.ButtonText, QtGui.QColor(208, 208, 208))
    dark_palette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.red)
    dark_palette.setColor(QtGui.QPalette.Link, QtGui.QColor(42, 130, 218))
    dark_palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(35, 109, 179))
    app.setPalette(dark_palette)

    my_dialog = MyDialog()
    #   Focus on keyword lineedit
    my_dialog.keywords_line_edit.setFocus()
    my_dialog.show()
    app.exec_()