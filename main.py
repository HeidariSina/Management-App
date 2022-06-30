from asyncio import Task
from importlib.util import set_loader
import os
import sys
from PyQt5 import uic 
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication , QMainWindow , QTableWidgetItem  ,QHeaderView 

Home = uic.loadUiType(os.path.join(os.getcwd() , "QT.ui"))[0]
Employee = uic.loadUiType(os.path.join(os.getcwd() , "Employee.ui"))[0]

class programData():
    def __init__(self) :
        self.employ = []
        self.task = []

    def addEmployee(self ,name ,serialNumber , sex , age , entranceTime , tasks , finishedTasks , unfinishedTasks):
        person = Person(name ,serialNumber , sex , age , entranceTime , tasks , finishedTasks , unfinishedTasks)
        self.employ.append(person)

    def addTask(self , name ,startedTime , deadline , importance , milestone  ,persons):
        task = Task(name ,startedTime , deadline , importance , milestone  ,persons)
        self.task.append(task)

class MileStone() :
    def __init__(self , name , checked):
        self.name = name
        self.checked = checked

class Person () :
    def __init__(self , name ,ID , sex , age , entranceTime , tasks , finishedTasks , unfinishedTasks ) :
        self.name = name
        self.ID = ID
        self.sex = sex
        self.age = age
        self.entranceTime = entranceTime
        self.tasks = tasks
        self.finishedTasks = finishedTasks
        self.unfinishedTasks = unfinishedTasks

class Task () :
    def __init__(self , name ,startedTime , deadline , importance , milestone  ,persons  ) :
        self.name = name
        self.startedTime = startedTime
        self.deadline = deadline
        self.importance = importance
        self.milestone = milestone
        self.persons = persons


class MainWindow (QMainWindow , Home):
    def __init__(self):
        super(MainWindow , self).__init__()
        self.data = programData()
        self.addSignal = "none"
        self.setupUi(self)
        self.backButton.hide()
        self.addbutton.hide()
        self.tableWidget.hide()
        self.emptyText.hide()
        self.emptyText2.hide()
        self.MainText.setStyleSheet("color : white ; border : none")
        self.employeeButton.setStyleSheet("background-color : #1a161c ; color : white")
        self.taskButton.setStyleSheet("background-color : #1a161c ; color : white")
        self.backButton.setStyleSheet("background-color : #1a161c ; color : white")
        self.addbutton.setStyleSheet("background-color : #1a161c ; color : white")
        self.tableWidget.setStyleSheet("background-color : #1a161c ; color : white")
        self.employeeButton.clicked.connect(self.employ)
        self.taskButton.clicked.connect(self.task)
        self.backButton.clicked.connect(self.back)
        self.addbutton.clicked.connect(self.add)
    def employ(self):
        self.addSignal = "employ"
        self.backButton.show()
        self.addbutton.show()
        self.taskButton.hide()
        self.employeeButton.hide()
        self.MainText.setText("Employees Section")
        self.MainText.setStyleSheet("color : white ; border : none")
        self.MainText.setAlignment(Qt.AlignCenter)
        if (len(self.data.employ) == 0) :
            self.tableWidget.show()
            self.tableWidget.setStyleSheet("background-color : #1a161c ; color : black ; border : none")
            self.tableWidget.setColumnCount(8)
            self.tableWidget.setRowCount(8)
            self.tableWidget.setHorizontalHeaderItem( 0 , QTableWidgetItem("Name"))
            self.tableWidget.setHorizontalHeaderItem( 1 , QTableWidgetItem("ID"))
            self.tableWidget.setHorizontalHeaderItem( 2 , QTableWidgetItem("Sex"))
            self.tableWidget.setHorizontalHeaderItem( 3 , QTableWidgetItem("Age"))
            self.tableWidget.setHorizontalHeaderItem( 4 , QTableWidgetItem("Entrance Time"))
            self.tableWidget.setHorizontalHeaderItem( 5 , QTableWidgetItem("Tasks"))
            self.tableWidget.setHorizontalHeaderItem( 6 , QTableWidgetItem("Finished Tasks"))
            self.tableWidget.setHorizontalHeaderItem( 7 , QTableWidgetItem("UnFinished Tasks"))
            self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        else :
            self.emptyText.show()
            self.emptyText2.show()
            self.emptyText2.setStyleSheet("color : white ; border : none")
            self.emptyText.setText("Sorry There is No Employee :(")
            self.emptyText.setStyleSheet("color : white ; border : none")
            self.emptyText.setAlignment(Qt.AlignCenter)
    def task(self) :
        self.addSignal = "task"
        self.backButton.show()
        self.addbutton.show()
        self.taskButton.hide()
        self.employeeButton.hide()
        self.MainText.setText("Tasks Section")
        self.MainText.setStyleSheet("color : white; border : none")
        self.MainText.setAlignment(Qt.AlignCenter)
        if (len(self.data.task) == 0) :
            self.tableWidget.show()
            self.tableWidget.setStyleSheet("background-color : #1a161c ; color : black ;border : none")
            self.tableWidget.setColumnCount(6)
            self.tableWidget.setRowCount(8)
            self.tableWidget.setHorizontalHeaderItem( 0 , QTableWidgetItem("Name"))
            self.tableWidget.setHorizontalHeaderItem( 1 , QTableWidgetItem("Started Time"))
            self.tableWidget.setHorizontalHeaderItem( 2 , QTableWidgetItem("Deadline"))
            self.tableWidget.setHorizontalHeaderItem( 3 , QTableWidgetItem("Importance"))
            self.tableWidget.setHorizontalHeaderItem( 4 , QTableWidgetItem("Milestone"))
            self.tableWidget.setHorizontalHeaderItem( 5 , QTableWidgetItem("Persons"))
            self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        else :
            self.emptyText.show()
            self.emptyText2.show()
            self.emptyText2.setStyleSheet("color : white ; border : none")
            self.emptyText.setText("Sorry There is No Tasks :(")
            self.emptyText.setStyleSheet("color : white ; border : none")
            self.emptyText.setAlignment(Qt.AlignCenter)
    def back(self):
        self.addSignal = "none"
        self.emptyText.hide()
        self.emptyText2.hide()
        self.addbutton.hide()
        self.backButton.hide()
        self.taskButton.show()
        self.employeeButton.show()
        self.tableWidget.hide()
        self.MainText.setText("Main Menu")
        self.MainText.setStyleSheet("color : white; border : none")
        self.MainText.setAlignment(Qt.AlignCenter)
    def add(self) :
        if (self.addSignal == "employ"):
            self.w = SecondWindow()
            self.w.show()
        elif(self.addSignal == "task"):
            #code for employ
            return
        else :
            return

        
class SecondWindow (QMainWindow , Employee):
    def __init__(self):
        super(SecondWindow, self).__init__()
        self.setupUi(self)

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())