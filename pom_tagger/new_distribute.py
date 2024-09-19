from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow
from PyQt5.QtCore import Qt
import extract as ext
import sys

path_name = "9509"
# an list that stores all filenames in the folder
file_list = ext.get_filenames(path_name)
# the number of files in the folder
file_size = len(file_list)
# a global variable that stores current file location,, from 0 to file_size
curr_file_location = 0
# a string that stores current file
curr_file = file_list[curr_file_location]
# a list that stores all variables in current file

var_list = ext.extract_list(curr_file)
# the number of variables in current file
variable_size = len(var_list) - 1
# a global variable that stores current variable location,, from 0 to variable_size
curr_var_location = 0
# a string taht stores current variable traced by curr_var_location
curr_var = var_list[curr_var_location]


# an Int value that used to determine the symbol's attribute
# 0 -> undefine, 1 -> variable, 2 -> constant, 3 -> operator, 4 -> unit descriptor
symbol_choice = 0
# an Int value that used to determine the variable's attribute
# 0 -> undefine, 1 -> scalar, 2 -> vector, 3 -> matrix
variable_choice = 0
# an Int value that used to determine the constant/operator's attribute
# 0 -> undefine, 1 -> local, 2 -> global, 3 -> discipline specified
constant_choice = 0

# a dummmy template class
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        pass

    def retranslateUi(self, MainWindow):
        pass


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(790, 755)

        # main menu part of GUI
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_next_file = QtWidgets.QPushButton(self.centralwidget)
        self.button_next_file.setGeometry(QtCore.QRect(490, 10, 101, 41))
        self.button_next_file.setObjectName("button_next_file")
        self.try_label1 = QtWidgets.QLabel(self.centralwidget)
        self.try_label1.setGeometry(QtCore.QRect(10, 20, 311, 31))
        self.try_label1.setObjectName("try_label1")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 50, 781, 121))
        self.listWidget.setObjectName("listWidget")
        self.button_prev_var = QtWidgets.QPushButton(self.centralwidget)
        self.button_prev_var.setGeometry(QtCore.QRect(590, 10, 101, 41))
        self.button_prev_var.setObjectName("button_prev_var")
        self.button_next_var = QtWidgets.QPushButton(self.centralwidget)
        self.button_next_var.setGeometry(QtCore.QRect(690, 10, 101, 41))
        self.button_next_var.setObjectName("button_next_var")
        self.file_lable = QtWidgets.QLabel(self.centralwidget)
        self.file_lable.setGeometry(QtCore.QRect(10, 50, 500, 41))
        self.file_lable.setObjectName("file_lable")
        self.curr_var_label = QtWidgets.QLabel(self.centralwidget)
        self.curr_var_label.setGeometry(QtCore.QRect(40, 80, 281, 41))
        self.curr_var_label.setObjectName("curr_var_label")
        self.symbol_label = QtWidgets.QLabel(self.centralwidget)
        self.symbol_label.setGeometry(QtCore.QRect(40, 110, 500, 31))
        self.symbol_label.setObjectName("symbol_label")
        self.content_label = QtWidgets.QLabel(self.centralwidget)
        self.content_label.setGeometry(QtCore.QRect(40, 140, 600, 21))
        self.content_label.setObjectName("content_label")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(10, 200, 781, 141))
        self.listWidget_2.setObjectName("listWidget_2")
        self.symbol_select_label = QtWidgets.QLabel(self.centralwidget)
        self.symbol_select_label.setGeometry(QtCore.QRect(10, 200, 350, 21))
        self.symbol_select_label.setObjectName("symbol_select_label")
        self.variable_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.variable_radio.setGeometry(QtCore.QRect(50, 220, 115, 19))
        self.variable_radio.setObjectName("variable_radio")
        self.constant_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.constant_radio.setGeometry(QtCore.QRect(50, 250, 115, 19))
        self.constant_radio.setObjectName("constant_radio")
        self.operator_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.operator_radio.setGeometry(QtCore.QRect(50, 280, 115, 19))
        self.operator_radio.setObjectName("operator_radio")
        self.unit_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.unit_radio.setGeometry(QtCore.QRect(50, 310, 151, 19))
        self.unit_radio.setObjectName("unit_radio")

        self.dummy_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.dummy_radio.setGeometry(QtCore.QRect(50, 500, 1, 200))
        self.dummy_radio.setObjectName("dummy_radio")

        # variable part of the GUI
        self.variable_frame = QtWidgets.QFrame(self.centralwidget)
        self.variable_frame.setGeometry(QtCore.QRect(10, 360, 771, 141))
        self.variable_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.variable_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.variable_frame.setObjectName("variable_frame")
        self.matrix_radio = QtWidgets.QRadioButton(self.variable_frame)
        self.matrix_radio.setGeometry(QtCore.QRect(50, 110, 115, 19))
        self.matrix_radio.setObjectName("matrix_radio")
        self.assign_attribute_label = QtWidgets.QLabel(self.variable_frame)
        self.assign_attribute_label.setGeometry(QtCore.QRect(0, 30, 300, 16))
        self.assign_attribute_label.setObjectName("assign_attribute_label")
        self.attribute_label = QtWidgets.QLabel(self.variable_frame)
        self.attribute_label.setGeometry(QtCore.QRect(0, 0, 411, 16))
        self.attribute_label.setObjectName("attribute_label")
        self.listWidget_3 = QtWidgets.QListWidget(self.variable_frame)
        self.listWidget_3.setGeometry(QtCore.QRect(0, 20, 791, 121))
        self.listWidget_3.setObjectName("listWidget_3")
        self.vector_radio = QtWidgets.QRadioButton(self.variable_frame)
        self.vector_radio.setGeometry(QtCore.QRect(50, 80, 115, 19))
        self.vector_radio.setObjectName("vector_radio")
        self.scalar_radio = QtWidgets.QRadioButton(self.variable_frame)
        self.scalar_radio.setGeometry(QtCore.QRect(50, 50, 115, 19))
        self.scalar_radio.setObjectName("scalar_radio")

        self.dummy_var_radio = QtWidgets.QRadioButton(self.variable_frame)
        self.dummy_var_radio.setGeometry(QtCore.QRect(50, 520, 1, 200))
        self.dummy_var_radio.setObjectName("dummy_var_radio")

        self.listWidget_3.raise_()
        self.matrix_radio.raise_()
        self.assign_attribute_label.raise_()
        self.attribute_label.raise_()
        self.vector_radio.raise_()
        self.scalar_radio.raise_()

        # classification part of the GUI
        self.classify_frame = QtWidgets.QFrame(self.centralwidget)
        self.classify_frame.setGeometry(QtCore.QRect(0, 180, 791, 161))
        self.classify_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.classify_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.classify_frame.setObjectName("classify_frame")
        self.classification_label = QtWidgets.QLabel(self.classify_frame)
        self.classification_label.setGeometry(QtCore.QRect(10, 0, 191, 16))
        self.classification_label.setObjectName("classification_label")
        self.constant_frame = QtWidgets.QFrame(self.centralwidget)
        self.constant_frame.setGeometry(QtCore.QRect(10, 510, 771, 141))
        self.constant_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.constant_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.constant_frame.setObjectName("constant_frame")
        self.Discipline_radio = QtWidgets.QRadioButton(self.constant_frame)
        self.Discipline_radio.setGeometry(QtCore.QRect(50, 110, 191, 19))
        self.Discipline_radio.setObjectName("Discipline_radio")
        self.assign_attribute_label_2 = QtWidgets.QLabel(self.constant_frame)
        self.assign_attribute_label_2.setGeometry(QtCore.QRect(0, 30, 400, 16))
        self.assign_attribute_label_2.setObjectName("assign_attribute_label_2")
        self.cons_op_attribute_label = QtWidgets.QLabel(self.constant_frame)
        self.cons_op_attribute_label.setGeometry(QtCore.QRect(0, 0, 521, 16))
        self.cons_op_attribute_label.setObjectName("cons_op_attribute_label")
        self.listWidget_4 = QtWidgets.QListWidget(self.constant_frame)
        self.listWidget_4.setGeometry(QtCore.QRect(0, 20, 791, 121))
        self.listWidget_4.setObjectName("listWidget_4")
        self.global_radio = QtWidgets.QRadioButton(self.constant_frame)
        self.global_radio.setGeometry(QtCore.QRect(50, 80, 115, 19))
        self.global_radio.setObjectName("global_radio")
        self.local_radio = QtWidgets.QRadioButton(self.constant_frame)
        self.local_radio.setGeometry(QtCore.QRect(50, 50, 115, 19))
        self.local_radio.setObjectName("local_radio")

        self.dummy_cons_radio = QtWidgets.QRadioButton(self.constant_frame)
        self.dummy_cons_radio.setGeometry(QtCore.QRect(50, 540, 1, 200))
        self.dummy_cons_radio.setObjectName("dummy_cons_radio")


        self.listWidget_4.raise_()
        self.Discipline_radio.raise_()
        self.assign_attribute_label_2.raise_()
        self.cons_op_attribute_label.raise_()
        self.global_radio.raise_()
        self.local_radio.raise_()

        # lower part of the main menu
        self.reset_button = QtWidgets.QPushButton(self.centralwidget)
        self.reset_button.setGeometry(QtCore.QRect(480, 660, 101, 41))
        self.reset_button.setObjectName("reset_button")
        self.submit_button = QtWidgets.QPushButton(self.centralwidget)
        self.submit_button.setGeometry(QtCore.QRect(580, 660, 101, 41))
        self.submit_button.setObjectName("submit_button")
        self.quit_button = QtWidgets.QPushButton(self.centralwidget)
        self.quit_button.setGeometry(QtCore.QRect(680, 660, 101, 41))
        self.quit_button.setObjectName("quit_button")
        self.classify_frame.raise_()
        self.listWidget.raise_()
        self.button_next_file.raise_()
        self.try_label1.raise_()
        self.button_prev_var.raise_()
        self.button_next_var.raise_()
        self.file_lable.raise_()
        self.curr_var_label.raise_()
        self.symbol_label.raise_()
        self.content_label.raise_()
        self.listWidget_2.raise_()
        self.symbol_select_label.raise_()
        self.variable_radio.raise_()
        self.constant_radio.raise_()
        self.operator_radio.raise_()
        self.unit_radio.raise_()
        self.variable_frame.raise_()
        self.constant_frame.raise_()
        self.reset_button.raise_()
        self.submit_button.raise_()
        self.quit_button.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 790, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionrandom = QtWidgets.QAction(MainWindow)
        self.actionrandom.setObjectName("actionrandom")
        self.menuFile.addAction(self.actionrandom)
        self.menuFile.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())

        # connect all radiobuttons and buttons to their events
        self.reset_button.clicked.connect(self.reset_pressed)
        self.quit_button.clicked.connect(self.quit_event)
        self.variable_radio.clicked.connect(self.variable_selected)
        self.constant_radio.clicked.connect(self.constant_selected)
        self.operator_radio.clicked.connect(self.operator_selected)
        self.unit_radio.clicked.connect(self.unit_selected)
        self.scalar_radio.clicked.connect(self.scalar_selected)
        self.vector_radio.clicked.connect(self.vector_selected)
        self.matrix_radio.clicked.connect(self.matrix_selected)
        self.local_radio.clicked.connect(self.local_selected)
        self.global_radio.clicked.connect(self.global_selected)
        self.Discipline_radio.clicked.connect(self.discipline_selected)
        self.button_prev_var.clicked.connect(self.previous_variable)
        self.button_next_var.clicked.connect(self.next_variable)
        self.button_next_file.clicked.connect(self.next_file)
        self.submit_button.clicked.connect(self.submit_variable)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    # function to detect key press events
    def keyPressEvent(self, e):
        # key press for operations
        if e.key() == Qt.Key_Escape:
            self.quit_event()
        if e.key() == Qt.Key_Q:
            self.quit_event()
        # I want to use arrow keys for them but pyqt5 have some strange bug with this setting
        # the arrow keys and other keys are exculsive, if I pressed arrows, then other keys will
        # stop working until I reset it manually or do one selection with mouse control
        if e.key() == Qt.Key_Period:
            self.next_variable()
        if e.key() == Qt.Key_Comma:
            self.previous_variable()
        if e.key() == Qt.Key_Slash:
            self.next_file()
        if e.key() == Qt.Key_R:
            self.reset_pressed()
        if e.key() == Qt.Key_S:
            self.submit_variable()
                
        # key press for radiobutton selection    
        if e.key() == Qt.Key_0:
            self.unit_selected()
        if e.key() == Qt.Key_1:
            self.variable_selected()
        if e.key() == Qt.Key_2:
            self.constant_selected()
        if e.key() == Qt.Key_3:
            self.operator_selected()
        if e.key() == Qt.Key_4:
            self.scalar_selected()
        if e.key() == Qt.Key_5:
            self.vector_selected()
        if e.key() == Qt.Key_6:
            self.matrix_selected()
        if e.key() == Qt.Key_7:
            self.local_selected()
        if e.key() == Qt.Key_8:
            self.global_selected()
        if e.key() == Qt.Key_9:
            self.discipline_selected()

             
    # functions that control the event of button press
    def quit_event(self):
        sys.exit()
    def variable_selected(self):
        self.symbol_select_label.setText("The selected symbol is a variable")
        self.variable_radio.setChecked(True)
        global symbol_choice
        symbol_choice = 1
    def constant_selected(self):
        self.symbol_select_label.setText("The selected symbol is a constant")
        self.constant_radio.setChecked(True)
        global symbol_choice
        symbol_choice = 2
    def operator_selected(self):
        self.symbol_select_label.setText("The selected symbol is a operator")
        self.operator_radio.setChecked(True)
        global symbol_choice
        symbol_choice = 3
    def unit_selected(self):
        self.symbol_select_label.setText("The selected symbol is a unit descriptor")
        self.unit_radio.setChecked(True)
        global symbol_choice
        symbol_choice = 4
    def scalar_selected(self):
        self.assign_attribute_label.setText("This variable is a scalar")
        self.scalar_radio.setChecked(True)
        global variable_choice
        variable_choice = 1
    def vector_selected(self):
        self.assign_attribute_label.setText("This variable is a vector")
        self.vector_radio.setChecked(True)
        global variable_choice
        variable_choice = 2
    def matrix_selected(self):
        self.assign_attribute_label.setText("This variable is a matrix")
        self.matrix_radio.setChecked(True)
        global variable_choice
        variable_choice = 3
    def local_selected(self):
        self.assign_attribute_label_2.setText("This constant/operator is local")
        self.local_radio.setChecked(True)
        global constant_choice
        constant_choice = 1
    def global_selected(self):
        self.assign_attribute_label_2.setText("This constant/operator is global")
        self.global_radio.setChecked(True)
        global constant_choice
        constant_choice = 2
    def discipline_selected(self):
        self.assign_attribute_label_2.setText("This constant/operator is discipline specified")
        self.Discipline_radio.setChecked(True)
        global constant_choice
        constant_choice = 3

    def reset_pressed(self):
        global symbol_choice
        global variable_choice
        global constant_choice
        # reset all global values 
        symbol_choice = 0
        variable_choice = 0
        constant_choice = 0
        # refresh all label texts
        self.symbol_select_label.setText("The selected symbol is a ")
        self.assign_attribute_label.setText("This variable is a ")
        self.assign_attribute_label_2.setText("This constant/operator is ")
        # Since deselect not working properly, using dummy radio button to reset
        self.dummy_radio.setChecked(True)
        self.dummy_var_radio.setChecked(True)
        self.dummy_cons_radio.setChecked(True)
    
    def next_file(self):
        # global variables
        global file_list
        global file_size
        global curr_file_location
        global curr_file
        global var_list
        global curr_var_location
        global curr_var
        global variable_size
        # go to next file if we can
        if curr_file_location < file_size - 1:
            curr_file_location += 1
            curr_file = file_list[curr_file_location]
        # update all variables
        var_list = ext.extract_list(curr_file)
        curr_var_location = 0
        curr_var = var_list[curr_var_location]
        variable_size = len(var_list) - 1
        # update all labels
        self.file_lable.setText("Now you are in file: %s" %(curr_file))
        self.curr_var_label.setText("With variable %d among %d variables" %(curr_var_location + 1, variable_size + 1))
        self.symbol_label.setText("The symbol represent by this varibale is: %s" %(curr_var))
        text = ext.first_word(curr_file, curr_var)
        print(text + "\n")
        self.content_label.setText(text)
        self.reset_pressed()

    def previous_variable(self):
        global var_list
        global curr_file
        global curr_var_location
        global curr_var
        if curr_var_location > 0:
            curr_var_location -= 1
            curr_var = var_list[curr_var_location]
        self.curr_var_label.setText("With variable %d among %d variables" %(curr_var_location + 1, variable_size + 1))
        self.symbol_label.setText("The symbol represent by this varibale is: %s" %(curr_var))
        text = ext.first_word(curr_file, curr_var)
        self.content_label.setText(text)
        print(text + "\n")
        self.reset_pressed()

    def next_variable(self):
        # global variables that we need
        global var_list
        global curr_file
        global curr_var_location
        global curr_var
        global variable_size

        if curr_var_location < variable_size:
            curr_var_location += 1
            curr_var = var_list[curr_var_location]
        self.curr_var_label.setText("With variable %d among %d variables" %(curr_var_location + 1, variable_size + 1))
        self.symbol_label.setText("The symbol represent by this varibale is: %s" %(curr_var))
        text = ext.first_word(curr_file, curr_var)
        self.content_label.setText(text)
        print(text + "\n")
        self.reset_pressed()

    def error_message(self):
        # message box for errors
        msg = QMessageBox()
        msg.setWindowTitle("Invalid input")
        msg.setIcon(QMessageBox.Warning)
        msg.setText("There is a conflict on your selection")
        msg.buttonClicked.connect(self.reset_pressed)
        error_print = msg.exec_()



    def submit_variable(self):
        global curr_file
        global curr_var

        global symbol_choice
        global variable_choice
        global constant_choice

        text = ext.first_word(curr_file, curr_var)

        symbol_dis = ""
        variable_dis = ""
        constant_dis = ""
        # edge cases for error
        if symbol_choice == 0:
            self.error_message()
            return
        elif (symbol_choice == 1 and variable_choice == 0) or (symbol_choice == 1 and constant_choice != 0):
            self.error_message()
            return
        elif (symbol_choice == 2 and constant_choice == 0) or (symbol_choice == 2 and variable_choice != 0):
            self.error_message()
            return
        elif (symbol_choice == 3 and constant_choice == 0) or (symbol_choice == 3 and variable_choice != 0):
            self.error_message()
            return

        if symbol_choice == 1:
            symbol_dis = "Variable"
        elif symbol_choice == 2:
            symbol_dis = "Constant"
        elif symbol_choice == 3:
            symbol_dis = "Operator"
        elif symbol_choice == 4:
            symbol_dis = "unit descriptor"

        if variable_choice == 1:
            variable_dis = "Scalar"
        elif variable_choice == 2:
            variable_dis = "Vector"
        elif variable_choice == 3:
            variable_dis = "Matrix"

        if constant_choice == 1:
            constant_dis = "Local"
        elif constant_choice == 2:
            constant_dis = "Global"
        elif constant_choice == 3:
            constant_dis = "Discipline specified"

        combine = "\n" + curr_file + " " + str(curr_var_location) + " " + curr_var + " " + symbol_dis  + " " + variable_dis + " " + constant_dis + "    " + text
        print(combine)
            
        with open("test_database", "ab") as in_file:
            in_file.write(combine.encode('utf8'))

        self.next_variable()

    def retranslateUi(self, MainWindow):
        global curr_file
        global curr_var_location
        global curr_var
        global variable_size
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_next_file.setText(_translate("MainWindow", "Next File"))
        self.try_label1.setText(_translate("MainWindow", "Information related to variables"))
        self.button_prev_var.setText(_translate("MainWindow", "Prev"))
        self.button_next_var.setText(_translate("MainWindow", "Next"))
        self.file_lable.setText(_translate("MainWindow", "Now you are in file: %s" %(curr_file)))
        self.curr_var_label.setText(_translate("MainWindow", "With variable %d among %d variables" %(curr_var_location + 1, variable_size + 1)))
        self.symbol_label.setText(_translate("MainWindow", "The symbol represent by this varibale is: %s" %(curr_var)))
        self.content_label.setText(_translate("MainWindow", " "))
        self.symbol_select_label.setText(_translate("MainWindow", "The selected symbol is a "))
        self.variable_radio.setText(_translate("MainWindow", "Variable"))
        self.constant_radio.setText(_translate("MainWindow", "Constant"))
        self.operator_radio.setText(_translate("MainWindow", "Operator"))
        self.unit_radio.setText(_translate("MainWindow", "Unit descriptor"))
        self.matrix_radio.setText(_translate("MainWindow", "Matrix"))
        self.assign_attribute_label.setText(_translate("MainWindow", "This variable is a "))
        self.attribute_label.setText(_translate("MainWindow", "If the symbol is a variable, what is its attribute?"))
        self.vector_radio.setText(_translate("MainWindow", "Vector"))
        self.scalar_radio.setText(_translate("MainWindow", "Scalar"))
        self.classification_label.setText(_translate("MainWindow", "Variable Classification"))
        self.Discipline_radio.setText(_translate("MainWindow", "Discipline specified"))
        self.assign_attribute_label_2.setText(_translate("MainWindow", "This constant/operator is "))
        self.cons_op_attribute_label.setText(_translate("MainWindow", "If the symbol is a constant or operator, what is its attribute?"))
        self.global_radio.setText(_translate("MainWindow", "Global"))
        self.local_radio.setText(_translate("MainWindow", "Local"))
        self.reset_button.setText(_translate("MainWindow", "Reset"))
        self.submit_button.setText(_translate("MainWindow", "Submit"))
        self.quit_button.setText(_translate("MainWindow", "Quit"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionrandom.setText(_translate("MainWindow", "random"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())