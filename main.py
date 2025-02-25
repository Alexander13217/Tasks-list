from PyQt5 import QtCore, QtGui, QtWidgets
from my_task import Ui_Dialog
from main_design import Ui_MainWindow
from addtask_design import Ui_Dialog2
import sys

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
MyTaskWindow = QtWidgets.QMainWindow()
AddTaskWindow = QtWidgets.QMainWindow()
task_window = Ui_Dialog()
add_task_window = Ui_Dialog2()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
task_window.setupUi(MyTaskWindow)
add_task_window.setupUi(AddTaskWindow)
MainWindow.show()

def my_task():
    with open('tasks.txt','r',encoding='utf-8') as file:
        i = 0
        for line in file:
            if i == 0:
                task_window.task_one.setText(line)

            if i == 1:
                task_window.task_two.setText(line)

            if i == 2:
                task_window.task_trhee.setText(line)
        
            if i == 3:
                task_window.task_four.setText(line)
            
            if i == 4:
                task_window.label_5.setText(line)
            i += 1
    MainWindow.hide()
    MyTaskWindow.show()

def go_home1():
    MainWindow.show()
    MyTaskWindow.hide()

def add_task():
    MainWindow.hide()
    AddTaskWindow.show()
    add_task_window.lineEdit.clear()
    
    with open('tasks.txt','r',encoding='utf-8') as file:
        i = 0
        for line in file:
            if i == 0:
                add_task_window.label.setText(line)
            if i == 1:
                add_task_window.label_2.setText(line)
            if i == 2:
                add_task_window.label_3.setText(line)
            if i == 3:
                add_task_window.label_4.setText(line)
            if i == 4:
                add_task_window.label_5.setText(line)
            i += 1
def go_home2():
    AddTaskWindow.hide()
    MainWindow.show()

def con1():
    
    with open('tasks.txt','r',encoding='utf-8') as file:
        text = add_task_window.lineEdit.text().strip()
        line = file.readlines()
        line[0] = text + '\n'
    with open('tasks.txt','w',encoding='utf-8') as file:
        file.writelines(line)
        add_task_window.label.setText(text)
    add_task_window.lineEdit.clear()
def con2():
    
    with open('tasks.txt','r',encoding='utf-8') as file:
        text = add_task_window.lineEdit_2.text().strip()
        line = file.readlines()
        line[1] = text + '\n'
    with open('tasks.txt','w',encoding='utf-8') as file:
        file.writelines(line)
        add_task_window.label_2.setText(text)    
    add_task_window.lineEdit_2.clear()
def con3():
    
    with open('tasks.txt','r',encoding='utf-8') as file:
        text = add_task_window.lineEdit_3.text().strip()
        line = file.readlines()
        line[2] = text + '\n'
    with open('tasks.txt','w',encoding='utf-8') as file:
        file.writelines(line)
        add_task_window.label_3.setText(text)    
    add_task_window.lineEdit_3.clear()
def con4():
    
    with open('tasks.txt','r',encoding='utf-8') as file:
        text = add_task_window.lineEdit_4.text().strip()
        line = file.readlines()
        line[3] = text + '\n'
    with open('tasks.txt','w',encoding='utf-8') as file:
        file.writelines(line)
        add_task_window.label_4.setText(text)    
    add_task_window.lineEdit_4.clear()
def con5():
    with open('tasks.txt','r',encoding='utf-8') as file:
        text = add_task_window.lineEdit_5.text().strip()
        line = file.readlines()
        line[4] = text + '\n'
    with open('tasks.txt','w',encoding='utf-8') as file:
        file.writelines(line)
        add_task_window.label_5.setText(text)
    add_task_window.lineEdit_5.clear()

add_task_window.con5.clicked.connect(con5)
add_task_window.con4.clicked.connect(con4)
add_task_window.con3.clicked.connect(con3)
add_task_window.con2.clicked.connect(con2)
add_task_window.con1.clicked.connect(con1)
add_task_window.gohome.clicked.connect(go_home2)
ui.pushButton_2.clicked.connect(add_task)
task_window.go_home.clicked.connect(go_home1)
ui.mytask.clicked.connect(my_task)
sys.exit(app.exec_())