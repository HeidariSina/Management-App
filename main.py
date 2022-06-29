from asyncio import Task
from importlib.util import set_loader
import os
import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication , QMainWindow
from PyQt5.QtWidgets import *

Test = uic.loadUiType(os.path.join(os.getcwd() , "QT.ui"))[0]
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

class Person () :
    def __init__(self , name ,serialNumber , sex , age , entranceTime , tasks , finishedTasks , unfinishedTasks ) :
        self.name = name
        self.serialNumber = serialNumber
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


class MainWindow (QMainWindow , Test):
    def __init__(self , data):
        super(MainWindow , self).__init__()
        self.data = data
        self.setupUi(self)
        self.backButton.hide()
        self.addbutton.hide()
        self.mainTable.hide()
        self.MainText.setStyleSheet("color : white ; border : none")
        self.employeeButton.setStyleSheet("background-color : #1a161c ; color : white")
        self.taskButton.setStyleSheet("background-color : #1a161c ; color : white")
        self.backButton.setStyleSheet("background-color : #1a161c ; color : white")
        self.addbutton.setStyleSheet("background-color : #1a161c ; color : white")
        self.mainTable.setStyleSheet("background-color : #1a161c ; color : white")
        self.employeeButton.clicked.connect(self.employ)
        self.taskButton.clicked.connect(self.task)
        self.backButton.clicked.connect(self.back)
        #self.tableAdd.clicked.connect(self.addRows)
    def employ(self):
        self.backButton.show()
        self.addbutton.show()
        self.taskButton.hide()
        self.mainTable.show()
        self.employeeButton.hide()
        self.MainText.setText("Employees Section")
        self.MainText.setStyleSheet("color : white ; border : none")
        self.MainText.setAlignment(Qt.AlignCenter)
    def task(self) :
        self.addSignal = "task"
        self.backButton.show()
        self.addbutton.show()
        self.taskButton.hide()
        self.employeeButton.hide()
        self.mainTable.show()
        self.MainText.setText("Tasks Section")
        self.MainText.setStyleSheet("color : white; border : none")
        self.MainText.setAlignment(Qt.AlignCenter)
    def back(self):
        self.addSignal = "none"
        self.addbutton.hide()
        self.backButton.hide()
        self.taskButton.show()
        self.employeeButton.show()
        self.mainTable.hide()
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

        
        
class SecondWindow (QMainWindow , QWidget, Employee):
    def __init__(self, data):
        super(SecondWindow, self).__init__()
        self.data = data
        self.title = 'Employees List'
        self.left = 0
        self.top = 0
        self.width = 300
        self.height = 200
   
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
   
        self.createTable()
   
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)
   
        #Show window
        self.show()
   
    #Create table
    def createTable(self):
        self.tableWidget = QTableWidget()
  
        #Row count
        self.tableWidget.setRowCount(4) 
  
        #Column count
        self.tableWidget.setColumnCount(2)  
  
        self.tableWidget.setItem(0,0, QTableWidgetItem("Name"))
        self.tableWidget.setItem(0,1, QTableWidgetItem("City"))
        self.tableWidget.setItem(1,0, QTableWidgetItem("Aloysius"))
        self.tableWidget.setItem(1,1, QTableWidgetItem("Indore"))
        self.tableWidget.setItem(2,0, QTableWidgetItem("Alan"))
        self.tableWidget.setItem(2,1, QTableWidgetItem("Bhopal"))
        self.tableWidget.setItem(3,0, QTableWidgetItem("Arnavi"))
        self.tableWidget.setItem(3,1, QTableWidgetItem("Mandsaur"))
   
        #Table will fit the screen horizontally
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)
        self.setupUi(self)
    #def addRows(self):
        
        

if __name__ == "__main__" :
    data = programData()
    app = QApplication(sys.argv)
    w = MainWindow(data)
    #e = SecondWindow(data)
    #e.show()
    w.show()
    sys.exit(app.exec_())