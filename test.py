from asyncio import Task
from importlib.util import set_loader
import os
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication , QMainWindow

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
        self.employeeButton.clicked.connect(self.employ)
    def employ(self):
        self.MainText.setText("Employees Section")

if __name__ == "__main__" :
    data = programData()
    app = QApplication(sys.argv)
    w = MainWindow(data)
    w.show()
    sys.exit(app.exec_())